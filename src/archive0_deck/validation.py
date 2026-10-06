"""Package validation for generated decks.

Two layers:

* structural checks that always run -- zip integrity, relationship targets,
  content-type coverage, slide element order, unique animation time-node ids and
  animation targets that resolve to a real shape;
* schema validation against the ISO/IEC 29500-4 presentationML schemas, when a
  schema directory is supplied (see :data:`SCHEMA_ENV_VAR`).

Markup-Compatibility attributes (``mc:Ignorable`` and attributes in the
namespaces it lists) are dropped before schema validation: they are allowed by the
MC spec but are not declared in the ISO schemas. python-pptx2 writes
``mc:Ignorable`` on every slide part.
"""

import os
import posixpath
import zipfile

from lxml import etree

SCHEMA_ENV_VAR = "ARCHIVE0_OOXML_XSD"
_PRESENTATIONML = "http://schemas.openxmlformats.org/presentationml/2006/main"
_MARKUP_COMPATIBILITY = "http://schemas.openxmlformats.org/markup-compatibility/2006"
_PACKAGE_RELATIONSHIPS = "http://schemas.openxmlformats.org/package/2006/relationships"
_CONTENT_TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"
_MC = "{%s}" % _MARKUP_COMPATIBILITY
_P = "{%s}" % _PRESENTATIONML
_RELATIONSHIP_TAG = "{%s}Relationship" % _PACKAGE_RELATIONSHIPS
_CONTENT_TYPE_DEFAULT = "{%s}Default" % _CONTENT_TYPES
_CONTENT_TYPE_OVERRIDE = "{%s}Override" % _CONTENT_TYPES

# slides must carry these children in this relative order
_ELEMENT_ORDER = ("cSld", "clrMapOvr", "transition", "timing")


def strip_mc_attributes(root):
    """Remove MC attributes from *root*; returns how many were dropped."""
    prefixes = (root.get(_MC + "Ignorable") or "").split()
    if not prefixes:
        return 0
    nsmap = root.nsmap
    ignorable = {_MARKUP_COMPATIBILITY} | {nsmap[p] for p in prefixes if p in nsmap}
    dropped = 0
    for element in root.iter():
        for attribute in list(element.attrib):
            if attribute.startswith("{") and etree.QName(attribute).namespace in ignorable:
                del element.attrib[attribute]
                dropped += 1
    return dropped


def _slide_parts(names):
    parts = (n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
    return sorted(parts, key=lambda name: int(name[len("ppt/slides/slide"):-len(".xml")]))


def _schema(schema_dir):
    schema_path = os.path.join(schema_dir, "pml.xsd")
    return etree.XMLSchema(etree.parse(schema_path))


def validate_package(path, schema_dir=None):
    """Validate the .pptx at *path*; returns a report dictionary."""
    schema_dir = schema_dir or os.environ.get(SCHEMA_ENV_VAR)
    with zipfile.ZipFile(path) as archive:
        return _inspect(archive, path, schema_dir)


def _inspect(archive, path, schema_dir):
    names = set(archive.namelist())
    report = {
        "path": str(path),
        "zip_ok": archive.testzip() is None,
        "parts": len(names),
        "mc_attributes_stripped": 0,
        "bad_relationships": [],
        "uncovered_parts": [],
        "element_order": {},
        "duplicate_time_node_ids": [],
        "dangling_animation_targets": [],
        "schema_checked": False,
        "schema": {},
    }

    validate = _schema(schema_dir) if schema_dir else None
    report["schema_checked"] = validate is not None

    for name in _slide_parts(names) + ["ppt/presentation.xml"]:
        document = etree.fromstring(archive.read(name))
        report["mc_attributes_stripped"] += strip_mc_attributes(document)

        if validate is not None:
            report["schema"][name] = validate.validate(document) or [
                error.message for error in validate.error_log]

        if not name.endswith("presentation.xml"):
            children = [etree.QName(child).localname for child in document]
            report["element_order"][name] = _ordered(children)

            time_ids = [el.get("id") for el in document.iter(_P + "cTn")]
            duplicates = sorted({i for i in time_ids if i and time_ids.count(i) > 1})
            if duplicates:
                report["duplicate_time_node_ids"].append((name, duplicates))

            shape_ids = {el.get("id") for el in document.iter()
                         if etree.QName(el).localname == "cNvPr"}
            dangling = sorted({el.get("spid") for el in document.iter(_P + "spTgt")
                               if el.get("spid") and el.get("spid") not in shape_ids})
            if dangling:
                report["dangling_animation_targets"].append((name, dangling))

    for name in names:
        if name.endswith(".rels"):
            base = posixpath.dirname(posixpath.dirname(name))
            for relationship in etree.fromstring(
                    archive.read(name)).findall(_RELATIONSHIP_TAG):
                if relationship.get("TargetMode") == "External":
                    continue
                target = posixpath.normpath(
                    posixpath.join(base, relationship.get("Target"))).lstrip("/")
                if target not in names:
                    report["bad_relationships"].append((name, relationship.get("Target")))

    content_types = etree.fromstring(archive.read("[Content_Types].xml"))
    defaults = {node.get("Extension").lower()
                for node in content_types.findall(_CONTENT_TYPE_DEFAULT)}
    overrides = {node.get("PartName").lstrip("/")
                 for node in content_types.findall(_CONTENT_TYPE_OVERRIDE)}
    report["uncovered_parts"] = [
        name for name in names
        if name != "[Content_Types].xml" and not name.endswith(".rels")
        and name not in overrides and name.rsplit(".", 1)[-1].lower() not in defaults]

    return report


def _ordered(children):
    """True when the slide children appear in schema order."""
    positions = [children.index(tag) for tag in _ELEMENT_ORDER if tag in children]
    return positions == sorted(positions)


def is_valid(report):
    """True when every check passed (schema checks only count when they ran)."""
    if not report["zip_ok"]:
        return False
    if (report["bad_relationships"] or report["uncovered_parts"]
            or report["duplicate_time_node_ids"] or report["dangling_animation_targets"]):
        return False
    if not all(report["element_order"].values()):
        return False
    return all(result is True for result in report["schema"].values())


def format_report(report):
    """Human-readable summary of a :func:`validate_package` report."""
    lines = [f"=== {report['path']}",
             f"  zip integrity: {'OK' if report['zip_ok'] else 'FAILED'}",
             f"  parts: {report['parts']}  "
             f"mc attributes stripped: {report['mc_attributes_stripped']}"]
    if report["schema_checked"]:
        invalid = {name: result for name, result in report["schema"].items()
                   if result is not True}
        lines.append(f"  schema: {len(report['schema']) - len(invalid)}/"
                     f"{len(report['schema'])} parts valid")
        for name, errors in invalid.items():
            lines.append(f"    INVALID {name}")
            for error in errors if isinstance(errors, list) else []:
                lines.append(f"      {error[:200]}")
    else:
        lines.append(f"  schema: skipped (set {SCHEMA_ENV_VAR} to a directory "
                     "containing pml.xsd)")
    if report["duplicate_time_node_ids"]:
        lines.append(f"  duplicate time-node ids: {report['duplicate_time_node_ids']}")
    if report["dangling_animation_targets"]:
        lines.append(f"  dangling animation targets: {report['dangling_animation_targets']}")
    if report["bad_relationships"]:
        lines.append(f"  broken relationships: {report['bad_relationships']}")
    if report["uncovered_parts"]:
        lines.append(f"  parts without content type: {report['uncovered_parts']}")
    bad_order = [name for name, ok in report["element_order"].items() if not ok]
    if bad_order:
        lines.append(f"  wrong element order: {bad_order}")
    lines.append(f"  RESULT: {'VALID' if is_valid(report) else 'INVALID'}")
    return "\n".join(lines)

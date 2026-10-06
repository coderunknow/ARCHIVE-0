"""Entrance animation timing (OOXML ``<p:timing>``) for slides built with pptx2.

python-pptx2 has no animation API, so the timing tree is written directly. A slide
gets a single reveal group that starts with the slide and staggers its shapes, so a
slide builds itself smoothly without extra clicks. The XML is validated against
pml.xsd (ISO/IEC 29500-4) when the test suite is given the schemas.
"""

from pptx2.oxml import parse_xml

# (presetID, presetSubtype, animEffect filter) for the PowerPoint built-ins used here
FADE = (10, 0, "fade")          # Fade
WIPE_UP = (22, 4, "wipe(up)")   # Wipe, from bottom

STAGGER_MS = 90      # delay between consecutive shapes on a slide
MAX_DELAY_MS = 2200  # cap, so a dense slide never drags
DURATION_MS = 380

_PML_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
_MAIN_SEQUENCE_ID = 2     # id of <p:cTn nodeType="mainSeq">
_REVEAL_GROUP_ID = 3      # id of the single reveal group wrapping every effect
_FIRST_EFFECT_ID = 4      # effect time nodes start here; ids must be unique per part


def _effect_xml(node_id, shape_id, preset, delay, node_type):
    preset_id, preset_subtype, effect_filter = preset
    return f"""<p:par><p:cTn id="{node_id}" dur="{DURATION_MS}" presetID="{preset_id}" presetClass="entr" presetSubtype="{preset_subtype}" fill="hold" grpId="0" nodeType="{node_type}">
<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>
<p:set><p:cBhvr><p:cTn id="{node_id + 1}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>
<p:animEffect transition="in" filter="{effect_filter}"><p:cBhvr><p:cTn id="{node_id + 2}" dur="{DURATION_MS}"/><p:tgtEl><p:spTgt spid="{shape_id}"/></p:tgtEl></p:cBhvr></p:animEffect>
</p:childTnLst></p:cTn></p:par>"""


def build_timing_xml(effects):
    """Return the ``<p:timing>`` element for *effects*.

    *effects* is a sequence of ``(shape_id, preset)`` pairs in reveal order; the
    stagger delay is derived from the position in that sequence.
    """
    if not effects:
        return None

    parts = []
    for index, (shape_id, preset) in enumerate(effects):
        node_id = _FIRST_EFFECT_ID + index * 3
        delay = min(index * STAGGER_MS, MAX_DELAY_MS)
        node_type = "afterEffect" if index == 0 else "withEffect"
        parts.append(_effect_xml(node_id, shape_id, preset, delay, node_type))

    build_list = "".join(f'<p:bldP spid="{shape_id}" grpId="0"/>'
                         for shape_id, _ in effects)
    return parse_xml(
        f'<p:timing xmlns:p="{_PML_NS}">'
        '<p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
        '<p:childTnLst><p:seq concurrent="1" nextAc="seek">'
        f'<p:cTn id="{_MAIN_SEQUENCE_ID}" dur="indefinite" nodeType="mainSeq">'
        f'<p:childTnLst><p:par><p:cTn id="{_REVEAL_GROUP_ID}" fill="hold">'
        '<p:stCondLst><p:cond delay="0"/></p:stCondLst>'
        f'<p:childTnLst>{"".join(parts)}</p:childTnLst>'
        '</p:cTn></p:par></p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0">'
        '<p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        '<p:nextCondLst><p:cond evt="onNext" delay="0">'
        '<p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
        '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst>'
        f'<p:bldLst>{build_list}</p:bldLst></p:timing>')


def build_transition_xml():
    """Return the ``<p:transition>`` element applied to every slide (Fade)."""
    # the p14 declaration is unused but keeps this element identical to the one in
    # the deck published before the python-pptx2 migration
    return parse_xml(
        f'<p:transition xmlns:p="{_PML_NS}" '
        'xmlns:p14="http://schemas.microsoft.com/office/powerpoint/2010/main" '
        'spd="med"><p:fade/></p:transition>')

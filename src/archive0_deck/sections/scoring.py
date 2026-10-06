"""Scoring, priority and direct-admission rules."""
from ..theme import (
    AMBER,
    CYAN,
    EDGE,
    FONT_HEAD,
    LIME,
    MUTED,
    MUTED2,
    PANEL,
    PINK,
    WHITE,
    CONTENT_LEFT,
    CONTENT_WIDTH,
)
from ..animation import FADE, WIPE_UP
from pptx2.enum.text import MSO_ANCHOR


def _slide_12_scoring(deck):
    s = deck.add_slide("PHẦN 05 · ĐIỂM & NGUYỆN VỌNG", "Điểm xét tuyển và các loại điểm cộng", notes="Điều 13 khoản 6: điểm xét tuyển vào lớp 10 THPT là điểm tổng của các môn thi, bài thi tính "
        "theo thang điểm 10 với mỗi môn thi, bài thi.\n"
        "Cùng khoản: việc công bố điểm chuẩn được thực hiện đồng thời với công bố điểm thi.\n"
        "Điều 14 khoản 2: điểm ưu tiên cộng vào tổng điểm xét tuyển — nhóm 1: 2,0 điểm; "
        "nhóm 2: 1,5 điểm; nhóm 3: 1,0 điểm.\n"
        "Điều 14 khoản 3: điểm khuyến khích — giải nhất 1,5 điểm; giải nhì 1,0 điểm; giải ba 0,5 điểm "
        "(học sinh THCS đạt giải cấp tỉnh do Sở GD&ĐT tổ chức hoặc phối hợp tổ chức).")
    s.card(CONTENT_LEFT, 2.05, CONTENT_WIDTH, 1.85, "Điểm xét tuyển = tổng điểm các môn thi",
           ["Mỗi môn thi, bài thi tính theo thang điểm 10.",
            "Điểm chuẩn được công bố đồng thời với điểm thi (Điều 13 khoản 6)."],
           accent=LIME, body_size=13.5)
    s.card(CONTENT_LEFT, 4.05, (CONTENT_WIDTH - 0.3) / 2, 2.2, "Điểm ưu tiên (Điều 14)",
           ["Nhóm 1: +2,0 điểm", "Nhóm 2: +1,5 điểm", "Nhóm 3: +1,0 điểm"],
           accent=CYAN, body_size=15, body_spacing=1.05)
    s.card(CONTENT_LEFT + (CONTENT_WIDTH - 0.3) / 2 + 0.3, 4.05, (CONTENT_WIDTH - 0.3) / 2, 2.2, "Điểm khuyến khích (Điều 14)",
           ["Giải nhất: +1,5 điểm", "Giải nhì: +1,0 điểm", "Giải ba: +0,5 điểm"],
           accent=PINK, body_size=15, body_spacing=1.05)
    s.text(CONTENT_LEFT, 6.5, CONTENT_WIDTH, 0.3, ["Nguồn: Điều 13 khoản 6, Điều 14 — Thông tư 30/2024/TT-BGDĐT"],
            size=10, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_13_direct_admission(deck):
    s = deck.add_slide("PHẦN 05 · ĐIỂM & NGUYỆN VỌNG", "Ai được tuyển thẳng vào lớp 10?", notes="Điều 14 khoản 1 — 05 nhóm được tuyển thẳng vào THPT:\n"
        "a) Học sinh trường phổ thông dân tộc nội trú cấp THCS.\n"
        "b) Học sinh là người dân tộc thiểu số rất ít người.\n"
        "c) Học sinh là người khuyết tật.\n"
        "d) Học sinh đạt giải cấp quốc gia do Bộ GD&ĐT tổ chức hoặc phối hợp tổ chức về văn hóa, "
        "văn nghệ, thể thao; cuộc thi nghiên cứu khoa học, kĩ thuật.\n"
        "đ) Học sinh đạt giải trong các cuộc thi quốc tế do Bộ trưởng Bộ GD&ĐT quyết định cử tham dự.")
    items = [("a", "Học sinh trường phổ thông dân tộc nội trú cấp THCS", LIME),
             ("b", "Học sinh là người dân tộc thiểu số rất ít người", CYAN),
             ("c", "Học sinh là người khuyết tật", PINK),
             ("d", "Đạt giải cấp quốc gia về văn hóa, văn nghệ, thể thao hoặc cuộc thi nghiên cứu khoa học, kĩ thuật", AMBER),
             ("đ", "Đạt giải trong các cuộc thi quốc tế do Bộ trưởng Bộ GD&ĐT quyết định cử tham dự", LIME)]
    y = 2.05
    for i, (tag, txt, acc) in enumerate(items):
        s.rect(CONTENT_LEFT, y, CONTENT_WIDTH, 0.72, PANEL, radius=0.08, line=EDGE, kind=None)
        s.text(CONTENT_LEFT + 0.24, y + 0.03, 0.6, 0.66, [tag], size=19, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=WIPE_UP, spacing=1.0, font=FONT_HEAD, shrink=False)
        s.text(CONTENT_LEFT + 0.92, y + 0.03, CONTENT_WIDTH - 1.15, 0.66, [txt], size=13.5, color=WHITE,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.05)
        y += 0.82
    s.text(CONTENT_LEFT, 6.28, CONTENT_WIDTH, 0.34,
            ["Lưu ý: ngoài tuyển thẳng, Điều 14 còn quy định điểm ưu tiên (3 nhóm) và điểm khuyến khích."],
            size=11.5, color=MUTED, anim_kind=FADE, spacing=1.0, italic=True)
    s.text(CONTENT_LEFT, 6.65, CONTENT_WIDTH, 0.3, ["Nguồn: Điều 14 khoản 1 — Thông tư 30/2024/TT-BGDĐT"],
            size=9.5, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_12_scoring(deck)
    _slide_13_direct_admission(deck)

"""Title and agenda slides."""
from ..theme import (
    AMBER,
    BODY,
    CYAN,
    EDGE,
    FONT_HEAD,
    LIME,
    MUTED,
    PANEL,
    PANEL2,
    PINK,
    WHITE,
    CONTENT_LEFT,
    CONTENT_WIDTH,
    SLIDE_HEIGHT,
)
from ..animation import FADE, WIPE_UP
from pptx2.enum.text import MSO_ANCHOR, PP_ALIGN


def _slide_01_title(deck):
    s = deck.add_slide(None, None, notes="Slide tiêu đề. Chủ đề: thông tin tuyển sinh lớp 10 năm 2025 tại Việt Nam.\n"
        "Số liệu toàn bộ bài nói là của KỲ THI NĂM 2025 (năm học 2025–2026).\n"
        "Nguồn chính: Thông tư 30/2024/TT-BGDĐT.", label="title")
    s.rect(0, 0, 0.22, SLIDE_HEIGHT, LIME, kind=WIPE_UP, radius=0)
    s.rect(0.22, 0, 0.1, SLIDE_HEIGHT, PINK, kind=WIPE_UP, radius=0)
    s.text(1.0, 1.32, 10.4, 0.34, ["KỲ THI VÀO LỚP 10 · VIỆT NAM · 2025"], size=12.5,
            color=LIME, bold=True, anim_kind=FADE, spacing=1.0, font=FONT_HEAD)
    s.text(0.98, 1.78, 9.9, 2.0, ["Tuyển sinh lớp 10", "năm 2025"], size=54, color=WHITE,
            bold=True, anim_kind=FADE, spacing=0.92, font=FONT_HEAD,
            sizes=[54, 54], space_after=2)
    s.text(1.0, 3.72, 9.6, 0.5,
            ["Toàn cảnh luật chơi mới và số liệu thật của kỳ thi năm 2025"],
            size=17, color=BODY, anim_kind=FADE, spacing=1.1)
    s.text(1.0, 4.22, 9.6, 0.4,
            ["Thông tư 30/2024/TT-BGDĐT — hiệu lực 14/02/2025"],
            size=13, color=CYAN, bold=True, anim_kind=FADE, spacing=1.0)
    cx = 1.0
    for txt, acc in [("3 môn thi", LIME), ("Môn thứ ba: công bố ≤ 31/3", CYAN),
                     ("63/63 tỉnh, thành công bố phương án", PINK)]:
        cx += s.chip(cx, 4.92, txt, accent=acc) + 0.18
    s.text(1.0, 6.05, 9.6, 0.4, ["Người trình bày: [Tên của bạn]  ·  Lớp: [Lớp]  ·  [Ngày]"],
            size=12, color=MUTED, anim_kind=FADE, spacing=1.0, italic=True)
    s.rect(10.62, 1.55, 1.95, 1.95, PANEL2, radius=0.12, line=LIME, line_w=1.25, kind=WIPE_UP)
    s.text(10.62, 1.82, 1.95, 1.0, ["10"], size=54, color=LIME, bold=True,
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=0.9,
            font=FONT_HEAD, shrink=False)
    s.text(10.62, 2.86, 1.95, 0.5, ["Kỳ thi", "lớp 10"], size=12, color=BODY,
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP, anim_kind=FADE, spacing=1.05, space_after=0)
    s.rect(10.62, 3.72, 1.95, 0.09, PINK, radius=0, kind=WIPE_UP)
    s.text(10.62, 3.95, 1.95, 1.2,
            ["Dữ liệu:", "kỳ thi 2025"], size=11, color=MUTED, align=PP_ALIGN.CENTER,
            anim_kind=FADE, spacing=1.15)
    s.footer(show_page=False)
    s.finish()


def _slide_02_agenda(deck):
    s = deck.add_slide("NỘI DUNG", "Hôm nay nói gì?", notes="Giới thiệu 5 phần. Tổng thời lượng gợi ý: 8–10 phút.\n"
        "Phần 2 (môn thi, thời gian) và phần 3 (xu hướng toàn quốc) là phần 'luật chơi'.\n"
        "Phần 4 là số liệu thật của Hà Nội, TP.HCM và Cần Thơ.")
    items = [
        ("01", "Luật chơi mới: Thông tư 30/2024/TT-BGDĐT", LIME),
        ("02", "Môn thi, thời gian làm bài, nội dung thi", CYAN),
        ("03", "Môn thứ ba năm 2025: cả nước chọn gì?", PINK),
        ("04", "Số liệu thật: Hà Nội · TP.HCM · Cần Thơ", AMBER),
        ("05", "Điểm, tuyển thẳng, và checklist trước ngày thi", LIME),
    ]
    y = 2.05
    for num, txt, acc in items:
        s.rect(CONTENT_LEFT, y, CONTENT_WIDTH, 0.78, PANEL, radius=0.09, line=EDGE, kind=None)
        s.text(CONTENT_LEFT + 0.28, y + 0.06, 0.9, 0.66, [num], size=20, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=WIPE_UP, spacing=1.0, font=FONT_HEAD, shrink=False)
        s.text(CONTENT_LEFT + 1.25, y + 0.06, CONTENT_WIDTH - 1.6, 0.66, [txt], size=16, color=WHITE,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0)
        s.rect(CONTENT_LEFT + 1.15, y + 0.14, 0.045, 0.5, acc, radius=0, kind=WIPE_UP)
        y += 0.9
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_01_title(deck)
    _slide_02_agenda(deck)

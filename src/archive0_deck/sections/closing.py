"""Timeline, checklist, the joke slide, sources and thanks."""
from ..theme import (
    AMBER,
    BODY,
    CYAN,
    EDGE,
    FONT_HEAD,
    LIME,
    MUTED,
    MUTED2,
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

_COLUMN_W = (CONTENT_WIDTH - 0.3) / 2


def _slide_14_timeline(deck):
    s = deck.add_slide("PHẦN 05 · ĐIỂM & NGUYỆN VỌNG", "Dòng thời gian kỳ thi 2025", notes="Các mốc đã được kiểm chứng:\n"
        "30/12/2024 — Bộ GD&ĐT ban hành Thông tư 30/2024/TT-BGDĐT.\n"
        "14/02/2025 — Thông tư có hiệu lực.\n"
        "26/02/2025 — Sở GD&ĐT Hà Nội công bố môn thứ ba là Ngoại ngữ (VnExpress).\n"
        "Đầu tháng 4/2025 — TP.HCM công bố 70.070 chỉ tiêu lớp 10 công lập (Sở GD&ĐT TP.HCM).\n"
        "11/4/2025 — Hà Nội công bố 79.740 chỉ tiêu vào 122 trường công lập (Tuổi Trẻ).\n"
        "5–7/6/2025 — các địa phương tổ chức thi: Cần Thơ 5–6/6; TP.HCM 6–7/6; Hà Nội 7–8/6.\n"
        "14/6/2025 — Cần Thơ công bố kết quả thi (Tuổi Trẻ).\n"
        "04/7/2025 — Hà Nội công bố điểm thi và điểm chuẩn cùng ngày (giaoduc247.vn).")
    tl = [("30/12/2024", "Bộ GD&ĐT ban hành Thông tư 30/2024/TT-BGDĐT", LIME),
          ("14/02/2025", "Thông tư có hiệu lực thi hành", CYAN),
          ("26/02/2025", "Hà Nội công bố môn thi thứ ba: Ngoại ngữ", PINK),
          ("Đầu 4/2025", "TP.HCM công bố 70.070 chỉ tiêu lớp 10 công lập", AMBER),
          ("11/4/2025", "Hà Nội công bố 79.740 chỉ tiêu vào 122 trường công lập", LIME),
          ("5–7/6/2025", "Các địa phương tổ chức thi (Cần Thơ 5–6/6; TP.HCM 6–7/6; Hà Nội 7–8/6)", CYAN),
          ("14/6 → 4/7/2025", "Cần Thơ công bố kết quả (14/6); Hà Nội công bố điểm thi & điểm chuẩn (4/7)", PINK)]
    y = 2.0
    for i, (date, txt, acc) in enumerate(tl):
        s.rect(CONTENT_LEFT, y, CONTENT_WIDTH, 0.62, PANEL, radius=0.08, line=EDGE, kind=None)
        s.rect(CONTENT_LEFT, y, 0.075, 0.62, acc, radius=0, kind=WIPE_UP)
        s.text(CONTENT_LEFT + 0.26, y + 0.02, 1.85, 0.58, [date], size=12, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0, font=FONT_HEAD)
        s.text(CONTENT_LEFT + 2.2, y + 0.02, CONTENT_WIDTH - 2.45, 0.58, [txt], size=12.5, color=WHITE,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0)
        y += 0.66
    s.text(CONTENT_LEFT, 6.68, CONTENT_WIDTH, 0.3, ["Nguồn: Thông tư 30/2024/TT-BGDĐT · VnExpress · Tuổi Trẻ · giaoduc247.vn · Sở GD&ĐT TP.HCM"],
            size=9.5, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_15_checklist(deck):
    s = deck.add_slide("PHẦN 05 · ĐIỂM & NGUYỆN VỌNG", "Checklist trước ngày thi", notes="Checklist được suy ra trực tiếp từ các quy định đã nêu, không thêm dữ kiện mới:\n"
        "1) Biết địa phương tuyển sinh theo phương thức nào (Điều 9).\n"
        "2) Theo dõi công bố môn thi thứ ba, muộn nhất 31/3 (Điều 13 khoản 1b).\n"
        "3) Đọc kỹ kế hoạch tuyển sinh và chỉ tiêu (Điều 12; ví dụ Hà Nội 79.740, TP.HCM 70.070).\n"
        "4) Ôn chắc kiến thức lớp 9 (Điều 13 khoản 1d).\n"
        "5) Chuẩn bị hồ sơ cho diện tuyển thẳng / ưu tiên / khuyến khích nếu thuộc diện (Điều 14).\n"
        "6) TP.HCM: dự thi đủ 3 bài, không để bài nào điểm 0.\n"
        "7) Nắm quy định nguyện vọng của thành phố mình (ví dụ TP.HCM: trúng NV nào học NV đó).")
    left_items = [("1", "Biết địa phương mình tuyển sinh theo phương thức nào: xét tuyển, thi tuyển hay kết hợp.", LIME),
                  ("2", "Theo dõi công bố môn thi thứ ba — muộn nhất 31/3 hằng năm.", CYAN),
                  ("3", "Đọc kỹ kế hoạch tuyển sinh & chỉ tiêu của Sở GD&ĐT địa phương.", PINK),
                  ("4", "Ôn chắc kiến thức lớp 9 — nội dung thi chủ yếu nằm ở lớp 9.", AMBER)]
    right_items = [("5", "Chuẩn bị hồ sơ nếu thuộc diện tuyển thẳng / ưu tiên / khuyến khích.", LIME),
                   ("6", "TP.HCM: dự thi đủ 3 bài và không để bài thi nào bị điểm 0.", CYAN),
                   ("7", "Nắm quy định nguyện vọng của thành phố mình trước khi đăng ký.", PINK)]
    y = 2.05
    for tag, txt, acc in left_items:
        s.rect(CONTENT_LEFT, y, _COLUMN_W, 0.92, PANEL, radius=0.08, line=EDGE, kind=None)
        s.text(CONTENT_LEFT + 0.22, y + 0.05, 0.5, 0.82, [tag], size=18, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=WIPE_UP, spacing=1.0, font=FONT_HEAD,
                shrink=False)
        s.text(CONTENT_LEFT + 0.82, y + 0.05, _COLUMN_W - 1.05, 0.82, [txt], size=12.5, color=BODY,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.12)
        y += 1.02
    y = 2.05
    for tag, txt, acc in right_items:
        s.rect(CONTENT_LEFT + _COLUMN_W + 0.3, y, _COLUMN_W, 0.92, PANEL, radius=0.08, line=EDGE, kind=None)
        s.text(CONTENT_LEFT + _COLUMN_W + 0.52, y + 0.05, 0.5, 0.82, [tag], size=18, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=WIPE_UP, spacing=1.0, font=FONT_HEAD,
                shrink=False)
        s.text(CONTENT_LEFT + _COLUMN_W + 1.12, y + 0.05, _COLUMN_W - 1.35, 0.82, [txt], size=12.5, color=BODY,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.12)
        y += 1.02
    s.rect(CONTENT_LEFT + _COLUMN_W + 0.3, y, _COLUMN_W, 1.35, PANEL2, radius=0.08, line=LIME, line_w=1.25, kind=WIPE_UP)
    s.text(CONTENT_LEFT + _COLUMN_W + 0.52, y + 0.08, _COLUMN_W - 0.44, 1.2,
            ["Note", "Môn thứ ba công bố muộn nhất 31/3 → bạn có thêm thời gian để \"tune\" lại kế hoạch ôn tập."],
            size=12.5, color=BODY, anim_kind=FADE, spacing=1.15, space_after=4,
            sizes=[15, 12.5], colors=[LIME, BODY], bolds=[True, False])
    s.footer(); s.finish()


def _slide_16_joke(deck):
    s = deck.add_slide("GIẢI LAO", "Góc hài hước (tự thêm joke của bạn)", notes="Slide dành sẵn cho phần hài hước của người trình bày.\n"
        "Khung lớn bên trên là chỗ dán câu joke: bấm vào khung và gõ đè lên phần chữ trong ngoặc vuông, "
        "không cần chỉnh layout.\n"
        "Câu ở khung dưới là câu an toàn, có thể giữ hoặc xoá: nó chỉ nhắc lại đúng một quy định "
        "(môn thứ ba công bố muộn nhất 31/3 hằng năm).\n"
        "Nguồn quy định: Điều 13 khoản 1b Thông tư 30/2024/TT-BGDĐT.")
    s.rect(CONTENT_LEFT, 2.05, CONTENT_WIDTH, 2.45, PANEL2, radius=0.08, line=LIME, line_w=1.5, kind=WIPE_UP)
    s.text(CONTENT_LEFT + 0.45, 2.2, CONTENT_WIDTH - 0.9, 2.15,
            ["[Dán câu joke của bạn vào đây]", "Khung này đã chừa sẵn chỗ — cứ gõ đè lên dòng chữ trong ngoặc vuông."],
            size=24, color=LIME, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
            anim_kind=FADE, spacing=1.15, space_after=10,
            sizes=[26, 13], colors=[LIME, MUTED], bolds=[True, False])
    s.rect(CONTENT_LEFT, 4.7, CONTENT_WIDTH, 1.35, PANEL, radius=0.08, line=EDGE, kind=None)
    s.text(CONTENT_LEFT + 0.45, 4.82, CONTENT_WIDTH - 0.9, 1.1,
            ["Còn môn thi thứ ba thì sao?", "\"Bí mật\" dài nhất cũng chỉ tới 31/3 — sau đó cả nước biết môn mình thi."],
            size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
            anim_kind=FADE, spacing=1.2, space_after=6,
            sizes=[15, 13.5], colors=[WHITE, BODY], bolds=[True, False])
    s.text(CONTENT_LEFT, 6.25, CONTENT_WIDTH, 0.34,
            ["Mẹo nhỏ: muốn đổi joke, bấm vào khung và sửa chữ — không cần chỉnh thiết kế slide."],
            size=11, color=MUTED2, align=PP_ALIGN.CENTER, anim_kind=FADE, spacing=1.0, italic=True)
    s.text(CONTENT_LEFT, 6.62, CONTENT_WIDTH, 0.3, ["Quy định được nhắc ở đây: Điều 13 khoản 1b — Thông tư 30/2024/TT-BGDĐT"],
            size=9.5, color=MUTED2, align=PP_ALIGN.CENTER, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_17_sources(deck):
    s = deck.add_slide("MINH BẠCH", "Nguồn tham khảo", notes="Danh sách nguồn đầy đủ kèm đường dẫn:\n"
        "1. Thông tư 30/2024/TT-BGDĐT (toàn văn, PDF) — Bộ GD&ĐT, 30/12/2024: "
        "https://xdcs.cdnchinhphu.vn/446259493575335936/2025/1/8/302024ttbgddtsigned-17363169420611167548229.pdf\n"
        "2. \"TOÀN VĂN: Thông tư 30/TT-BGDĐT…\" — Cổng TTĐT Chính phủ, 04/02/2025: "
        "https://xaydungchinhsach.chinhphu.vn/thong-tu-30-tt-bgddt-quy-che-tuyen-sinh-thcs-va-tuyen-sinh-thpt-11925010810085927.htm\n"
        "3. \"Bộ Giáo dục chốt quy chế thi lớp 10\" — VnExpress, 08/01/2025: "
        "https://vnexpress.net/bo-giao-duc-chot-quy-che-thi-lop-10-4830885.html\n"
        "4. \"Chi tiết môn thi thứ 3 vào lớp 10 của 63 tỉnh thành\" — VTV, 03/03/2025: "
        "https://vtv.vn/giao-duc/chi-tiet-mon-thi-thu-3-vao-lop-10-cua-63-tinh-thanh-20250303143924782.htm\n"
        "5. \"Hà Nội công bố môn thứ ba thi lớp 10\" — VnExpress, 26/02/2025: "
        "https://vnexpress.net/ha-noi-cong-bo-mon-thu-ba-thi-lop-10-4849639.html\n"
        "6. \"Chi tiết lịch thi tuyển sinh vào lớp 10 của Hà Nội năm học 2025-2026\" — VietnamPlus, 24/02/2025: "
        "https://www.vietnamplus.vn/chi-tiet-lich-thi-tuyen-sinh-vao-lop-10-cua-ha-noi-nam-hoc-2025-2026-post1014045.vnp\n"
        "7. \"Chi tiêu tuyển sinh lớp 10 tại Hà Nội năm 2025: 79.740 suất…\" — Tuổi Trẻ, 11/4/2025.\n"
        "8. \"Công bố chỉ tiêu lớp 10 công lập ở TP HCM năm 2025\" — VnExpress, 11/4/2025.\n"
        "9. \"TP.HCM công bố số lượng thí sinh đăng ký dự thi tuyển sinh lớp 10 năm học 2025–2026\" — "
        "Sở GD&ĐT TP.HCM, 15/5/2025.\n"
        "10. \"Môn thi thứ ba vào lớp 10 tại 63 tỉnh thành\" — Dân trí, 20/01/2025: "
        "https://dantri.com.vn/giao-duc/mon-thi-thu-ba-vao-lop-10-tai-63-tinh-thanh-20250120000312429.htm\n"
        "11. \"Kỳ thi tuyển sinh vào lớp 10 TP Cần Thơ năm nay có gì mới?\" — Tuổi Trẻ, 19/3/2025; "
        "\"Công bố điểm thi vào lớp 10 THPT Cần Thơ, điểm chuẩn giảm\" — Tuổi Trẻ, 14/6/2025.\n"
        "12. Hà Nội: hơn 127.000 thí sinh và công bố điểm chuẩn ngày 4/7 — giaoduc247.vn, 2025.\n"
        "13. \"Điểm xét tuyển\" Hà Nội — VOV2, 24/02/2025.")
    src_left = [("Thông tư 30/2024/TT-BGDĐT (toàn văn)", "Bộ GD&ĐT · 30/12/2024"),
                ("TOÀN VĂN: Thông tư 30/TT-BGDĐT", "Cổng TTĐT Chính phủ · 04/02/2025"),
                ("Bộ Giáo dục chốt quy chế thi lớp 10", "VnExpress · 08/01/2025"),
                ("Chi tiết môn thi thứ 3 vào lớp 10 của 63 tỉnh thành", "VTV · 03/03/2025"),
                ("Hà Nội công bố môn thứ ba thi lớp 10", "VnExpress · 26/02/2025"),
                ("Chi tiết lịch thi tuyển sinh vào lớp 10 của Hà Nội", "VietnamPlus · 24/02/2025")]
    src_right = [("Chỉ tiêu tuyển sinh lớp 10 tại Hà Nội: 79.740 suất", "Tuổi Trẻ · 11/4/2025"),
                 ("Công bố chỉ tiêu lớp 10 công lập ở TP HCM", "VnExpress · 11/4/2025"),
                 ("Số thí sinh đăng ký dự thi lớp 10 TP.HCM", "Sở GD&ĐT TP.HCM · 15/5/2025"),
                 ("Kỳ thi tuyển sinh lớp 10 TP Cần Thơ; công bố điểm thi", "Tuổi Trẻ · 19/3 & 14/6/2025"),
                 ("Môn thi thứ ba vào lớp 10 tại 63 tỉnh thành", "Dân trí · 20/01/2025"),
                 ("Hà Nội: hơn 127.000 thí sinh; điểm chuẩn 4/7", "giaoduc247.vn · 2025")]
    y = 2.02
    for i in range(6):
        yy = y + i * 0.72
        s.rect(CONTENT_LEFT, yy, _COLUMN_W, 0.64, PANEL, radius=0.07, line=EDGE, kind=None)
        t, d = src_left[i]
        s.text(CONTENT_LEFT + 0.18, yy + 0.03, _COLUMN_W - 0.36, 0.58, [t, d], size=11.5, color=WHITE,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0, space_after=1, sizes=[11.5, 9], colors=[WHITE, MUTED2],
                bolds=[False, False])
        s.rect(CONTENT_LEFT + _COLUMN_W + 0.3, yy, _COLUMN_W, 0.64, PANEL, radius=0.07, line=EDGE, kind=None)
        t, d = src_right[i]
        s.text(CONTENT_LEFT + _COLUMN_W + 0.48, yy + 0.03, _COLUMN_W - 0.36, 0.58, [t, d], size=11.5, color=WHITE,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0, space_after=1, sizes=[11.5, 9], colors=[WHITE, MUTED2],
                bolds=[False, False])
    s.text(CONTENT_LEFT, 6.62, CONTENT_WIDTH, 0.34,
            ["Đường dẫn đầy đủ của từng nguồn nằm trong phần ghi chú (speaker notes) của slide này."],
            size=11, color=MUTED, anim_kind=FADE, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_18_thanks(deck):
    s = deck.add_slide(None, None, notes="Tóm tắt 3 điều cần nhớ:\n"
        "1) Thi tuyển lớp 10 = Toán + Ngữ văn + môn thứ ba (công bố muộn nhất 31/3).\n"
        "2) Điểm xét tuyển theo thang điểm 10 cho mỗi môn; điểm chuẩn công bố cùng ngày với điểm thi.\n"
        "3) Số liệu bài này là của kỳ thi năm 2025 — các năm sau có thể khác.\n"
        "Nếu cần bổ sung phần hỏi đáp, thêm slide sau slide này.", label="thanks")
    s.rect(0, 0, 0.22, SLIDE_HEIGHT, LIME, kind=WIPE_UP, radius=0)
    s.text(1.1, 2.15, 10.6, 1.3, ["Cảm ơn!"], size=54, color=WHITE, bold=True,
            anim_kind=FADE, spacing=0.95, font=FONT_HEAD, shrink=False)
    s.text(1.15, 3.5, 10.4, 0.5, ["3 điều nên nhớ trước khi rời khỏi slide này"],
            size=15, color=LIME, bold=True, anim_kind=FADE, spacing=1.0)
    lines = [("1", "Thi tuyển lớp 10 = Toán + Ngữ văn + môn thứ ba (công bố muộn nhất 31/3).", LIME),
             ("2", "Điểm xét tuyển theo thang điểm 10 cho mỗi môn; điểm chuẩn công bố cùng ngày với điểm thi.", CYAN),
             ("3", "Số liệu trong bài là của kỳ thi năm 2025 — các năm sau có thể khác.", PINK)]
    y = 4.15
    for i, (tag, txt, acc) in enumerate(lines):
        s.rect(1.1, y, 11.4, 0.66, PANEL, radius=0.08, line=EDGE, kind=None)
        s.text(1.32, y + 0.03, 0.45, 0.6, [tag], size=16, color=acc, bold=True,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=WIPE_UP, spacing=1.0, font=FONT_HEAD, shrink=False)
        s.text(1.85, y + 0.03, 10.4, 0.6, [txt], size=13, color=BODY,
                anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.05)
        y += 0.74
    s.text(1.15, 6.42, 10.4, 0.4, ["Hỏi đáp (Q&A) — nguồn đầy đủ ở slide 17."],
            size=12.5, color=MUTED, anim_kind=FADE, spacing=1.0, italic=True)
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_14_timeline(deck)
    _slide_15_checklist(deck)
    _slide_16_joke(deck)
    _slide_17_sources(deck)
    _slide_18_thanks(deck)

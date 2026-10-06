"""The regulation: admission methods, subjects, deadlines, durations."""
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
    CONTENT_LEFT,
    CONTENT_RIGHT,
    CONTENT_WIDTH,
)
from ..animation import FADE, WIPE_UP
from pptx2.enum.text import MSO_ANCHOR, PP_ALIGN

_THIRD_CARD_W = (CONTENT_WIDTH - 2 * 0.26) / 3


def _slide_03_why_2025(deck):
    s = deck.add_slide("PHẦN 01 · LUẬT CHƠI MỚI", "Vì sao 2025 là năm bản lề?", notes="Ba điểm cần nhấn:\n"
        "1) 2025 là năm đầu tiên kỳ thi lớp 10 theo Chương trình GDPT 2018 (VnExpress 8/1/2025; "
        "VietnamNet).\n"
        "2) Quy chế mới: Thông tư 30/2024/TT-BGDĐT ban hành 30/12/2024, hiệu lực 14/02/2025, "
        "thay thế Thông tư 11/2014/TT-BGDĐT.\n"
        "3) Ba nguyên tắc cốt lõi của Bộ GD&ĐT theo bài giới thiệu trên Cổng TTĐT Chính phủ "
        "(04/02/2025).\n"
        "Nguồn: xaydungchinhsach.chinhphu.vn/thong-tu-30-tt-bgddt-quy-che-tuyen-sinh-thcs-va-tuyen-sinh-thpt-11925010810085927.htm")
    s.card(CONTENT_LEFT, 2.05, _THIRD_CARD_W, 3.95, "Chương trình mới",
           ["2025 là năm đầu tiên kỳ thi tuyển sinh lớp 10 được tổ chức theo Chương trình "
            "giáo dục phổ thông 2018.",
            "Học sinh lớp 9 năm học 2024–2025 là lứa đầu tiên thi theo chương trình mới."],
           accent=LIME, source="Nguồn: VnExpress, 08/01/2025")
    s.card(CONTENT_LEFT + _THIRD_CARD_W + 0.26, 2.05, _THIRD_CARD_W, 3.95, "Quy chế mới",
           ["Thông tư 30/2024/TT-BGDĐT ban hành ngày 30/12/2024.",
            "Có hiệu lực từ 14/02/2025 và thay thế Thông tư 11/2014/TT-BGDĐT.",
            "Lần đầu có quy định chung toàn quốc về số môn thi lớp 10."],
           accent=CYAN, source="Nguồn: Thông tư 30/2024/TT-BGDĐT")
    s.card(CONTENT_LEFT + 2 * (_THIRD_CARD_W + 0.26), 2.05, _THIRD_CARD_W, 3.95, "3 nguyên tắc của Bộ",
           ["1. Không gây áp lực, tốn kém cho học sinh, phụ huynh và xã hội.",
            "2. Thúc đẩy giáo dục toàn diện, chuẩn bị năng lực cho cấp học cao hơn.",
            "3. Quy định thống nhất toàn quốc, đồng thời phân cấp rõ trách nhiệm."],
           accent=PINK, source="Nguồn: Cổng TTĐT Chính phủ, 04/02/2025")
    s.footer(); s.finish()


def _slide_04_methods(deck):
    s = deck.add_slide("PHẦN 01 · LUẬT CHƠI MỚI", "Có 3 phương thức tuyển sinh", notes="Điều 9 Quy chế (Thông tư 30/2024/TT-BGDĐT): tuyển sinh THPT tổ chức 01 lần/năm theo "
        "01 trong 03 phương thức: xét tuyển, thi tuyển, hoặc kết hợp.\n"
        "Xét tuyển căn cứ kết quả rèn luyện và học tập các năm học cấp THCS (lưu ban lớp nào "
        "thì lấy kết quả năm học lại của lớp đó).\n"
        "Thi tuyển thực hiện theo Điều 13. Kết hợp = xét tuyển + thi tuyển.\n"
        "Thẩm quyền lựa chọn phương thức thuộc về địa phương.\n"
        "Nguồn: Toàn văn Thông tư 30/2024/TT-BGDĐT (PDF) trên Cổng TTĐT Chính phủ.")
    s.card(CONTENT_LEFT, 2.05, _THIRD_CARD_W, 3.4, "1 · XÉT TUYỂN",
           ["Căn cứ là kết quả rèn luyện và kết quả học tập các năm học cấp THCS.",
            "Không tổ chức thi."], accent=LIME)
    s.card(CONTENT_LEFT + _THIRD_CARD_W + 0.26, 2.05, _THIRD_CARD_W, 3.4, "2 · THI TUYỂN",
           ["Thực hiện theo Điều 13: Toán, Ngữ văn và 01 môn thi hoặc bài thi thứ ba.",
            "Là phương thức phổ biến nhất trong kỳ thi 2025."],
           accent=CYAN)
    s.card(CONTENT_LEFT + 2 * (_THIRD_CARD_W + 0.26), 2.05, _THIRD_CARD_W, 3.4, "3 · KẾT HỢP",
           ["Kết hợp thi tuyển với xét tuyển theo quy định của cả hai phương thức trên."],
           accent=PINK)
    s.rect(CONTENT_LEFT, 5.68, CONTENT_WIDTH, 0.72, PANEL2, radius=0.08, line=LIME, line_w=1.0, kind=WIPE_UP)
    s.text(CONTENT_LEFT + 0.25, 5.72, CONTENT_WIDTH - 0.5, 0.64,
            ["Mỗi địa phương chọn 01 trong 03 phương thức  ·  Tuyển sinh THPT được tổ chức 01 lần/năm"],
            size=14, color=LIME, bold=True, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE,
            spacing=1.0)
    s.text(CONTENT_LEFT, 6.5, CONTENT_WIDTH, 0.34, ["Điều 9 — Quy chế tuyển sinh THCS và THPT (Thông tư 30/2024/TT-BGDĐT)"],
            size=10, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_05_subjects(deck):
    s = deck.add_slide("PHẦN 02 · MÔN THI", "Thi tuyển: Toán + Ngữ văn + môn thứ ba", notes="Điều 13 khoản 1: số môn thi gồm Toán, Ngữ văn và 01 môn thi hoặc bài thi thứ ba do "
        "Sở GD&ĐT lựa chọn.\n"
        "Môn thi thứ ba: chọn trong các môn có đánh giá bằng điểm số ở cấp THCS; không chọn cùng "
        "một môn quá 03 năm liên tiếp.\n"
        "Bài thi thứ ba: là bài thi tổ hợp của một số môn học.\n"
        "Danh sách môn có thể được chọn (theo VnExpress 08/01/2025): Ngoại ngữ 1, Giáo dục công dân, "
        "Khoa học tự nhiên, Lịch sử và Địa lý, Công nghệ, Tin học.\n"
        "Trường THPT chuyên: thí sinh thi thêm 01 môn chuyên (Điều 13 khoản 1đ).")
    wcard = (CONTENT_WIDTH - 2 * 0.7) / 3
    y0 = 2.15
    for i, (name, acc) in enumerate([("TOÁN", LIME), ("NGỮ VĂN", CYAN), ("MÔN THỨ BA", PINK)]):
        x = CONTENT_LEFT + i * (wcard + 0.7)
        s.rect(x, y0, wcard, 1.05, PANEL2, radius=0.08, line=acc, line_w=1.25, kind=WIPE_UP)
        s.text(x + 0.1, y0 + 0.05, wcard - 0.2, 0.95, [name], size=17, color=acc, bold=True,
                align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.0,
                font=FONT_HEAD)
        if i < 2:
            s.text(x + wcard, y0 + 0.15, 0.7, 0.75, ["+"], size=26, color=MUTED,
                    align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE,
                    spacing=1.0, font=FONT_HEAD, shrink=False)
    s.text(CONTENT_LEFT, 3.42, CONTENT_WIDTH, 0.36,
            ["Môn thứ ba được chọn từ các môn có đánh giá bằng điểm số ở cấp THCS:"],
            size=13.5, color=BODY, anim_kind=FADE, spacing=1.0)
    chips = ["Ngoại ngữ 1", "Giáo dục công dân", "Khoa học tự nhiên",
             "Lịch sử và Địa lý", "Công nghệ", "Tin học"]
    cx, cy = CONTENT_LEFT, 3.86
    for i, t in enumerate(chips):
        w = s.chip(cx, cy, t, accent=CYAN)
        cx += w + 0.16
        if cx > CONTENT_RIGHT - 2.2 and i < len(chips) - 1:
            cx = CONTENT_LEFT; cy += 0.56
    s.rect(CONTENT_LEFT, 5.34, CONTENT_WIDTH, 1.06, PANEL, radius=0.07, line=EDGE, kind=None)
    s.text(CONTENT_LEFT + 0.25, 5.42, CONTENT_WIDTH - 0.5, 0.9,
            ["Hoặc: bài thi thứ ba là bài thi tổ hợp của một số môn học.",
             "Trường THPT chuyên: thí sinh thi các môn trên và thêm 01 môn chuyên."],
            size=13, color=BODY, anim_kind=FADE, spacing=1.15, space_after=4)
    s.text(CONTENT_LEFT, 6.52, CONTENT_WIDTH, 0.3, ["Nguồn: Điều 13 Thông tư 30/2024/TT-BGDĐT  ·  VnExpress, 08/01/2025"],
            size=10, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_06_deadlines(deck):
    s = deck.add_slide("PHẦN 02 · MÔN THI", "Hai mốc thời gian phải nhớ", notes="Điều 13 khoản 1b: môn thi/bài thi thứ ba được công bố sau khi kết thúc học kì I nhưng "
        "không muộn hơn ngày 31 tháng 3 hằng năm.\n"
        "Điều 13 khoản 1a: không chọn cùng một môn thi thứ ba quá 03 năm liên tiếp.\n"
        "Điều 12: kế hoạch tuyển sinh THPT được công bố trước ngày 31 tháng 3 hằng năm.\n"
        "Ví dụ 2025: Hà Nội công bố môn thứ ba (Ngoại ngữ) ngày 26/02/2025 — trong hạn.\n"
        "Nguồn: Toàn văn Thông tư 30/2024/TT-BGDĐT; VnExpress 26/02/2025.")
    s.kpi(CONTENT_LEFT, 2.1, (CONTENT_WIDTH - 0.3) / 2, 2.15, "31/3", "Hạn muộn nhất để công bố môn thi hoặc bài thi thứ ba hằng năm", LIME, value_size=46)
    s.kpi(CONTENT_LEFT + (CONTENT_WIDTH - 0.3) / 2 + 0.3, 2.1, (CONTENT_WIDTH - 0.3) / 2, 2.15, "3 năm", "Không chọn cùng một môn thi thứ ba quá 03 năm liên tiếp", PINK, value_size=40)
    s.rect(CONTENT_LEFT, 4.5, CONTENT_WIDTH, 1.9, PANEL, radius=0.07, line=EDGE, kind=None)
    s.text(CONTENT_LEFT + 0.28, 4.62, CONTENT_WIDTH - 0.56, 1.7,
            ["Kế hoạch tuyển sinh THPT của địa phương cũng được công bố trước ngày 31/3 hằng năm.",
             "Vì vậy môn thi thứ ba luôn là thông tin công khai, biết trước — học sinh có thời gian ôn tập đúng hướng.",
             "Điều này khác với đề xuất ban đầu (bốc thăm môn ngẫu nhiên) từng gây tranh luận năm 2024."],
            size=13.5, color=BODY, anim_kind=FADE, spacing=1.2, space_after=6)
    s.text(CONTENT_LEFT, 6.5, CONTENT_WIDTH, 0.3, ["Nguồn: Điều 12, Điều 13 khoản 1 — Thông tư 30/2024/TT-BGDĐT"],
            size=10, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_07_durations(deck):
    s = deck.add_slide("PHẦN 02 · MÔN THI", "Thời gian làm bài và nội dung thi", notes="Điều 13 khoản 1c: Ngữ văn 120 phút; Toán 90 hoặc 120 phút; môn thi thứ ba 60 hoặc 90 phút; "
        "bài thi tổ hợp 90 hoặc 120 phút.\n"
        "Điều 13 khoản 1d: nội dung thi nằm trong chương trình GDPT cấp THCS, chủ yếu là lớp 9.\n"
        "Địa phương chọn mức thời gian cụ thể: ví dụ 2025 — Hà Nội: Toán 120', Ngoại ngữ 60'; "
        "TP.HCM: Toán và Ngữ văn 120', Ngoại ngữ 90'; Cần Thơ: Toán và Ngữ văn 120', Ngoại ngữ 60'.")
    rows = [("Ngữ văn", "120 phút", LIME),
            ("Toán", "90 hoặc 120 phút", CYAN),
            ("Môn thi thứ ba", "60 hoặc 90 phút", PINK),
            ("Bài thi thứ ba (tổ hợp)", "90 hoặc 120 phút", AMBER)]
    y = 2.1
    for i, (subj, t, acc) in enumerate(rows):
        s.row(CONTENT_LEFT, y, CONTENT_WIDTH, 0.78, subj, t, accent=acc, size=15)
        y += 0.88
    s.rect(CONTENT_LEFT, 5.75, CONTENT_WIDTH, 0.72, PANEL2, radius=0.08, line=LIME, line_w=1.0, kind=WIPE_UP)
    s.text(CONTENT_LEFT + 0.25, 5.79, CONTENT_WIDTH - 0.5, 0.64,
            ["Nội dung thi: trong chương trình GDPT cấp THCS — chủ yếu là kiến thức lớp 9"],
            size=14, color=LIME, bold=True, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE,
            spacing=1.0)
    s.text(CONTENT_LEFT, 6.55, CONTENT_WIDTH, 0.3, ["Nguồn: Điều 13 khoản 1c, 1d — Thông tư 30/2024/TT-BGDĐT"],
            size=10, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_03_why_2025(deck)
    _slide_04_methods(deck)
    _slide_05_subjects(deck)
    _slide_06_deadlines(deck)
    _slide_07_durations(deck)

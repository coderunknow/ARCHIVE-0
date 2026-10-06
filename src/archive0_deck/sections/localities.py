"""Locality facts for the 2025 exam: Hà Nội, TP.HCM, Cần Thơ."""
from ..theme import AMBER, BODY, CYAN, LIME, MUTED2, PINK, CONTENT_LEFT, CONTENT_WIDTH

_KPI_W = (CONTENT_WIDTH - 3 * 0.22) / 4


def _slide_09_ha_noi(deck):
    s = deck.add_slide("PHẦN 04 · SỐ LIỆU THẬT", "Hà Nội 2025", notes="Hơn 127.000 thí sinh tham gia kỳ thi lớp 10 Hà Nội năm 2025 (giaoduc247, 2025).\n"
        "Chỉ tiêu: 79.740 suất vào 122 trường THPT công lập và công lập tự chủ (Tuổi Trẻ, 11/4/2025).\n"
        "Lịch thi 7–8/6/2025: sáng 7/6 Ngữ văn 120', chiều 7/6 Ngoại ngữ 60', sáng 8/6 Toán 120' "
        "(VietnamPlus 24/02/2025; VnExpress 26/02/2025).\n"
        "Môn thứ ba: Ngoại ngữ (Anh, Pháp, Đức, Nhật, Hàn), công bố 26/2/2025.\n"
        "Điểm xét tuyển = Toán + Ngữ văn + môn thứ ba + ưu tiên + khuyến khích (VOV2, 24/02/2025).\n"
        "Điểm chuẩn công bố chiều 4/7, cùng ngày công bố điểm thi (giaoduc247).")
    kp = [("127.000+", "thí sinh đăng ký nguyện vọng thi lớp 10", LIME),
          ("79.740", "chỉ tiêu vào 122 trường THPT công lập & tự chủ", CYAN),
          ("7–8/6", "ngày thi năm 2025", PINK),
          ("60 phút", "bài thi Ngoại ngữ (Toán, Ngữ văn: 120 phút)", AMBER)]
    for i, (v, l, acc) in enumerate(kp):
        s.kpi(CONTENT_LEFT + i * (_KPI_W + 0.22), 2.05, _KPI_W, 1.75, v, l, acc, value_size=27)
    facts = [("Môn thi thứ ba", "Ngoại ngữ (Anh, Pháp, Đức, Nhật, Hàn) — công bố 26/2/2025", LIME),
             ("Điểm xét tuyển", "Toán + Ngữ văn + môn thứ ba + điểm ưu tiên + khuyến khích", CYAN),
             ("Điểm chuẩn", "công bố chiều 4/7, cùng ngày công bố điểm thi", PINK)]
    y = 4.05
    for i, (l, r, acc) in enumerate(facts):
        s.row(CONTENT_LEFT, y, CONTENT_WIDTH, 0.74, l, r, accent=acc, size=13, left_w=2.6,
              right_color=BODY)
        y += 0.84
    s.text(CONTENT_LEFT, 6.56, CONTENT_WIDTH, 0.3,
            ["Nguồn: Tuổi Trẻ 11/4/2025 · VietnamPlus 24/02/2025 · VnExpress 26/02/2025 · VOV2 24/02/2025 · giaoduc247.vn"],
            size=9.5, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_10_tp_hcm(deck):
    s = deck.add_slide("PHẦN 04 · SỐ LIỆU THẬT", "TP.HCM 2025", notes="Chỉ tiêu lớp 10 công lập: 70.070 (công bố đầu tháng 4/2025), tương đương khoảng 79% số học "
        "sinh tốt nghiệp THCS — Sở GD&ĐT TP.HCM.\n"
        "Số đăng ký dự thi: 76.435 thí sinh lớp 10 thường; 5.550 thí sinh lớp 10 chuyên; 1.169 thí sinh "
        "lớp 10 tích hợp (Sở GD&ĐT TP.HCM, 15/5/2025).\n"
        "Ngày thi 6–7/6/2025; Ngữ văn và Toán 120 phút; Ngoại ngữ 90 phút.\n"
        "Nguyện vọng: tối đa 3 NV lớp 10 thường, 2 NV chuyên, 3 NV tích hợp (tổng tối đa 8).\n"
        "Trúng nguyện vọng nào phải học nguyện vọng đó và không được thay đổi; thí sinh trúng tuyển phải "
        "dự thi đủ 3 bài thi và không có bài thi nào bị điểm 0.\n"
        "Nguồn: Tuổi Trẻ 25/4/2025; Sở GD&ĐT TP.HCM 15/5/2025.")
    kp = [("70.070", "chỉ tiêu lớp 10 công lập (≈79% số tốt nghiệp THCS)", LIME),
          ("76.435", "thí sinh đăng ký thi lớp 10 thường", CYAN),
          ("6–7/6", "ngày thi năm 2025", PINK),
          ("90 phút", "bài thi Ngoại ngữ (Toán, Ngữ văn: 120 phút)", AMBER)]
    for i, (v, l, acc) in enumerate(kp):
        s.kpi(CONTENT_LEFT + i * (_KPI_W + 0.22), 2.05, _KPI_W, 1.75, v, l, acc, value_size=27)
    facts = [("Đăng ký nguyện vọng", "tối đa 3 NV thường + 2 NV chuyên + 3 NV tích hợp", LIME),
             ("Nguyên tắc", "trúng NV nào phải học NV đó, không được thay đổi", CYAN),
             ("Điều kiện trúng tuyển", "dự thi đủ 3 bài và không có bài thi nào bị điểm 0", PINK)]
    y = 4.05
    for i, (l, r, acc) in enumerate(facts):
        s.row(CONTENT_LEFT, y, CONTENT_WIDTH, 0.74, l, r, accent=acc, size=13, left_w=3.0,
              right_color=BODY)
        y += 0.84
    s.text(CONTENT_LEFT, 6.56, CONTENT_WIDTH, 0.3,
            ["Nguồn: Sở GD&ĐT TP.HCM (15/5/2025) · Tuổi Trẻ 25/4/2025 · VnExpress 11/4/2025"],
            size=9.5, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def _slide_11_can_tho(deck):
    s = deck.add_slide("PHẦN 04 · SỐ LIỆU THẬT", "Cần Thơ 2025", notes="Kế hoạch tuyển sinh lớp 10 năm học 2025–2026 của TP Cần Thơ: thi tuyển với 3 môn Toán, "
        "Ngữ văn và Ngoại ngữ (tiếng Anh hoặc tiếng Pháp); Toán và Ngữ văn 120 phút, Ngoại ngữ 60 phút "
        "(Tuổi Trẻ, 19/3/2025 — theo kế hoạch UBND thành phố).\n"
        "Kỳ thi diễn ra ngày 5 và 6/6/2025.\n"
        "Có 11.057 thí sinh đăng ký dự thi vào các trường THPT công lập.\n"
        "Cách tính điểm: tổng điểm 3 môn + điểm ưu tiên (nếu có), làm tròn 2 chữ số thập phân; năm 2025 "
        "không nhân hệ số 2 môn Ngữ văn, Toán như trước.\n"
        "Kết quả được công bố ngày 14/6/2025.\n"
        "Nguồn: Tuổi Trẻ 19/3/2025 và 14/6/2025.")
    kp = [("5–6/6", "ngày thi năm 2025", LIME),
          ("11.057", "thí sinh đăng ký dự thi THPT công lập", CYAN),
          ("60 phút", "bài thi Ngoại ngữ (Toán, Ngữ văn: 120 phút)", PINK),
          ("14/6", "ngày công bố kết quả thi", AMBER)]
    for i, (v, l, acc) in enumerate(kp):
        s.kpi(CONTENT_LEFT + i * (_KPI_W + 0.22), 2.05, _KPI_W, 1.75, v, l, acc, value_size=27)
    facts = [("Môn thi", "Toán, Ngữ văn và Ngoại ngữ (tiếng Anh hoặc tiếng Pháp)", LIME),
             ("Cách tính điểm", "tổng điểm 3 môn + điểm ưu tiên; làm tròn 2 chữ số thập phân", CYAN),
             ("Thay đổi năm 2025", "không nhân hệ số 2 môn Ngữ văn, Toán như các năm trước", PINK)]
    y = 4.05
    for i, (l, r, acc) in enumerate(facts):
        s.row(CONTENT_LEFT, y, CONTENT_WIDTH, 0.74, l, r, accent=acc, size=13, left_w=2.9,
              right_color=BODY)
        y += 0.84
    s.text(CONTENT_LEFT, 6.56, CONTENT_WIDTH, 0.3, ["Nguồn: Tuổi Trẻ 19/3/2025 (kế hoạch của UBND TP Cần Thơ) · Tuổi Trẻ 14/6/2025"],
            size=9.5, color=MUTED2, anim_kind=None, spacing=1.0, italic=True)
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_09_ha_noi(deck)
    _slide_10_tp_hcm(deck)
    _slide_11_can_tho(deck)

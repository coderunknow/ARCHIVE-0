"""Nationwide third-subject picture for the 2025 cycle."""
from ..theme import AMBER, BODY, CYAN, LIME, CONTENT_LEFT, CONTENT_WIDTH
from ..animation import FADE
from pptx2.enum.text import MSO_ANCHOR


def _slide_08_third_subject_2025(deck):
    s = deck.add_slide("PHẦN 03 · XU HƯỚNG", "Môn thứ ba năm 2025: cả nước chọn gì?", notes="Số liệu ngày 03/03/2025 (VTV): 63 địa phương đã công bố phương án tuyển sinh lớp 10 "
        "năm học 2025–2026; đa số chọn Tiếng Anh là môn thứ ba.\n"
        "Ngoại lệ: Hà Giang chọn Lịch sử và Địa lý; Bình Thuận chọn Lịch sử và Địa lý nhưng chỉ áp "
        "dụng với trường phổ thông dân tộc nội trú, các trường khác thi Tiếng Anh.\n"
        "03 địa phương chọn xét tuyển: Cà Mau, Vĩnh Long, Gia Lai.\n"
        "Nguồn: https://vtv.vn/giao-duc/chi-tiet-mon-thi-thu-3-vao-lop-10-cua-63-tinh-thanh-20250303143924782.htm\n"
        "Ví dụ Tiền Giang: Dân trí, 18–20/01/2025 — "
        "https://dantri.com.vn/giao-duc/mon-thi-thu-ba-vao-lop-10-tai-63-tinh-thanh-20250120000312429.htm")
    s.kpi(CONTENT_LEFT, 2.05, 3.4, 1.6, "63/63", "địa phương công bố phương án tuyển sinh lớp 10", LIME,
          value_size=34)
    s.text(CONTENT_LEFT + 3.6, 2.05, CONTENT_WIDTH - 3.6, 1.6,
            ["Đa số tỉnh, thành chọn Tiếng Anh (Ngoại ngữ 1) làm môn thi thứ ba.",
             "Ví dụ: Sở GD&ĐT Tiền Giang cho biết 100% phòng GD&ĐT các huyện, thị xã, thành phố chọn tiếng Anh khi được xin ý kiến."],
            size=13.5, color=BODY, anchor=MSO_ANCHOR.MIDDLE, anim_kind=FADE, spacing=1.2,
            space_after=5)
    s.card(CONTENT_LEFT, 3.85, (CONTENT_WIDTH - 0.3) / 2, 2.4, "Chọn Tiếng Anh / Ngoại ngữ",
           ["Phần lớn các địa phương.", "Ví dụ: TP.HCM, Hà Nội, Hải Phòng, Cần Thơ, Nghệ An, "
            "Lâm Đồng, Đồng Nai, Vĩnh Phúc…"],
           accent=CYAN, source="Nguồn: VTV, 03/03/2025", body_size=13)
    s.card(CONTENT_LEFT + (CONTENT_WIDTH - 0.3) / 2 + 0.3, 3.85, (CONTENT_WIDTH - 0.3) / 2, 2.4, "Ngoại lệ đáng chú ý",
           ["Hà Giang: Lịch sử và Địa lý.",
            "Bình Thuận: trường phổ thông dân tộc nội trú thi Lịch sử và Địa lý; các trường khác thi Tiếng Anh.",
            "Xét tuyển (không thi): Cà Mau, Vĩnh Long, Gia Lai."],
           accent=AMBER, source="Nguồn: VTV, 03/03/2025", body_size=12.5)
    s.footer(); s.finish()


def build(deck):
    """Append this section's slides to *deck*, in order."""
    _slide_08_third_subject_2025(deck)

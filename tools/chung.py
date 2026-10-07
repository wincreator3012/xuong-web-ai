# -*- coding: utf-8 -*-
"""Hàm dùng chung cho các công cụ của xưởng web (không chạy trực tiếp).

Giữ mã TRUNG TÍNH: không viết tên người, thương hiệu, chương trình vào đây. Mọi thứ riêng nằm ở brand/brand.json,
phong-cach/tu-ngu.json, cau-hinh.json, để đồng bộ máy móc sang repo chung được.
"""
import datetime
import functools
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True  # không để __pycache__ trong repo
for _luong in (sys.stdout, sys.stderr):  # Windows: cửa sổ lệnh, ống dẫn mặc định không phải UTF-8, in chữ có dấu sẽ lỗi
    try:
        _luong.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
TOOLS = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.dirname(TOOLS)
DUOI_VAN_BAN = {'.html', '.htm', '.css', '.js', '.mjs', '.json', '.jsonc', '.md', '.txt', '.xml', '.toml', '.yml',
                '.yaml', '.astro', '.ts', '.rules', '.svg', ''}


def doc(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def ghi(p, s):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)


def doc_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def ghi_json(p, d):
    ghi(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')


def hom_nay():
    return datetime.date.today().isoformat()


# ---------------------------------------------------------------- cấu hình, thư mục
def cau_hinh():
    for ten in ('cau-hinh.json', 'cau-hinh.mau.json'):
        p = os.path.join(GOC, ten)
        if os.path.exists(p):
            try:
                return doc_json(p)
            except ValueError:
                raise SystemExit(f'{ten} hỏng (không đọc được JSON): sửa tay hoặc chép lại từ cau-hinh.mau.json.')
    return {}


def duong_cau_hinh(khoa, mac_dinh):
    v = os.path.expanduser((cau_hinh().get(khoa) or mac_dinh).strip())
    return os.path.normpath(v if os.path.isabs(v) else os.path.join(GOC, v))


def thu_muc_du_an():
    return duong_cau_hinh('thuMucDuAn', '../Du an')


def thu_muc_web():
    return duong_cau_hinh('thuMucWeb', '../Web')


def thu_muc_tam():
    return os.path.join(thu_muc_du_an(), '_tam')


def trong_repo(p):
    a, g = os.path.realpath(p), os.path.realpath(GOC)
    return a == g or a.startswith(g + os.sep)


def chan_ghi_repo(p, viec='ghi'):
    """Repo chỉ chứa năng lực: công cụ tự dừng nếu bị bắt ghi nháp, web, báo cáo vào repo."""
    if trong_repo(p) and not os.environ.get('XUONG_CHO_PHEP_GHI_REPO'):
        raise SystemExit(f'DỪNG: không {viec} vào trong repo xưởng ({p}). Web ở thuMucWeb, hồ sơ ở thuMucDuAn '
                         f'(cau-hinh.json), việc tạm ở "{thu_muc_tam()}".')


def ten_khong_dau(s):
    s = s.replace('đ', 'd').replace('Đ', 'D')
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def slug(s):
    s = re.sub(r'[^a-zA-Z0-9]+', '-', ten_khong_dau(s).lower()).strip('-')
    return re.sub(r'-{2,}', '-', s) or 'web'


# ---------------------------------------------------------------- web và dự án
def tim_web(ten):
    """Nhận đường dẫn, hoặc tên thư mục trong thuMucWeb; trả đường dẫn tuyệt đối tới gốc web."""
    for p in (ten, os.path.join(thu_muc_web(), ten)):
        if p and os.path.isdir(p):
            return os.path.abspath(p)
    raise SystemExit(f'Không thấy web "{ten}" (đường dẫn, hoặc tên thư mục trong {thu_muc_web()}).')


def thu_muc_cong_khai(web):
    """Thư mục được đưa lên mạng: public/ (web tĩnh, Firebase), dist/ sau khi dựng (Astro)."""
    hs = ho_so_web(web)
    if hs.get('loai') == 'astro':
        return os.path.join(web, 'dist')
    return os.path.join(web, hs.get('thuMucCongKhai', 'public'))


def ho_so_web(web):
    p = os.path.join(web, 'xuong.json')
    return doc_json(p) if os.path.exists(p) else {}


def tim_du_an(web):
    """Hồ sơ dự án ứng với một web: thư mục trong thuMucDuAn có du-an.json trỏ tới web này."""
    goc = thu_muc_du_an()
    ten = os.path.basename(os.path.abspath(web))
    if os.path.isdir(goc):
        for d in sorted(os.listdir(goc)):
            p = os.path.join(goc, d, 'du-an.json')
            if os.path.exists(p):
                try:
                    if doc_json(p).get('web') == ten:
                        return os.path.join(goc, d)
                except ValueError:
                    pass
    return None


# ---------------------------------------------------------------- thương hiệu, chủ đề màu
def brand():
    for ten in ('brand.json', 'brand.mau.json'):
        p = os.path.join(GOC, 'brand', ten)
        if os.path.exists(p):
            return doc_json(p)
    raise SystemExit('Thiếu brand/brand.json: chạy bước thiết lập trước.')


def kebab(k):
    return re.sub(r'([A-Z])', lambda m: '-' + m.group(1).lower(), k)


def css_token(ten_chu_de, cd):
    dong = [f'/* Màu và phông của web này, sinh từ brand/brand.json > chuDe.{ten_chu_de} ngày {hom_nay()}.',
            '   Gọi theo VAI (nen, chu, nhan...), he-thong/nen.css chỉ dùng các biến này.',
            '   Đổi màu riêng cho web này thì sửa ngay tại đây, rồi chạy tools/kiem-web.py để kiểm tương phản. */',
            ':root {', f'  color-scheme: {"dark" if cd.get("toi") else "light"};']
    for k, v in cd['mau'].items():
        dong.append(f'  --{kebab(k)}: {v};')
    ph = cd.get('phong', {})
    dong.append(f"  --phong-tieu-de: '{ph.get('tieuDe', 'Lora')}';")
    dong.append(f"  --phong-noi-dung: '{ph.get('noiDung', 'Be Vietnam Pro')}';")
    dong.append('}')
    return '\n'.join(dong) + '\n'


def ho_phong(ten):
    return slug(ten)  # 'Be Vietnam Pro' -> 'be-vietnam-pro', khớp thư mục trong fonts/


# ---------------------------------------------------------------- luật chữ
# Lớp chung: đúng cho mọi người viết tiếng Việt trên web. Lớp riêng: phong-cach/tu-ngu.json (tuCam, tuNenTranh).
TU_CAM_CHUNG = [
    (r'\u2014', 'không dùng gạch dài (em dash): đổi thành gạch ngang thường (-) hoặc dấu hai chấm'),
    (r'\u2026', 'không dùng dấu ba chấm Unicode: gõ ba dấu chấm (...)'),
    (r'(?i)lorem ipsum', 'còn chữ giả lorem ipsum: thay bằng nội dung thật'),
    (r'(?i)(đừng để|kẻo|không muốn) bị bỏ lại|tụt hậu|đi trước đối thủ', 'không dùng khung "đua tranh, bị bỏ lại"'),
    (r'(?i)\bchỉ còn \d+ (chỗ|suất|ghế|vé)\b', 'không nêu số ghế cụ thể; khan hiếm thật thì nói bằng lời định tính kèm lý do'),
]
TU_NEN_TRANH_CHUNG = [
    (r'(?i)\b(hành trình|kỷ nguyên|cuộc cách mạng|chìa khoá|chìa khóa|bí quyết|lăng kính|cánh cửa|bức tranh toàn cảnh)\b',
     'danh từ "to lớn" dễ thành sáo: giữ khi là nghĩa thật, không thì gọi đúng điều cụ thể'),
    (r'(?i)\b(đột phá|vượt trội|tiên tiến|liền mạch|ngoạn mục|đáng kinh ngạc|toàn diện|then chốt)\b',
     'tính từ "đẹp lời" rỗng: thay bằng thông tin cụ thể (con số, việc làm được)'),
    (r'(?i)\b(kiến tạo|vun đắp|ươm mầm|đắm mình|vén màn|chinh phục|khai phá|phát huy tối đa)\b',
     'động từ "khai sáng" sáo: thay bằng động từ cụ thể'),
    (r'(?i)\b(vô cùng|cực kỳ|hết sức)\b', 'trạng từ phóng đại: bỏ hoặc thay bằng chi tiết'),
    (r'(?i)trong (thời đại|kỷ nguyên|bối cảnh)|hãy cùng|đừng bỏ lỡ|người bạn đồng hành|mở ra (một )?(chương|kỷ nguyên|cánh cửa)|hơn bao giờ hết|mang lại trải nghiệm',
     'cụm sáo văn AI: viết thẳng điều người đọc nhận được'),
    (r'(?i)\bkhông chỉ\b[^.!?]{0,80}\bmà còn\b', 'đối ngẫu "không chỉ... mà còn": tối đa một lần cả trang'),
    (r'[“”]', 'dấu nháy cong: dùng nháy thẳng "..."'),
    (r'(?i)\b(click vào đây|bấm vào đây|submit)\b', 'chữ trên nút, liên kết: động từ cụ thể nói điều sẽ xảy ra'),
]


@functools.lru_cache(None)
def tu_ngu_rieng():
    p = os.path.join(GOC, 'phong-cach', 'tu-ngu.json')
    if not os.path.exists(p):
        p = os.path.join(GOC, 'phong-cach', 'tu-ngu.mau.json')
    if not os.path.exists(p):
        return [], []
    d = doc_json(p)

    def lay(k):
        return [('(?i)' + m['mau'], m.get('lyDo', '')) for m in d.get(k, []) if isinstance(m, dict) and m.get('mau')]
    return lay('tuCam'), lay('tuNenTranh')


def luat_chu():
    cam, nen = tu_ngu_rieng()
    return TU_CAM_CHUNG + cam, TU_NEN_TRANH_CHUNG + nen


@functools.lru_cache(None)
def ten_rieng():
    """Tên người, thương hiệu trong brand.json: viết hoa mọi chữ là đúng, không phải Title Case."""
    try:
        b = brand()
    except SystemExit:
        return set()
    ra = {v.get('ten', '') for v in b.get('thuongHieu', {}).values()}
    for nv in b.get('nhanVat', {}).values():
        ra |= {nv.get('ten', ''), nv.get('tenDayDu', '')}
    return {x for x in ra if x}


def la_title_case(s):
    """Viết hoa chữ cái đầu mọi từ (Title Case): sai quy ước chữ Việt. Bỏ qua câu ngắn, VIẾT HOA, tên người
    (có học vị như ThS, TS, hoặc khai trong brand.json)."""
    if re.search(r'\b(ThS|TS|PGS|GS|BS|NCS|CN|KS|Dr|MSc|MA|PhD)\b', s):
        return False
    for t in ten_rieng():
        s = s.replace(t, '')
    tu = [t for t in re.findall(r"[^\W\d_]+", s) if len(t) > 1]
    return len(tu) >= 4 and all(t[0].isupper() for t in tu) and not s.isupper()

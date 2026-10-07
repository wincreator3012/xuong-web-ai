#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CÀI ĐẶT XƯỞNG WEB - một lệnh, chạy lại bao nhiêu lần cũng an toàn.

    python3 tools/cai-dat.py                     # làm mọi bước còn thiếu, rồi tạo thử và kiểm thử một web mẫu
    python3 tools/cai-dat.py --trang-thai        # chỉ xem: bước nào xong, trình duyệt kiểm, Node, việc tiếp theo
    python3 tools/cai-dat.py --khong-cai         # không cài gì qua mạng, chỉ kiểm và tạo thử
    python3 tools/cai-dat.py --khong-thu         # bỏ bước tạo thử
    python3 tools/cai-dat.py --danh-dau thiet-lap|gioi-thieu   # trợ lý ghi dấu sau bước thiết lập phong cách, buổi giới thiệu

Các bước (mỗi bước tự bỏ qua nếu đã xong):
  1. Python 3.9+.
  2. cau-hinh.json (chép từ cau-hinh.mau.json): hồ sơ dự án ở ../Du an, mã nguồn web ở ../Web, cạnh repo.
  3. Tạo hai thư mục đó (và Du an/_tam cho việc tạm) NGOÀI repo; chép các tệp phong cách của bạn từ bản khởi đầu
     (brand/brand.json, phong-cach/PHONG-CACH.md, phong-cach/tu-ngu.json) nếu chưa có. Không bao giờ ghi đè bản đã có.
  4. Pillow (thu logo, làm ảnh chia sẻ).
  5. Trình duyệt kiểm: Playwright + Chromium (chụp ba khổ, đo tràn chữ, tương phản thật, khả năng tiếp cận).
     Cần mạng; mỗi lần chạy tối đa khoảng 150 giây, thoát mã 2 = chạy lại y nguyên.
  6. Node.js: chỉ báo có hay chưa (cần cho web nhiều trang Astro và lệnh đưa lên Cloudflare); không tự cài.
  7. Tạo thử một web từ khuôn trang-don vào Du an/_tam/thu-xuong/ rồi chạy tools/kiem-web.py.
Trạng thái ghi vào cau-hinh.json > caiDat (không lên git).

Nơi không có trình duyệt và không cài được (ví dụ máy ảo của Claude Cowork): mọi phần khác vẫn dùng được; bước kiểm
bằng trình duyệt chạy ở sandbox đám mây của phiên, hoặc trên máy bạn (docs/QUY-TRINH-KY-THUAT.md).
"""
import argparse
import datetime
import importlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time

sys.dont_write_bytecode = True  # không để __pycache__ trong repo
for _luong in (sys.stdout, sys.stderr):  # Windows: in chữ có dấu không lỗi
    try:
        _luong.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
MOI_TRUONG = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
TOOLS = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.dirname(TOOLS)
CAU_HINH = os.path.join(GOC, 'cau-hinh.json')
MAU = os.path.join(GOC, 'cau-hinh.mau.json')
HAN_GIAY = 150
BAT_DAU = time.time()
TEP_CUA_BAN = [('brand/brand.mau.json', 'brand/brand.json'),
               ('phong-cach/PHONG-CACH.mau.md', 'phong-cach/PHONG-CACH.md'),
               ('phong-cach/tu-ngu.mau.json', 'phong-cach/tu-ngu.json')]


# ---------------------------------------------------------------- tiện ích
def doc_cau_hinh():
    if os.path.exists(CAU_HINH):
        try:
            with open(CAU_HINH, encoding='utf-8') as f:
                return json.load(f)
        except ValueError:
            print('! cau-hinh.json hỏng (không đọc được JSON): sửa tay hoặc xoá để tạo lại.')
            sys.exit(1)
    return {}


def ghi_cau_hinh(ch):
    with open(CAU_HINH, 'w', encoding='utf-8') as f:
        json.dump(ch, f, ensure_ascii=False, indent=2)
        f.write('\n')


def duong(ch, khoa):
    v = (ch.get(khoa) or '').strip()
    if not v:
        return None
    v = os.path.expanduser(v)
    return os.path.normpath(v if os.path.isabs(v) else os.path.join(GOC, v))


def co_module(ten):
    try:
        importlib.import_module(ten)
        return True
    except Exception:
        return False


def pip_cai(goi):
    """Cài gói Python cho đúng trình thông dịch đang chạy; tự thử lại khi gặp môi trường 'externally managed'."""
    lenh = [sys.executable, '-m', 'pip', 'install', '--user', '--quiet', '--disable-pip-version-check'] + goi
    if os.environ.get('VIRTUAL_ENV'):
        lenh.remove('--user')
    r = subprocess.run(lenh, capture_output=True, text=True, encoding='utf-8', errors='replace', env=MOI_TRUONG)
    if r.returncode != 0 and 'externally-managed' in (r.stdout + r.stderr):
        r = subprocess.run(lenh + ['--break-system-packages'], capture_output=True, text=True, encoding='utf-8', errors='replace', env=MOI_TRUONG)
    if r.returncode != 0:
        print('    ' + ((r.stderr or r.stdout).strip().splitlines() or ['pip lỗi'])[-1][:300])
    importlib.invalidate_caches()
    return r.returncode == 0


def playwright_chay_duoc():
    if not co_module('playwright'):
        return False
    ma = ('from playwright.sync_api import sync_playwright\n'
          'with sync_playwright() as p:\n b = p.chromium.launch(); b.close()\n')
    try:
        r = subprocess.run([sys.executable, '-c', ma], capture_output=True, text=True, encoding='utf-8', errors='replace', env=MOI_TRUONG, timeout=90)
        return r.returncode == 0
    except Exception:
        return False


def phien_ban_node():
    node = shutil.which('node')
    if not node:
        return None
    try:
        return subprocess.run([node, '--version'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=20).stdout.strip() or None
    except Exception:
        return None


def node_du_moi(v):
    """Astro 7 cần Node 22.12 trở lên."""
    m = re.match(r'v?(\d+)\.(\d+)', v or '')
    return bool(m) and (int(m.group(1)), int(m.group(2))) >= (22, 12)


CHO_TRONG = re.compile(r'\[(?:TÊN BẠN|Tên hiển thị|Chức danh|Danh sách|ai, đến từ đâu|ví dụ|tên chủ đề|danh sách|bạn, anh chị|loại web|có / chưa|nền nào|ngày)[^\]]*\]')


def cho_trong_phong_cach():
    """Các chỗ còn để trống trong phong-cach/PHONG-CACH.md (dấu [...] của bản khởi đầu)."""
    p = os.path.join(GOC, 'phong-cach', 'PHONG-CACH.md')
    if not os.path.exists(p):
        return ['(không có tệp)']
    with open(p, encoding='utf-8') as f:
        return CHO_TRONG.findall(f.read())


def cho_trong_brand():
    """Các giá trị còn dạng "[...]" trong brand/brand.json (tên, chức danh, liên hệ chưa điền)."""
    p = os.path.join(GOC, 'brand', 'brand.json')
    if not os.path.exists(p):
        return ['(không có tệp)']
    ra = []

    def duyet(x, duong_dan):
        if isinstance(x, dict):
            for k, v in x.items():
                if not k.startswith('_'):
                    duyet(v, duong_dan + [k])
        elif isinstance(x, str) and x.startswith('[') and x.endswith(']'):
            ra.append('.'.join(duong_dan))
    with open(p, encoding='utf-8') as f:
        b = json.load(f)
    for khoa in ('thuongHieu', 'nhanVat'):
        duyet(b.get(khoa, {}), [khoa])
    return ra


def con_thoi_gian():
    return HAN_GIAY - (time.time() - BAT_DAU)


# ---------------------------------------------------------------- trạng thái
def trang_thai(in_ra=True):
    ch = doc_cau_hinh()
    cd = ch.get('caiDat', {})
    da, web = duong(ch, 'thuMucDuAn'), duong(ch, 'thuMucWeb')
    node = phien_ban_node()
    con_pc, con_br = cho_trong_phong_cach(), cho_trong_brand()
    tt = {
        'python': sys.version.split()[0],
        'heDieuHanh': f'{platform.system()} {platform.machine()}',
        'cauHinh': bool(ch),
        'thuMucDuAn': da if da and os.path.isdir(da) else None,
        'thuMucWeb': web if web and os.path.isdir(web) else None,
        'pillow': co_module('PIL'),
        'trinhDuyet': playwright_chay_duoc(),
        'node': node,
        'taoThu': bool(cd.get('taoThu')),
        'daThietLap': bool(cd.get('daThietLap')) and not con_pc and not con_br,
        'daGioiThieu': bool(cd.get('daGioiThieu')),
    }
    if in_ra:
        v = lambda b: 'có' if b else 'chưa'
        print('TRẠNG THÁI XƯỞNG WEB')
        print(f'  Repo:              {GOC}')
        print(f'  Python:            {tt["python"]} ({tt["heDieuHanh"]})')
        print(f'  cau-hinh.json:     {v(tt["cauHinh"])}')
        print(f'  Thư mục dự án:     {tt["thuMucDuAn"] or "chưa có"}')
        print(f'  Thư mục web:       {tt["thuMucWeb"] or "chưa có"}')
        print(f'  Pillow:            {v(tt["pillow"])}')
        print(f'  Trình duyệt kiểm:  {"Playwright + Chromium" if tt["trinhDuyet"] else "KHÔNG CÓ (kiểm chữ, mã vẫn chạy; chụp ảnh, đo tràn thì chưa)"}')
        print(f'  Node.js:           {node or "chưa có"}' + ('' if not node or node_du_moi(node) else ' (Astro 7 cần 22.12 trở lên)')
              + ('' if node else ' (chỉ cần cho web nhiều trang Astro và đưa lên Cloudflare từ máy; nodejs.org, bản LTS)'))
        print(f'  Tạo thử web:       {"ĐẠT" if tt["taoThu"] else "chưa"}')
        if tt['daThietLap']:
            print('  Phong cách:        đã thiết lập')
        else:
            print(f'  Phong cách:        CHƯA ({len(con_pc)} chỗ trống trong phong-cach/PHONG-CACH.md, '
                  f'{len(con_br)} trong brand/brand.json' + (f': {", ".join(con_br[:4])}' if con_br and con_br[0][0] != '(' else '') + ')')
        print(f'  Giới thiệu xưởng:  {"đã" if tt["daGioiThieu"] else "chưa"}')
        print('\nViệc tiếp theo: ' + viec_tiep(tt))
    return tt


def viec_tiep(tt):
    if not tt['cauHinh'] or not tt['thuMucDuAn'] or not tt['thuMucWeb']:
        return 'chạy python3 tools/cai-dat.py'
    if not tt['taoThu']:
        return 'chạy python3 tools/cai-dat.py để tạo thử và kiểm thử một web'
    if not tt['daThietLap']:
        return 'thiết lập phong cách: skill skills/web-thiet-lap/SKILL.md'
    if not tt['daGioiThieu']:
        return 'giới thiệu xưởng cho người dùng: skills/web-thiet-lap/references/gioi-thieu-xuong.md'
    return 'xưởng sẵn sàng: làm web đầu tiên (skill skills/web-thiet-ke/SKILL.md)'


# ---------------------------------------------------------------- các bước
def buoc_python():
    if sys.version_info < (3, 9):
        print(f'✗ Python {sys.version.split()[0]} quá cũ, cần 3.9 trở lên (python.org).')
        sys.exit(1)
    print(f'✓ Python {sys.version.split()[0]}')


def buoc_cau_hinh():
    ch = doc_cau_hinh()
    if ch.get('thuMucDuAn') and ch.get('thuMucWeb'):
        print('✓ cau-hinh.json')
        return ch
    mau = {}
    if os.path.exists(MAU):
        with open(MAU, encoding='utf-8') as f:
            mau = {k: v for k, v in json.load(f).items() if not k.startswith('_')}
    ch = dict({'thuMucDuAn': '../Du an', 'thuMucWeb': '../Web'}, **mau, **ch)
    ghi_cau_hinh(ch)
    print(f'✓ tạo cau-hinh.json (hồ sơ dự án ở {ch["thuMucDuAn"]}, mã nguồn web ở {ch["thuMucWeb"]}, cạnh repo)')
    return ch


def buoc_thu_muc(ch):
    for khoa, ten in (('thuMucDuAn', 'hồ sơ dự án'), ('thuMucWeb', 'mã nguồn web')):
        d = duong(ch, khoa)
        r, g = os.path.realpath(d), os.path.realpath(GOC)
        if r == g or r.startswith(g + os.sep):
            print(f'✗ cau-hinh.json > {khoa} trỏ vào trong repo ({d}): đổi ra ngoài repo, ví dụ "../Du an".')
            sys.exit(1)
        os.makedirs(d, exist_ok=True)
        print(f'✓ thư mục {ten}: {d}')
    os.makedirs(os.path.join(duong(ch, 'thuMucDuAn'), '_tam'), exist_ok=True)


def buoc_tep_cua_ban():
    """Phần của người dùng: chép từ bản khởi đầu *.mau.* nếu chưa có; không bao giờ ghi đè bản đã có."""
    tao = []
    for mau, that in TEP_CUA_BAN:
        pm, pt = os.path.join(GOC, mau), os.path.join(GOC, that)
        if os.path.exists(pm) and not os.path.exists(pt):
            shutil.copyfile(pm, pt)
            tao.append(that)
    print('✓ tệp phong cách của bạn: ' + ('tạo ' + ', '.join(tao) if tao else 'đã có (giữ nguyên)'))


def buoc_pillow(khong_cai):
    if co_module('PIL'):
        print('✓ Pillow')
        return
    if khong_cai:
        print('! thiếu Pillow (bỏ qua vì --khong-cai): logo sẽ không được thu nhỏ, không làm được ảnh chia sẻ')
        return
    print('... cài Pillow (xử lý ảnh nhẹ)')
    print('✓ Pillow' if pip_cai(['pillow']) and co_module('PIL') else '! chưa cài được Pillow (xưởng vẫn chạy, kém vài tính năng)')


def buoc_trinh_duyet(khong_cai):
    if playwright_chay_duoc():
        print('✓ trình duyệt kiểm: Playwright + Chromium')
        return True
    if khong_cai:
        print('! chưa có trình duyệt kiểm; bỏ qua cài vì --khong-cai')
        return False
    print('... cài Playwright (thư viện điều khiển trình duyệt để chụp và kiểm web)')
    if not co_module('playwright') and not pip_cai(['playwright']):
        print('! không cài được Playwright qua mạng.')
        return False
    if con_thoi_gian() < 40:
        print('... hết lượt thời gian, chạy lại lệnh này để cài tiếp.')
        sys.exit(2)
    print('... tải Chromium cho Playwright (khoảng 150 MB)')
    try:
        r = subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', env=MOI_TRUONG, timeout=max(30, con_thoi_gian() - 5))
        if r.returncode != 0:
            print('    ' + ((r.stderr or r.stdout).strip().splitlines() or ['lỗi'])[-1][:300])
    except subprocess.TimeoutExpired:
        print('... chưa tải xong, chạy lại lệnh này để tải tiếp.')
        sys.exit(2)
    if playwright_chay_duoc():
        print('✓ trình duyệt kiểm: Playwright + Chromium')
        return True
    print('! không tải được Chromium ở nơi này (mạng chặn hoặc thiếu thư viện hệ thống). Kiểm chữ, mã vẫn chạy.')
    return False


def buoc_node():
    v = phien_ban_node()
    if v and node_du_moi(v):
        print(f'✓ Node.js {v}')
    elif v:
        print(f'! Node.js {v}: web nhiều trang (Astro 7) cần 22.12 trở lên; cập nhật ở nodejs.org khi cần')
    else:
        print('- chưa có Node.js: chỉ cần cho web nhiều trang (Astro) và đưa web lên Cloudflare từ máy; cài bản LTS ở nodejs.org khi cần')


def buoc_tao_thu(ch, co_trinh_duyet):
    tam = os.path.join(duong(ch, 'thuMucDuAn'), '_tam', 'thu-xuong')
    shutil.rmtree(tam, ignore_errors=True)
    env = MOI_TRUONG
    r = subprocess.run([sys.executable, os.path.join(TOOLS, 'web-moi.py'), 'Thu xuong', '--khuon', 'trang-don', '--web', 'thu-xuong',
                        '--goc', os.path.join(tam, 'du-an'), '--goc-web', os.path.join(tam, 'web')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    if r.returncode != 0:
        print('✗ tạo thử web KHÔNG ĐẠT:\n    ' + '\n    '.join((r.stdout + r.stderr).strip().splitlines()[-8:]))
        return False
    lenh = [sys.executable, os.path.join(TOOLS, 'kiem-web.py'), os.path.join(tam, 'web', 'thu-xuong'), '--ra', os.path.join(tam, 'kiem'), '--im']
    if not co_trinh_duyet:
        lenh.append('--khong-trinh-duyet')
    r = subprocess.run(lenh, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    dong = [d for d in (r.stdout + r.stderr).splitlines() if d.startswith('KIỂM WEB') or d.startswith('Tờ tổng thể')]
    if r.returncode == 0:
        print('✓ tạo thử và kiểm thử ĐẠT: ' + ' | '.join(dong))
        return True
    print('✗ kiểm thử KHÔNG ĐẠT:\n    ' + '\n    '.join((r.stdout + r.stderr).strip().splitlines()[-10:]))
    return False


# ---------------------------------------------------------------- chạy
def main():
    ap = argparse.ArgumentParser(description='Cài đặt, kiểm môi trường Xưởng web.')
    ap.add_argument('--trang-thai', action='store_true')
    ap.add_argument('--khong-cai', action='store_true')
    ap.add_argument('--khong-thu', action='store_true')
    ap.add_argument('--danh-dau', choices=['thiet-lap', 'gioi-thieu'])
    a = ap.parse_args()
    if a.trang_thai:
        trang_thai()
        return
    if a.danh_dau:
        ch = doc_cau_hinh()
        cd = ch.setdefault('caiDat', {})
        cd['daThietLap' if a.danh_dau == 'thiet-lap' else 'daGioiThieu'] = datetime.date.today().isoformat()
        ghi_cau_hinh(ch)
        print(f'✓ đã ghi dấu {a.danh_dau}')
        return
    print(f'CÀI ĐẶT XƯỞNG WEB ({GOC})\n')
    buoc_python()
    ch = buoc_cau_hinh()
    buoc_thu_muc(ch)
    buoc_tep_cua_ban()
    buoc_pillow(a.khong_cai)
    co_trinh_duyet = buoc_trinh_duyet(a.khong_cai)
    buoc_node()
    ch = doc_cau_hinh()
    cd = ch.setdefault('caiDat', {})
    if not a.khong_thu:
        cd['taoThu'] = buoc_tao_thu(ch, co_trinh_duyet)
    cd['trinhDuyet'] = co_trinh_duyet
    cd['luc'] = datetime.datetime.now().isoformat(timespec='seconds')
    ghi_cau_hinh(ch)
    print()
    tt = trang_thai(in_ra=False)
    if tt['taoThu'] and co_trinh_duyet:
        print('✓ CÀI XONG.')
    elif tt['taoThu']:
        print('✓ CÀI XONG PHẦN KHÔNG CẦN TRÌNH DUYỆT (chụp ảnh, đo tràn chữ sẽ chạy ở sandbox đám mây hoặc trên máy bạn).')
    print('Việc tiếp theo: ' + viec_tiep(tt))


if __name__ == '__main__':
    main()

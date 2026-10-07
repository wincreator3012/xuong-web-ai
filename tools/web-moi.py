#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WEB MỚI: tạo hồ sơ dự án và bộ mã nguồn một web từ một khuôn, đã mang sẵn thương hiệu và chủ đề màu.

    python3 tools/web-moi.py "Trang khoá học mùa thu" --khuon landing
    python3 tools/web-moi.py "Hồ sơ cá nhân" --khuon ho-so --chu-de giay-muc --web ho-so
    python3 tools/web-moi.py "Bảng tra cứu bài tập" --khuon tra-cuu --thuong-hieu chinh --ten-mien https://tracuu.vidu.vn
    python3 tools/web-moi.py --ds                       # liệt kê khuôn, chủ đề màu, thương hiệu

Tạo hai thứ, cả hai NGOÀI repo (cau-hinh.json):
  1. Hồ sơ dự án  <thuMucDuAn>/<YYYY-MM tên>/ : BRIEF.md, THIET-KE.md, SO-GOP-Y.md, VAN-HANH.md, du-an.json, nguon/, kiem/
  2. Mã nguồn web <thuMucWeb>/<tên-web>/      : public/ (phần đưa lên mạng) + README.md (cách sửa) + xuong.json
Web dùng he-thong/nen.css, nen.js (chép vào public/assets/), tokens.css sinh từ brand/brand.json > chuDe, phông tự lưu trữ
(chỉ những họ chủ đề cần), logo của thương hiệu. Chỗ cần điền đánh dấu [[...]] trên trang và <!-- SỬA Ở ĐÂY --> trong mã;
tools/kiem-web.py liệt kê chúng, và chặn đưa lên mạng khi còn sót.
"""
import argparse
import datetime
import glob
import json
import os
import re
import shutil
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402

KHUON = os.path.join(C.GOC, 'khuon')
HT = os.path.join(C.GOC, 'he-thong')


def ds_khuon():
    ra = {}
    for p in sorted(glob.glob(os.path.join(KHUON, '*', 'khuon.json'))):
        ra[os.path.basename(os.path.dirname(p))] = C.doc_json(p)
    return ra


def in_danh_sach():
    b = C.brand()
    print('KHUÔN')
    for k, v in ds_khuon().items():
        print(f'  {k:<14} bậc {v.get("bac")}  {v.get("ten")}')
    print('\nCHỦ ĐỀ MÀU (brand/brand.json > chuDe)')
    for k, v in b['chuDe'].items():
        print(f'  {k:<14} {v.get("ten")}: {v.get("khiNao", "")}')
    print('\nTHƯƠNG HIỆU (brand/brand.json > thuongHieu)')
    for k, v in b['thuongHieu'].items():
        print(f'  {k:<18} {v.get("ten")} (chủ đề mặc định: {v.get("chuDeMacDinh")})')


def cho_trong(v):
    """Giá trị còn để trống trong brand.json ("[...]") thành chỗ cần điền [[...]] trên trang."""
    v = (v or '').strip()
    if not v:
        return '[[cần điền]]'
    if v.startswith('[') and v.endswith(']') and not v.startswith('[['):
        return '[' + v + ']'
    return v


def dau_trong(v):
    """Như cho_trong nhưng giữ nguyên giá trị rỗng (dòng tuỳ chọn như khẩu hiệu)."""
    return cho_trong(v) if (v or '').strip() else ''


def bang_thay(b, th_key, chu_de, tieu_de, ten_mien, web_slug):
    th = b['thuongHieu'][th_key]
    nv_key = th.get('nhanVat') or next(iter(b.get('nhanVat', {})), None)
    nv = b.get('nhanVat', {}).get(nv_key, {}) if nv_key else {}
    lh = dict(b.get('lienHe', {}))
    lh.update(th.get('lienHe', {}))
    zalo = re.sub(r'\D', '', lh.get('zalo', '')) if re.search(r'\d{9,}', lh.get('zalo', '')) else ''
    logo = th.get('logo', {})
    cd = b['chuDe'][chu_de]
    ra = {
        'TIEU_DE': tieu_de,
        'TEN': dau_trong(th.get('ten', '')),
        'TEN_NGUOI': dau_trong(nv.get('tenDayDu') or nv.get('ten', '') or th.get('ten', '')),
        'CHUC_DANH': dau_trong((nv.get('chucDanh') or {}).get('macDinh', '') or th.get('khauHieu', '')),
        'KHAU_HIEU': dau_trong(th.get('khauHieu', '')),
        'CHU_QUAN': cho_trong(lh.get('chuQuan') or th.get('ten')),
        'EMAIL': cho_trong(lh.get('email')),
        'DIEN_THOAI': cho_trong(lh.get('dienThoai')),
        'ZALO_LINK': f'https://zalo.me/{zalo}' if zalo else '#lien-he',
        'DIA_CHI': cho_trong(lh.get('diaChi')),
        'WEBSITE': dau_trong(th.get('website') or lh.get('website', '')),
        'URL': (ten_mien or 'https://[[ten-mien]]').rstrip('/'),
        'URL_HOP_LE': (ten_mien or 'https://chua-dat-ten-mien.invalid').rstrip('/'),  # nơi cần URL hợp lệ (Astro)
        'NAM': str(datetime.date.today().year),
        'MAU_NEN': cd['mau']['nen'],
        'MA_TIEN_TO': re.sub(r'[^A-Z]', '', C.ten_khong_dau(th.get('ten', 'DH')).upper())[:3] or 'DH',
        'WEB': web_slug,
    }
    ra['LOGO_DAU'] = (f'<img src="assets/img/logo-sang.png" alt="{ra["TEN"]}" width="160" height="48">'
                      if logo.get('nenSang') and not cd.get('toi') else
                      f'<img src="assets/img/logo-toi.png" alt="{ra["TEN"]}" width="160" height="48">'
                      if logo.get('nenToi') and cd.get('toi') else ra['TEN'])
    ra['LOGO_CHAN'] = (f'<img src="assets/img/logo-toi.png" alt="{ra["TEN"]}" width="160" height="48">'
                       if logo.get('nenToi') else ra['TEN'])
    ra['FAVICON'] = ('<link rel="icon" href="assets/img/bieu-tuong.png">' if (logo.get('bieuTuongSang') or logo.get('nenSang')) else '')
    return ra, logo


def thay_chu(goc_web, bang):
    for dp, dn, fn in os.walk(goc_web):
        dn[:] = [d for d in dn if d not in ('node_modules', '.git', 'fonts')]
        for f in fn:
            p = os.path.join(dp, f)
            if os.path.splitext(f)[1].lower() not in C.DUOI_VAN_BAN:
                continue
            s = C.doc(p)
            moi = re.sub(r'\{\{([A-Z_]+)\}\}', lambda m: bang.get(m.group(1), m.group(0)), s)
            if moi != s:
                C.ghi(p, moi)


def chep_logo(nguon, dich, cao):
    """Logo gốc thường rất nặng (vài trăm KB): thu về chiều cao đủ nét cho màn hình 2x, giữ nền trong suốt."""
    try:
        from PIL import Image
        im = Image.open(nguon)
        if im.height > cao:
            im = im.resize((round(im.width * cao / im.height), cao), Image.LANCZOS)
        im.save(dich, optimize=True)
    except Exception:
        shutil.copy(nguon, dich)


def chep_phong(cd, dich):
    can = {C.ho_phong(cd['phong'].get('tieuDe', 'Lora')), C.ho_phong(cd['phong'].get('noiDung', 'Be Vietnam Pro'))}
    goc = os.path.join(C.GOC, 'fonts')
    css = C.doc(os.path.join(goc, 'fonts.css'))
    giu = []
    dau = css[:css.index('*/') + 2] + '\n\n'
    for m in re.finditer(r'/\* ([\w-]+) \*/\s*@font-face \{.*?\}\n', css, re.S):
        if any(m.group(1).startswith(h + '-') for h in can):
            giu.append(m.group(0))
    os.makedirs(dich, exist_ok=True)
    C.ghi(os.path.join(dich, 'fonts.css'), dau + '\n'.join(giu))
    for h in can:
        shutil.copytree(os.path.join(goc, h), os.path.join(dich, h), dirs_exist_ok=True)
    return sorted(can)


def tao(a):
    b = C.brand()
    kh = ds_khuon()
    if a.khuon not in kh:
        raise SystemExit(f'Không có khuôn "{a.khuon}". Có: {", ".join(kh)}')
    k = kh[a.khuon]
    th_key = a.thuong_hieu or b.get('thuongHieuMacDinh')
    if th_key not in b['thuongHieu']:
        raise SystemExit(f'Không có thương hiệu "{th_key}" trong brand/brand.json. Có: {", ".join(b["thuongHieu"])}')
    chu_de = a.chu_de or b['thuongHieu'][th_key].get('chuDeMacDinh')
    if chu_de not in b['chuDe']:
        raise SystemExit(f'Không có chủ đề "{chu_de}". Có: {", ".join(b["chuDe"])}')
    web_slug = a.web or C.slug(a.ten)
    goc_web = os.path.join(os.path.abspath(a.goc_web) if a.goc_web else C.thu_muc_web(), web_slug)
    thang = datetime.date.today().strftime('%Y-%m')
    goc_da = os.path.join(os.path.abspath(a.goc) if a.goc else C.thu_muc_du_an(), f'{thang} {a.ten}')
    for p in (goc_web, goc_da):
        C.chan_ghi_repo(p, 'tạo web, hồ sơ')
    if os.path.exists(goc_web) and os.listdir(goc_web):
        raise SystemExit(f'DỪNG: đã có web ở {goc_web}. Chọn tên khác (--web) hoặc sửa web đó.')

    # 1. mã nguồn web
    shutil.copytree(os.path.join(KHUON, a.khuon), goc_web, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('khuon.json', 'KHUON.md', '.DS_Store', 'node_modules'))
    cong_khai = os.path.join(goc_web, 'public')
    tai_nguyen = os.path.join(cong_khai, 'assets')
    os.makedirs(os.path.join(tai_nguyen, 'img'), exist_ok=True)
    for thu in ('css', 'js'):
        os.makedirs(os.path.join(tai_nguyen, thu), exist_ok=True)
    shutil.copy(os.path.join(HT, 'nen.css'), os.path.join(tai_nguyen, 'css', 'nen.css'))
    shutil.copy(os.path.join(HT, 'nen.js'), os.path.join(tai_nguyen, 'js', 'nen.js'))
    cd = b['chuDe'][chu_de]
    C.ghi(os.path.join(tai_nguyen, 'css', 'tokens.css'), C.css_token(chu_de, cd))
    trang_css = os.path.join(tai_nguyen, 'css', 'trang.css')
    if not os.path.exists(trang_css):
        C.ghi(trang_css, '/* Chỉnh riêng cho web này (ghi đè nen.css). Giữ gọn: màu gọi theo vai (var(--nhan)...), không viết mã màu rời. */\n')
    phong = chep_phong(cd, os.path.join(tai_nguyen, 'fonts'))
    for tep in os.listdir(os.path.join(HT, 'mau-web')):
        nguon = os.path.join(HT, 'mau-web', tep)
        dich = os.path.join(cong_khai, tep) if tep in ('_headers', 'robots.txt') else os.path.join(goc_web, tep)
        if not os.path.exists(dich):
            shutil.copy(nguon, dich)
    for tep in k.get('trangChung', []):
        dich = os.path.join(cong_khai, tep)
        if not os.path.exists(dich):
            shutil.copy(os.path.join(HT, 'trang-chung', tep), dich)
    bang, logo = bang_thay(b, th_key, chu_de, a.ten, a.ten_mien, web_slug)
    lg = os.path.join(C.GOC, 'brand', 'logo')
    for vai, ten in (('nenSang', 'logo-sang.png'), ('nenToi', 'logo-toi.png'), ('bieuTuongSang', 'bieu-tuong.png')):
        if logo.get(vai) and os.path.exists(os.path.join(lg, logo[vai])):
            chep_logo(os.path.join(lg, logo[vai]), os.path.join(tai_nguyen, 'img', ten), 512 if vai == 'bieuTuongSang' else 192)
    if not os.path.exists(os.path.join(tai_nguyen, 'img', 'bieu-tuong.png')) and os.path.exists(os.path.join(tai_nguyen, 'img', 'logo-sang.png')):
        shutil.copy(os.path.join(tai_nguyen, 'img', 'logo-sang.png'), os.path.join(tai_nguyen, 'img', 'bieu-tuong.png'))
    if k.get('loai') == 'astro':  # Astro: trang dùng đường dẫn tuyệt đối /assets/...
        bang['LOGO_DAU'] = bang['LOGO_DAU'].replace('src="assets/', 'src="/assets/')
        bang['LOGO_CHAN'] = bang['LOGO_CHAN'].replace('src="assets/', 'src="/assets/')
        bang['FAVICON'] = bang['FAVICON'].replace('href="assets/', 'href="/assets/')
    thay_chu(goc_web, bang)
    C.ghi_json(os.path.join(goc_web, 'xuong.json'), {
        '_ghiChu': 'Hồ sơ máy đọc của web này cho công cụ xưởng (không đưa lên mạng vì nằm ngoài public/).',
        'khuon': a.khuon, 'loai': k.get('loai', 'tinh'), 'bac': k.get('bac'), 'thuMucCongKhai': 'public',
        'thuongHieu': th_key, 'chuDe': chu_de, 'phong': phong, 'tenMien': a.ten_mien or '', 'noiDat': '',
        'duAn': os.path.basename(goc_da), 'taoLuc': C.hom_nay()})

    # 2. hồ sơ dự án
    os.makedirs(os.path.join(goc_da, 'nguon'), exist_ok=True)
    os.makedirs(os.path.join(goc_da, 'kiem'), exist_ok=True)
    bang_da = dict(bang, NGAY=C.hom_nay(), KHUON=a.khuon, KHUON_TEN=k.get('ten', ''), BAC=str(k.get('bac', '')),
                   CHU_DE=chu_de, THUONG_HIEU=th_key, DUONG_WEB=goc_web)
    for tep in sorted(os.listdir(os.path.join(HT, 'mau-du-an'))):
        dich = os.path.join(goc_da, tep)
        if not os.path.exists(dich):
            s = C.doc(os.path.join(HT, 'mau-du-an', tep))
            C.ghi(dich, re.sub(r'\{\{([A-Z_]+)\}\}', lambda m: bang_da.get(m.group(1), m.group(0)), s))
    C.ghi_json(os.path.join(goc_da, 'du-an.json'), {'ten': a.ten, 'web': web_slug, 'khuon': a.khuon,
                                                    'thuongHieu': th_key, 'chuDe': chu_de, 'taoLuc': C.hom_nay()})
    print(f'ĐÃ TẠO\n  hồ sơ dự án: {goc_da}\n  mã nguồn web: {goc_web}  (khuôn {a.khuon}, chủ đề {chu_de}, thương hiệu {th_key})')
    print(f'Tiếp theo: điền BRIEF.md, THIET-KE.md cùng người dùng; sửa public/index.html; kiểm bằng python3 tools/kiem-web.py "{web_slug}"')


def main():
    ap = argparse.ArgumentParser(description='Tạo hồ sơ dự án và mã nguồn web mới từ một khuôn.')
    ap.add_argument('ten', nargs='?', help='tên dự án, có dấu, ví dụ "Trang khoá học mùa thu"')
    ap.add_argument('--khuon', default='trang-don')
    ap.add_argument('--thuong-hieu')
    ap.add_argument('--chu-de')
    ap.add_argument('--web', help='tên thư mục web (không dấu, gạch nối); mặc định sinh từ tên dự án')
    ap.add_argument('--ten-mien', help='địa chỉ web nếu đã biết, ví dụ https://khoahoc.vidu.vn')
    ap.add_argument('--goc', help='thư mục hồ sơ dự án cho phiên này (mặc định cau-hinh.json > thuMucDuAn)')
    ap.add_argument('--goc-web', help='thư mục chứa web cho phiên này (mặc định cau-hinh.json > thuMucWeb)')
    ap.add_argument('--ds', action='store_true', help='liệt kê khuôn, chủ đề, thương hiệu')
    a = ap.parse_args()
    if a.ds or not a.ten:
        in_danh_sach()
        return
    tao(a)


if __name__ == '__main__':
    main()

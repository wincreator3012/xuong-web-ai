#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐÓNG GÓI SKILL: biến skill nguồn của xưởng thành gói trọn vẹn để lưu vào tài khoản trợ lý AI
(Claude: Customize > Skills > + > Create skill > Upload a skill): SKILL.md + bản chụp tài liệu kèm (references/).

    python3 tools/dong-goi-skill.py                    # đóng gói mọi skill vào <thuMucDuAn>/_skill/: thư mục + tệp .zip
    python3 tools/dong-goi-skill.py web-thiet-ke       # chỉ vài skill (tên thư mục nguồn)
    python3 tools/dong-goi-skill.py --ds               # liệt kê: skill nguồn, tên trên tài khoản, tệp kèm
    python3 tools/dong-goi-skill.py --van-tay          # in dấu gói và vân tay từng tệp, không ghi gì
    python3 tools/dong-goi-skill.py --so <thư mục>     # so gói với bản đang cài (thư mục chứa các skill theo tên)
    python3 tools/dong-goi-skill.py --mo-ta-ngan       # rút description còn tối đa 200 ký tự (khi nơi tải lên từ chối mô tả dài)
    python3 tools/dong-goi-skill.py --ra <thư mục>     # nơi ghi khác (phải nằm ngoài xưởng)

Nguồn skill: skills-nguon/ nếu có (xưởng gốc của tác giả: tên skill giữ nguyên), không thì skills/ (xưởng dựng từ
bản vẽ: tên trên tài khoản thêm tiền tố "xuong-", ví dụ web-thiet-ke thành xuong-web-thiet-ke, để không trùng skill
khác của người dùng; chỗ thân skill gọi tên skill anh em cũng đổi theo, đường dẫn trong xưởng giữ nguyên).
Thư mục _chung/ không phải skill: các skill trỏ tới nó bằng đường dẫn trong xưởng.

Mỗi skill nguồn có thể có kem.json: danh sách tệp của xưởng (đường dẫn tính từ gốc xưởng) được chụp vào references/
lúc đóng gói, giữ nguyên đường dẫn (chuan/03-thiet-ke-web.md thành references/chuan/03-thiet-ke-web.md), để skill
trên tài khoản vẫn làm được khi phiên chưa gắn thư mục xưởng. Tệp kèm chưa có (ví dụ phong-cach/PHONG-CACH.md khi chưa
thiết lập) thì báo và bỏ qua. references/DONG-GOI.md ghi nguồn và vân tay.

Xưởng dựng từ bản vẽ: thêm khối "Cấu hình cá nhân" ngay dưới tiêu đề SKILL.md, lấy từ brand/brand.json (tên hiển thị,
thương hiệu), phong-cach/PHONG-CACH.md (xưng hô với người xem), XUONG.json (thuMucLamViec: thư mục làm việc trên máy
người dùng, ví dụ "~/Documents/Web AI"; xungHoNguoiDung: trợ lý gọi người dùng thế nào); cau-hinh.json > skillTaiKhoan
với cùng hai khoá thì ghi đè.

Kiểm trước khi ghi: name chỉ gồm chữ thường không dấu, số, gạch nối, tối đa 64 ký tự; description có, tối đa 1024 ký
tự (chuẩn Agent Skills), không ngoặc nhọn, báo khi dài hơn 200; không có dấu hiệu khoá bí mật trong mọi tệp của gói.
Gói tạo lại từ cùng nguồn cho cùng dấu gói và cùng tệp .zip (ngày giờ trong .zip cố định).
"""
import argparse
import glob
import hashlib
import io
import json
import os
import re
import sys
import zipfile

sys.dont_write_bytecode = True  # không để __pycache__ trong xưởng
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402

GOC = C.GOC
TIEN_TO = 'xuong-'
TEN_HOP_LE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
KHOA_BI_MAT = re.compile(r'AIza[0-9A-Za-z_\-]{30,}|(?<![\w-])sk-[A-Za-z0-9_\-]{20,}|gh[pousr]_[A-Za-z0-9]{30,}'
                         r'|-----BEGIN [A-Z ]*PRIVATE KEY|(?<![\w-])re_[A-Za-z0-9]{20,}|xox[abprs]-[A-Za-z0-9-]{10,}')
NGAY_ZIP = (2026, 1, 1, 0, 0, 0)
BO_QUA = {'.DS_Store', 'Thumbs.db', 'kem.json'}


def nguon():
    for ten, doi in (('skills-nguon', False), ('skills', True)):
        if os.path.isdir(os.path.join(GOC, ten)):
            return ten, doi
    raise SystemExit('Không thấy thư mục skill nguồn (skills-nguon/ hoặc skills/) ở gốc xưởng.')


def ds_skill(thu):
    return sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(os.path.join(GOC, thu, '*', 'SKILL.md')))


def bo_dau_dong_bo(t):
    """Dấu đồng bộ sang repo chung chỉ có nghĩa trong xưởng gốc: giữ chữ trong khối RIENG, bỏ chữ chỉ dành cho bản chung."""
    t = re.sub(r'<!-- REPO:.*?-->', '', t, flags=re.S)
    return t.replace('<!-- RIENG -->', '').replace('<!-- /RIENG -->', '')


def ten_tk(s, doi):
    return TIEN_TO + s if doi and not s.startswith(TIEN_TO) else s


def bam(b):
    return hashlib.sha256(b).hexdigest()


def tach_dau(text):
    """Tách phần đầu YAML (giữ thứ tự dòng) và thân."""
    if not text.startswith('---\n'):
        raise ValueError('SKILL.md không mở bằng ---')
    j = text.find('\n---', 4)
    if j < 0:
        raise ValueError('phần đầu YAML không đóng')
    dong = text[4:j].splitlines()
    than = text[j + 4:].lstrip('\n')
    return dong, than


def gia_tri(dong, khoa):
    for d in dong:
        if d.startswith(khoa + ':'):
            v = d.split(':', 1)[1].strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
                v = v[1:-1]
            return v
    return ''


def dat(dong, khoa, v):
    moi = f'{khoa}: "' + v.replace('"', "'") + '"' if khoa == 'description' else f'{khoa}: {v}'
    for i, d in enumerate(dong):
        if d.startswith(khoa + ':'):
            dong[i] = moi
            return dong
    return dong + [moi]


def rut_ngan(mo, tran=200):
    if len(mo) <= tran:
        return mo
    cat = mo[:tran - 1]
    for dau in ('. ', ': ', '; ', ', '):
        k = cat.rfind(dau)
        if k > tran // 2:
            return cat[:k].rstrip(' ,;:') + '.'
    return cat.rsplit(' ', 1)[0].rstrip(' ,;:') + '.'


def gia_tri_that(v):
    v = (v or '').strip()
    return '' if not v or (v.startswith('[') and v.endswith(']')) else v


def khoi_cau_hinh():
    """Khối cấu hình cá nhân cho xưởng dựng từ bản vẽ (đọc phần của người dùng, không đọc bản *.mau.*).
    Trả (khối chữ, danh sách mục còn thiếu)."""
    ten, th, xh_xem = '', '', ''
    try:
        b = C.doc_json(os.path.join(GOC, 'brand', 'brand.json'))
        nv = (b.get('nhanVat') or {}).get('chinh') or {}
        ten = gia_tri_that(nv.get('tenDayDu')) or gia_tri_that(nv.get('ten'))
        th = gia_tri_that(((b.get('thuongHieu') or {}).get(b.get('thuongHieuMacDinh')) or {}).get('ten'))
    except (OSError, ValueError):
        pass
    p = os.path.join(GOC, 'phong-cach', 'PHONG-CACH.md')
    if os.path.exists(p):
        m = re.search(r'Xưng hô với người xem:\s*(.+)', C.doc(p))
        if m:
            xh_xem = gia_tri_that(m.group(1).strip().rstrip('.'))
    sk = dict(C.cau_hinh().get('skillTaiKhoan') or {})
    try:  # xưởng dựng từ bản vẽ: XUONG.json ghi thư mục làm việc, cách gọi người dùng; cau-hinh.json > skillTaiKhoan ghi đè
        x = C.doc_json(os.path.join(GOC, 'XUONG.json'))
        for k in ('thuMucLamViec', 'xungHoNguoiDung'):
            if not gia_tri_that(sk.get(k)) and gia_tri_that(x.get(k)):
                sk[k] = x[k]
    except (OSError, ValueError):
        pass
    lam_viec = gia_tri_that(sk.get('thuMucLamViec'))
    goi = gia_tri_that(sk.get('xungHoNguoiDung')) or 'bạn'
    chua = '(chưa thiết lập)'
    xuong = os.path.basename(GOC)
    thieu = [m for m, v in (('tên hiển thị (brand/brand.json > nhanVat.chinh.tenDayDu)', ten),
                            ('xưng hô với người xem (dòng "Xưng hô với người xem:" trong phong-cach/PHONG-CACH.md)', xh_xem),
                            ('thư mục làm việc (XUONG.json > thuMucLamViec)', lam_viec)) if not v]
    dong = [
        '> **Cấu hình cá nhân** (công cụ đóng gói điền từ phong cách trong xưởng; muốn đổi thì đổi phong cách trong xưởng'
        ' rồi đóng gói lại, không sửa tay ở đây)',
        '>',
        f'> - Người dùng, tức chủ skill: {ten or chua}' + (f'; thương hiệu chính: {th}' if th and th != ten else ''),
        f'> - Trợ lý gọi người dùng là: {goi}',
        f'> - Xưng hô với người xem web: {xh_xem or chua}',
        (f'> - Thư mục làm việc trên máy người dùng: `{lam_viec}` (xưởng ở `{xuong}/` bên trong, web ở `Web/`, hồ sơ ở `Du an/`)'
         if lam_viec else f'> - Thư mục làm việc trên máy người dùng: {chua} (hỏi người dùng thư mục chứa `{xuong}/`)'),
        '> - Phong cách đầy đủ: `phong-cach/PHONG-CACH.md` trong xưởng; bản chụp lúc đóng gói: `references/phong-cach/PHONG-CACH.md`',
    ]
    return '\n'.join(dong) + '\n', thieu


def lam_goi(s, thu, doi, tat_ca, mo_ta_ngan):
    """Trả (tên, {đường dẫn trong gói: bytes}, cảnh báo, lỗi, dấu gói)."""
    canh, loi = [], []
    ten = ten_tk(s, doi)
    text = C.doc(os.path.join(GOC, thu, s, 'SKILL.md'))
    try:
        dong, than = tach_dau(text)
    except ValueError as e:
        return ten, {}, canh, [f'{s}: {e}'], ''
    than = bo_dau_dong_bo(than)
    if gia_tri(dong, 'name') != s:
        loi.append(f'{s}: name trong SKILL.md là "{gia_tri(dong, "name")}", khác tên thư mục')
    mo = gia_tri(dong, 'description')
    if doi:
        mau = re.compile(r'(?<![\w/.-])(' + '|'.join(re.escape(x) for x in sorted(tat_ca, key=len, reverse=True))
                         + r')(?![\w/-])')
        doi_ten = lambda t: mau.sub(lambda m: ten_tk(m.group(1), True), t)  # noqa: E731
        mo, than = doi_ten(mo), doi_ten(than)
        khoi, thieu = khoi_cau_hinh()
        for m in thieu:
            canh.append(f'{ten}: cấu hình cá nhân còn thiếu {m}; skill vẫn đóng gói, khối cấu hình ghi "(chưa thiết lập)"')
        tieu_de = re.match(r'(#[^\n]*\n)\n?', than)
        than = (tieu_de.group(1) + '\n' + khoi + '\n' + than[tieu_de.end():]) if tieu_de else khoi + '\n' + than
    if mo_ta_ngan:
        mo = rut_ngan(mo)
    if not TEN_HOP_LE.match(ten) or len(ten) > 64:
        loi.append(f'{ten}: tên chỉ được chữ thường không dấu, số, gạch nối, tối đa 64 ký tự')
    if not mo:
        loi.append(f'{ten}: thiếu description')
    elif len(mo) > 1024:
        loi.append(f'{ten}: description {len(mo)} ký tự (trần 1024)')
    elif '<' in mo or '>' in mo:
        loi.append(f'{ten}: description chứa ngoặc nhọn')
    elif len(mo) > 200:
        canh.append(f'{ten}: description {len(mo)} ký tự (trang trợ giúp Claude ghi trần 200 cho skill tải lên; '
                    'tài khoản thường vẫn nhận tới 1024). Bị từ chối thì đóng gói lại với --mo-ta-ngan')
    dong = dat(dat(dong, 'name', ten), 'description', mo)
    tep = {f'{ten}/SKILL.md': ('---\n' + '\n'.join(dong) + '\n---\n\n' + than).encode('utf-8')}
    goc_skill = os.path.join(GOC, thu, s)
    for dp, dn, fn in os.walk(goc_skill):
        dn[:] = sorted(d for d in dn if d not in ('__pycache__',))
        for f in sorted(fn):
            rel = os.path.relpath(os.path.join(dp, f), goc_skill).replace(os.sep, '/')
            if f in BO_QUA or rel == 'SKILL.md':
                continue
            with open(os.path.join(dp, f), 'rb') as h:
                tep[f'{ten}/{rel}'] = h.read()
    pk = os.path.join(goc_skill, 'kem.json')
    kem = []
    if os.path.exists(pk):
        try:
            kem = C.doc_json(pk).get('tep') or []
        except ValueError:
            loi.append(f'{s}/kem.json hỏng (JSON)')
    chup = []
    for rel in kem:
        p = os.path.join(GOC, rel)
        if not os.path.isfile(p):
            canh.append(f'{ten}: tệp kèm `{rel}` chưa có trong xưởng, bỏ qua')
            continue
        with open(p, 'rb') as h:
            b = h.read()
        tep[f'{ten}/references/{rel}'] = b
        chup.append((rel, bam(b)[:12]))
    dau = bam(json.dumps(sorted((k, bam(v)) for k, v in tep.items())).encode())[:12]
    # luôn ghi DONG-GOI.md để mọi gói có dấu gói, kể cả skill không có tệp kèm
    bang = '\n'.join(f'| `{r}` | {h} |' for r, h in chup) or '| (không có tệp chụp) | |'
    tep[f'{ten}/references/DONG-GOI.md'] = (
        f'# Gói skill {ten}\n\nGói do `tools/dong-goi-skill.py` tạo từ `{thu}/{s}/` của xưởng. Dấu gói: {dau}.\n\n'
        'Các tệp trong `references/` là BẢN CHỤP lúc đóng gói, giữ nguyên đường dẫn như trong xưởng (ví dụ '
        '`references/chuan/03-thiet-ke-web.md` là `chuan/03-thiet-ke-web.md`). Phiên đã gắn thư mục xưởng thì luôn đọc '
        'bản trong xưởng (mới hơn); chỉ dùng bản chụp khi chưa gắn được, và nói rõ với người dùng đang dựa vào bản '
        'chụp, công cụ kiểm của xưởng chưa chạy.\n\n| Tệp chụp | Vân tay sha256 (12 ký tự đầu) |\n|---|---|\n'
        f'{bang}\n').encode('utf-8')
    for k, v in tep.items():
        try:
            t = v.decode('utf-8')
        except UnicodeDecodeError:
            continue
        if KHOA_BI_MAT.search(t):
            loi.append(f'{k}: có dấu hiệu khoá bí mật, không đóng gói')
    return ten, tep, canh, loi, dau


def zip_bytes(tep):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for k in sorted(tep):
            zi = zipfile.ZipInfo(k, NGAY_ZIP)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            z.writestr(zi, tep[k])
    return buf.getvalue()


def ghi_bytes(p, b):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as h:
        h.write(b)


def so_sanh(ten, tep, thu_muc):
    goc = os.path.join(thu_muc, ten)
    if not os.path.isdir(goc):
        return [f'chưa cài (không thấy {goc})']
    co = {}
    for dp, dn, fn in os.walk(goc):
        for f in fn:
            if f in BO_QUA:
                continue
            p = os.path.join(dp, f)
            with open(p, 'rb') as h:
                b = h.read()
            if f == 'SKILL.md':  # nơi lưu skill thường tự thêm ngoặc kép quanh name: không tính là lệch
                b = re.sub(rb'^name: "([^"\n]*)"$', rb'name: \1', b, count=1, flags=re.M)
            co[f'{ten}/' + os.path.relpath(p, goc).replace(os.sep, '/')] = bam(b)
    khac = []
    for k in sorted(set(tep) | set(co)):
        if k not in co:
            khac.append(f'thiếu ở bản đang cài: {k}')
        elif k not in tep:
            khac.append(f'thừa ở bản đang cài (gói mới không có): {k}')
        elif bam(tep[k]) != co[k]:
            khac.append(f'khác nội dung: {k}')
    return khac


def main():
    ap = argparse.ArgumentParser(description='Đóng gói skill của xưởng để lưu vào tài khoản trợ lý AI.')
    ap.add_argument('skill', nargs='*', help='tên thư mục skill nguồn; bỏ trống = tất cả')
    ap.add_argument('--ds', action='store_true')
    ap.add_argument('--van-tay', action='store_true')
    ap.add_argument('--so', metavar='THU_MUC')
    ap.add_argument('--mo-ta-ngan', action='store_true')
    ap.add_argument('--ra', metavar='THU_MUC')
    a = ap.parse_args()
    thu, doi = nguon()
    tat_ca = ds_skill(thu)
    chon = a.skill or tat_ca
    la = [s for s in chon if s not in tat_ca]
    if la:
        raise SystemExit(f'Không có skill nguồn: {", ".join(la)}. Có: {", ".join(tat_ca)}')
    if a.ds:
        print(f'Skill nguồn ở {thu}/ ({"đổi tên khi đóng gói" if doi else "giữ tên"}):')
        for s in tat_ca:
            pk = os.path.join(GOC, thu, s, 'kem.json')
            kem = C.doc_json(pk).get('tep', []) if os.path.exists(pk) else []
            print(f'  {s:22} -> {ten_tk(s, doi):28} kèm: {", ".join(kem) or "không"}')
        return
    ra = os.path.abspath(a.ra) if a.ra else os.path.join(C.thu_muc_du_an(), '_skill')
    if not (a.van_tay or a.so):
        C.chan_ghi_repo(ra, 'ghi gói skill')
    tong_loi = 0
    for s in chon:
        ten, tep, canh, loi, dau = lam_goi(s, thu, doi, tat_ca, a.mo_ta_ngan)
        print(f'\n{ten}  (nguồn {thu}/{s}/, {len(tep)} tệp, dấu gói {dau})')
        for c in canh:
            print('  cảnh báo: ' + c)
        for l in loi:
            print('  LỖI: ' + l)
        tong_loi += len(loi)
        if a.van_tay:
            for k in sorted(tep):
                print(f'    {bam(tep[k])[:12]}  {k}')
        if a.so:
            khac = so_sanh(ten, tep, os.path.abspath(os.path.expanduser(a.so)))
            print('  so với bản đang cài: ' + ('KHỚP' if not khac else f'LỆCH ({len(khac)})'))
            for k in khac[:20]:
                print('    ' + k)
        if loi or a.van_tay or a.so:
            continue
        for k, v in tep.items():
            ghi_bytes(os.path.join(ra, k), v)
        ghi_bytes(os.path.join(ra, ten + '.zip'), zip_bytes(tep))
        hien = lambda x: os.path.relpath(x, os.path.dirname(GOC))  # noqa: E731  (đường dẫn trong thư mục làm việc)
        print(f'  đã ghi: {hien(os.path.join(ra, ten + ".zip"))} (tải tệp này lên) và thư mục {hien(os.path.join(ra, ten))}/')
    if a.van_tay or a.so:
        sys.exit(1 if tong_loi else 0)
    if tong_loi:
        print(f'\nĐÓNG GÓI: KHÔNG ĐẠT ({tong_loi} lỗi): sửa skill nguồn rồi chạy lại.')
        sys.exit(1)
    print('\nĐÓNG GÓI: ĐẠT. Lưu vào tài khoản Claude: Customize > Skills > + > Create skill > Upload a skill, chọn tệp .zip.'
          ' Thay bản cũ: tắt skill cũ, chọn ... > Delete, rồi tải bản mới. Nếu thư mục gói còn tệp thừa từ lần trước'
          ' (do không xoá được), tệp .zip vẫn đúng: tải .zip.')


if __name__ == '__main__':
    main()

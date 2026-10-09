#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BẢN DỰNG: danh mục tệp của bản vẽ Xưởng web AI và công cụ để trợ lý AI dựng, kiểm, cập nhật một xưởng riêng.

Bản vẽ (repo công khai trên GitHub) không phải thứ để tải về rồi làm việc bên trong. Trợ lý AI đọc bản vẽ, rồi dựng
trên máy người dùng một xưởng riêng (thư mục xuong-web-ai/ trong thư mục làm việc, ví dụ "Web AI"). BAN-DUNG.json
liệt kê từng tệp của bản vẽ và cách dùng nó khi dựng:
  chep         năng lực dùng nguyên (công cụ, khuôn, nền chung, phông, chuẩn, thẻ hướng dẫn, nghiên cứu, skill nguồn,
               bản khởi đầu *.mau.*): đọc và ghi lại vào xưởng ĐÚNG TỪNG BYTE (vân tay sha256 phải khớp).
  mau          mẫu điểm vào của xưởng (mau-xuong/...): trợ lý điền rồi ghi vào xưởng theo "dich"; không so vân tay.
  chi-ban-ve   chỉ có nghĩa ở bản vẽ (README, BAT-DAU, AGENTS, DUNG-XUONG, CHANGELOG...): không đưa vào xưởng.

    python3 tools/ban-dung.py --lap                     # (tác giả, ở bản vẽ) lập lại BAN-DUNG.json từ tệp hiện có
    python3 tools/ban-dung.py --doc-tho                 # (trong xưởng) đọc thô từ bản vẽ trực tuyến mọi tệp "chep" còn
                                                        #   thiếu hoặc khác, kiểm vân tay, ghi vào xưởng; ghi BAN-DUNG.json
    python3 tools/ban-dung.py --doc-tho --chi 'tools/*' # chỉ một phần (mẫu glob trên đường dẫn)
    python3 tools/ban-dung.py --kiem                    # (trong xưởng) đối chiếu xưởng với BAN-DUNG.json đã dựng
    python3 tools/ban-dung.py --kiem --chi-nang-luc     # chỉ phần năng lực (lúc tệp điểm vào của xưởng chưa viết)
    python3 tools/ban-dung.py --so-ban-ve               # (trong xưởng) bản vẽ trực tuyến có gì mới so với lần dựng
    tuỳ chọn: --ban-ve <địa chỉ BAN-DUNG.json hoặc thư mục bản vẽ trên máy>   --ra <thư mục xưởng>   --ghi-de

Không bao giờ ghi vào: phần của người dùng (brand/brand.json, logo đã thả, phong-cach/PHONG-CACH.md, tu-ngu.json,
cau-hinh.json, XUONG.json, CLAUDE.md, AGENTS.md của xưởng), vì chúng không nằm trong nhóm "chep". Tệp "chep" mà người
dùng đã chủ ý sửa trong xưởng (vân tay khác cả bản lúc dựng lẫn bản mới) được giữ nguyên và báo ra, trừ khi --ghi-de.
Tệp .bat được lưu xuống dòng CRLF trong xưởng (Windows cần), vân tay tính trên bản xuống dòng LF như ở bản vẽ.
Chạy được độc lập (không cần tệp nào khác), Python 3.9+, chỉ dùng thư viện chuẩn; mạng theo cấu hình proxy của máy.
"""
import argparse
import datetime
import fnmatch
import hashlib
import json
import os
import re
import sys
import urllib.request

sys.dont_write_bytecode = True
for _luong in (sys.stdout, sys.stderr):  # Windows: in chữ có dấu không lỗi
    try:
        _luong.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
TOOLS = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.dirname(TOOLS)
TEN = 'BAN-DUNG.json'
BAN_VE = 'https://github.com/wincreator3012/xuong-web-ai'
NGUON_THO = 'https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/'
CHI_BAN_VE = ['README.md', 'BAT-DAU.md', 'AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'DUNG-XUONG.md', TEN, 'CHANGELOG.md',
              'docs/DONG-GOP.md', '.gitignore', '.gitattributes', 'mau-xuong/*']
MAU = {'mau-xuong/CLAUDE.md': 'CLAUDE.md', 'mau-xuong/AGENTS.md': 'AGENTS.md', 'mau-xuong/XUONG.mau.json': 'XUONG.json'}
BO_QUA_THU_MUC = {'.git', '__pycache__', 'Claude outputs', 'node_modules', '.DS_Store'}
BO_QUA_TEP = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}


def bam(b):
    return hashlib.sha256(b).hexdigest()


def chuan_hoa(duong, b):
    return b.replace(b'\r\n', b'\n') if duong.lower().endswith('.bat') else b


def doc_byte(p):
    with open(p, 'rb') as h:
        return h.read()


def ghi_byte(p, b):
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    with open(p, 'wb') as h:
        h.write(b)


def loai_cua(rel):
    if rel in MAU:
        return 'mau'
    if any(fnmatch.fnmatch(rel, g) for g in CHI_BAN_VE):
        return 'chi-ban-ve'
    return 'chep'


def phien_ban(goc):
    p = os.path.join(goc, 'CHANGELOG.md')
    if os.path.exists(p):
        m = re.search(r'^##\s+(\d{4}\.\d{2}\.\d{2}[\w.-]*)', open(p, encoding='utf-8').read(), re.M)
        if m:
            return m.group(1)
    return datetime.date.today().strftime('%Y.%m.%d')


def la_xuong(goc):
    return os.path.exists(os.path.join(goc, 'XUONG.json'))


def doc_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'xuong-web-ai-ban-dung'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def nap_ban_dung(nguon):
    """nguon: địa chỉ http(s) tới BAN-DUNG.json, hoặc thư mục bản vẽ trên máy, hoặc đường dẫn tệp."""
    if nguon.startswith('http'):
        d = json.loads(doc_url(nguon).decode('utf-8'))
        d.setdefault('_nap', {'kieu': 'mang', 'nguon': nguon})
        return d
    p = os.path.join(nguon, TEN) if os.path.isdir(nguon) else nguon
    d = json.load(open(p, encoding='utf-8'))
    d['_nap'] = {'kieu': 'may', 'goc': os.path.dirname(os.path.abspath(p))}
    return d


def doc_tep_ban_ve(bd, rel):
    nap = bd.get('_nap', {})
    if nap.get('kieu') == 'may':
        return doc_byte(os.path.join(nap['goc'], rel))
    from urllib.parse import quote
    return doc_url(bd.get('nguonTho', NGUON_THO) + quote(rel))


def nguon_mac_dinh(goc):
    try:
        x = json.load(open(os.path.join(goc, 'XUONG.json'), encoding='utf-8'))
        if x.get('nguonTho'):
            return x['nguonTho'] + TEN
    except (OSError, ValueError):
        pass
    return NGUON_THO + TEN


# ---------------------------------------------------------------- lập (ở bản vẽ)
def ds_tep_ban_ve():
    """Tệp của bản vẽ: có git thì theo git (đã theo dõi, cộng tệp mới chưa bị .gitignore loại), để tệp riêng trên máy
    người bảo trì (cau-hinh.json, brand/brand.json...) không lọt vào danh mục; không có git thì duyệt thư mục."""
    if os.path.isdir(os.path.join(GOC, '.git')):
        import subprocess
        r = subprocess.run(['git', '-C', GOC, 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
                           capture_output=True)
        if r.returncode == 0:
            return sorted(x.decode('utf-8') for x in r.stdout.split(b'\0') if x and os.path.isfile(os.path.join(GOC, x.decode('utf-8'))))
    ra = []
    for dp, dn, fn in os.walk(GOC):
        dn[:] = sorted(d for d in dn if d not in BO_QUA_THU_MUC)
        for f in sorted(fn):
            ra.append(os.path.relpath(os.path.join(dp, f), GOC).replace(os.sep, '/'))
    return sorted(ra)


def lap():
    if la_xuong(GOC):
        raise SystemExit('DỪNG: đây là xưởng đã dựng (có XUONG.json), không phải bản vẽ. --lap chỉ chạy ở bản vẽ.')
    tep = []
    for rel in ds_tep_ban_ve():
        f = rel.rsplit('/', 1)[-1]
        if f in BO_QUA_TEP or f.endswith('.pyc') or rel == TEN:
            continue
        b = chuan_hoa(rel, doc_byte(os.path.join(GOC, rel)))
        muc = {'duong': rel, 'loai': loai_cua(rel), 'sha256': bam(b), 'byte': len(b)}
        if rel in MAU:
            muc['dich'] = MAU[rel]
        tep.append(muc)
    d = {
        '_huong-dan': 'Danh mục tệp của bản vẽ Xưởng web AI. Trợ lý AI dựng xưởng riêng theo DUNG-XUONG.md: tệp "chep" '
                      'ghi lại vào xưởng đúng từng byte (sha256 khớp; .bat lưu CRLF), tệp "mau" điền rồi ghi theo "dich", '
                      'tệp "chi-ban-ve" không đưa vào xưởng. Lập bằng: python3 tools/ban-dung.py --lap',
        'banVe': BAN_VE,
        'nguonTho': NGUON_THO,
        'phienBan': phien_ban(GOC),
        'ngayLap': datetime.date.today().isoformat(),
        'tong': {k: sum(1 for t in tep if t['loai'] == k) for k in ('chep', 'mau', 'chi-ban-ve')},
        'tep': tep,
    }
    with open(os.path.join(GOC, TEN), 'w', encoding='utf-8', newline='\n') as h:
        json.dump(d, h, ensure_ascii=False, indent=1)
        h.write('\n')
    print(f'✓ lập {TEN}: phiên bản {d["phienBan"]}, {d["tong"]["chep"]} tệp chép, {d["tong"]["mau"]} mẫu, '
          f'{d["tong"]["chi-ban-ve"]} chỉ ở bản vẽ')


# ---------------------------------------------------------------- trong xưởng
def trang_thai_tep(goc, muc, cu):
    """moi: chưa có | khop: giống bản vẽ | doi: khác bản vẽ, chưa sửa tay | sua-tay: người dùng đã sửa."""
    p = os.path.join(goc, muc['duong'])
    if not os.path.exists(p):
        return 'moi'
    h = bam(chuan_hoa(muc['duong'], doc_byte(p)))
    if h == muc['sha256']:
        return 'khop'
    h_cu = (cu or {}).get(muc['duong'])
    return 'doi' if h_cu is None or h == h_cu else 'sua-tay'


def vay_tay_cu(goc):
    p = os.path.join(goc, TEN)
    if not os.path.exists(p):
        return {}
    try:
        return {t['duong']: t['sha256'] for t in json.load(open(p, encoding='utf-8')).get('tep', []) if t['loai'] == 'chep'}
    except (OSError, ValueError, KeyError):
        return {}


def doc_tho(a, goc):
    bd = nap_ban_dung(a.ban_ve or nguon_mac_dinh(goc))
    cu = vay_tay_cu(goc)
    chep = [t for t in bd['tep'] if t['loai'] == 'chep' and (not a.chi or any(fnmatch.fnmatch(t['duong'], g) for g in a.chi))]
    da, giu, loi = 0, [], []
    for t in chep:
        tt = trang_thai_tep(goc, t, cu)
        if tt == 'khop':
            continue
        if tt == 'sua-tay' and not a.ghi_de:
            giu.append(t['duong'])
            continue
        try:
            b = doc_tep_ban_ve(bd, t['duong'])
        except Exception as e:  # mạng, 404...
            loi.append(f'{t["duong"]}: không đọc được ({e})')
            continue
        if bam(chuan_hoa(t['duong'], b)) != t['sha256']:
            loi.append(f'{t["duong"]}: vân tay không khớp bản vẽ (bản vẽ đang được cập nhật? chạy lại sau ít phút)')
            continue
        if t['duong'].lower().endswith('.bat'):
            b = chuan_hoa(t['duong'], b).replace(b'\n', b'\r\n')
        ghi_byte(os.path.join(goc, t['duong']), b)
        da += 1
        print(f'  ✓ {t["duong"]}')
    for d in giu:
        print(f'  giữ bản người dùng đã sửa: {d} (muốn lấy bản vẽ thì chạy lại với --ghi-de --chi "{d}")')
    for l in loi:
        print('  LỖI: ' + l)
    if not loi and not a.chi:
        bd2 = {k: v for k, v in bd.items() if k != '_nap'}
        with open(os.path.join(goc, TEN), 'w', encoding='utf-8', newline='\n') as h:
            json.dump(bd2, h, ensure_ascii=False, indent=1)
            h.write('\n')
    print(f'\nĐỌC THÔ: ghi {da} tệp, giữ {len(giu)} tệp đã sửa tay, {len(loi)} lỗi (phiên bản bản vẽ {bd.get("phienBan")}).')
    sys.exit(1 if loi else 0)


def kiem(a, goc):
    p = a.ban_ve or os.path.join(goc, TEN)
    if not a.ban_ve and not os.path.exists(p):
        raise SystemExit(f'Chưa có {TEN} trong xưởng: chạy --doc-tho trước, hoặc --ban-ve <địa chỉ>.')
    bd = nap_ban_dung(p)
    nhom = {'moi': [], 'doi': []}
    for t in bd['tep']:
        if t['loai'] != 'chep' or (a.chi and not any(fnmatch.fnmatch(t['duong'], g) for g in a.chi)):
            continue
        tt = trang_thai_tep(goc, t, None)
        if tt != 'khop':
            nhom['moi' if tt == 'moi' else 'doi'].append(t['duong'])
    thieu_mau = [] if a.chi_nang_luc else [t['dich'] for t in bd['tep'] if t['loai'] == 'mau'
                                            and not os.path.exists(os.path.join(goc, t['dich']))]
    for k, ten in (('moi', 'THIẾU'), ('doi', 'KHÁC bản dựng')):
        if nhom[k]:
            print(f'{ten} ({len(nhom[k])}):')
            for d in nhom[k][:40]:
                print('  ' + d)
    if thieu_mau:
        print('CHƯA VIẾT tệp điểm vào của xưởng (từ mau-xuong/): ' + ', '.join(thieu_mau))
    dat = not nhom['moi'] and not thieu_mau
    print(f'\nKIỂM XƯỞNG THEO BẢN DỰNG ({bd.get("phienBan")}' + (', chỉ phần năng lực' if a.chi_nang_luc else '') + '): '
          + ('ĐẠT' if dat else 'KHÔNG ĐẠT')
          + (f' ({len(nhom["doi"])} tệp khác bản vẽ: do người dùng chủ ý sửa thì giữ, không thì chạy --doc-tho)'
             if nhom['doi'] else ''))
    sys.exit(0 if dat else 1)


def so_ban_ve(a, goc):
    bd = nap_ban_dung(a.ban_ve or nguon_mac_dinh(goc))
    cu = vay_tay_cu(goc)
    try:
        pb_cu = json.load(open(os.path.join(goc, TEN), encoding='utf-8')).get('phienBan')
    except (OSError, ValueError):
        pb_cu = None
    moi_ds = {t['duong'] for t in bd['tep'] if t['loai'] == 'chep'}
    nhom = {'moi': [], 'doi': [], 'sua-tay': []}
    for t in bd['tep']:
        if t['loai'] == 'chep':
            tt = trang_thai_tep(goc, t, cu)
            if tt != 'khop':
                nhom[tt].append(t['duong'])
    bo = sorted(d for d in cu if d not in moi_ds)
    mau_doi = [t['duong'] for t in bd['tep'] if t['loai'] == 'mau']
    print(f'Bản vẽ trực tuyến: phiên bản {bd.get("phienBan")} (lập {bd.get("ngayLap")}); xưởng dựng từ: {pb_cu or "không rõ"}')
    for k, ten in (('moi', 'Tệp mới ở bản vẽ'), ('doi', 'Tệp bản vẽ đã đổi'),
                   ('sua-tay', 'Tệp người dùng đã sửa trong xưởng, khác bản vẽ (giữ nguyên khi --doc-tho; cùng người dùng quyết giữ, lấy bản mới hay trộn tay)')):
        if nhom[k]:
            print(f'{ten} ({len(nhom[k])}):')
            for d in nhom[k][:60]:
                print('  ' + d)
    if bo:
        print(f'Tệp bản vẽ đã bỏ ({len(bo)}): giữ hay chuyển vào thùng chờ xoá là việc người dùng quyết:')
        for d in bo:
            print('  ' + d)
    if pb_cu != bd.get('phienBan'):
        print('Mẫu điểm vào có thể đã đổi (đọc CHANGELOG.md của bản vẽ): ' + ', '.join(mau_doi))
    if not any(nhom.values()) and not bo:
        print('Xưởng đã khớp bản vẽ mới nhất.')
    print('\nĐọc CHANGELOG.md của bản vẽ để biết vì sao đổi, giải thích cho người dùng, xin đồng ý, rồi --doc-tho.')


def main():
    ap = argparse.ArgumentParser(description='Bản dựng của Xưởng web AI: lập, đọc thô, kiểm, so với bản vẽ.')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--lap', action='store_true')
    g.add_argument('--doc-tho', action='store_true')
    g.add_argument('--kiem', action='store_true')
    g.add_argument('--so-ban-ve', action='store_true')
    ap.add_argument('--ban-ve', help='địa chỉ BAN-DUNG.json, hoặc thư mục bản vẽ trên máy')
    ap.add_argument('--ra', help='thư mục xưởng (mặc định: thư mục chứa tools/ này)')
    ap.add_argument('--chi', action='append', help='chỉ các đường dẫn khớp mẫu glob (lặp được)')
    ap.add_argument('--ghi-de', action='store_true', help='ghi đè cả tệp người dùng đã sửa tay')
    ap.add_argument('--chi-nang-luc', action='store_true', help='--kiem: bỏ qua tệp điểm vào (CLAUDE.md, AGENTS.md, XUONG.json)')
    a = ap.parse_args()
    if a.lap:
        return lap()
    goc = os.path.abspath(a.ra) if a.ra else GOC
    if os.path.exists(os.path.join(goc, 'AGENTS.md')) and not la_xuong(goc) \
            and os.path.exists(os.path.join(goc, 'DUNG-XUONG.md')):
        raise SystemExit('DỪNG: thư mục này là bản vẽ (có DUNG-XUONG.md, chưa có XUONG.json), không phải xưởng. '
                         'Dựng xưởng ở thư mục làm việc khác theo DUNG-XUONG.md: chép tools/ban-dung.py vào '
                         '<xưởng>/tools/, rồi chạy nó từ đó với --ban-ve <thư mục bản vẽ này>.')
    if a.ra and not (la_xuong(goc) or os.path.exists(os.path.join(goc, 'tools', 'ban-dung.py'))):
        raise SystemExit(f'DỪNG: {goc} chưa phải xưởng (chưa có XUONG.json hay tools/ban-dung.py): không ghi vào đó.')
    if a.doc_tho:
        doc_tho(a, goc)
    elif a.kiem:
        kiem(a, goc)
    else:
        so_ban_ve(a, goc)


if __name__ == '__main__':
    main()

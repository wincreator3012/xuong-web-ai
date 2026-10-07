#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐƯA LÊN MẠNG: chuẩn bị cấu hình cho nơi lưu trữ, đặt tên miền, chạy cổng kiểm, rồi mới đưa web lên.

    python3 tools/dua-len.py <web> --noi cloudflare            # chuẩn bị cấu hình + in các bước (chưa đưa lên)
    python3 tools/dua-len.py <web> --ten-mien https://khoahoc.vidu.vn   # gắn tên miền vào canonical, Open Graph, sitemap, robots
    python3 tools/dua-len.py <web> --noi cloudflare --that     # kiểm --len ĐẠT rồi mới chạy lệnh đưa lên thật
    python3 tools/dua-len.py --so-sanh                         # bảng chọn nơi lưu trữ (chuan/07-trien-khai.md)

Nơi lưu trữ (--noi): cloudflare (mặc định của xưởng), vercel, netlify, firebase, github-pages.
Lệnh đưa lên thật cần đăng nhập một lần (người dùng tự làm, huong-dan/) hoặc mã truy cập trong biến môi trường:
CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID, VERCEL_TOKEN, NETLIFY_AUTH_TOKEN, GOOGLE_APPLICATION_CREDENTIALS.
Mã truy cập không bao giờ ghi vào tệp trong thư mục web. Cách thường ngày tốt hơn: nối kho GitHub với nơi lưu trữ một lần,
từ đó mỗi lần đẩy [push] lên nhánh main là web tự cập nhật (huong-dan/02-cloudflare.md, 03-vercel.md...).
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402

NOI = {
    'cloudflare': {'huongDan': 'huong-dan/02-cloudflare.md', 'thuongMai': True, 'lenh': ['npx', '--yes', 'wrangler@4', 'deploy']},
    'vercel': {'huongDan': 'huong-dan/03-vercel.md', 'thuongMai': False, 'lenh': ['npx', '--yes', 'vercel@latest', 'deploy', '--prod', '--yes']},
    'netlify': {'huongDan': 'huong-dan/04-netlify.md', 'thuongMai': True, 'lenh': ['npx', '--yes', 'netlify-cli', 'deploy', '--prod']},
    'firebase': {'huongDan': 'huong-dan/05-firebase.md', 'thuongMai': True, 'lenh': ['npx', '--yes', 'firebase-tools', 'deploy']},
    'github-pages': {'huongDan': 'huong-dan/01-github.md', 'thuongMai': False, 'lenh': None},
}
SO_SANH = """NƠI LƯU TRỮ (kiểm 07/10/2026; giá và hạn mức đổi nhanh, xem chuan/07-trien-khai.md và kho-dich-vu.json)
  cloudflare    MẶC ĐỊNH. Miễn phí, được dùng thương mại, băng thông tệp tĩnh không giới hạn, có máy chủ ở Hà Nội và TP.HCM.
                Gắn tên miền riêng: chuyển máy chủ tên miền [nameserver] sang Cloudflare.
  vercel        Dễ nhất cho người mới, nhưng gói Hobby CHỈ phi thương mại (trang có bán, quảng bá dịch vụ là vi phạm).
  netlify       Gói Free tính theo tín dụng: khoảng 20 lần đưa bản chính thức mỗi tháng; hết tín dụng là MỌI web trong
                tài khoản tạm dừng. Có biểu mẫu miễn phí. Chỉ chọn khi web ít sửa.
  firebase      Cho web-app đã dùng Firebase (đăng nhập, Firestore). Gói Spark: 10 GB truyền dữ liệu mỗi tháng.
  github-pages  Trang cá nhân, tài liệu công khai, phi thương mại. Kho phải công khai (gói miễn phí)."""


def cap_ten_mien(web, url):
    url = url.rstrip('/')
    if not re.match(r'https://[a-z0-9.-]+\.[a-z]{2,}$', url):
        raise SystemExit('Tên miền dạng https://ten.vn hoặc https://www.ten.com (không có đường dẫn phía sau).')
    hs = C.ho_so_web(web)
    cu = [x for x in ('https://[[ten-mien]]', 'https://chua-dat-ten-mien.invalid', hs.get('tenMien', '').rstrip('/')) if x]
    doi = 0
    for dp, dn, fn in os.walk(web):
        dn[:] = [d for d in dn if d not in ('node_modules', '.git', 'dist', 'fonts', '.astro')]
        for f in fn:
            p = os.path.join(dp, f)
            if os.path.splitext(f)[1].lower() not in C.DUOI_VAN_BAN:
                continue
            s = C.doc(p)
            moi = s
            for x in cu:
                moi = moi.replace(x, url)
            if moi != s:
                C.ghi(p, moi)
                doi += 1
    if hs.get('loai') != 'astro':  # Astro tự sinh sitemap khi dựng
        ck = C.thu_muc_cong_khai(web)
        trang = []
        for dp, dn, fn in os.walk(ck):
            dn[:] = [d for d in dn if d != 'assets']
            for f in sorted(fn):
                if f.endswith('.html') and f != '404.html':
                    p = os.path.join(dp, f)
                    if 'noindex' in C.doc(p):
                        continue
                    rel = os.path.relpath(p, ck).replace(os.sep, '/')
                    rel = '' if rel == 'index.html' else rel[:-10] if rel.endswith('/index.html') else rel
                    trang.append(f'  <url><loc>{url}/{rel}</loc><lastmod>{C.hom_nay()}</lastmod></url>')
        C.ghi(os.path.join(ck, 'sitemap.xml'), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
              + '\n'.join(trang) + '\n</urlset>\n')
    hs['tenMien'] = url
    C.ghi_json(os.path.join(web, 'xuong.json'), hs)
    print(f'Đã gắn tên miền {url} ({doi} tệp; sitemap.xml đã cập nhật). Bước DNS người dùng tự làm: huong-dan/07-dns.md')


def doc_headers(ck):
    """Đọc public/_headers (Cloudflare, Netlify) để dựng phần headers cho vercel.json, firebase.json."""
    p = os.path.join(ck, '_headers')
    if not os.path.exists(p):
        return []
    ra, hien = [], None
    for dong in C.doc(p).splitlines():
        if not dong.strip() or dong.lstrip().startswith('#'):
            continue
        if not dong.startswith((' ', '\t')):
            hien = {'source': dong.strip().replace('/*', '/(.*)'), 'headers': []}
            ra.append(hien)
        elif hien and ':' in dong:
            k, v = dong.strip().split(':', 1)
            hien['headers'].append({'key': k.strip(), 'value': v.strip()})
    return ra


def chuan_bi(web, noi):
    hs = C.ho_so_web(web)
    ten = os.path.basename(web)
    thu_muc = 'dist' if hs.get('loai') == 'astro' else 'public'
    ck = os.path.join(web, 'public')
    tao = []
    if noi == 'cloudflare':
        p = os.path.join(web, 'wrangler.jsonc')
        if not os.path.exists(p):
            C.ghi(p, '// Cloudflare Workers, chỉ tệp tĩnh (không có mã chạy ở máy chủ). Chỉ thư mục ' + thu_muc + '/ được đưa lên.\n'
                  + json.dumps({'name': ten, 'compatibility_date': C.hom_nay(),
                                'assets': {'directory': f'./{thu_muc}', 'not_found_handling': '404-page'}},
                               ensure_ascii=False, indent=2) + '\n')
            tao.append('wrangler.jsonc')
    elif noi == 'vercel':
        p = os.path.join(web, 'vercel.json')
        if not os.path.exists(p):
            d = {'outputDirectory': thu_muc, 'cleanUrls': True, 'headers': doc_headers(ck)}
            if hs.get('loai') == 'astro':
                d['buildCommand'] = 'npm run build'
            C.ghi_json(p, d)
            tao.append('vercel.json')
    elif noi == 'netlify':
        p = os.path.join(web, 'netlify.toml')
        if not os.path.exists(p):
            C.ghi(p, f'[build]\n  publish = "{thu_muc}"\n' + ('  command = "npm run build"\n' if hs.get('loai') == 'astro' else ''))
            tao.append('netlify.toml')
    elif noi == 'firebase':
        p = os.path.join(web, 'firebase.json')
        if not os.path.exists(p):
            C.ghi_json(p, {'hosting': {'public': thu_muc, 'ignore': ['**/.*'], 'cleanUrls': True, 'headers': doc_headers(ck)}})
            tao.append('firebase.json')
    elif noi == 'github-pages':
        p = os.path.join(web, '.github', 'workflows', 'pages.yml')
        if not os.path.exists(p):
            buoc_dung = ('      - uses: actions/setup-node@v4\n        with: { node-version: 22 }\n      - run: npm ci && npm run build\n'
                         if hs.get('loai') == 'astro' else '')
            C.ghi(p, f"""# Đưa thư mục {thu_muc}/ lên GitHub Pages mỗi lần đẩy lên nhánh main.
name: Dua len GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  dua-len:
    runs-on: ubuntu-latest
    environment: github-pages
    steps:
      - uses: actions/checkout@v4
{buoc_dung}      - uses: actions/upload-pages-artifact@v3
        with: {{ path: {thu_muc} }}
      - uses: actions/deploy-pages@v4
""")
            tao.append('.github/workflows/pages.yml')
    hs['noiDat'] = noi
    C.ghi_json(os.path.join(web, 'xuong.json'), hs)
    return tao


def main():
    ap = argparse.ArgumentParser(description='Chuẩn bị và đưa một web lên mạng.')
    ap.add_argument('web', nargs='?')
    ap.add_argument('--noi', choices=list(NOI))
    ap.add_argument('--ten-mien')
    ap.add_argument('--that', action='store_true', help='chạy lệnh đưa lên thật (sau khi kiểm --len ĐẠT)')
    ap.add_argument('--bo-kiem-trinh-duyet', action='store_true', help='máy không có trình duyệt: chỉ kiểm tĩnh')
    ap.add_argument('--so-sanh', action='store_true')
    a = ap.parse_args()
    if a.so_sanh or not a.web:
        print(SO_SANH)
        return
    web = C.tim_web(a.web)
    hs = C.ho_so_web(web)
    if a.ten_mien:
        cap_ten_mien(web, a.ten_mien)
    noi = a.noi or hs.get('noiDat')
    if not noi:
        if not a.ten_mien:
            print(SO_SANH + '\n\nChọn nơi lưu trữ bằng --noi.')
        return
    tao = chuan_bi(web, noi)
    if tao:
        print('Đã tạo cấu hình: ' + ', '.join(tao))
    if not NOI[noi]['thuongMai'] and hs.get('khuon') in ('landing', 'bao-gia', 'app-firebase'):
        print(f'CẢNH BÁO: {noi} (gói miễn phí) không cho dùng thương mại; web "{hs.get("khuon")}" thường là thương mại. Cân nhắc cloudflare.')
    if hs.get('loai') == 'astro':
        if not os.path.isdir(os.path.join(web, 'node_modules')):
            subprocess.run(['npm', 'install', '--no-audit', '--no-fund'], cwd=web, check=True)
        subprocess.run(['npm', 'run', 'build'], cwd=web, check=True)
    kiem = [sys.executable, os.path.join(C.TOOLS, 'kiem-web.py'), web, '--len', '--im']
    if a.bo_kiem_trinh_duyet:
        kiem.append('--khong-trinh-duyet')
    if subprocess.run(kiem).returncode != 0:
        raise SystemExit('DỪNG: cổng kiểm trước khi đưa lên mạng chưa ĐẠT (xem BAO-CAO.md). Sửa xong chạy lại.')
    lenh = NOI[noi]['lenh']
    if not a.that:
        print(f'\nĐã sẵn sàng đưa lên {noi}. Việc người dùng tự làm một lần: {NOI[noi]["huongDan"]}.')
        print('Lệnh đưa lên: ' + (' '.join(lenh) if lenh else 'đẩy kho lên GitHub (git push), quy trình .github/workflows/pages.yml tự chạy')
              + f'  (chạy trong {web})\nHoặc chạy lại công cụ này với --that.')
        return
    if not lenh:
        raise SystemExit('GitHub Pages: đưa lên bằng git push lên nhánh main (huong-dan/01-github.md).')
    if not shutil.which('npx'):
        raise SystemExit('Máy này chưa có Node.js (npx). Cài Node 22 LTS từ nodejs.org, hoặc nối kho GitHub với nơi lưu trữ để tự đưa lên.')
    if noi == 'vercel' and os.environ.get('VERCEL_TOKEN'):
        lenh = lenh + ['--token', os.environ['VERCEL_TOKEN']]
    if noi == 'netlify':
        lenh = lenh + ['--dir', 'dist' if hs.get('loai') == 'astro' else 'public']
    print('Chạy: ' + ' '.join(x if not x.startswith(os.environ.get('VERCEL_TOKEN', '\0')) else '***' for x in lenh))
    r = subprocess.run(lenh, cwd=web)
    if r.returncode == 0:
        hs = C.ho_so_web(web)
        hs['lanCuoi'] = datetime.datetime.now().isoformat(timespec='minutes')
        C.ghi_json(os.path.join(web, 'xuong.json'), hs)
        print('Đã đưa lên. Ghi địa chỉ và ngày vào VAN-HANH.md của dự án; mở thử trên điện thoại.')
    sys.exit(r.returncode)


if __name__ == '__main__':
    main()

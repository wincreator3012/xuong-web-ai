#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XEM THỬ: mở web trên máy để xem trước khi đưa lên mạng.

    python3 tools/xem.py <web>            # chạy máy chủ nhỏ ở http://localhost:8000 và mở trình duyệt; Ctrl+C để dừng
    python3 tools/xem.py                  # không nêu tên: liệt kê các web, hỏi chọn (Enter = web sửa gần nhất)
    python3 tools/xem.py <web> --cong 8100

Web tĩnh: phục vụ thư mục public/ (đường dẫn /assets/... chạy đúng như trên mạng, khác với bấm đúp tệp).
Web Astro: chạy npm run dev (tự cập nhật khi sửa tệp). Trên máy ảo của Claude Cowork không có trình duyệt:
người dùng tự chạy lệnh này trên máy của mình, hoặc nhìn ảnh chụp do tools/kiem-web.py tạo.
"""
import argparse
import functools
import http.server
import os
import subprocess
import sys
import threading
import webbrowser

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402


def chon_web():
    """Không nêu tên web: liệt kê các web trong thuMucWeb, mới sửa nhất lên đầu, hỏi chọn."""
    goc = C.thu_muc_web()
    ds = sorted((d for d in (os.listdir(goc) if os.path.isdir(goc) else [])
                 if os.path.isdir(os.path.join(goc, d)) and not d.startswith(('.', '_'))),
                key=lambda d: os.path.getmtime(os.path.join(goc, d)), reverse=True)
    if not ds:
        raise SystemExit(f'Chưa có web nào trong {goc}. Nhờ trợ lý tạo web trước.')
    if len(ds) == 1 or not sys.stdin.isatty():
        return ds[0]
    print('Các web của bạn (mới sửa nhất ở đầu):')
    for i, d in enumerate(ds, 1):
        print(f'  {i}. {d}')
    try:
        tl = input(f'Gõ số hoặc tên web rồi Enter (chỉ Enter = {ds[0]}): ').strip()
    except EOFError:
        tl = ''
    if not tl:
        return ds[0]
    if tl.isdigit() and 1 <= int(tl) <= len(ds):
        return ds[int(tl) - 1]
    return tl


def mo_may_chu(goc, cong):
    """Thử cổng đã chọn rồi các cổng kế tiếp (cổng có thể đang bận vì một cửa sổ xem khác)."""
    loi = None
    for c in range(cong, cong + 20):
        try:
            return http.server.ThreadingHTTPServer(('127.0.0.1', c), functools.partial(http.server.SimpleHTTPRequestHandler, directory=goc)), c
        except OSError as e:
            loi = e
    raise SystemExit(f'Không mở được máy chủ xem thử từ cổng {cong} tới {cong + 19}: {loi}')


def main():
    ap = argparse.ArgumentParser(description='Xem thử một web trên máy.')
    ap.add_argument('web', nargs='?')
    ap.add_argument('--cong', type=int, default=8000)
    a = ap.parse_args()
    web = C.tim_web(a.web or chon_web())
    if C.ho_so_web(web).get('loai') == 'astro':
        if not os.path.isdir(os.path.join(web, 'node_modules')):
            subprocess.run(['npm', 'install', '--no-audit', '--no-fund'], cwd=web, check=True)
        sys.exit(subprocess.run(['npm', 'run', 'dev', '--', '--port', str(a.cong), '--open'], cwd=web).returncode)
    goc = os.path.join(web, 'public')
    srv, cong = mo_may_chu(goc, a.cong)
    url = f'http://localhost:{cong}/'
    print(f'Đang phục vụ {goc}\nMở {url} (Ctrl+C để dừng)')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print('\nĐã dừng.')


if __name__ == '__main__':
    main()

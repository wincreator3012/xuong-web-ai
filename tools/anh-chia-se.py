#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ẢNH CHIA SẺ: dựng ảnh 1200x630 (Open Graph) hiện khi gửi link web qua Zalo, Facebook, Messenger, LinkedIn.

    python3 tools/anh-chia-se.py <web>                                  # lấy tiêu đề, mô tả từ trang chính
    python3 tools/anh-chia-se.py <web> --tieu-de "Khoá học mùa thu" --dong-phu "Khai giảng 12/11, TP.HCM"
    python3 tools/anh-chia-se.py <web> --anh public/assets/img/chan-dung.webp     # thêm ảnh thật bên phải

Bố cục mặc định theo chuẩn xưởng (chuan/03-thiet-ke-web.md): nền tối của chủ đề, tiêu đề phông tiêu đề, một dòng phụ,
tên thương hiệu; chữ nằm trong vùng an toàn giữa ảnh vì Zalo, Facebook cắt mép khác nhau. Ghi ra
<public>/assets/img/chia-se.jpg. Cần trình duyệt (Playwright). Có ảnh thiết kế sẵn từ xưởng thiết kế (khổ og 1200x630)
thì chép đè vào đúng đường dẫn đó, không cần chạy công cụ này.
Sau khi web đã lên mạng mà Zalo còn hiện ảnh cũ: dùng công cụ làm mới bộ đệm https://developers.zalo.me/tools/debug-sharing
và https://developers.facebook.com/tools/debug/.
"""
import argparse
import html
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402

MAU = """<!doctype html><html lang="vi"><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts/fonts.css"><link rel="stylesheet" href="assets/css/tokens.css">
<style>
 html,body{margin:0}
 .og{width:1200px;height:630px;box-sizing:border-box;padding:84px 96px;display:flex;gap:56px;align-items:center;
   background:var(--toi-nen);color:var(--toi-chu);font-family:var(--phong-noi-dung),sans-serif;position:relative;overflow:hidden}
 .chu{flex:1;display:flex;flex-direction:column;gap:28px}
 .nhan{font-size:24px;letter-spacing:.06em;text-transform:uppercase;color:var(--toi-nhan);font-weight:600}
 h1{font-family:var(--phong-tieu-de),Georgia,serif;font-weight:600;font-size:SIZEpx;line-height:1.18;margin:0;text-wrap:balance}
 p{font-size:30px;line-height:1.45;margin:0;color:var(--toi-chu-phu)}
 .ten{font-size:24px;color:var(--toi-chu-phu);margin-top:8px}
 .vach{position:absolute;left:96px;right:96px;bottom:56px;height:2px;background:var(--vang);opacity:.6}
 img{width:340px;height:420px;object-fit:cover;border-radius:10px}
</style></head><body><div class="og"><div class="chu">NHAN<h1>TIEU_DE</h1>DONG_PHU<div class="ten">TEN</div></div>ANH<div class="vach"></div></div></body></html>"""


def lay_tu_trang(cong_khai):
    p = os.path.join(cong_khai, 'index.html')
    if not os.path.exists(p):
        return '', ''
    s = C.doc(p)

    def meta(k):
        m = re.search(r'<meta\s+(?:property|name)="' + re.escape(k) + r'"\s+content="([^"]*)"', s)
        return html.unescape(m.group(1)) if m else ''
    return meta('og:title'), meta('og:description')


def main():
    ap = argparse.ArgumentParser(description='Dựng ảnh chia sẻ 1200x630 cho một web.')
    ap.add_argument('web')
    ap.add_argument('--tieu-de')
    ap.add_argument('--dong-phu')
    ap.add_argument('--nhan', default='', help='nhãn nhỏ phía trên tiêu đề, ví dụ "Khai giảng 12/11/2026"')
    ap.add_argument('--anh', help='ảnh thật đặt bên phải (đường dẫn tính từ thư mục web)')
    a = ap.parse_args()
    web = C.tim_web(a.web)
    ck = os.path.join(web, 'public')  # nguồn tài sản (Astro cũng giữ ở public/)
    td, mt = lay_tu_trang(C.thu_muc_cong_khai(web))
    tieu_de = a.tieu_de or td or os.path.basename(web)
    dong_phu = a.dong_phu if a.dong_phu is not None else mt
    if '[[' in tieu_de + (dong_phu or ''):
        raise SystemExit('Tiêu đề, mô tả trang chính còn chỗ trống [[...]]: điền trước, hoặc truyền --tieu-de, --dong-phu.')
    b = C.brand()
    hs = C.ho_so_web(web)
    ten = b['thuongHieu'].get(hs.get('thuongHieu') or b.get('thuongHieuMacDinh'), {}).get('ten', '')
    co = 64 if len(tieu_de) < 40 else 54 if len(tieu_de) < 70 else 46
    anh = ''
    if a.anh:
        pa = os.path.abspath(os.path.join(web, a.anh))
        anh = f'<img src="file://{pa}" alt="">'
    trang = (MAU.replace('SIZE', str(co)).replace('TIEU_DE', html.escape(tieu_de))
             .replace('DONG_PHU', f'<p>{html.escape(dong_phu)}</p>' if dong_phu else '')
             .replace('NHAN', f'<div class="nhan">{html.escape(a.nhan)}</div>' if a.nhan else '')
             .replace('TEN', html.escape(ten)).replace('ANH', anh))
    tam = os.path.join(ck, '_anh-chia-se-tam.html')
    C.ghi(tam, trang)
    dich = os.path.join(ck, 'assets', 'img', 'chia-se.jpg')
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        os.remove(tam)
        raise SystemExit('Cần Playwright (chạy ở sandbox đám mây của phiên, hoặc pip install playwright).')
    try:
        with sync_playwright() as pw:
            tr = pw.chromium.launch()
            pg = tr.new_page(viewport={'width': 1200, 'height': 630})
            pg.goto('file://' + tam)
            pg.evaluate('document.fonts.ready')
            pg.wait_for_timeout(300)
            pg.screenshot(path=dich, type='jpeg', quality=88, clip={'x': 0, 'y': 0, 'width': 1200, 'height': 630})
            tr.close()
    finally:
        os.remove(tam)
    print(f'Đã dựng {dich} (1200x630). Nhìn ảnh trước khi dùng; Astro: dựng lại (npm run build) để dist/ có ảnh mới.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIỂM WEB: cổng nghiệm thu tự động của xưởng. Chưa ĐẠT thì chưa nói "xong", chưa đưa lên mạng.

    python3 tools/kiem-web.py <web>                    # kiểm đủ: mã nguồn, chữ, an toàn, rồi trình duyệt (nếu có)
    python3 tools/kiem-web.py <web> --len              # chế độ trước khi đưa lên mạng: chỗ còn trống [[...]], ảnh chờ,
                                                       #   tên miền chưa đặt, khoá form chưa dán đều thành LỖI
    python3 tools/kiem-web.py <web> --khong-trinh-duyet   # chỉ kiểm tĩnh (máy không có trình duyệt)
    python3 tools/kiem-web.py <web> --ra <thư mục>     # nơi ghi báo cáo, ảnh chụp (mặc định <hồ sơ dự án>/kiem/)

<web>: tên thư mục trong thuMucWeb (cau-hinh.json) hoặc đường dẫn. Kiểm phần công khai (public/, Astro: dist/ sau
khi dựng) và cả thư mục web (tìm khoá bí mật, luật Firebase lỏng).

Ba mức: LỖI (chặn), CẢNH BÁO (xem và có lý do mới bỏ qua), GỢI Ý (chữ nên cân nhắc). Thoát mã 1 nếu còn LỖI.

TĨNH (không cần trình duyệt)
  html     lang, một h1, thứ bậc tiêu đề, title <= 60, mô tả <= 155, Open Graph, viewport, ảnh có alt và kích thước,
           liên kết nội bộ tới tệp và #id có thật, target=_blank có rel=noopener
  form     ô có nhãn, form thu thông tin cá nhân có ô đồng ý KHÔNG đánh dấu sẵn và liên kết chính sách, có bẫy rác,
           đã khai data-gui, khoá Web3Forms đã dán
  chữ      gạch dài, ba chấm Unicode, nháy cong, Title Case ở tiêu đề và nút, từ cấm và sáo ngữ (chung + phong-cach/tu-ngu.json),
           chỗ còn trống [[...]], khung ảnh chờ
  an toàn  khoá bí mật trong mã (tài khoản dịch vụ, khoá Resend, Stripe, GitHub, Supabase secret...), tệp không nên công khai
           nằm trong public/, luật Firestore/Storage lỏng, firebase.json đăng cả thư mục gốc, dữ liệu đáp án gửi xuống trình duyệt
TRÌNH DUYỆT (Playwright + Chromium)
  chụp mỗi trang ở 390, 768, 1280 px (và tờ tổng thể), tràn ngang, lỗi JavaScript, tệp nội bộ hỏng, chữ dưới 14 px,
  khả năng tiếp cận WCAG 2.2 AA bằng axe-core (tương phản, nhãn, tên nút, vùng bấm...), trọng lượng trang, ảnh quá nặng
"""
import argparse
import functools
import html.parser
import http.server
import json
import os
import re
import socket
import sys
import threading
import urllib.parse

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chung as C  # noqa: E402

KHO = (390, 768, 1280)
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
AN_CHU = {'script', 'style', 'template', 'noscript', 'svg'}
BI_MAT = [
    (r'-----BEGIN (RSA |EC )?PRIVATE KEY-----', 'khoá riêng [private key]'),
    (r'"private_key"\s*:', 'tệp tài khoản dịch vụ Google/Firebase [service account]'),
    (r'\bsb_secret_[A-Za-z0-9_-]{10,}', 'khoá bí mật Supabase (vượt qua mọi luật bảo vệ)'),
    (r'service_role', 'khoá service_role Supabase'),
    (r'\bre_[A-Za-z0-9]{8,}_[A-Za-z0-9]{8,}', 'khoá API Resend (gửi thư dưới tên bạn)'),
    (r'\bsk_live_[A-Za-z0-9]{10,}', 'khoá bí mật Stripe'),
    (r'\bgh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}', 'mã truy cập GitHub'),
    (r'\bAKIA[0-9A-Z]{16}\b', 'khoá truy cập AWS'),
    (r'\bxox[baprs]-[A-Za-z0-9-]{10,}', 'mã Slack'),
    (r'\bAIza[0-9A-Za-z_-]{35}\b(?=[^\n]*(gemini|generativelanguage|maps))', 'khoá Google API dùng cho Gemini/Maps (khoá Firebase thì được công khai)'),
    (r'(?i)(api[_-]?key|secret|password|mat[_-]?khau)\s*[:=]\s*["\'][^"\'\s\[]{12,}["\']', 'chuỗi trông như khoá bí mật gán thẳng trong mã'),
]
TEP_KHONG_CONG_KHAI = re.compile(r'(?i)\.(md|py|sh|command|bat|env|log|bak|pem|key|sqlite|db|numbers|xlsx|csv)$|(^|/)(\.env.*|token\.json|credentials\.json|serviceAccountKey\.json)$')
AXE_VI = {
    'color-contrast': 'tương phản chữ trên nền chưa đủ (4.5:1 chữ thường, 3:1 chữ lớn)',
    'image-alt': 'ảnh thiếu văn bản thay thế (alt)',
    'label': 'ô nhập thiếu nhãn',
    'link-name': 'liên kết không có chữ mô tả',
    'button-name': 'nút không có tên',
    'html-has-lang': 'thiếu lang ở thẻ html',
    'target-size': 'vùng bấm nhỏ hơn 24x24 px',
    'heading-order': 'tiêu đề nhảy bậc',
    'landmark-one-main': 'thiếu vùng <main>',
    'region': 'nội dung nằm ngoài các vùng chính (header, main, footer)',
    'document-title': 'thiếu tiêu đề trang',
    'list': 'danh sách chứa phần tử không hợp lệ',
    'listitem': 'mục danh sách nằm ngoài ul/ol',
    'definition-list': 'danh sách định nghĩa dl chứa phần tử không hợp lệ',
    'dlitem': 'dt/dd nằm ngoài dl',
    'duplicate-id': 'trùng id',
    'frame-title': 'khung nhúng thiếu title',
    'scrollable-region-focusable': 'vùng cuộn không dùng được bằng bàn phím',
    'meta-viewport': 'chặn phóng to trên điện thoại',
    'page-has-heading-one': 'trang thiếu h1',
    'aria-allowed-attr': 'thuộc tính ARIA không hợp lệ',
    'nested-interactive': 'thành phần bấm được lồng nhau',
}


# ---------------------------------------------------------------- cây HTML tối giản
class Nut:
    __slots__ = ('tag', 'attrs', 'con', 'cha', 'chu', 'dong')

    def __init__(self, tag, attrs, cha, dong):
        self.tag, self.attrs, self.cha, self.con, self.chu, self.dong = tag, dict(attrs), cha, [], [], dong

    def lop(self):
        return (self.attrs.get('class') or '').split()

    def text(self):
        if self.tag in AN_CHU:
            return ''
        return ' '.join(x if isinstance(x, str) else x.text() for x in self.chu).strip()

    def duyet(self):
        yield self
        for c in self.con:
            yield from c.duyet()

    def to_tien(self):
        n = self.cha
        while n:
            yield n
            n = n.cha


class DungCay(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.goc = Nut('#goc', [], None, 0)
        self.hien = self.goc
        self.chu_thich = []

    def handle_starttag(self, tag, attrs):
        n = Nut(tag, attrs, self.hien, self.getpos()[0])
        self.hien.con.append(n)
        self.hien.chu.append(n)
        if tag not in VOID:
            self.hien = n

    def handle_startendtag(self, tag, attrs):
        n = Nut(tag, attrs, self.hien, self.getpos()[0])
        self.hien.con.append(n)
        self.hien.chu.append(n)

    def handle_endtag(self, tag):
        n = self.hien
        while n is not self.goc and n.tag != tag:
            n = n.cha
        if n is not self.goc:
            self.hien = n.cha

    def handle_data(self, data):
        if data.strip():
            self.hien.chu.append(re.sub(r'\s+', ' ', data))

    def handle_comment(self, data):
        self.chu_thich.append((self.getpos()[0], data.strip()))


def phan_tich(p):
    d = DungCay()
    d.feed(C.doc(p))
    return d


# ---------------------------------------------------------------- báo cáo
class BaoCao:
    def __init__(self):
        self.muc = []

    def them(self, muc, loai, tep, chi_tiet, dong=None):
        if dong is None:  # cùng một điều ở nhiều trang: gộp một dòng, liệt kê các trang
            for m in self.muc:
                if m['muc'] == muc and m['loai'] == loai and m['chiTiet'] == chi_tiet and m['dong'] is None:
                    m['tep'] += ', ' + tep
                    return
        self.muc.append({'muc': muc, 'loai': loai, 'tep': tep, 'dong': dong, 'chiTiet': chi_tiet})

    def loi(self, *a, **k):
        self.them('LỖI', *a, **k)

    def canh(self, *a, **k):
        self.them('CẢNH BÁO', *a, **k)

    def goi_y(self, *a, **k):
        self.them('GỢI Ý', *a, **k)

    def dem(self, muc):
        return sum(1 for m in self.muc if m['muc'] == muc)


# ---------------------------------------------------------------- kiểm tĩnh
def kiem_chu(bc, rel, chu, dong=None, la_tieu_de=False):
    cam, nen = C.luat_chu()
    for mau, ly_do in cam:
        if re.search(mau, chu):
            bc.loi('chu', rel, f'{ly_do}: "{chu[:70]}"', dong)
    for mau, ly_do in nen:
        m = re.search(mau, chu)
        if m:
            bc.goi_y('chu', rel, f'"{m.group(0)[:40]}": {ly_do}', dong)
    if la_tieu_de and C.la_title_case(chu):
        bc.loi('chu', rel, f'Title Case (viết hoa đầu mọi từ): dùng sentence case hoặc FULL-CAP: "{chu[:70]}"', dong)


def kiem_html(bc, web, cong_khai, p, len_mang):
    rel = os.path.relpath(p, web)
    d = phan_tich(p)
    goc = d.goc
    tat = list(goc.duyet())
    the = lambda t: [n for n in tat if n.tag == t]  # noqa: E731
    htm = the('html')
    if not htm or not htm[0].attrs.get('lang'):
        bc.loi('html', rel, 'thiếu lang="vi" ở thẻ <html> (trình đọc màn hình đọc sai giọng)')
    metas = the('meta')

    def meta(k, v):
        return next((m.attrs.get('content', '') for m in metas if m.attrs.get(k) == v), None)
    if not any(m.attrs.get('name') == 'viewport' for m in metas):
        bc.loi('html', rel, 'thiếu meta viewport: điện thoại sẽ hiện trang thu nhỏ')
    elif 'user-scalable=no' in (meta('name', 'viewport') or '') or 'maximum-scale=1' in (meta('name', 'viewport') or ''):
        bc.loi('html', rel, 'meta viewport chặn phóng to: người mắt kém không đọc được')
    la_404 = os.path.basename(p) == '404.html'
    tieu_de = the('title')
    td = tieu_de[0].text() if tieu_de else ''
    if not td:
        bc.loi('html', rel, 'thiếu <title>')
    elif len(td) > 60:
        bc.canh('seo', rel, f'tiêu đề {len(td)} ký tự (Google cắt sau khoảng 60): "{td}"')
    mo_ta = meta('name', 'description')
    noindex = 'noindex' in (meta('name', 'robots') or '')
    if not la_404 and not noindex:
        if not mo_ta:
            bc.canh('seo', rel, 'thiếu meta description (chữ hiện dưới tiêu đề trên Google, Zalo, Facebook)')
        elif len(mo_ta) > 155:
            bc.canh('seo', rel, f'mô tả {len(mo_ta)} ký tự (nên dưới 155)')
        la_chinh = os.path.basename(p) == 'index.html'
        for k in ('og:title', 'og:description', 'og:image', 'og:url'):
            if not meta('property', k) and la_chinh:
                bc.canh('chia-se', rel, f'thiếu {k}: link chia sẻ qua Zalo, Facebook sẽ không có ảnh, tiêu đề đẹp')
        og = meta('property', 'og:image') or ''
        if og and not og.startswith('http'):
            bc.canh('chia-se', rel, 'og:image phải là địa chỉ tuyệt đối https://...')
        if og and og.startswith('http') and '[[' not in og:
            duong = urllib.parse.urlparse(og).path.lstrip('/')
            if duong and not os.path.exists(os.path.join(cong_khai, duong)):
                (bc.loi if len_mang else bc.canh)('chia-se', rel, f'chưa có ảnh chia sẻ {duong} (1200x630 JPG): tools/anh-chia-se.py')
    h1 = the('h1')
    if len(h1) != 1 and not la_404:
        bc.loi('html', rel, f'cần đúng một h1, đang có {len(h1)}')
    bac_truoc = 0
    for n in tat:
        if re.fullmatch(r'h[1-6]', n.tag):
            bac = int(n.tag[1])
            if bac_truoc and bac > bac_truoc + 1:
                bc.canh('html', rel, f'tiêu đề nhảy bậc h{bac_truoc} sang h{bac}: "{n.text()[:50]}"', n.dong)
            bac_truoc = bac
            kiem_chu(bc, rel, n.text(), n.dong, la_tieu_de=True)
    ids = {n.attrs.get('id') for n in tat if n.attrs.get('id')}
    trung = [i for i in ids if sum(1 for n in tat if n.attrs.get('id') == i) > 1]
    for i in trung:
        bc.loi('html', rel, f'trùng id "{i}"')
    # ảnh
    for n in the('img'):
        if 'alt' not in n.attrs:
            bc.loi('anh', rel, f'ảnh thiếu alt: {n.attrs.get("src", "")}', n.dong)
        if not (n.attrs.get('width') and n.attrs.get('height')) and 'data-vietqr' not in n.attrs:
            bc.canh('anh', rel, f'ảnh thiếu width, height (trang giật khi tải): {n.attrs.get("src", "")}', n.dong)
        src = n.attrs.get('src', '')
        if src and not re.match(r'(https?:|data:|//)', src):
            pa = os.path.normpath(os.path.join(os.path.dirname(p), src.split('?')[0]) if not src.startswith('/') else os.path.join(cong_khai, src.lstrip('/')))
            if not os.path.exists(pa):
                bc.loi('anh', rel, f'ảnh không tồn tại: {src}', n.dong)
            elif os.path.getsize(pa) > 350_000:
                bc.canh('anh', rel, f'ảnh nặng {os.path.getsize(pa) // 1024} KB: nén WebP, rộng tối đa 1600 px: {src}', n.dong)
    # liên kết
    for n in the('a') + the('link'):
        h = n.attrs.get('href', '')
        if n.tag == 'a' and n.attrs.get('target') == '_blank' and 'noopener' not in (n.attrs.get('rel') or ''):
            bc.canh('html', rel, f'liên kết mở tab mới thiếu rel="noopener": {h}', n.dong)
        if n.tag == 'a' and not n.text() and not any(c.tag == 'img' and c.attrs.get('alt') for c in n.duyet()) and not n.attrs.get('aria-label'):
            bc.loi('html', rel, f'liên kết không có chữ: {h}', n.dong)
        if not h or re.match(r'(https?:|mailto:|tel:|data:|//|javascript:)', h) or '{{' in h or '[[' in h:
            continue
        duong, _, neo = h.partition('#')
        if not duong:
            if neo and neo not in ids:
                bc.loi('html', rel, f'liên kết tới #{neo} nhưng không có phần tử id="{neo}"', n.dong)
            continue
        pa = os.path.join(cong_khai, duong.lstrip('/')) if duong.startswith('/') else os.path.join(os.path.dirname(p), duong)
        pa = os.path.normpath(urllib.parse.unquote(pa.split('?')[0]))
        if os.path.isdir(pa):
            pa = os.path.join(pa, 'index.html')
        if not os.path.exists(pa) and not os.path.exists(pa + '.html'):
            bc.loi('html', rel, f'liên kết hỏng: {h}', n.dong)
    # form
    nhan_cho = {n.attrs.get('for') for n in the('label')}
    for f in the('form'):
        o_nhap = [n for n in f.duyet() if n.tag in ('input', 'select', 'textarea')
                  and n.attrs.get('type') not in ('hidden', 'submit', 'button')
                  and not any('mat-ong' in t.lop() for t in n.to_tien())]
        for o in o_nhap:
            co_nhan = (o.attrs.get('id') in nhan_cho or any(t.tag == 'label' for t in o.to_tien())
                       or o.attrs.get('aria-label') or o.attrs.get('aria-labelledby'))
            if not co_nhan:
                bc.loi('form', rel, f'ô nhập "{o.attrs.get("name", "")}" thiếu nhãn <label>', o.dong)
            if 'placeholder' in o.attrs and not co_nhan:
                bc.canh('form', rel, 'đừng dùng placeholder thay nhãn', o.dong)
        thu_ca_nhan = any(o.attrs.get('type') in ('email', 'tel') or re.search(r'(?i)ten|name|email|phone|dien', o.attrs.get('name', ''))
                          for o in o_nhap if o.attrs.get('type') != 'checkbox')
        dong_y = [o for o in o_nhap if o.attrs.get('type') == 'checkbox' and any('dong-y' in t.lop() for t in o.to_tien())]
        if thu_ca_nhan:
            if not dong_y:
                bc.loi('phap-ly', rel, 'form thu thông tin cá nhân mà không có ô đồng ý (Luật Bảo vệ dữ liệu cá nhân 2025): thêm label.dong-y', f.dong)
            for o in dong_y:
                if 'checked' in o.attrs:
                    bc.loi('phap-ly', rel, 'ô đồng ý đang đánh dấu sẵn: luật cấm, bỏ thuộc tính checked', o.dong)
            if dong_y and not any('required' in o.attrs for o in dong_y):
                bc.canh('phap-ly', rel, 'ô đồng ý xử lý dữ liệu nên bắt buộc (required) để form không gửi khi chưa đồng ý', f.dong)
            if not any(re.search(r'chinh-sach|bao-mat|privacy', a.attrs.get('href', '')) for a in f.duyet() if a.tag == 'a'):
                bc.loi('phap-ly', rel, 'form thu thông tin cá nhân cần liên kết tới trang chính sách bảo vệ dữ liệu', f.dong)
        if f.attrs.get('data-gui') is None and not f.attrs.get('action') and f.attrs.get('role') != 'search' and o_nhap and thu_ca_nhan:
            bc.loi('form', rel, 'form chưa có nơi nhận (data-gui="web3forms|apps-script|netlify" hoặc action)', f.dong)
        if thu_ca_nhan and not any('mat-ong' in n.lop() for n in f.duyet()):
            bc.canh('form', rel, 'form chưa có bẫy máy gửi rác (div.mat-ong)', f.dong)
        khoa = next((n.attrs.get('value', '') for n in f.duyet() if n.attrs.get('name') == 'access_key'), None)
        if khoa is not None and (not khoa or '[[' in khoa):
            (bc.loi if len_mang else bc.canh)('form', rel, 'chưa dán khoá Web3Forms vào access_key (huong-dan/09-form-va-du-lieu.md)', f.dong)
        if f.attrs.get('data-gui') == 'apps-script' and not f.attrs.get('data-dich', '').startswith('https://script.google.com/'):
            bc.loi('form', rel, 'form apps-script thiếu data-dich="https://script.google.com/macros/s/.../exec"', f.dong)
    # chữ hiển thị
    for n in tat:
        if n.tag in AN_CHU or any(t.tag in AN_CHU for t in n.to_tien()):
            continue
        for x in n.chu:
            if isinstance(x, str):
                kiem_chu(bc, rel, x, n.dong, la_tieu_de=n.tag in ('button', 'summary') or 'nut' in n.lop())
        for k in ('alt', 'title', 'aria-label', 'placeholder'):
            if n.attrs.get(k):
                kiem_chu(bc, rel, n.attrs[k], n.dong)
    for k in ('description', 'og:title', 'og:description'):
        v = meta('name', k) or meta('property', k)
        if v:
            kiem_chu(bc, rel, v)
    if td:
        kiem_chu(bc, rel, td, la_tieu_de=True)
    nguon = C.doc(p)
    if 'chua-dat-ten-mien' in nguon or 'https://[[ten-mien]]' in nguon:
        (bc.loi if len_mang else bc.canh)('chia-se', rel, 'chưa đặt tên miền (canonical, og:url, og:image): tools/dua-len.py <web> --ten-mien https://...')
    cho = sorted(set(x for x in re.findall(r'\[\[([^\]]{1,80})\]\]', nguon) if x != 'ten-mien'))
    if cho:
        (bc.loi if len_mang else bc.canh)('cho-trong', rel, f'còn {len(cho)} chỗ cần điền [[...]]: ' + '; '.join(cho[:8]) + (' ...' if len(cho) > 8 else ''))
    so_cho_anh = len(re.findall(r'class="cho-anh', nguon))
    if so_cho_anh:
        (bc.loi if len_mang else bc.canh)('cho-trong', rel, f'còn {so_cho_anh} khung ảnh chờ (.cho-anh): thay bằng ảnh thật')
    sua = [c for c in d.chu_thich if c[1].startswith('SỬA Ở ĐÂY')]
    if sua:
        bc.goi_y('cho-sua', rel, f'{len(sua)} chỗ đánh dấu SỬA Ở ĐÂY (danh sách bàn giao cho chủ web)')
    if re.search(r'googletagmanager|gtag\(|fbq\(|connect\.facebook\.net', nguon) and 'dong-y-cookie' not in nguon:
        bc.canh('phap-ly', rel, 'có mã theo dõi (Google Analytics, Meta Pixel) mà chưa có hỏi đồng ý: chỉ tải sau khi người xem đồng ý, hoặc dùng Cloudflare Web Analytics')
    return d


def kiem_chan_trang(bc, rel, d):
    chan = [n for n in d.goc.duyet() if n.tag == 'footer']
    if not chan:
        bc.canh('phap-ly', rel, 'trang không có chân trang: nên ghi chủ quản, email, điện thoại, người chịu trách nhiệm nội dung')
        return
    t = chan[0].text()
    if '@' not in t and not re.search(r'\d{9,}|\d{3,4}[ .]\d{3}[ .]\d{3}', t) and '[[' not in t:
        bc.canh('phap-ly', rel, 'chân trang chưa có email hoặc điện thoại liên hệ (Nghị định 174/2026)')


def kiem_an_toan(bc, web, cong_khai):
    hs = C.ho_so_web(web)
    for dp, dn, fn in os.walk(web):
        dn[:] = [x for x in dn if x not in ('node_modules', '.git', '.astro', '.wrangler', 'fonts')]
        for f in fn:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, web).replace(os.sep, '/')
            trong_cong_khai = os.path.realpath(p).startswith(os.path.realpath(cong_khai) + os.sep)
            if trong_cong_khai and TEP_KHONG_CONG_KHAI.search(rel) and f != 'robots.txt':
                bc.loi('an-toan', rel, 'tệp này nằm trong thư mục đưa lên mạng: ai cũng tải được. Chuyển ra ngoài public/')
            if re.search(r'(?i)(serviceAccount|service-account|adminsdk|admin[_-]key).*\.json$|^\.env$', f):
                bc.loi('an-toan', rel, 'tệp khoá tài khoản dịch vụ, biến môi trường nằm trong thư mục web: chuyển ra ngoài, xoay khoá nếu đã từng đẩy lên git')
            if os.path.splitext(f)[1].lower() not in C.DUOI_VAN_BAN or os.path.getsize(p) > 3_000_000:
                continue
            try:
                s = C.doc(p)
            except (UnicodeDecodeError, OSError):
                continue
            for mau, ten in BI_MAT:
                for m in re.finditer(mau, s):
                    dong = s.count('\n', 0, m.start()) + 1
                    bc.loi('an-toan', rel, f'có thể là {ten} viết thẳng trong mã: chuyển sang biến môi trường phía máy chủ, xoay khoá', dong)
                    break
            if f in ('firestore.rules', 'storage.rules', 'database.rules.json'):
                kiem_luat(bc, rel, s)
            if f == 'firebase.json':
                try:
                    host = json.loads(s).get('hosting', {})
                    for h in (host if isinstance(host, list) else [host]):
                        if h.get('public') in ('.', './', ''):
                            bc.loi('an-toan', rel, 'hosting.public là thư mục gốc: đăng cả ghi chú, dữ liệu, khoá lên mạng. Dùng "public"')
                except ValueError:
                    bc.loi('an-toan', rel, 'firebase.json không đọc được')
            if trong_cong_khai or rel.startswith('src/'):
                if re.search(r'(?i)(dap[-_]?an|answer[-_]?key|exam[-_]?key|_key\.json|correct(Answer|Option|Index)?"?\s*:)', s) and hs.get('bac', 0) >= 2:
                    bc.canh('an-toan', rel, 'có vẻ đáp án, lời giải nằm trong mã gửi xuống trình duyệt: người dùng xem được bằng công cụ của trình duyệt. Bài thi có điểm: chấm ở máy chủ')


def kiem_luat(bc, rel, s):
    sach = re.sub(r'//[^\n]*', '', s)
    if re.search(r'allow\s+[\w, ]*:\s*if\s+true\s*;', sach):
        for m in re.finditer(r'match\s+(/[^{]+)\{[^{}]*allow\s+([\w, ]+):\s*if\s+true\s*;', sach):
            muc = 'LỖI' if 'write' in m.group(2) or 'create' in m.group(2) or 'update' in m.group(2) else 'CẢNH BÁO'
            bc.them(muc, 'firebase', rel, f'"{m.group(1).strip()}" cho {m.group(2).strip()} với mọi người (if true): chỉ chấp nhận cho dữ liệu công khai thật sự, không bao giờ cho ghi')
    if re.search(r'match\s+/\{document=\*\*\}\s*\{[^}]*allow', sach):
        bc.loi('firebase', rel, 'luật mở cho mọi tài liệu ({document=**}): viết luật riêng cho từng bộ sưu tập')
    for m in re.finditer(r'allow\s+([\w, ]+):\s*if\s+request\.auth\s*!=\s*null\s*;', sach):
        bc.canh('firebase', rel, f'"allow {m.group(1)}: if request.auth != null": ai đăng nhập cũng {m.group(1)} được dữ liệu của người khác. Đối chiếu chủ sở hữu (request.auth.uid == userId)')
    if 'request.auth.token.email' in sach and 'email_verified' not in sach:
        bc.canh('firebase', rel, 'phân quyền theo email mà không kiểm email_verified: với đăng nhập bằng email/mật khẩu, người khác có thể đăng ký trùng email chưa xác minh')


# ---------------------------------------------------------------- trình duyệt
class ImLang(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def chay_may_chu(goc):
    s = socket.socket()
    s.bind(('127.0.0.1', 0))
    cong = s.getsockname()[1]
    s.close()
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', cong), functools.partial(ImLang, directory=goc))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, cong


JS_DO = r"""() => {
  const ra = {tran: [], chuNho: [], dongChat: []};
  const W = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth > W + 1) {
    for (const el of document.querySelectorAll('body *')) {
      const r = el.getBoundingClientRect();
      if (r.width && (r.right > W + 1 || r.left < -1) && getComputedStyle(el).position !== 'fixed') {
        if (![...el.children].some(c => { const q = c.getBoundingClientRect(); return q.right > W + 1; }))
          ra.tran.push((el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '')) + ` (${Math.round(r.right)}px > ${W}px)`);
      }
      if (ra.tran.length > 6) break;
    }
  }
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const thay = new Set();
  while (tw.nextNode()) {
    const t = tw.currentNode; const el = t.parentElement;
    if (!t.textContent.trim() || !el || thay.has(el)) continue;
    thay.add(el);
    const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
    if (cs.visibility === 'hidden' || cs.display === 'none' || !r.width || el.closest('.an-di,.mat-ong,[hidden]')) continue;
    const co = parseFloat(cs.fontSize);
    if (co < 14) ra.chuNho.push(`${el.tagName.toLowerCase()} ${co}px: "${t.textContent.trim().slice(0, 40)}"`);
    if (el.tagName === 'P' && parseFloat(cs.lineHeight) / co < 1.5 && t.textContent.length > 80) ra.dongChat.push(`"${t.textContent.trim().slice(0, 40)}" line-height ${(parseFloat(cs.lineHeight) / co).toFixed(2)}`);
  }
  ra.phong = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/"/g, ''));
  ra.dauViet = document.fonts.check('16px "' + getComputedStyle(document.body).fontFamily.split(',')[0].replace(/["']/g, '') + '"', 'Tiếng Việt có dấu: ữ ặ ộ ẽ');
  return ra;
}"""


def kiem_trinh_duyet(bc, web, cong_khai, trang, ra_dir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        bc.canh('trinh-duyet', '-', 'máy này chưa có Playwright: chưa chụp, chưa kiểm tràn ngang, tương phản thật, khả năng tiếp cận. '
                'Chạy ở nơi có trình duyệt (sandbox đám mây của phiên, hoặc pip install playwright && python3 -m playwright install chromium)')
        return []
    axe = os.path.join(C.TOOLS, 'vendor', 'axe.min.js')
    srv, cong = chay_may_chu(cong_khai)
    anh = []
    try:
        with sync_playwright() as pw:
            tr = pw.chromium.launch()
            for rel in trang:
                url_rel = os.path.relpath(rel, cong_khai).replace(os.sep, '/')
                ten = re.sub(r'[^\w-]+', '-', url_rel[:-5]) or 'index'
                ds_anh = []
                for rong in KHO:
                    ctx = tr.new_context(viewport={'width': rong, 'height': 900 if rong > 500 else 844},
                                         device_scale_factor=1, locale='vi-VN', is_mobile=rong < 500, has_touch=rong < 500)
                    pg = ctx.new_page()
                    loi_js, hong, nang = [], [], {}
                    pg.on('pageerror', lambda e, l=loi_js: l.append(str(e)[:160]))
                    pg.on('console', lambda m, l=loi_js: l.append(m.text[:160]) if m.type == 'error' and 'net::' not in m.text and 'Failed to load resource' not in m.text else None)
                    pg.on('requestfailed', lambda r, h=hong: h.append(r.url))

                    def nhan(r, n=nang):
                        try:
                            if r.url.startswith(f'http://127.0.0.1:{cong}'):
                                n[r.url] = len(r.body())
                        except Exception:
                            pass
                    pg.on('response', nhan)
                    pg.goto(f'http://127.0.0.1:{cong}/{url_rel}', wait_until='networkidle', timeout=30000)
                    pg.evaluate("() => { document.querySelectorAll('.hien').forEach(e => e.classList.add('da-hien')); window.scrollTo(0, document.body.scrollHeight); }")
                    pg.wait_for_timeout(450)
                    pg.evaluate('() => window.scrollTo(0, 0)')
                    pg.wait_for_timeout(150)
                    do = pg.evaluate(JS_DO)
                    nhan_trang = f'{url_rel} @{rong}px'
                    for t in do['tran']:
                        bc.loi('bo-cuc', nhan_trang, f'tràn ngang: {t}')
                    for t in do['chuNho'][:5]:
                        bc.canh('chu-nho', nhan_trang, f'chữ dưới 14 px khó đọc trên điện thoại: {t}')
                    for t in do['dongChat'][:3]:
                        bc.canh('chu-nho', nhan_trang, f'khoảng cách dòng dưới 1.5 cho chữ Việt: {t}')
                    if not do['dauViet']:
                        bc.loi('phong', nhan_trang, 'phông nội dung không vẽ được dấu tiếng Việt (thiếu tệp vietnamese hoặc phông chưa nạp)')
                    for e in loi_js:
                        if re.search(r'https?://(?!127\.0\.0\.1)', e):  # tài nguyên ngoài (CDN) không tải được: thường do mạng nơi kiểm
                            bc.canh('js', nhan_trang, f'không tải được tài nguyên ngoài (kiểm lại khi có mạng): {e}')
                        else:
                            bc.loi('js', nhan_trang, f'lỗi JavaScript: {e}')
                    for u in hong:
                        if u.startswith(f'http://127.0.0.1:{cong}'):
                            bc.loi('tep', nhan_trang, f'tệp hỏng, không tải được: {u.split(str(cong), 1)[1]}')
                    if rong == KHO[0]:
                        tong = sum(nang.values())
                        if tong > 1_500_000:
                            bc.canh('hieu-nang', url_rel, f'trang nặng {tong // 1024} KB khi tải lần đầu (nên dưới 1.500 KB cho mạng di động)')
                    if rong in (KHO[0], KHO[-1]) and os.path.exists(axe):
                        pg.add_script_tag(path=axe)
                        kq = pg.evaluate("""async () => { const r = await axe.run(document, {runOnly: {type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}, resultTypes: ['violations']});
                                         return r.violations.map(v => ({id: v.id, impact: v.impact, help: v.help, tags: v.tags, nodes: v.nodes.slice(0, 3).map(n => n.target.join(' ') + (n.any[0] && n.any[0].data && n.any[0].data.contrastRatio ? ' (' + n.any[0].data.contrastRatio + ':1)' : ''))})); }""")
                        for v in kq:
                            wcag = any(t.startswith('wcag') for t in v['tags'])
                            muc = 'LỖI' if wcag and v['impact'] in ('serious', 'critical') else 'CẢNH BÁO'
                            bc.them(muc, 'tiep-can', nhan_trang, f'{AXE_VI.get(v["id"], v["help"])} [{v["id"]}]: ' + '; '.join(v['nodes']))
                    p = os.path.join(ra_dir, f'{ten}-{rong}.png')
                    pg.screenshot(path=p, full_page=True)
                    ds_anh.append(p)
                    ctx.close()
                anh.append(to_tong_the(ds_anh, os.path.join(ra_dir, f'{ten}-tong-the.jpg')))
            tr.close()
    finally:
        srv.shutdown()
    return [a for a in anh if a]


def to_tong_the(ds, dich):
    """Ghép ba khổ cạnh nhau (điện thoại, máy tính bảng, máy tính) để người và AI nhìn một lần thấy cả bố cục."""
    try:
        from PIL import Image
    except ImportError:
        return None
    rong_dich = (330, 400, 560)
    hinh = []
    for p, w in zip(ds, rong_dich):
        im = Image.open(p).convert('RGB')
        h = round(im.height * w / im.width)
        hinh.append(im.resize((w, h), Image.LANCZOS))
    cao = min(max(i.height for i in hinh), 4200)
    le = 24
    nen = Image.new('RGB', (sum(i.width for i in hinh) + le * (len(hinh) + 1), cao + 2 * le), (232, 230, 226))
    x = le
    for i in hinh:
        nen.paste(i.crop((0, 0, i.width, min(i.height, cao))), (x, le))
        x += i.width + le
    nen.save(dich, quality=84)
    return dich


# ---------------------------------------------------------------- chạy
def viet_bao_cao(bc, web, ra_dir, anh, trinh_duyet):
    dat = bc.dem('LỖI') == 0
    dong = [f'# BÁO CÁO KIỂM WEB: {os.path.basename(web)}', '',
            f'Ngày {C.hom_nay()}. Kết quả: **{"ĐẠT" if dat else "KHÔNG ĐẠT"}** ({bc.dem("LỖI")} lỗi, {bc.dem("CẢNH BÁO")} cảnh báo, {bc.dem("GỢI Ý")} gợi ý chữ). '
            + ('Đã kiểm bằng trình duyệt.' if trinh_duyet else 'CHƯA kiểm bằng trình duyệt.'), '']
    for muc in ('LỖI', 'CẢNH BÁO', 'GỢI Ý'):
        ds = [m for m in bc.muc if m['muc'] == muc]
        if ds:
            dong += [f'## {muc} ({len(ds)})', '']
            for m in ds:
                dong.append(f'- `{m["tep"]}{":" + str(m["dong"]) if m["dong"] else ""}` [{m["loai"]}] {m["chiTiet"]}')
            dong.append('')
    if anh:
        dong += ['## Ảnh chụp', ''] + [f'- `{os.path.basename(a)}`' for a in anh] + ['']
    dong += ['## Kiểm bằng tay (máy không thay được)', '',
             '- Mở trên điện thoại thật, bấm thử mọi nút, gửi thử form tới email của mình.',
             '- Dùng phím Tab đi hết trang: luôn thấy ô đang chọn, thứ tự hợp lý.',
             '- Đọc to toàn bộ chữ: tên, chức danh đúng nguyên văn, không còn câu văn AI (chuan/04-ngon-tu-web.md).',
             '- Mọi con số, lời chứng thực, tên đơn vị là thật và kiểm chứng được.', '']
    C.ghi(os.path.join(ra_dir, 'BAO-CAO.md'), '\n'.join(dong))
    C.ghi_json(os.path.join(ra_dir, 'bao-cao.json'), {'web': os.path.basename(web), 'ngay': C.hom_nay(), 'dat': dat,
                                                     'trinhDuyet': trinh_duyet, 'muc': bc.muc})
    return dat


def main():
    ap = argparse.ArgumentParser(description='Cổng nghiệm thu tự động cho một web của xưởng.')
    ap.add_argument('web')
    ap.add_argument('--len', action='store_true', help='chế độ trước khi đưa lên mạng: chỗ trống thành LỖI')
    ap.add_argument('--khong-trinh-duyet', action='store_true')
    ap.add_argument('--ra')
    ap.add_argument('--im', action='store_true', help='chỉ in tổng kết')
    a = ap.parse_args()
    web = C.tim_web(a.web)
    cong_khai = C.thu_muc_cong_khai(web)
    if not os.path.isdir(cong_khai):
        raise SystemExit(f'Không thấy thư mục công khai {cong_khai} (web Astro: chạy npm run build trước).')
    du_an = C.tim_du_an(web)
    ra_dir = os.path.abspath(a.ra) if a.ra else os.path.join(du_an, 'kiem') if du_an else os.path.join(C.thu_muc_tam(), 'kiem', os.path.basename(web))
    C.chan_ghi_repo(ra_dir, 'ghi báo cáo kiểm')
    os.makedirs(ra_dir, exist_ok=True)
    bc = BaoCao()
    trang = []
    for dp, dn, fn in os.walk(cong_khai):
        dn[:] = [x for x in dn if x not in ('assets', 'node_modules', '_astro')]
        trang += [os.path.join(dp, f) for f in sorted(fn) if f.endswith('.html')]
    if not trang:
        bc.loi('html', '-', 'thư mục công khai không có trang .html nào')
    for p in trang:
        d = kiem_html(bc, web, cong_khai, p, a.len)
        if os.path.basename(p) != '404.html':
            kiem_chan_trang(bc, os.path.relpath(p, web), d)
    kiem_an_toan(bc, web, cong_khai)
    if not os.path.exists(os.path.join(cong_khai, '_headers')) and not os.path.exists(os.path.join(web, 'vercel.json')) and C.ho_so_web(web).get('loai') != 'firebase':
        bc.canh('an-toan', '-', 'chưa có tệp _headers (lớp bảo vệ HTTP): chép từ he-thong/mau-web/_headers')
    anh = []
    if not a.khong_trinh_duyet:
        anh = kiem_trinh_duyet(bc, web, cong_khai, trang, ra_dir)
    co_trinh_duyet = not a.khong_trinh_duyet and not any(m['loai'] == 'trinh-duyet' for m in bc.muc)
    dat = viet_bao_cao(bc, web, ra_dir, anh, co_trinh_duyet)
    if not a.im:
        for muc in ('LỖI', 'CẢNH BÁO', 'GỢI Ý'):
            for m in [x for x in bc.muc if x['muc'] == muc][:40]:
                print(f'{muc:<9} {m["tep"]}{":" + str(m["dong"]) if m["dong"] else ""} [{m["loai"]}] {m["chiTiet"]}')
    print(f'\nKIỂM WEB: {"ĐẠT" if dat else "KHÔNG ĐẠT"} ({bc.dem("LỖI")} lỗi, {bc.dem("CẢNH BÁO")} cảnh báo, {bc.dem("GỢI Ý")} gợi ý)'
          + ('' if co_trinh_duyet else ', CHƯA kiểm bằng trình duyệt'))
    print(f'Báo cáo: {os.path.join(ra_dir, "BAO-CAO.md")}' + (f'\nTờ tổng thể: {", ".join(anh)}' if anh else ''))
    sys.exit(0 if dat else 1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TƯƠNG PHẢN: kiểm mọi chủ đề màu web trong brand/brand.json theo WCAG 2.2 AA (và mức xưởng tự đặt cao hơn).

    python3 tools/tuong-phan.py                  # kiểm mọi chủ đề; thoát mã 1 nếu có cặp rớt chuẩn
    python3 tools/tuong-phan.py giay-muc         # chỉ một chủ đề
    python3 tools/tuong-phan.py --cap "#127D49" "#F7F5F0"   # đo nhanh một cặp màu bất kỳ

Mỗi chủ đề khai màu theo VAI (nen, chu, nhan...). Bảng CAP dưới đây là các cặp chữ trên nền thật sự xuất hiện trong
he-thong/nen.css; thêm vai mới vào nen.css thì thêm cặp vào đây. Mức: 4.5 cho chữ thường, 3 cho viền ô nhập và chữ lớn,
7 cho chữ chính (xưởng tự nâng để chữ Việt có dấu đọc êm trên điện thoại ngoài nắng).
"""
import json
import os
import sys

sys.dont_write_bytecode = True
for _luong in (sys.stdout, sys.stderr):  # Windows: in chữ có dấu không lỗi
    try:
        _luong.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
TOOLS = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.dirname(TOOLS)

CAP = [  # (chữ, nền, mức tối thiểu, dùng ở đâu)
    ('chu', 'nen', 7, 'chữ chính'),
    ('chu', 'nenPhu', 7, 'chữ chính trên khối nền phụ'),
    ('chu', 'nenO', 7, 'chữ trong ô nhập'),
    ('chuPhu', 'nen', 4.5, 'chữ phụ, chú thích'),
    ('chuPhu', 'nenPhu', 4.5, 'chữ phụ trên khối nền phụ'),
    ('lienKet', 'nen', 4.5, 'liên kết, nhãn mục nhỏ'),
    ('lienKet', 'nenPhu', 4.5, 'liên kết trên khối nền phụ'),
    ('nhanChu', 'nhan', 4.5, 'chữ trên nút chính'),
    ('nhanChu', 'nhanDam', 4.5, 'chữ trên nút chính khi rê chuột'),
    ('cauTruc', 'nen', 4.5, 'tiêu đề phụ, số liệu, bảng'),
    ('cauTruc', 'nenPhu', 4.5, 'tiêu đề phụ trên nền phụ'),
    ('loi', 'nen', 4.5, 'thông báo lỗi'),
    ('loi', 'nenO', 4.5, 'thông báo lỗi trong khung form'),
    ('vienO', 'nen', 3, 'viền ô nhập (thành phần giao diện)'),
    ('vienO', 'nenO', 3, 'viền ô nhập trên nền ô'),
    ('toiChu', 'toiNen', 7, 'chữ chính trên khối tối'),
    ('toiChu', 'toiNenPhu', 7, 'chữ chính trên khối tối phụ'),
    ('toiChuPhu', 'toiNen', 4.5, 'chữ phụ trên khối tối'),
    ('toiChuPhu', 'toiNenPhu', 4.5, 'chữ phụ trên khối tối phụ'),
    ('toiNhan', 'toiNen', 4.5, 'liên kết, nhấn trên khối tối'),
    ('toiNhanChu', 'toiNhan', 4.5, 'chữ trên nút ở khối tối'),
    ('vang', 'toiNen', 4.5, 'trích dẫn trên khối tối'),
]


def rgb(hex_):
    h = hex_.strip().lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def do_sang(c):
    def k(v):
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (k(v) for v in rgb(c))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ti_le(a, b):
    la, lb = sorted((do_sang(a), do_sang(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def kiem_chu_de(ten, cd):
    mau = cd.get('mau', {})
    loi = []
    for chu, nen, muc, dung in CAP:
        if chu not in mau or nen not in mau:
            loi.append((ten, chu, nen, None, muc, f'thiếu vai "{chu if chu not in mau else nen}"'))
            continue
        t = ti_le(mau[chu], mau[nen])
        if t + 1e-9 < muc:
            loi.append((ten, chu, nen, t, muc, dung))
    return loi


def main():
    a = sys.argv[1:]
    if a[:1] == ['--cap'] and len(a) == 3:
        print(f'{a[1]} trên {a[2]}: {ti_le(a[1], a[2]):.2f}:1')
        return
    p = os.path.join(GOC, 'brand', 'brand.json')
    if not os.path.exists(p):
        p = os.path.join(GOC, 'brand', 'brand.mau.json')
    b = json.load(open(p, encoding='utf-8'))
    ds = b.get('chuDe', {})
    if a:
        ds = {k: v for k, v in ds.items() if k in a}
    tong = []
    for ten, cd in ds.items():
        l = kiem_chu_de(ten, cd)
        tong += l
        print(f'{"ĐẠT " if not l else "LỖI "} {ten}' + ('' if not l else f' ({len(l)} cặp)'))
        for _, c, n, t, muc, dung in l:
            print(f'      {c} trên {n}: ' + (f'{t:.2f}:1 < {muc}' if t else '') + f' ({dung})')
    print(f'\nTƯƠNG PHẢN: {"ĐẠT" if not tong else "KHÔNG ĐẠT"} ({len(ds)} chủ đề)')
    sys.exit(1 if tong else 0)


if __name__ == '__main__':
    main()

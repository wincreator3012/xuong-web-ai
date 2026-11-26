# -*- coding: utf-8 -*-
"""Tìm KHO TƯ LIỆU CHUNG (repo riêng chứa logo, ảnh, hồ sơ, luật chữ, ẩn dụ dùng chung cho nhiều xưởng) và nạp
thư viện đọc kho của nó. Không có kho thì mọi công cụ dùng tư liệu trong chính repo này (brand/, phong-cach/...).

    import kho_tu_lieu
    K = kho_tu_lieu.kho()        # module thư viện của kho, hoặc None khi không tìm thấy kho
    if K: K.tron_brand(...), K.logo(ten), K.tu_ngu() ...

Thứ tự tìm (thư mục được nhận là kho khi có tệp kho.json):
  1. biến môi trường KHO_TU_LIEU (hoặc LDN_KHO_TU_LIEU);
  2. cau-hinh.json > "khoTuLieu": một đường dẫn hoặc danh sách, tương đối so với repo; đặt "khoTuLieu": false để tắt;
  3. thư mục con có kho.json nằm cạnh repo (../), cạnh thư mục chứa repo (../../), trong ~/Documents/ và ~/mnt/.
Cùng một mã cho mọi xưởng: sửa thì chép y nguyên sang tools/kho_tu_lieu.py của các xưởng kia.
"""
import functools
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True  # không để __pycache__ trong repo

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _la_kho(p):
    return bool(p) and os.path.isfile(os.path.join(p, 'kho.json')) and os.path.isfile(
        os.path.join(p, 'cong-cu', 'kho_tu_lieu.py'))


def _cau_hinh():
    p = os.path.join(_REPO, 'cau-hinh.json')
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


@functools.lru_cache(None)
def tim():
    """Đường dẫn tuyệt đối của kho, hoặc None."""
    for bien in ('KHO_TU_LIEU', 'LDN_KHO_TU_LIEU'):
        v = os.environ.get(bien)
        if v:
            v = os.path.abspath(os.path.expanduser(v))
            if _la_kho(v):
                return v
            raise SystemExit(f'{bien}={v} không phải kho tư liệu (thiếu kho.json hoặc cong-cu/kho_tu_lieu.py).')
    ch = _cau_hinh().get('khoTuLieu')
    if ch is False:
        return None
    for v in ([ch] if isinstance(ch, str) else ch or []):
        p = os.path.abspath(os.path.join(_REPO, os.path.expanduser(v)))
        if _la_kho(p):
            return p
    for cha in (os.path.dirname(_REPO), os.path.dirname(os.path.dirname(_REPO)),
                os.path.expanduser('~/Documents'), os.path.expanduser('~/mnt')):
        try:
            con = sorted(os.listdir(cha))
        except OSError:
            continue
        for ten in con:
            p = os.path.join(cha, ten)
            if p != _REPO and _la_kho(p):
                return p
    return None


@functools.lru_cache(None)
def kho():
    """Thư viện đọc kho (cong-cu/kho_tu_lieu.py của kho) đã nạp, hoặc None khi không có kho."""
    goc = tim()
    if not goc:
        return None
    spec = importlib.util.spec_from_file_location('kho_tu_lieu_goc', os.path.join(goc, 'cong-cu', 'kho_tu_lieu.py'))
    m = importlib.util.module_from_spec(spec)
    sys.modules['kho_tu_lieu_goc'] = m
    spec.loader.exec_module(m)
    return m


def bat_buoc():
    """Như kho() nhưng dừng với lời nhắc rõ ràng khi không tìm thấy kho (dùng cho việc chỉ kho mới có, vd ảnh gốc)."""
    m = kho()
    if m is None:
        raise SystemExit('Không tìm thấy kho tư liệu chung. Kết nối thư mục kho vào phiên làm việc (cạnh thư mục xưởng), '
                         'hoặc khai đường dẫn ở cau-hinh.json > "khoTuLieu", hoặc đặt biến KHO_TU_LIEU.')
    return m


if __name__ == '__main__':
    g = tim()
    print(g or 'Không tìm thấy kho tư liệu.')
    sys.exit(0 if g else 1)

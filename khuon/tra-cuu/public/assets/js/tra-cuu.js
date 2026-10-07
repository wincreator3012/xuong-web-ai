/* Tra cứu: đọc du-lieu/muc.json, tìm không dấu, lọc theo nhóm, mở chi tiết theo địa chỉ #id để chia sẻ được.
   Dữ liệu tách khỏi giao diện: người không viết mã chỉ cần sửa muc.json (mỗi mục: id, ten, nhom, tomTat, noiDung, nguon, tuKhoa). */
(function () {
  'use strict';
  var tim = document.getElementById('tim'), loc = document.getElementById('loc');
  var ds = document.getElementById('ket-qua'), dem = document.getElementById('dem'), ct = document.getElementById('chi-tiet');
  var muc = [];
  function khongDau(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
  }
  function the(tag, lop, chu) { var e = document.createElement(tag); if (lop) e.className = lop; if (chu != null) e.textContent = chu; return e; }
  function veDanhSach() {
    var q = khongDau(tim.value).trim().split(/\s+/).filter(Boolean), n = loc.value;
    var kq = muc.filter(function (m) { return (!n || m.nhom === n) && q.every(function (t) { return m._tim.indexOf(t) >= 0; }); });
    ds.textContent = '';
    kq.forEach(function (m) {
      var li = the('li'), a = the('article', 'the');
      a.appendChild(the('span', 'nhom', m.nhom));
      var h = the('h2'), l = the('a', '', m.ten); l.href = '#' + encodeURIComponent(m.id); h.appendChild(l); a.appendChild(h);
      a.appendChild(the('p', '', m.tomTat));
      li.appendChild(a); ds.appendChild(li);
    });
    dem.textContent = kq.length ? 'Có ' + kq.length + ' mục' + (q.length || n ? ' khớp' : '') + '.' : 'Không có mục nào khớp. Bạn thử từ khoá ngắn hơn, hoặc chọn "Tất cả".';
    var p = new URLSearchParams(); if (tim.value) p.set('q', tim.value); if (n) p.set('nhom', n);
    history.replaceState(null, '', (p.toString() ? '?' + p : location.pathname) + location.hash);
  }
  function veChiTiet() {
    var id = decodeURIComponent(location.hash.slice(1)), m = muc.find(function (x) { return x.id === id; });
    if (!m) { ct.hidden = true; return; }
    ct.textContent = '';
    ct.appendChild(the('span', 'nhom', m.nhom));
    ct.appendChild(the('h2', '', m.ten));
    (m.noiDung || '').split(/\n\n+/).forEach(function (d) { ct.appendChild(the('p', '', d)); });
    if (m.nguon) ct.appendChild(the('p', 'nguon', 'Nguồn: ' + m.nguon));
    var ve = the('a', 'nut nut--chu', 'Đóng'); ve.href = '#'; ct.appendChild(ve);
    ct.hidden = false; ct.focus();
  }
  document.querySelector('form[role="search"]').addEventListener('submit', function (e) { e.preventDefault(); });
  fetch('du-lieu/muc.json').then(function (r) { return r.json(); }).then(function (d) {
    muc = (d.muc || d).map(function (m) { m._tim = khongDau([m.ten, m.nhom, m.tomTat, m.noiDung, (m.tuKhoa || []).join(' ')].join(' ')); return m; });
    Array.from(new Set(muc.map(function (m) { return m.nhom; }))).sort().forEach(function (n) { var o = the('option', '', n); o.value = n; loc.appendChild(o); });
    var p = new URLSearchParams(location.search); tim.value = p.get('q') || ''; loc.value = p.get('nhom') || '';
    tim.addEventListener('input', veDanhSach); loc.addEventListener('change', veDanhSach);
    window.addEventListener('hashchange', veChiTiet);
    veDanhSach(); veChiTiet();
  }).catch(function () { dem.textContent = 'Chưa đọc được dữ liệu. Nếu bạn đang mở tệp trực tiếp trên máy, hãy xem qua máy chủ thử (README.md, mục Xem thử).'; });
})();

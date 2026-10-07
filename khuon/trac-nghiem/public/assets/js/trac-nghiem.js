/* Trắc nghiệm tự soi chiếu: đọc du-lieu/cau-hoi.json, tính điểm từng chiều ngay trên máy người dùng, không lưu, không gửi.
   Muốn lưu kết quả về máy chủ: đó là bậc 2-3, dữ liệu tâm lý là dữ liệu nhạy cảm (chuan/08-phap-ly-vn.md), phải xin đồng ý riêng. */
(function () {
  'use strict';
  var form = document.getElementById('bai'), vung = document.getElementById('cac-cau'), kq = document.getElementById('ket-qua');
  var thanh = document.getElementById('thanh-tien-do'), viTri = document.getElementById('vi-tri'), nhac = document.getElementById('nhac');
  var D;
  function the(tag, lop, chu) { var e = document.createElement(tag); if (lop) e.className = lop; if (chu != null) e.textContent = chu; return e; }
  function ve() {
    vung.textContent = '';
    D.cauHoi.forEach(function (c, i) {
      var fs = the('fieldset', 'cau'); fs.appendChild(the('legend', '', (i + 1) + '. ' + c.cau));
      var th = the('div', 'thang');
      D.thang.forEach(function (m) {
        var l = the('label'), r = the('input'); r.type = 'radio'; r.name = 'c' + i; r.value = m.diem; r.required = true;
        l.appendChild(r); l.appendChild(document.createTextNode(m.nhan)); th.appendChild(l);
      });
      fs.appendChild(th); vung.appendChild(fs);
    });
    capNhat();
  }
  function capNhat() {
    var xong = D.cauHoi.filter(function (c, i) { return form.querySelector('input[name="c' + i + '"]:checked'); }).length;
    thanh.style.width = (100 * xong / D.cauHoi.length) + '%';
    viTri.textContent = 'Đã trả lời ' + xong + '/' + D.cauHoi.length + ' câu';
  }
  form.addEventListener('change', capNhat);
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var thieu = D.cauHoi.findIndex(function (c, i) { return !form.querySelector('input[name="c' + i + '"]:checked'); });
    if (thieu >= 0) { nhac.textContent = 'Còn câu ' + (thieu + 1) + ' chưa trả lời.'; form.querySelectorAll('fieldset')[thieu].querySelector('input').focus(); return; }
    nhac.textContent = '';
    var tong = {}, so = {};
    D.cauHoi.forEach(function (c, i) {
      var d = +form.querySelector('input[name="c' + i + '"]:checked').value;
      if (c.dao) d = D.thang.length + 1 - d;
      tong[c.chieu] = (tong[c.chieu] || 0) + d; so[c.chieu] = (so[c.chieu] || 0) + 1;
    });
    var cc = document.getElementById('cac-chieu'), dg = document.getElementById('dien-giai'); cc.textContent = ''; dg.textContent = '';
    Object.keys(D.chieu).forEach(function (k) {
      var tb = tong[k] / so[k], pt = Math.round(100 * (tb - 1) / (D.thang.length - 1));
      var b = the('div', 'chieu'); b.appendChild(the('p', '', D.chieu[k].ten + ': ' + tb.toFixed(1) + '/' + D.thang.length));
      var t = the('div', 'thanh'); var s = the('span'); s.style.width = pt + '%'; t.appendChild(s); b.appendChild(t); cc.appendChild(b);
      var muc = D.chieu[k].dienGiai.find(function (m) { return tb <= m.den; }) || D.chieu[k].dienGiai.slice(-1)[0];
      var h = the('h3', '', D.chieu[k].ten); dg.appendChild(h); dg.appendChild(the('p', '', muc.chu));
    });
    form.hidden = true; kq.hidden = false; kq.focus(); window.scrollTo(0, 0);
  });
  document.getElementById('lam-lai').addEventListener('click', function () { form.reset(); capNhat(); kq.hidden = true; form.hidden = false; });
  fetch('du-lieu/cau-hoi.json').then(function (r) { return r.json(); }).then(function (d) { D = d; ve(); form.hidden = false; })
    .catch(function () { nhac.textContent = 'Chưa đọc được bộ câu hỏi.'; form.hidden = false; });
})();

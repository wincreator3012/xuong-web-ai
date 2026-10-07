/* ==========================================================================
   NỀN CHUNG CỦA XƯỞNG WEB (he-thong/nen.js): JavaScript thuần, không thư viện.
   Mã nguồn mở MIT, (c) 2026 Lương Dũng Nhân (Xưởng web AI): giữ dòng này khi chép lại.
   Trang vẫn đọc đủ khi tệp này không chạy (nâng cấp dần [progressive enhancement]).
   Các phần, bật bằng thuộc tính trong HTML (không phải sửa tệp này):
     1. html.js                 đánh dấu JS đang chạy (để hiệu ứng hiện dần chỉ áp khi có JS)
     2. .hien                   hiện dần khi cuộn tới
     3. .mo-menu                nút mở menu trên điện thoại
     4. form[data-gui]          gửi biểu mẫu: web3forms | apps-script | netlify; kiểm ô bắt buộc, ô đồng ý, bẫy rác
     5. [data-ma-don]           sinh mã đơn ngắn, điền vào form và nội dung chuyển khoản
     6. img[data-vietqr]        dựng ảnh mã VietQR từ số tài khoản, số tiền, nội dung
     7. [data-chep]             nút chép (số tài khoản, nội dung chuyển khoản)
     8. [data-nam]              năm hiện tại ở chân trang
     9. .nut-dinh[data-an-khi]  ẩn nút nổi khi phần đích (ví dụ form đăng ký) đang hiện
   ========================================================================== */
(function () {
  'use strict';
  var doc = document;
  doc.documentElement.classList.add('js');

  function tatCa(chon, goc) { return Array.prototype.slice.call((goc || doc).querySelectorAll(chon)); }

  // 2. hiện dần ----------------------------------------------------------------
  var hien = tatCa('.hien');
  if ('IntersectionObserver' in window && hien.length) {
    var io = new IntersectionObserver(function (ds) {
      ds.forEach(function (d) { if (d.isIntersecting) { d.target.classList.add('da-hien'); io.unobserve(d.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    hien.forEach(function (el) { io.observe(el); });
  } else {
    hien.forEach(function (el) { el.classList.add('da-hien'); });
  }

  // 3. menu điện thoại -------------------------------------------------------------
  tatCa('.mo-menu').forEach(function (nut) {
    nut.addEventListener('click', function () {
      var dau = nut.closest('.dau-trang');
      var mo = dau.classList.toggle('dang-mo');
      nut.setAttribute('aria-expanded', mo ? 'true' : 'false');
    });
  });

  // 5. mã đơn ----------------------------------------------------------------------
  // <span data-ma-don="KHT"></span>: sinh một lần mỗi lượt xem, dạng KHT7KQ2M (chỉ chữ in hoa và số để
  // ngân hàng không cắt, dễ đối soát bằng biểu thức chính quy). Mọi chỗ cùng tiền tố nhận cùng một mã.
  var maDon = {};
  function sinhMa(tienTo) {
    if (!maDon[tienTo]) {
      var ky = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', s = '';
      var ngau = (window.crypto && crypto.getRandomValues) ? crypto.getRandomValues(new Uint32Array(5)) : [1, 2, 3, 4, 5].map(function () { return Math.random() * 4e9; });
      for (var i = 0; i < 5; i++) s += ky[ngau[i] % ky.length];
      maDon[tienTo] = tienTo + s;
    }
    return maDon[tienTo];
  }
  tatCa('[data-ma-don]').forEach(function (el) {
    var ma = sinhMa(el.getAttribute('data-ma-don') || 'DH');
    if (el.tagName === 'INPUT') el.value = ma; else el.textContent = ma;
  });

  // 6. VietQR ----------------------------------------------------------------------
  // <img data-vietqr data-ngan-hang="VCB" data-so-tk="0123456789" data-ten="NGUYEN VAN A"
  //      data-so-tien="1500000" data-noi-dung="{ma} Ho Ten" data-ma-tien-to="KHT" alt="...">
  // Ảnh do img.vietqr.io dựng, miễn phí, không cần khoá. Nội dung tối đa 50 ký tự, không dấu, không ký tự đặc biệt.
  function boDau(s) {
    return s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D')
      .replace(/[^A-Za-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 50);
  }
  tatCa('img[data-vietqr]').forEach(function (img) {
    var d = img.dataset;
    var noiDung = (d.noiDung || '').replace('{ma}', d.maTienTo ? sinhMa(d.maTienTo) : '');
    var url = 'https://img.vietqr.io/image/' + encodeURIComponent(d.nganHang) + '-' + encodeURIComponent(d.soTk) + '-' + (d.mau || 'compact2') + '.png'
      + '?amount=' + encodeURIComponent(d.soTien || '') + '&addInfo=' + encodeURIComponent(boDau(noiDung))
      + '&accountName=' + encodeURIComponent(d.ten || '');
    img.src = url;
    tatCa('[data-noi-dung-ck]').forEach(function (el) { el.textContent = boDau(noiDung); });
  });

  // 7. nút chép --------------------------------------------------------------------
  tatCa('[data-chep]').forEach(function (nut) {
    nut.addEventListener('click', function () {
      var nguon = doc.querySelector(nut.getAttribute('data-chep'));
      var chu = nguon ? nguon.textContent.trim() : '';
      if (!chu || !navigator.clipboard) return;
      navigator.clipboard.writeText(chu).then(function () {
        var cu = nut.textContent; nut.textContent = 'Đã chép';
        setTimeout(function () { nut.textContent = cu; }, 1600);
      });
    });
  });

  // 8. năm -------------------------------------------------------------------------
  tatCa('[data-nam]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // 9. nút nổi ---------------------------------------------------------------------
  tatCa('.nut-dinh[data-an-khi]').forEach(function (thanh) {
    var dich = doc.querySelector(thanh.getAttribute('data-an-khi'));
    if (!dich || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (ds) {
      ds.forEach(function (d) { thanh.classList.toggle('da-an', d.isIntersecting); });
    }).observe(dich);
  });

  // 4. biểu mẫu --------------------------------------------------------------------
  // <form data-gui="web3forms" ...> có <input type="hidden" name="access_key" value="...">
  // <form data-gui="apps-script" data-dich="https://script.google.com/macros/s/.../exec">
  // <form data-gui="netlify" name="dang-ky" data-netlify="true">
  // Tuỳ chọn: data-sau="#cam-on" (hiện phần cảm ơn, ẩn form) hoặc data-chuyen="cam-on.html".
  var LOI_MAC_DINH = {
    valueMissing: 'Bạn điền giúp ô này nhé.',
    typeMismatch: 'Định dạng chưa đúng, bạn kiểm tra lại giúp.',
    patternMismatch: 'Định dạng chưa đúng, bạn kiểm tra lại giúp.',
    tooShort: 'Nội dung hơi ngắn, bạn viết thêm giúp.',
    dongY: 'Bạn đánh dấu ô đồng ý để chúng tôi được phép dùng thông tin này.'
  };
  function baoLoi(o, chu) {
    var khung = o.closest('.o') || o.parentNode;
    var loi = khung.querySelector('.bao-loi');
    if (!loi) { loi = doc.createElement('p'); loi.className = 'bao-loi'; loi.id = (o.id || o.name) + '-loi'; khung.appendChild(loi); }
    loi.textContent = chu || '';
    if (chu) { o.setAttribute('aria-invalid', 'true'); o.setAttribute('aria-describedby', loi.id); }
    else { o.removeAttribute('aria-invalid'); }
  }
  function kiemForm(form) {
    var dauTien = null;
    tatCa('input, select, textarea', form).forEach(function (o) {
      if (o.type === 'hidden' || o.closest('.mat-ong')) return;
      var chu = '';
      if (!o.checkValidity()) {
        var v = o.validity;
        chu = o.getAttribute('data-loi') || (o.type === 'checkbox' && v.valueMissing ? LOI_MAC_DINH.dongY :
          v.valueMissing ? LOI_MAC_DINH.valueMissing : v.typeMismatch ? LOI_MAC_DINH.typeMismatch :
          v.patternMismatch ? LOI_MAC_DINH.patternMismatch : v.tooShort ? LOI_MAC_DINH.tooShort : o.validationMessage);
      }
      baoLoi(o, chu);
      if (chu && !dauTien) dauTien = o;
    });
    if (dauTien) dauTien.focus();
    return !dauTien;
  }
  function ghiDongY(form, du) {
    // bằng chứng đồng ý theo Luật Bảo vệ dữ liệu cá nhân 2025: thời điểm, nội dung câu đồng ý, phiên bản chính sách
    tatCa('.dong-y input[type="checkbox"]', form).forEach(function (o, i) {
      if (!o.checked) return;
      var nhan = o.closest('.dong-y').textContent.replace(/\s+/g, ' ').trim();
      du.append('dongY_' + (o.name || i), nhan);
    });
    du.append('dongY_luc', new Date().toISOString());
    if (form.dataset.phienBanChinhSach) du.append('dongY_phienBan', form.dataset.phienBanChinhSach);
  }
  function gui(form, du) {
    var cach = form.getAttribute('data-gui');
    if (cach === 'web3forms') {
      var obj = {}; du.forEach(function (v, k) { obj[k] = v; });
      return fetch('https://api.web3forms.com/submit', {
        method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(obj)
      }).then(function (r) { return r.json(); }).then(function (j) { if (!j.success) throw new Error(j.message || 'gửi lỗi'); });
    }
    if (cach === 'apps-script') {
      // gửi dạng urlencoded: yêu cầu "đơn giản", trình duyệt không hỏi trước [preflight] mà Apps Script không trả lời được
      return fetch(form.getAttribute('data-dich'), { method: 'POST', body: new URLSearchParams(du) })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); })
        .catch(function (e) {
          if (e instanceof TypeError) { // bị chặn đọc phản hồi: gửi lại kiểu không đọc phản hồi, dữ liệu vẫn tới
            return fetch(form.getAttribute('data-dich'), { method: 'POST', mode: 'no-cors', body: new URLSearchParams(du) });
          }
          throw e;
        });
    }
    if (cach === 'netlify') {
      du.append('form-name', form.getAttribute('name'));
      return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(du).toString() })
        .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); });
    }
    return Promise.reject(new Error('form chưa khai data-gui'));
  }
  tatCa('form[data-gui]').forEach(function (form) {
    form.setAttribute('novalidate', '');
    var trangThai = form.querySelector('.trang-thai');
    if (trangThai) { trangThai.setAttribute('role', 'status'); trangThai.setAttribute('aria-live', 'polite'); }
    tatCa('input, select, textarea', form).forEach(function (o) {
      o.addEventListener('change', function () { if (o.getAttribute('aria-invalid')) baoLoi(o, o.checkValidity() ? '' : o.validationMessage); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!kiemForm(form)) { if (trangThai) { trangThai.dataset.loai = 'loi'; trangThai.textContent = 'Còn ô chưa đúng, bạn xem dòng chữ đỏ giúp.'; } return; }
      var bay = form.querySelector('.mat-ong input');
      var nut = form.querySelector('[type="submit"]');
      var nhanNut = nut ? nut.textContent : '';
      var du = new FormData(form);
      if (bay && bay.value) { hoanTat(); return; }   // máy gửi rác: giả như xong, không gửi
      ghiDongY(form, du);
      if (nut) { nut.setAttribute('aria-busy', 'true'); nut.disabled = true; nut.textContent = 'Đang gửi...'; }
      if (trangThai) { trangThai.dataset.loai = ''; trangThai.textContent = 'Đang gửi...'; }
      gui(form, du).then(hoanTat).catch(function () {
        if (trangThai) {
          trangThai.dataset.loai = 'loi';
          trangThai.textContent = form.getAttribute('data-loi-gui') || 'Chưa gửi được, có thể do mạng. Bạn thử lại sau ít phút, hoặc liên hệ trực tiếp qua thông tin ở cuối trang.';
        }
      }).then(function () {
        if (nut) { nut.removeAttribute('aria-busy'); nut.disabled = false; nut.textContent = nhanNut; }
      });
      function hoanTat() {
        if (form.dataset.chuyen) { location.href = form.dataset.chuyen; return; }
        var sau = form.dataset.sau && doc.querySelector(form.dataset.sau);
        if (sau) { sau.hidden = false; form.hidden = true; sau.setAttribute('tabindex', '-1'); sau.focus(); return; }
        if (trangThai) { trangThai.dataset.loai = 'xong'; trangThai.textContent = form.getAttribute('data-xong') || 'Đã gửi. Cảm ơn bạn, chúng tôi sẽ phản hồi sớm.'; }
        form.reset();
      }
    });
  });
})();

// Ứng dụng mẫu bậc 3: đăng nhập Google, mỗi người một sổ ghi chép riêng, quản trị xuất CSV.
// Firebase JS SDK nạp thẳng từ máy chủ của Google (không cần bước dựng). Đổi phiên bản: sửa PB ở dưới, kiểm lại toàn bộ.
// An toàn: chỉ dùng textContent khi hiện dữ liệu người dùng (chống chèn mã độc); phân quyền thật nằm ở firestore.rules.
import { cauHinhFirebase } from './firebase-cau-hinh.js';

const PB = '12.19.0';
const $ = (id) => document.getElementById(id);
const chuaCauHinh = Object.values(cauHinhFirebase).some((v) => String(v).includes('[['));
const nhung = /FBAN|FBAV|FB_IAB|Messenger|Instagram|Zalo|TikTok|Line\//i.test(navigator.userAgent);
if (nhung) { $('canh-bao-nhung').hidden = false; $('dia-chi-trang').textContent = location.href; }

if (chuaCauHinh) {
  $('trang-thai-dang-nhap').textContent = 'Ứng dụng chưa nối Firebase: dán cấu hình vào assets/js/firebase-cau-hinh.js.';
} else {
  chay().catch(() => {
    $('trang-thai-dang-nhap').dataset.loai = 'loi';
    $('trang-thai-dang-nhap').textContent = 'Chưa tải được dịch vụ đăng nhập, có thể do mạng. Bạn tải lại trang sau ít phút.';
  });
}

async function chay() {
  const [{ initializeApp }, A, F] = await Promise.all([
    import(`https://www.gstatic.com/firebasejs/${PB}/firebase-app.js`),
    import(`https://www.gstatic.com/firebasejs/${PB}/firebase-auth.js`),
    import(`https://www.gstatic.com/firebasejs/${PB}/firebase-firestore.js`),
  ]);
  const app = initializeApp(cauHinhFirebase);
  const auth = A.getAuth(app);
  const db = F.getFirestore(app);
  let huyNghe = null;

  $('nut-dang-nhap').disabled = false;
  $('nut-dang-nhap').addEventListener('click', async () => {
    const nhaCC = new A.GoogleAuthProvider();
    try { await A.signInWithPopup(auth, nhaCC); }
    catch (e) {
      if (e.code === 'auth/popup-blocked') return A.signInWithRedirect(auth, nhaCC);
      $('trang-thai-dang-nhap').dataset.loai = 'loi';
      $('trang-thai-dang-nhap').textContent = e.code === 'auth/popup-closed-by-user' ? 'Bạn đã đóng cửa sổ đăng nhập.' : 'Chưa đăng nhập được, bạn thử lại hoặc mở bằng Chrome, Safari.';
    }
  });
  $('nut-thoat').addEventListener('click', () => A.signOut(auth));

  A.onAuthStateChanged(auth, async (u) => {
    $('chua-dang-nhap').hidden = !!u; $('da-dang-nhap').hidden = !u;
    $('nut-thoat').hidden = !u; $('ten-nguoi').hidden = !u; $('quan-tri').hidden = true;
    if (huyNghe) { huyNghe(); huyNghe = null; }
    if (!u) return;
    $('ten-nguoi').textContent = u.displayName || u.email;
    $('ngay').value = new Date().toLocaleDateString('sv-SE');
    await F.setDoc(F.doc(db, 'nguoiDung', u.uid), { ten: (u.displayName || '').slice(0, 80), email: u.email, capNhat: F.serverTimestamp() });
    const q = F.query(F.collection(db, 'ghiChep'), F.where('uid', '==', u.uid), F.orderBy('taoLuc', 'desc'), F.limit(50));
    huyNghe = F.onSnapshot(q, (snap) => veDanhSach(snap.docs), () => { $('ds-cua-toi').textContent = 'Chưa đọc được dữ liệu.'; });
    try { // thử đọc danh sách quản trị: luật chỉ cho quản trị đọc, người thường nhận lỗi quyền (bình thường)
      const qt = await F.getDoc(F.doc(db, 'quanTri', u.email));
      if (qt.exists()) moQuanTri();
    } catch (e) { /* không phải quản trị */ }
  });

  function veDanhSach(docs) {
    const ul = $('ds-cua-toi'); ul.textContent = '';
    if (!docs.length) { const li = document.createElement('li'); li.className = 'phu'; li.textContent = 'Chưa có ghi chép nào.'; ul.appendChild(li); return; }
    for (const d of docs) {
      const g = d.data(), li = document.createElement('li'), the = document.createElement('article');
      the.className = 'the';
      const ngay = document.createElement('span'); ngay.className = 'dau-goi'; ngay.textContent = g.ngay;
      const p = document.createElement('p'); p.textContent = g.noiDung;
      const xoa = document.createElement('button'); xoa.className = 'nut nut--chu'; xoa.type = 'button'; xoa.textContent = 'Xoá';
      xoa.addEventListener('click', () => { if (confirm('Xoá ghi chép này?')) F.deleteDoc(d.ref); });
      the.append(ngay, p, xoa); li.appendChild(the); ul.appendChild(li);
    }
  }

  $('form-ghi').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target, tt = $('trang-thai-ghi');
    if (!f.reportValidity()) return;
    try {
      await F.addDoc(F.collection(db, 'ghiChep'), { uid: auth.currentUser.uid, noiDung: f.noiDung.value.trim(), ngay: f.ngay.value, taoLuc: F.serverTimestamp() });
      f.noiDung.value = ''; tt.dataset.loai = 'xong'; tt.textContent = 'Đã lưu.';
    } catch (err) { tt.dataset.loai = 'loi'; tt.textContent = 'Chưa lưu được (mạng hoặc dữ liệu chưa hợp lệ).'; }
  });

  async function moQuanTri() {
    $('quan-tri').hidden = false;
    const snap = await F.getDocs(F.collection(db, 'ghiChep'));
    $('dem-tat-ca').textContent = `Có ${snap.size} ghi chép.`;
    $('nut-xuat').onclick = () => {
      const o = (v) => '"' + String(v ?? '').replace(/"/g, '""') + '"';
      const dong = [['uid', 'ngay', 'noiDung'].join(',')].concat(snap.docs.map((d) => [d.get('uid'), d.get('ngay'), d.get('noiDung')].map(o).join(',')));
      const blob = new Blob(['﻿' + dong.join('\n')], { type: 'text/csv;charset=utf-8' });   // ﻿ để Excel đọc đúng dấu tiếng Việt
      const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'ghi-chep.csv'; a.click();
    };
  }
}

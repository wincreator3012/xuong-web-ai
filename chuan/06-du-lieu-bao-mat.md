# 06. Dữ liệu và bảo mật

Rủi ro lớn nhất của web làm cùng AI không nằm ở giao diện mà ở dữ liệu: 45% đoạn mã do mô hình sinh ra có lỗ hổng thuộc OWASP Top 10 (Veracode, 2025); commit có Claude Code hỗ trợ để lộ bí mật 3,2% so với mức nền 1,5% (GitGuardian, 2026); hơn 170 ứng dụng Lovable (2025), ứng dụng Tea (2025), Moltbook (2026) lộ dữ liệu vì luật bảo vệ thiếu hoặc khoá bí mật nằm trong mã trình duyệt. Nguồn: nghien-cuu/B-du-lieu-dich-vu.md mục 2, nghien-cuu/D mục 4.4, và chính các web-app cũ của tác giả xưởng (nghien-cuu/E-bai-hoc-web-app.md).

## 1. Năm nguyên tắc

1. **Không thu thì không lộ.** Bậc thấp nhất đủ dùng (chuan/01). Chỉ hỏi những ô thật cần.
2. **Công khai và bí mật là hai loại khoá khác nhau.** Được để trong trang: cấu hình web Firebase (apiKey Firebase), khoá truy cập Web3Forms, khoá `sb_publishable_` của Supabase, mã đo lường. Không bao giờ để trong trang hay trong kho git: tệp tài khoản dịch vụ (có `"private_key"`), khoá Resend, Stripe, Supabase `sb_secret_`/`service_role`, mã truy cập GitHub, khoá Gemini, OpenAI. Khoá bí mật chỉ sống ở biến môi trường của máy chủ (Cloud Functions, Cloudflare Worker) hoặc trình quản lý mật khẩu.
3. **Luật trước, giao diện sau.** Với bậc 3, viết luật bảo vệ dữ liệu (Firestore Security Rules, Supabase RLS) trước, giải thích từng dòng bằng lời thường cho người dùng, rồi mới viết giao diện. Giao diện ẩn hiện nút không phải là bảo vệ.
4. **Trình duyệt là đất của người dùng.** Mọi thứ gửi xuống trình duyệt (mã, dữ liệu, đáp án) người dùng đều xem và sửa được. Điểm thi, giá tiền, quyền quản trị phải được tính, kiểm ở máy chủ.
5. **Lộ thì xoay.** Khoá đã từng nằm trong kho git, tin nhắn, ảnh chụp màn hình là khoá đã lộ: thu hồi, tạo khoá mới, rồi mới dọn mã (xoá trong lịch sử git không đủ).

## 2. Biểu mẫu không cần máy chủ

| Cách | Khi nào | Thiết lập |
|---|---|---|
| Web3Forms (mặc định) | form liên hệ, đăng ký đơn giản; 250 lượt/tháng miễn phí | tạo khoá ở web3forms.com bằng email nhận thư, dán vào `access_key`; `data-gui="web3forms"` |
| Tally nhúng | câu hỏi phức tạp, tải tệp, nối Google Sheets sẵn | tạo form ở tally.so, nhúng khung; mở `frame-src https://tally.so` trong `_headers` |
| Google Apps Script | form tự thiết kế ghi thẳng vào Google Sheets | công thức dưới đây; `data-gui="apps-script" data-dich=".../exec"` |
| Netlify Forms | web đã đặt trên Netlify | `data-gui="netlify"`, thuộc tính `name`, `data-netlify="true"` |

Mọi form thu thông tin cá nhân: bẫy rác `.mat-ong` (máy điền vào là bị loại lặng lẽ), ô đồng ý không đánh dấu sẵn, liên kết chính sách. `nen.js` tự ghi bằng chứng đồng ý (nội dung câu đồng ý, thời điểm, phiên bản chính sách) kèm dữ liệu gửi đi.

### Công thức Apps Script ghi vào Google Sheets

Trong Google Sheet: Tiện ích [Extensions] > Apps Script, dán:

```javascript
// Nhận form từ web tĩnh, ghi một dòng vào trang tính đầu tiên. Đổi BI_MAT thành chuỗi ngẫu nhiên của bạn.
const BI_MAT = 'doi-chuoi-nay';
function doPost(e) {
  const p = e.parameter;
  if (p.botcheck) return ContentService.createTextOutput('ok');            // bẫy rác
  if (p.token !== BI_MAT) return ContentService.createTextOutput('sai');   // chặn người lạ gọi thẳng
  const khoa = LockService.getScriptLock(); khoa.waitLock(10000);           // hai lượt gửi cùng lúc không đè nhau
  try {
    const sh = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    const cot = ['luc', 'hoTen', 'email', 'dienThoai', 'loiNhan', 'maDon', 'dongY_luc', 'dongY_dongYXuLy'];
    if (sh.getLastRow() === 0) sh.appendRow(cot);
    sh.appendRow(cot.map(c => c === 'luc' ? new Date() : (p[c] || '')));
  } finally { khoa.releaseLock(); }
  return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
}
```

Triển khai [Deploy] > Triển khai mới [New deployment] > Ứng dụng web [Web app], Thực thi với tư cách [Execute as]: Tôi, Ai có quyền [Who has access]: Bất kỳ ai [Anyone]. Chép địa chỉ `/exec` vào `data-dich`, thêm ô ẩn `<input type="hidden" name="token" value="...">` cùng chuỗi BI_MAT (chuỗi này lộ trong trang, chỉ để chặn gọi bừa, không phải bảo mật thật). Ba cái bẫy: sửa mã xong phải vào Quản lý triển khai [Manage deployments] > Sửa > Phiên bản mới thì địa chỉ cũ mới chạy mã mới; Apps Script không đọc được tiêu đề HTTP nên không xác thực webhook kiểu `Authorization`; tài khoản Gmail cá nhân gửi tối đa 100 thư/ngày từ Apps Script.

## 3. Bậc 3 với Firebase

- **Mặc định Firebase gói Spark** (không cần thẻ, không tạm dừng dự án khi ít dùng, đăng nhập Google một nút). Lưu ảnh (Cloud Storage) và hàm máy chủ (Cloud Functions) cần gói Blaze (có thẻ): khi lên Blaze, đặt cảnh báo ngân sách và giới hạn chi [spend cap]; cảnh báo ngân sách không tự dừng dịch vụ.
- **Luật Firestore** (khuôn `app-firebase/firestore.rules` là mẫu chuẩn): mặc định cấm hết; mỗi bộ sưu tập mở đúng phần cần cho đúng người (`request.auth.uid == resource.data.uid`); kiểm từng trường khi ghi (`keys().hasOnly`, kiểu, độ dài, `taoLuc == request.time`); quản trị bằng tài liệu `quanTri/<email>` tạo tay và kiểm `email_verified`. Ba mẫu nguy hiểm kiem-web bắt: `allow read, write: if true`, `match /{document=**}`, `if request.auth != null` đứng một mình.
- **Đáp án, điểm, tiền:** không để trình duyệt tự chấm rồi ghi điểm. Trình duyệt chỉ gửi lựa chọn; Cloud Function đọc đáp án (bộ sưu tập không ai đọc được từ trình duyệt) rồi ghi điểm.
- **Gửi thư tự động:** qua Cloud Function hoặc tiện ích Trigger Email; khoá dịch vụ thư ở biến môi trường của hàm.
- **Tên miền được phép đăng nhập:** Firebase Console > Authentication > Settings > Authorized domains, chỉ để tên miền thật.
- **Trình duyệt nhúng của Zalo, Facebook:** Google chặn đăng nhập; khuôn có lá chắn hướng dẫn mở bằng Chrome, Safari.
- Supabase chỉ khi cần cơ sở dữ liệu quan hệ (SQL) thật: bật RLS cho mọi bảng, không bao giờ để `sb_secret_` trong trình duyệt, nhớ dự án miễn phí tạm dừng sau 7 ngày yên ắng.

## 4. Thu tiền

- Mặc định: mã VietQR có số tiền và mã đơn (`img[data-vietqr]` trong nen.js, dịch vụ img.vietqr.io miễn phí), đối soát tay với sao kê. Mã đơn chỉ chữ in hoa và số, có tiền tố.
- Tự động: SePay theo dõi tài khoản nhận tiền, đẩy giao dịch vào Google Sheets (miễn phí 50 giao dịch/tháng), khớp mã đơn bằng công thức; luôn có cột "cần xử lý tay" (người chuyển sửa nội dung, chuyển thiếu, chuyển hai lần).
- PayOS (link thanh toán có xác nhận) cần một hàm máy chủ ký yêu cầu và nhận webhook (Cloudflare Worker). Stripe không hỗ trợ doanh nghiệp Việt Nam.
- Thuế và pháp lý thu tiền (Nghị định 68/2026, 141/2026): xưởng không kết luận; người dùng hỏi kế toán (chuan/08).

## 5. Danh sách kiểm trước khi có dữ liệu thật

- [ ] `tools/kiem-web.py <web> --len` ĐẠT (không khoá bí mật, không tệp riêng trong `public/`, luật không mở toang).
- [ ] Bậc 3: làm đủ `KIEM-BAO-MAT.md` của khuôn app (thử bằng hai tài khoản, thử khi chưa đăng nhập).
- [ ] Bảng tính, tài khoản chứa dữ liệu bật xác thực hai lớp; bảng tính không chia sẻ "ai có liên kết".
- [ ] Ghi nơi lưu dữ liệu, thời hạn giữ, người được xem vào VAN-HANH.md và chính sách dữ liệu.

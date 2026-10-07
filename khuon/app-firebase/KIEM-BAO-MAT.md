# Kiểm bảo mật trước khi mở ứng dụng cho người dùng thật

Ứng dụng bậc 3 giữ dữ liệu của nhiều người: một dòng luật sai là lộ dữ liệu của tất cả (vụ Tea 2025, Lovable 2025, Moltbook 2026 đều bắt đầu như vậy; chuan/06-du-lieu-bao-mat.md). Làm đủ danh sách này, ghi kết quả vào VAN-HANH.md của dự án.

## Máy kiểm

- [ ] `python3 tools/kiem-web.py <web> --len` ĐẠT (không khoá bí mật trong mã, luật không mở toang, firebase.json chỉ đăng thư mục public).
- [ ] Không có tệp tài khoản dịch vụ (`*adminsdk*.json`, `serviceAccountKey.json`) trong thư mục web; nếu từng có và từng đẩy lên git: xoá khoá đó trong Google Cloud Console > IAM > Service accounts, tạo khoá mới, cất ngoài thư mục web.

## Người kiểm (10 phút, hai tài khoản Google)

- [ ] Tài khoản A tạo hai ghi chép. Đăng xuất, đăng nhập tài khoản B: B không thấy ghi chép của A.
- [ ] Chưa đăng nhập, mở công cụ của trình duyệt (F12) > Console, chạy thử đọc bộ sưu tập ghiChep: phải nhận lỗi quyền [permission-denied].
- [ ] Tài khoản B (không phải quản trị) không thấy khối Quản trị; tạo tài liệu `quanTri/<email của A>` trong Console thì A thấy và tải được CSV.
- [ ] Mở trang trong Zalo hoặc Messenger: hiện cảnh báo mở bằng trình duyệt, không treo ở bước đăng nhập.
- [ ] Firebase Console > Authentication > Settings > Authorized domains: chỉ có tên miền của bạn, `localhost`, `<mã dự án>.web.app`, `<mã dự án>.firebaseapp.com`.
- [ ] Dữ liệu có điểm số, đáp án, kết quả thi: KHÔNG để trình duyệt tự chấm và tự ghi điểm. Đáp án nằm ở máy chủ (Cloud Functions, cần gói Blaze, đặt hạn mức chi), trình duyệt chỉ gửi lựa chọn.

## Định kỳ

- [ ] Mỗi tháng: Firebase Console > Usage, xem lượt đọc ghi bất thường; Authentication > Users, xoá tài khoản thử.
- [ ] Khi đổi luật: kiểm lại hai mục "Người kiểm" đầu tiên.

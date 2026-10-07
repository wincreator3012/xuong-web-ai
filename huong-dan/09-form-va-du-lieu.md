# 09. Biểu mẫu, dữ liệu và người biên tập

Ba cách nhận dữ liệu từ form trên web tĩnh, xếp từ đơn giản tới linh hoạt, và cách cho người khác tự sửa nội dung mà không cần biết mã. Chọn cách nào: chuan/06-du-lieu-bao-mat.md mục 2.

## A. Web3Forms (mặc định cho form liên hệ, đăng ký)

1. Vào web3forms.com, nhập email muốn nhận thư (email chủ hoặc email tên miền), bấm **Create Access Key**.
2. Mở thư Web3Forms gửi, chép khoá truy cập [access key] gửi Claude (khoá này công khai theo thiết kế, nằm trong HTML được; nó chỉ cho phép gửi thư về đúng email bạn đã đăng ký).
3. Claude dán vào ô `access_key` của form, đưa lên, cùng bạn gửi thử một lần.
4. Gói miễn phí 250 lượt/tháng. Thư báo có thể rơi vào thư rác ở lần đầu: đánh dấu "Không phải thư rác".

## B. Tally (form nhiều câu hỏi, tải tệp, tự vào Google Sheets)

1. Vào tally.so, đăng ký, tạo form (gõ `/` để thêm loại câu hỏi). Thêm câu đồng ý dạng ô đánh dấu bắt buộc, không đánh dấu sẵn, có liên kết chính sách.
2. **Integrations** > **Google Sheets** > kết nối tài khoản Google, chọn tạo bảng mới.
3. **Share** > **Embed** > chép đường dẫn form gửi Claude; Claude nhúng vào trang và mở `frame-src https://tally.so` trong `_headers`.

## C. Google Apps Script (form tự thiết kế, ghi thẳng vào Google Sheets)

1. Tạo một Google Sheet mới (Drive > Mới > Google Trang tính), đặt tên rõ (ví dụ "Đăng ký khoá thu 2026").
2. **Tiện ích** [Extensions] > **Apps Script**. Xoá mã có sẵn, dán mã Claude đưa (mẫu ở chuan/06 mục 2), đổi dòng `BI_MAT` theo chuỗi Claude gợi ý, bấm biểu tượng lưu.
3. **Triển khai** [Deploy] > **Triển khai mới** [New deployment] > biểu tượng bánh răng chọn **Ứng dụng web** [Web app] > **Thực thi với tư cách** [Execute as]: **Tôi** [Me]; **Ai có quyền truy cập** [Who has access]: **Bất kỳ ai** [Anyone] > **Triển khai**. Lần đầu Google hỏi cấp quyền: chọn tài khoản > **Nâng cao** [Advanced] > **Đi tới ... (không an toàn)** > **Cho phép** (đây là mã của chính bạn).
4. Chép **URL ứng dụng web** (kết thúc bằng `/exec`) gửi Claude.
5. Sau này sửa mã: **Triển khai** > **Quản lý triển khai** [Manage deployments] > biểu tượng bút chì > **Phiên bản** [Version]: **Phiên bản mới** > **Triển khai**. Làm vậy địa chỉ giữ nguyên; bấm "Triển khai mới" sẽ ra địa chỉ khác.
6. Bảng tính: **Chia sẻ** chỉ với người cần xem; không bật "Bất kỳ ai có đường liên kết".

## D. Cho người khác sửa nội dung web nhiều trang (Pages CMS)

Dành cho web từ khuôn `site-astro` (đã có tệp `.pages.yml`).
1. Vào pagescms.org, **Sign in with GitHub** (tài khoản chủ kho), cài ứng dụng Pages CMS cho đúng kho của web.
2. Mở kho trong Pages CMS: thấy mục **Bài viết**. Thêm, sửa bài ngay trên giao diện; lưu là tạo một lần commit, nơi lưu trữ tự cập nhật web.
3. Mời người biên tập: **Collaborators** > nhập email; người được mời không cần tài khoản GitHub.

## Xong khi

- [ ] Gửi thử form: dữ liệu về đúng nơi, có cột đồng ý và thời điểm đồng ý.
- [ ] Ghi vào VAN-HANH.md: dịch vụ nhận form, email nhận, bảng dữ liệu, ai được xem, thời hạn giữ dữ liệu.

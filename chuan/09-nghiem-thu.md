# 09. Nghiệm thu: chưa qua cổng thì chưa nói "xong"

Bốn lớp kiểm, theo thứ tự. Lớp sau không thay lớp trước. Nguồn: hướng dẫn thực hành Claude Code của Anthropic ("cho Claude một phép kiểm chạy được; đưa bằng chứng thay vì tự khẳng định"), Playwright, axe-core, WebAIM (nghien-cuu/D mục 4.3, 5).

## 1. Máy kiểm: `tools/kiem-web.py <web>`

Chạy sau mỗi đợt sửa. Ba mức: LỖI (chặn), CẢNH BÁO (xem, có lý do mới bỏ qua, ghi lý do khi trình), GỢI Ý (chữ nên cân nhắc). Báo cáo `BAO-CAO.md`, ảnh chụp ba khổ 390, 768, 1280 px và tờ tổng thể ghi vào `kiem/` của hồ sơ dự án.

Kiểm tĩnh (mọi máy): HTML, Open Graph, ảnh, liên kết, form (nhãn, ô đồng ý, chính sách, bẫy rác, nơi nhận), chữ (gạch dài, nháy cong, Title Case, từ cấm, sáo ngữ), chỗ trống `[[...]]`, khoá bí mật, tệp riêng trong `public/`, luật Firebase, đáp án gửi xuống trình duyệt.
Kiểm trình duyệt (nơi có Playwright: sandbox đám mây của phiên, hoặc máy người dùng đã cài): tràn ngang, lỗi JavaScript, tệp hỏng, chữ dưới 14 px, dấu tiếng Việt, WCAG 2.2 AA bằng axe-core, trọng lượng trang.

## 2. Claude nhìn

Máy không thấy được cái đẹp, cái lệch nhịp, cái sai giọng. Trước khi trình:
- Mở tờ tổng thể và ảnh từng khổ ở cỡ thật; đối chiếu THIET-KE.md và danh sách cấm (chuan/03 mục 9).
- Đọc soát toàn bộ chữ từng âm tiết; tên, chức danh đúng PHONG-CACH mục 1.
- Trình người dùng: tờ tổng thể + 3-6 dòng (lựa chọn chính và lý do, cảnh báo còn lại, điều cần người dùng chốt).

## 3. Người dùng thử

Danh sách kiểm bằng tay in sẵn ở cuối mỗi BAO-CAO.md: mở trên điện thoại thật, bấm hết nút, gửi thử form tới email của mình, đi hết trang bằng phím Tab, đọc to chữ, xác nhận mọi số liệu và lời chứng thực là thật. Bậc 3 thêm `KIEM-BAO-MAT.md` (thử bằng hai tài khoản).

## 4. Cổng trước khi đưa lên mạng: `--len`

`tools/kiem-web.py <web> --len` (dua-len.py tự chạy): mọi chỗ trống `[[...]]`, khung ảnh chờ, tên miền chưa đặt (khi đã có tên miền), khoá form chưa dán, ảnh chia sẻ chưa có đều thành LỖI. Chưa ĐẠT thì không đưa lên.

## 5. Sau khi lên mạng

Danh sách ở chuan/07 mục 7 (điện thoại thật, chia sẻ Zalo, gửi thử form, quét thử QR, ghi VAN-HANH.md). Rồi mới báo người dùng "đã lên mạng", kèm địa chỉ.

## 6. Khi sửa nền chung, khuôn

Sửa `he-thong/nen.css`, `nen.js` hay một khuôn: tạo thử web từ MỌI khuôn bị ảnh hưởng (`tools/web-moi.py`, vào `Du an/_tam/` hoặc một thư mục thử ngoài repo), chạy kiem-web từng cái, nhìn tờ tổng thể; chỉ còn cảnh báo chỗ trống mới coi là đạt. Web đang chạy không tự nhận bản nen.css mới: chép sang khi người dùng muốn, kiểm lại web đó.

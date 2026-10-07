# 10. Thu tiền bằng mã VietQR, đối soát tự động với SePay

Mã VietQR trên web (khuôn `landing` có sẵn) hiện số tiền và nội dung chuyển khoản gồm mã đơn; người mua quét bằng ứng dụng ngân hàng là đủ thông tin. Dịch vụ dựng ảnh mã img.vietqr.io miễn phí, không cần khoá. Mã QR không tự biết người mua đã trả chưa: đối soát tay với sao kê, hoặc tự động bằng SePay.

Trước khi thu tiền qua web: xác định tài khoản nhận (tổ chức hay cá nhân), và hỏi kế toán về thuế (Nghị định 68/2026 yêu cầu hộ kinh doanh khai báo mọi tài khoản nhận tiền kinh doanh; chuan/08 mục 7). Web có chức năng đặt hàng, thanh toán trực tuyến: xem nghĩa vụ thông báo với Bộ Công Thương (chuan/08 mục 3).

## Bạn làm: thông tin cho mã QR

Gửi Claude:
1. Ngân hàng nhận (Claude đổi sang mã của VietQR, ví dụ VCB, TCB, MB, ACB, BIDV, ICB cho VietinBank; danh sách đầy đủ ở api.vietqr.io/v2/banks).
2. Số tài khoản, tên chủ tài khoản viết HOA không dấu đúng như trong ngân hàng.
3. Số tiền từng gói.
Đây là thông tin bạn vốn in lên tài liệu gửi người mua, không phải bí mật. Claude điền vào `img[data-vietqr]`; mỗi lượt đăng ký có một mã đơn (ví dụ `KHT7KQ2M`: tiền tố lấy từ tên thương hiệu, cộng 5 ký tự ngẫu nhiên) vừa ghi vào form, vừa nằm trong nội dung chuyển khoản.

Thử: mở web, gửi đăng ký thử, quét mã bằng ứng dụng ngân hàng (không cần chuyển): đúng tên người nhận, số tiền, nội dung.

## Bạn làm: đối soát tự động với SePay (tuỳ chọn)

1. Vào sepay.vn, đăng ký, liên kết tài khoản ngân hàng nhận tiền (xác nhận bằng mã OTP của ngân hàng; gói miễn phí hỗ trợ một số ngân hàng lớn, 50 giao dịch/tháng).
2. Trong SePay bật tích hợp **Google Sheets**, chọn bảng (có thể là chính bảng đăng ký, trang tính riêng tên "Giao dịch").
3. Claude thêm công thức khớp mã đơn giữa trang Đăng ký và trang Giao dịch (đánh dấu "đã trả"), và cột "cần xử lý tay" cho trường hợp người mua sửa nội dung, chuyển thiếu, chuyển hai lần.
4. Cần xác nhận tức thời, gửi thư tự động: dùng webhook của SePay tới một hàm nhỏ (Cloudflare Worker hoặc Apps Script có chuỗi bí mật trong địa chỉ); Claude thiết kế, bạn tạo khoá và dán vào biến môi trường theo hướng dẫn riêng.

## Xong khi

- [ ] Quét thử mã: đúng người nhận, số tiền, nội dung có mã đơn.
- [ ] Biết ai đối soát, bao lâu một lần, gửi xác nhận cho người mua bằng cách nào (ghi VAN-HANH.md).

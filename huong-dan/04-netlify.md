# 04. Netlify: cho web ít sửa cần form có sẵn

Từ 04/09/2025 tài khoản Netlify mới dùng gói tính theo tín dụng: gói Free 300 tín dụng/tháng, mỗi lần đưa bản chính thức tốn 15 tín dụng (khoảng 20 lần mỗi tháng), băng thông 20 tín dụng/GB; hết tín dụng thì MỌI web trong tài khoản tạm dừng tới chu kỳ sau. Bù lại, biểu mẫu Netlify Forms miễn phí, không giới hạn. Chọn Netlify khi web ít sửa; sửa thử trên bản xem trước (không tốn tín dụng), chỉ đưa bản chính thức khi đã chốt.

Cần: kho GitHub của web (thẻ 01), khoảng 15 phút.

## Bạn làm

1. Vào app.netlify.com/signup, đăng ký bằng GitHub.
2. Claude đã tạo `netlify.toml` (`python3 tools/dua-len.py <web> --noi netlify`), bạn đã Commit và Push.
3. **Add new site** (hoặc **Add new project**) > **Import an existing project** > **GitHub** > chọn kho. Giữ cấu hình đọc từ netlify.toml > **Deploy**.
4. Form: đổi form trong trang sang `data-gui="netlify"` và thêm `name="..." data-netlify="true"` (Claude làm); dữ liệu xem ở mục **Forms** của web trên Netlify, bật thông báo email ở **Form notifications**.
5. Tên miền: **Domain management** > **Add a domain**; làm theo thẻ 07 (www: CNAME tới `<tên>.netlify.app`; tên miền gốc: bản ghi A `75.2.60.5` hoặc ALIAS tới `apex-loadbalancer.netlify.com`).

## Xong khi

- [ ] Web chạy, form gửi thử về được mục Forms.
- [ ] Đã ghi vào VAN-HANH.md: đây là web Netlify, giới hạn lượt đưa lên mỗi tháng.

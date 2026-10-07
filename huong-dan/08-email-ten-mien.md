# 08. Email theo tên miền (ví dụ lienhe@ten.vn)

Không bắt buộc để có web; cần khi muốn gửi nhận thư bằng địa chỉ tên miền. Lưu ý 2026: Gmail bỏ tính năng "Send mail as" cho địa chỉ bên ngoài từ 01/2027, nên đừng xây cách làm mới kiểu "chuyển tiếp về Gmail rồi gửi bằng Gmail".

## Chọn dịch vụ

| Dịch vụ | Chi phí | Hợp khi |
|---|---|---|
| Zoho Mail Forever Free | miễn phí, tối đa 5 người, 5 GB/người, 1 tên miền | cá nhân, nhóm nhỏ; đọc thư trên web và ứng dụng Zoho (không IMAP ở gói miễn phí) |
| Google Workspace | khoảng 220.000 đ/người/tháng (qua đại lý, chưa VAT) | muốn dùng giao diện Gmail, Drive, Meet theo tên miền |
| Microsoft 365 Business Basic | theo trang Microsoft Việt Nam | tổ chức quen Outlook, Teams |
| Cloudflare Email Routing | miễn phí | chỉ cần NHẬN thư rồi chuyển tiếp về hộp thư có sẵn |

## Bạn làm (ví dụ Zoho Mail miễn phí)

1. Vào trang giá Zoho Mail (zoho.com/mail/zohomail-pricing.html), chọn gói **Forever Free** (thường ở cuối trang), đăng ký bằng tên miền của bạn.
2. Xác minh tên miền: Zoho đưa một bản ghi TXT (hoặc CNAME). Thêm vào bảng DNS (nơi giữ nameserver), quay lại bấm **Verify**.
3. Tạo hộp thư (ví dụ `lienhe@ten.vn`).
4. Thêm các bản ghi Zoho hiện ra ở bước cấu hình thư, chép ĐÚNG giá trị trên màn hình (Zoho có nhiều vùng máy chủ, giá trị khác nhau):
   - **MX**: thường ba bản ghi với ưu tiên 10, 20, 50.
   - **SPF** (TXT ở `@`): dạng `v=spf1 include:... ~all`. Mỗi tên miền chỉ MỘT bản ghi SPF; dùng thêm dịch vụ gửi thư khác thì gộp vào cùng bản ghi.
   - **DKIM** (TXT, tên dạng `zmail._domainkey`): Zoho sinh trong trang quản trị.
   - **DMARC** (TXT ở `_dmarc`): bắt đầu bằng `v=DMARC1; p=none; rua=mailto:lienhe@ten.vn`.
5. Gửi thử một thư tới Gmail của bạn: thư phải vào hộp thư chính, không vào thư rác; mở thư > **Show original** [Hiển thị thư gốc] thấy SPF, DKIM, DMARC đều **PASS**.

## Claude làm

- Chép lại mọi bản ghi email đang có trước khi đổi nameserver hay sửa DNS.
- Đọc kết quả **Show original** bạn gửi (che địa chỉ người nhận nếu muốn), chỉ ra bản ghi còn sai.

## Xong khi

- [ ] Gửi và nhận thư được bằng địa chỉ tên miền; SPF, DKIM, DMARC đều PASS.
- [ ] Đã ghi dịch vụ email, người quản trị, ngày gia hạn vào VAN-HANH.md.

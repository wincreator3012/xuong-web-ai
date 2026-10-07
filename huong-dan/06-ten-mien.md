# 06. Chọn và mua tên miền

Tên miền là tài sản thương hiệu: đứng tên chủ thật, bật tự gia hạn, giữ lâu dài. Nguồn: nghien-cuu/C-ten-mien-email-phap-ly.md phần 1 (giá kiểm 10/2026).

## Chọn đuôi

| Đuôi | Hợp khi | Mua ở đâu | Chi phí năm (gia hạn) |
|---|---|---|---|
| .com | thương hiệu cá nhân, quốc tế, muốn quản lý dễ | Cloudflare Registrar (giá gốc, khoảng 10,5 USD), Porkbun | khoảng 270.000 đ |
| .vn | tín hiệu Việt Nam rõ | nhà đăng ký trong nước (danh sách ở vnnic.vn: PA Việt Nam, Mắt Bão, Nhân Hoà, iNET, Tenten...) | khoảng 650.000-830.000 đ |
| .com.vn | doanh nghiệp Việt Nam | nhà đăng ký trong nước | rẻ hơn .vn một chút |
| .edu.vn | CHỈ tổ chức hoạt động giáo dục (từ 10/02/2026), cần hồ sơ tổ chức | nhà đăng ký trong nước | |

Thương hiệu quan trọng: cân nhắc giữ cả .vn và .com, trỏ một cái về cái kia. Tên ngắn, dễ đọc qua điện thoại, không dấu gạch nối nếu tránh được.

## Bạn làm: mua .com ở Cloudflare

1. Đăng nhập Cloudflare (thẻ 02) > **Domain Registration** > **Register Domains** > tìm tên > **Purchase**.
2. Điền thông tin liên hệ đúng của chủ tên miền; thanh toán bằng thẻ đã bật thanh toán quốc tế (thẻ 00).
3. Tên miền mua ở Cloudflare dùng sẵn nameserver Cloudflare, ẩn thông tin WHOIS, tự gia hạn: bỏ qua bước chuyển nameserver ở thẻ 02.

## Bạn làm: mua .vn ở nhà đăng ký trong nước

1. Tạo tài khoản ở nhà đăng ký bằng email chủ; bật xác thực hai lớp nếu có.
2. Tìm tên, **hỏi rõ giá gia hạn** (giá năm đầu thường là khuyến mãi). Chỉ mua tên miền; không mua kèm gói lưu trữ, SSL, email nếu chưa cần (nơi lưu trữ của xưởng cấp HTTPS miễn phí).
3. Khai bản khai đăng ký: cá nhân khai họ tên, số định danh cá nhân, địa chỉ thường trú, ngày sinh, điện thoại, email (Nghị định 147/2024); tổ chức khai mã số doanh nghiệp, người quản lý. Thông tin sai là căn cứ thu hồi tên miền. Làm theo hướng dẫn xác thực của nhà đăng ký (có thể qua định danh điện tử).
4. Thanh toán, chờ tên miền được kích hoạt (thường trong ngày).
5. Bật **tự động gia hạn**, **khoá chuyển tên miền** [domain lock] nếu có; ghi ngày hết hạn vào lịch, nhắc trước 30 ngày.

## Ghi lại

Vào VAN-HANH.md: tên miền, nhà đăng ký, email đăng nhập, ngày hết hạn, tự gia hạn bật chưa. Báo Claude để làm tiếp thẻ 07.

## Lỗi hay gặp

- Mua qua người làm hộ, tên miền đứng tên họ: khi cần chuyển đi không lấy được mã chuyển [auth code]. Yêu cầu chuyển tên chủ thể về bạn ngay.
- Để hết hạn: tên miền bị người khác mua lại và có thể đòi tiền chuộc.
- Vừa mua hoặc vừa chuyển nhà đăng ký: tên miền quốc tế bị khoá chuyển 60 ngày (quy định ICANN), bình thường.

# 11. Đo lượt xem và có mặt trên Google

Hai công cụ miễn phí, không cookie theo dõi người xem, nên không cần hộp hỏi đồng ý cookie.

## Cloudflare Web Analytics (đếm lượt xem, tốc độ thật)

1. Đăng nhập Cloudflare > **Analytics & Logs** > **Web Analytics** > **Add a site**.
2. Web đã đặt ở Cloudflare với tên miền riêng: chọn bật tự động. Web đặt nơi khác: nhập tên miền, chép đoạn mã JavaScript gửi Claude; Claude dán vào cuối mọi trang (chính sách bảo mật nội dung trong `_headers` đã mở sẵn cho Cloudflare Analytics).
3. Sau vài giờ có số liệu: lượt xem, nguồn đến, quốc gia, thiết bị, chỉ số tốc độ thật (Core Web Vitals).

## Google Search Console (Google thấy web thế nào)

1. Vào search.google.com/search-console, đăng nhập email chủ > **Add property** > chọn **Domain** [Miền], nhập `ten.vn`.
2. Google đưa một bản ghi TXT: thêm vào bảng DNS (thẻ 07), quay lại bấm **Verify**. Có thể mất vài phút tới vài giờ.
3. **Sitemaps** > nhập `sitemap.xml` (web Astro: `sitemap-index.xml`) > **Submit**.
4. Một hai tuần sau, xem **Performance** [Hiệu suất]: người ta gõ gì trên Google để tìm thấy web; **Pages** [Trang]: trang nào chưa được lập chỉ mục và vì sao.

## Xong khi

- [ ] Web Analytics có số liệu; Search Console đã xác minh và nhận sitemap.
- [ ] Ghi vào VAN-HANH.md: hai công cụ, tài khoản đăng nhập.

Mỗi tháng, nhờ Claude đọc số liệu cùng bạn: trang nào được xem, người đến từ đâu, form có tăng đăng ký không; đối chiếu mục tiêu ở BRIEF.md.

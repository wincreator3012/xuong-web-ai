# 07. Trỏ tên miền về web (DNS)

Bản ghi DNS nói cho cả thế giới biết tên miền của bạn trỏ tới máy chủ nào. Nguyên tắc vàng: **chép đúng giá trị nơi lưu trữ hiện trên màn hình**, không chép từ bài hướng dẫn cũ (Vercel, Firebase cấp giá trị riêng cho từng dự án).

## Vài khái niệm

- Tên miền gốc [apex]: `ten.vn`, ô Tên ghi `@`. Tên miền phụ: `www.ten.vn`, ô Tên ghi `www`.
- Bản ghi A: trỏ tên tới một địa chỉ IP. CNAME: trỏ tên tới một tên khác (không đặt ở tên miền gốc, trừ khi nhà cung cấp hỗ trợ "làm phẳng").
- Nameserver: nơi giữ toàn bộ bản ghi. Đã chuyển sang Cloudflare thì sửa bản ghi ở Cloudflare, không ở nhà đăng ký.
- TTL: thời gian máy khác nhớ bản ghi cũ. Thay đổi thường có tác dụng sau vài phút tới vài giờ, tối đa 48 giờ.

## Theo nơi lưu trữ

| Nơi | Làm gì |
|---|---|
| Cloudflare | chuyển nameserver sang Cloudflare, rồi thêm Custom domain cho Worker (thẻ 02); Cloudflare tự tạo bản ghi |
| Vercel | Settings > Domains > Add; thêm đúng bản ghi A (tên miền gốc) và CNAME (www) Vercel hiện ra |
| Netlify | www: CNAME tới `<tên>.netlify.app`; gốc: ALIAS tới `apex-loadbalancer.netlify.com` hoặc A `75.2.60.5` |
| Firebase | Hosting > Add custom domain; thêm bản ghi TXT xác minh (giữ vĩnh viễn) và bản ghi A Firebase cấp |
| GitHub Pages | gốc: bốn bản ghi A `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; www: CNAME tới `<tên-người-dùng>.github.io`; xác minh tên miền trong cài đặt tài khoản trước |

## Bạn làm (ở bảng DNS của nơi giữ nameserver)

1. Xoá bản ghi A, CNAME cũ ở `@` và `www` (thường trỏ trang "đỗ" của nhà đăng ký). Giữ nguyên MX, TXT của email.
2. Thêm bản ghi mới đúng giá trị nơi lưu trữ đưa. Ô Tên chỉ gõ `@` hoặc `www` (nhiều bảng tự nối tên miền phía sau).
3. Lưu, chờ 5-30 phút, quay lại trang tên miền của nơi lưu trữ bấm kiểm lại [Refresh / Verify].
4. Báo Claude; Claude kiểm bằng `dig`, dnschecker.org, mở thử HTTPS, rồi gắn tên miền vào web (`tools/dua-len.py --ten-mien`).

## Lỗi hay gặp ở bảng DNS nhà đăng ký Việt Nam

- Nhập `www.ten.vn` vào ô Tên ở bảng tự nối, thành `www.ten.vn.ten.vn`: chỉ nhập `www`.
- Còn bản ghi A cũ song song bản ghi mới: web lúc hiện lúc không.
- Dùng "chuyển hướng URL" [URL forwarding] thay bản ghi: HTTPS không cấp được.
- Bảng không cho đặt CNAME ở tên miền gốc: dùng bản ghi A, hoặc chuyển nameserver sang Cloudflare.
- Bảng đòi dấu chấm cuối (`cname.vercel-dns-0.com.`) hoặc cấm dấu chấm cuối: thử cách còn lại.
- Có bản ghi CAA cũ chỉ cho một nhà phát hành chứng chỉ khác: thêm `letsencrypt.org` hoặc xoá CAA.
- Không thấy nút sửa: tên miền đang dùng nameserver nơi khác; sửa ở nơi đó.
- .vn chưa được duyệt bản khai: DNS chưa chạy dù nhập đúng.

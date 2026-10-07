# 02. Cloudflare: nơi lưu trữ mặc định của xưởng

Miễn phí, được dùng cho web thương mại, băng thông tệp tĩnh không giới hạn, có máy chủ tại Hà Nội và TP.HCM. Web chạy dưới dạng Cloudflare Workers chỉ phục vụ tệp tĩnh (không có mã chạy ở máy chủ). Nguồn: nghien-cuu/A-hosting.md.

Cần: tài khoản GitHub có kho của web (thẻ 01), khoảng 20 phút; gắn tên miền riêng thêm 20 phút và quyền vào trang quản lý tên miền.

## Bạn làm: tài khoản và nối kho

1. Vào dash.cloudflare.com/sign-up, đăng ký bằng email chủ, xác nhận email.
2. Bật xác thực hai lớp: ảnh đại diện > **Profile** > **Authentication** > **Two-Factor Authentication**; cất mã khôi phục.
3. Claude đã tạo `wrangler.jsonc` trong kho (`python3 tools/dua-len.py <web> --noi cloudflare`), bạn đã Commit và Push.
4. Trong bảng điều khiển: **Workers & Pages** > **Create application** [Tạo ứng dụng] > **Get started** cạnh **Import a repository** [Nhập từ kho]. Lần đầu chọn **Git account** > kết nối GitHub, cho phép Cloudflare đọc đúng kho của web (chọn **Only select repositories**, chọn kho).
5. Chọn kho của web. Ở phần cấu hình:
   - Web tĩnh: **Build command** để trống; **Deploy command** giữ mặc định `npx wrangler deploy`.
   - Web Astro: **Build command**: `npm run build`; **Deploy command**: `npx wrangler deploy`.
6. Bấm **Save and Deploy** [Lưu và đưa lên]. Sau khoảng một phút, web chạy ở địa chỉ dạng `https://<tên-web>.<tên-tài-khoản>.workers.dev`. Gửi địa chỉ đó cho Claude.

Từ nay, mỗi lần Push lên nhánh `main`, Cloudflare tự đưa bản mới lên.

## Bạn làm: gắn tên miền riêng

Cloudflare chỉ gắn tên miền riêng cho Workers khi tên miền "nằm trên Cloudflare", nghĩa là chuyển máy chủ tên miền [nameserver] sang Cloudflare. Tên miền .vn mua ở nhà đăng ký trong nước vẫn chuyển được.

1. Trước khi chuyển: chụp lại (hoặc nhờ Claude ghi) mọi bản ghi DNS đang có ở nhà đăng ký, nhất là MX (email), TXT. Quên là mất email.
2. Bảng điều khiển Cloudflare > **Add a domain** [Thêm tên miền] > nhập tên miền > chọn gói **Free** > Cloudflare tự quét bản ghi cũ; đối chiếu với bản chụp, thêm bản ghi thiếu.
3. Cloudflare đưa hai địa chỉ nameserver (dạng `ten.ns.cloudflare.com`). Vào trang quản lý tên miền ở nhà đăng ký, mục **Nameserver** / **Máy chủ tên miền**, thay các địa chỉ cũ bằng hai địa chỉ này, lưu. Chờ vài phút tới vài giờ, Cloudflare gửi email báo tên miền đã hoạt động.
4. **Workers & Pages** > chọn web > **Settings** > **Domains & Routes** > **Add** > **Custom domain** > nhập `ten.vn` (và thêm lần nữa cho `www.ten.vn` nếu muốn). HTTPS tự cấp.
5. Báo Claude tên miền để chạy `python3 tools/dua-len.py <web> --ten-mien https://ten.vn`, rồi Commit và Push.

## Claude làm

- Tạo `wrangler.jsonc` (chỉ đưa thư mục `public/` hoặc `dist/` lên), kiểm `--len` trước khi bạn Push.
- Đối chiếu bản ghi DNS trước và sau khi chuyển nameserver.
- Sau khi lên mạng: kiểm địa chỉ, HTTPS, ảnh chia sẻ, form (chuan/07 mục 7).

## Xong khi

- [ ] Web mở được ở địa chỉ workers.dev (hoặc tên miền riêng) có ổ khoá HTTPS.
- [ ] Push một thay đổi nhỏ, sau khoảng một phút thấy trên web.

## Lỗi hay gặp

- Bản dựng báo lỗi tên: tên Worker trên Cloudflare phải trùng `name` trong `wrangler.jsonc` (mặc định là tên thư mục web). Đổi một trong hai cho khớp.

- Bản ghi để chế độ proxy (đám mây màu cam) với dịch vụ khác như Vercel gây lỗi chuyển hướng vòng lặp: với bản ghi trỏ ra ngoài Cloudflare, để **DNS only** (đám mây xám).
- Không thấy nút Import a repository: tài khoản mới có thể bị giới hạn tạo dự án trong 48 giờ đầu; hoặc giao diện đổi tên: Claude tra developers.cloudflare.com/workers/ci-cd/builds/.
- Muốn thử nhanh không cần tài khoản: kéo thư mục `public/` vào cloudflare.com/drop (bản thử sống một giờ).

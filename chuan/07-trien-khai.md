# 07. Triển khai: đưa lên mạng, tên miền, email, đo lường, bảo trì

Phần này chia hai loại việc: việc máy làm (`tools/dua-len.py`, Claude chạy) và việc người dùng tự tay làm vì gắn với danh tính, tiền, quyền sở hữu tài khoản (thẻ hướng dẫn trong `huong-dan/`). Nguồn: nghien-cuu/A-hosting.md, nghien-cuu/C-ten-mien-email-phap-ly.md (kiểm 07/10/2026; giá và giao diện các dịch vụ đổi nhanh, mở lại nguồn trước khi khẳng định với người dùng).

## 1. Chọn nơi lưu trữ

| Nơi | Chọn khi | Không chọn khi | Thẻ hướng dẫn |
|---|---|---|---|
| **Cloudflare** (Workers, tệp tĩnh) | MẶC ĐỊNH cho web tĩnh và Astro: miễn phí, được dùng thương mại, băng thông tệp tĩnh không giới hạn, có máy chủ ở Hà Nội và TP.HCM, đặt được lớp bảo vệ HTTP | người dùng không chịu chuyển máy chủ tên miền [nameserver] sang Cloudflare (bắt buộc khi gắn tên miền riêng) | huong-dan/02-cloudflare.md |
| **Firebase Hosting** | web-app đã dùng Firebase (đăng nhập, Firestore): cùng dự án, một lệnh đưa lên | web tĩnh thuần lượng xem lớn (gói Spark 10 GB/tháng) | huong-dan/05-firebase.md |
| **Vercel** | web cá nhân phi thương mại, người dùng đã quen Vercel | web có bán hàng, quảng bá dịch vụ trả phí (gói Hobby cấm thương mại; Pro 20 USD/tháng) | huong-dan/03-vercel.md |
| **Netlify** | web ít sửa cần form có sẵn | web sửa nhiều (gói Free khoảng 20 lần đưa bản chính thức/tháng; hết tín dụng thì mọi web trong tài khoản tạm dừng) | huong-dan/04-netlify.md |
| **GitHub Pages** | trang cá nhân, tài liệu công khai | web thương mại, kho riêng tư (cần GitHub trả phí), cần lớp bảo vệ HTTP | huong-dan/01-github.md |

Web đã chạy ở nơi khác (ví dụ Vercel) mà đang ổn: không bắt chuyển; chỉ cảnh báo khi vi phạm điều khoản (web thương mại trên Vercel Hobby).

## 2. Cách đưa lên: nối kho git là cách thường ngày

1. **Lần đầu (người dùng tự làm, Claude hướng dẫn từng bước):** tạo tài khoản GitHub và nơi lưu trữ, tạo kho cho web, nối kho với nơi lưu trữ. Từ đó mỗi lần đẩy [push] lên nhánh `main` là web tự cập nhật sau khoảng một phút.
2. **Mỗi lần sửa:** Claude sửa, chạy `tools/kiem-web.py <web>`, người dùng duyệt, rồi lưu thay đổi [commit] và đẩy lên (người dùng tự commit, hoặc cho phép Claude làm trong phiên đó).
3. **Đưa thẳng bằng dòng lệnh** (khi chưa nối git, hoặc trợ lý chạy trên máy người dùng): `python3 tools/dua-len.py <web> --noi cloudflare --that`. Công cụ tạo cấu hình, chạy cổng kiểm `--len`, rồi mới gọi `wrangler deploy` (hoặc `vercel`, `netlify`, `firebase deploy`). Lần đầu cần đăng nhập trên trình duyệt, hoặc mã truy cập [API token] quyền tối thiểu trong biến môi trường; không bao giờ ghi mã vào tệp.
4. **Chỉ thư mục công khai được đưa lên** (`public/`, Astro: `dist/`). Cấu hình do dua-len.py tạo đều trỏ đúng thư mục này.

## 3. Tên miền

- **.com** rẻ, quản lý dễ: mua ở Cloudflare Registrar (bán đúng giá gốc, khoảng 10,5 USD/năm, tăng nhẹ từ 01/11/2026) hoặc Porkbun; cần thẻ Visa/Mastercard đã bật thanh toán quốc tế.
- **.vn, .com.vn** tín hiệu Việt Nam: chỉ mua qua nhà đăng ký trong nước (danh sách ở vnnic.vn: PA Việt Nam, Mắt Bão, Nhân Hoà, iNET, Tenten...), khai số định danh cá nhân và địa chỉ thường trú (Nghị định 147/2024); gia hạn khoảng 650.000-830.000 đ/năm.
- **.edu.vn**: từ 10/02/2026 chỉ tổ chức hoạt động giáo dục được đăng ký, duy trì; cá nhân không chọn đuôi này.
- Luôn hỏi giá gia hạn; bật tự gia hạn, khoá chuyển [transfer lock]; đứng tên chủ thật; không mua kèm gói lưu trữ, SSL (nơi lưu trữ cấp HTTPS miễn phí).
- Cách mua từng bước: huong-dan/06-ten-mien.md.

## 4. Trỏ tên miền (DNS)

- Không chép giá trị bản ghi từ bài hướng dẫn cũ trên mạng: mở trang tên miền của nơi lưu trữ, chép đúng giá trị nó hiện ra (Vercel đã đổi IP và tên CNAME cho dự án mới; Firebase cấp IP và bản ghi TXT riêng từng dự án).
- Cloudflare: gắn tên miền riêng cho Workers cần tên miền "nằm trên Cloudflare" (đổi nameserver ở nhà đăng ký sang hai địa chỉ Cloudflare đưa). Trước khi đổi, chép đủ mọi bản ghi đang có, nhất là MX của email, kẻo mất thư.
- Lỗi hay gặp ở bảng DNS của nhà đăng ký Việt Nam: ô Tên tự nối tên miền (chỉ nhập `www`, không nhập `www.ten.vn`); còn bản ghi A cũ trỏ trang "đỗ" (xoá trước); dùng "chuyển hướng URL" thay cho bản ghi (SSL không cấp được); bản ghi CAA chặn Let's Encrypt.
- Kiểm: dnschecker.org, toolbox.googleapps.com/apps/dig; xong khi nơi lưu trữ báo hợp lệ và trang có ổ khoá HTTPS. Thường vài phút tới vài giờ, tối đa 48 giờ.
- Sau khi tên miền chạy: `python3 tools/dua-len.py <web> --ten-mien https://ten.vn` để gắn vào canonical, Open Graph, sitemap.
- Từng bước theo nơi lưu trữ: huong-dan/07-dns.md.

## 5. Email theo tên miền

- Lựa chọn: Zoho Mail Forever Free (tối đa 5 người, gửi nhận trong Zoho, không IMAP); Google Workspace (khoảng 220.000 đ/người/tháng qua đại lý); Microsoft 365. Cloudflare Email Routing chỉ chuyển tiếp thư đến.
- Không xây mô hình mới dựa trên "chuyển tiếp về Gmail + Gmail Send as": Gmail bỏ "Send as" cho địa chỉ ngoài từ 01/2027.
- Bản ghi bắt buộc: MX, SPF (một bản ghi duy nhất), DKIM, DMARC (`v=DMARC1; p=none; rua=mailto:...` để bắt đầu). Web có gửi thư tự động (Resend, Brevo) thì thêm bản ghi của dịch vụ đó.
- Từng bước: huong-dan/08-email-ten-mien.md.

## 6. Đo lường

- Mặc định: Cloudflare Web Analytics (miễn phí, không cookie, không cần chuyển DNS) + Google Search Console (từ khoá, lỗi lập chỉ mục, gửi sitemap).
- Không cài Google Analytics, Meta Pixel làm mặc định: dùng cookie, cần hỏi đồng ý (chuan/08).
- Từng bước: huong-dan/11-do-luong-search-console.md.

## 7. Sau khi lên mạng

- [ ] Mở trên điện thoại thật bằng 4G; gửi link qua Zalo cho chính mình, xem ảnh và tiêu đề chia sẻ.
- [ ] Gửi thử form: thư về đúng hộp, dữ liệu vào đúng bảng, ô đồng ý được ghi.
- [ ] Quét mã VietQR thử bằng ứng dụng ngân hàng (không cần chuyển): đúng tên, số tiền, nội dung.
- [ ] Ghi vào VAN-HANH.md: địa chỉ, nơi lưu trữ, tài khoản (email đăng nhập, chủ tài khoản, xác thực hai lớp), tên miền và ngày hết hạn.

## 8. Bảo trì

- Sửa nội dung: người dùng nói, Claude sửa, kiểm, đưa lên. Nội dung đổi thường (lịch, danh sách) nên tách sang JSON hoặc Google Sheet để sửa không đụng mã.
- Định kỳ: gia hạn tên miền (nhắc trước 30 ngày), xoá dữ liệu hết hạn giữ, xem số liệu đo lường, rà lại giá dịch vụ (`chuan/kho-dich-vu.json`, 6 tháng một lần).
- Web không còn dùng: gỡ khỏi nơi lưu trữ, giữ kho mã, quyết định giữ hay bỏ tên miền (bỏ thì có người khác mua lại và dùng tên của bạn).

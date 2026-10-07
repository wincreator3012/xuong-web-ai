# Thẻ hướng dẫn: những việc chủ web tự tay làm

Trợ lý AI viết mã, dựng trang, kiểm, chuẩn bị cấu hình được. Nhưng có những việc gắn với danh tính, tiền và quyền sở hữu tài khoản mà chỉ chủ web làm được: tạo tài khoản, bật xác thực hai lớp, nhập thẻ thanh toán, khai thông tin mua tên miền, bấm nút trong bảng điều khiển của nhà cung cấp, xác nhận email, cấp quyền cho ứng dụng. Mỗi thẻ dưới đây dẫn một việc như vậy.

| Thẻ | Việc | Thời gian |
|---|---|---|
| `huong-dan/00-tai-khoan-goc.md` | email chủ, xác thực hai lớp, trình quản lý mật khẩu, bảng ghi tài khoản | 20 phút, làm một lần |
| `huong-dan/01-github.md` | tài khoản GitHub, kho cho web, đưa mã lên bằng GitHub Desktop; GitHub Pages | 20 phút |
| `huong-dan/02-cloudflare.md` | tài khoản Cloudflare, nối kho để web tự cập nhật, gắn tên miền | 20-40 phút |
| `huong-dan/03-vercel.md` | Vercel (web cá nhân phi thương mại) | 15 phút |
| `huong-dan/04-netlify.md` | Netlify (web ít sửa cần form có sẵn) | 15 phút |
| `huong-dan/05-firebase.md` | dự án Firebase: đăng nhập Google, Firestore, cấu hình web, đưa lên, quản trị | 30-45 phút |
| `huong-dan/06-ten-mien.md` | chọn và mua tên miền .vn hoặc .com | 20 phút (+ chờ duyệt .vn) |
| `huong-dan/07-dns.md` | trỏ tên miền về nơi lưu trữ, kiểm, sửa lỗi | 15 phút (+ chờ lan truyền) |
| `huong-dan/08-email-ten-mien.md` | email theo tên miền, bản ghi MX, SPF, DKIM, DMARC | 30 phút |
| `huong-dan/09-form-va-du-lieu.md` | khoá Web3Forms, form Tally, Apps Script ghi Google Sheets, Pages CMS cho người biên tập | 10-30 phút |
| `huong-dan/10-thanh-toan-vietqr.md` | mã chuyển khoản VietQR, đối soát SePay | 15-30 phút |
| `huong-dan/11-do-luong-search-console.md` | Cloudflare Web Analytics, Google Search Console | 15 phút |
| `huong-dan/12-ban-giao-cho-khach.md` | khi làm web cho người khác: ai giữ tài khoản, bàn giao thế nào | 30 phút |

## Claude dẫn thế nào

1. **Một bước mỗi lượt.** Nói bước, chờ người dùng báo xong (hoặc gửi ảnh chụp màn hình) rồi mới sang bước sau. Người dùng mới dễ lạc khi nhận mười bước một lúc.
2. **Nói chỗ bấm bằng đúng chữ trên màn hình**, kèm nghĩa Việt: nút **Create** [Tạo]. Giao diện nhà cung cấp đổi tên nút thường xuyên: chữ trên màn hình người dùng khác thẻ thì tra trang tài liệu chính thức (đường dẫn trong `chuan/kho-dich-vu.json`) rồi dẫn theo màn hình thật, và sửa thẻ sau phiên.
3. **Không bao giờ xin mật khẩu, mã xác thực, mã khôi phục.** Người dùng tự nhập vào trang của nhà cung cấp. Thứ người dùng được phép gửi Claude: cấu hình công khai (cấu hình web Firebase, khoá truy cập Web3Forms), giá trị bản ghi DNS, địa chỉ web, ảnh chụp màn hình đã che thông tin nhạy cảm.
4. **Mã truy cập [API token] để Claude tự đưa web lên:** chỉ khi người dùng muốn, quyền tối thiểu, có hạn dùng; cách mặc định tốt hơn là nối kho GitHub với nơi lưu trữ (không cần đưa token cho ai).
5. **Trình duyệt dựng sẵn hoặc Claude in Chrome** (khi phiên có): Claude mở đúng trang, chỉ chỗ bấm; người dùng tự đăng nhập, tự nhập thông tin và bấm xác nhận những bước liên quan tiền, danh tính.
6. **Ghi lại:** xong mỗi thẻ, ghi vào `VAN-HANH.md` của dự án (dịch vụ, email đăng nhập, chủ tài khoản, xác thực hai lớp bật chưa, ngày gia hạn). Không ghi mật khẩu.

---
name: web-trien-khai
description: "Đưa web của xưởng web AI (repo xuong-web-ai) lên mạng và vận hành: chọn nơi lưu trữ (Cloudflare mặc định, Firebase, Vercel, Netlify, GitHub Pages), dẫn người dùng từng bước tạo tài khoản GitHub, Cloudflare, Firebase, bật xác thực hai lớp, nối kho để web tự cập nhật, mua tên miền .vn hoặc .com, trỏ DNS, email theo tên miền, đo lượt xem, Search Console, gia hạn, bàn giao web cho đối tác. Kích hoạt khi người dùng nói đưa web lên mạng, deploy, publish, đưa lên GitHub, Vercel, Cloudflare, Netlify, Firebase, mua tên miền, trỏ tên miền, cấu hình DNS, web không vào được, lỗi SSL, email tên miền, đo lượt xem, Google không tìm thấy web, bàn giao web cho khách, gia hạn tên miền. Dùng sau khi web đã qua cổng kiểm của web-thiet-ke, kể cả khi người dùng không nhắc tên skill."
---

# Xưởng web AI: đưa lên mạng và vận hành

Đọc `CLAUDE.md` và `docs/QUY-TRINH-KY-THUAT.md` của repo `xuong-web-ai` trước. Chuẩn: `chuan/07-trien-khai.md` (nơi lưu trữ, tên miền, DNS, email, đo lường, bảo trì), `chuan/08-phap-ly-vn.md`. Việc người dùng tự tay làm: thẻ trong `huong-dan/` (danh mục và cách dẫn ở `huong-dan/README.md`).

Chưa gắn thư mục "Web AI" vào phiên (không thấy `CLAUDE.md` của repo) thì nhờ người dùng gắn trước bằng nút thêm thư mục. Không gắn được (ví dụ người dùng đang dùng ứng dụng trên điện thoại) thì vẫn làm theo các bước dưới: bản skill có kèm `references/` (gói .zip của `tools/dong-goi-skill.py`) thì dựa vào bản chụp chuẩn và phong cách ở đó (danh sách, dấu gói: `references/DONG-GOI.md`); bản chỉ có SKILL.md (lưu qua thẻ đề xuất skill) thì dựa vào các bước và quy tắc cứng trong tệp này. Nói rõ với người dùng là đang làm khi chưa có xưởng, công cụ kiểm chưa chạy, khuôn chưa dùng được, và việc nào nên làm lại khi gắn được thư mục.

## Quy trình

### 1. Xác định hiện trạng

Đọc `xuong.json` (noiDat, tenMien) của web và `VAN-HANH.md` của dự án. Hỏi người dùng (tối đa 4 câu): đã có tài khoản nào (GitHub, Cloudflare, Firebase), đã có tên miền chưa và mua ở đâu, web có thương mại không, ai sẽ giữ tài khoản (người dùng hay đối tác).

### 2. Chọn nơi lưu trữ (chuan/07 mục 1)

Mặc định Cloudflare; web-app Firebase dùng Firebase Hosting; Vercel chỉ cho web phi thương mại. Web đang chạy ổn ở nơi khác thì giữ, chỉ cảnh báo khi vi phạm điều khoản. `python3 tools/dua-len.py --so-sanh` in bảng gọn để trình người dùng.

### 3. Chuẩn bị và cổng kiểm

`python3 tools/dua-len.py <web> --noi <nơi>`: tạo cấu hình (chỉ đưa `public/` hoặc `dist/`), dựng Astro nếu cần, chạy `kiem-web.py --len`. Chưa ĐẠT thì quay lại sửa (chỗ trống `[[...]]`, ảnh chờ, khoá form, ảnh chia sẻ).

### 4. Dẫn người dùng làm phần tự tay

Theo thứ tự: `huong-dan/00-tai-khoan-goc.md` (nếu chưa), `01-github.md`, rồi thẻ của nơi lưu trữ (02 Cloudflare, 03 Vercel, 04 Netlify, 05 Firebase). Một bước mỗi lượt; nói đúng chữ trên màn hình; không bao giờ xin mật khẩu, mã xác thực, khoá bí mật; giao diện khác thẻ thì tra tài liệu chính thức và dẫn theo màn hình thật, sửa thẻ sau phiên. Có trình duyệt dựng sẵn hoặc Claude in Chrome: mở đúng trang, chỉ chỗ bấm; người dùng tự đăng nhập, tự xác nhận.

Cách thường ngày: nối kho GitHub với nơi lưu trữ một lần; mỗi lần người dùng Commit, Push thì web tự cập nhật. Đưa thẳng bằng dòng lệnh (`dua-len.py --that`) chỉ khi chạy trên máy người dùng đã đăng nhập công cụ, hoặc người dùng chủ động tạo mã truy cập quyền tối thiểu.

### 5. Tên miền, DNS, email

`huong-dan/06-ten-mien.md` (chọn đuôi, mua; .edu.vn chỉ cho tổ chức giáo dục; luôn hỏi giá gia hạn), `07-dns.md` (chép đúng giá trị nơi lưu trữ hiện ra; chép lại mọi bản ghi cũ, nhất là MX, trước khi đổi nameserver), `08-email-ten-mien.md`. Tên miền chạy rồi: `python3 tools/dua-len.py <web> --ten-mien https://...`, kiểm lại, người dùng Push.

### 6. Sau khi lên mạng (chuan/07 mục 7)

Mở thật, kiểm HTTPS, gửi link qua Zalo xem ảnh chia sẻ (làm mới bộ đệm Zalo, Facebook nếu cần), gửi thử form, quét thử mã QR. Đo lường, Search Console: `huong-dan/11-do-luong-search-console.md`. Ghi mọi thứ vào `VAN-HANH.md` (không mật khẩu).

### 7. Vận hành, bàn giao

Sửa định kỳ qua web-thiet-ke; gia hạn, dữ liệu hết hạn giữ, rà giá dịch vụ (`chuan/kho-dich-vu.json`). Web làm cho đối tác: `huong-dan/12-ban-giao-cho-khach.md` ngay từ đầu (tài khoản đứng tên họ).

## Quy tắc cứng

1. Không đưa lên khi `kiem-web.py --len` chưa ĐẠT.
2. Không xin, không nhận, không ghi mật khẩu, mã xác thực, mã khôi phục; khoá bí mật không bao giờ vào tệp trong thư mục web hay kho git. Thấy khoá lộ (trong mã, trong địa chỉ remote của git): báo người dùng thu hồi ngay.
3. Tài khoản, tên miền đứng tên chủ thật của web.
4. Chép giá trị DNS từ màn hình của nơi lưu trữ, không từ trí nhớ hay bài cũ.
5. Không khẳng định giá, hạn mức mà chưa kiểm lại khi số liệu trong `chuan/kho-dich-vu.json` đã cũ hơn 6 tháng.
6. Không tự commit, push, mua, xoá tài nguyên trên dịch vụ của người dùng khi người dùng chưa cho phép trong phiên.

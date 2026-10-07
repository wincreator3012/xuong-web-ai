# 01. GitHub: nơi giữ mã nguồn của web

GitHub giữ mã nguồn và lịch sử mọi lần sửa của web. Khi kho GitHub đã nối với nơi lưu trữ (Cloudflare, Vercel, Netlify), mỗi lần đẩy thay đổi lên là web tự cập nhật. Người không quen dòng lệnh dùng **GitHub Desktop** (ứng dụng có giao diện, miễn phí).

Cần: email chủ (thẻ 00), khoảng 20 phút.

## Bạn làm

1. Vào github.com/signup, đăng ký bằng email chủ, chọn tên người dùng ngắn, chuyên nghiệp (sẽ hiện trong địa chỉ kho). Xác nhận email.
2. Bật xác thực hai lớp: ảnh đại diện góc phải > **Settings** [Cài đặt] > **Password and authentication** > **Enable two-factor authentication**; quét mã bằng ứng dụng tạo mã; tải và cất **recovery codes**.
3. Cài GitHub Desktop từ desktop.github.com, đăng nhập bằng tài khoản vừa tạo (đăng nhập qua trình duyệt, không dán mật khẩu vào đâu khác).
4. Tạo kho cho web: trong GitHub Desktop chọn **File > Add Local Repository**, chọn thư mục web (trong `Web/<tên-web>`), bấm **create a repository** nếu được hỏi; đặt tên trùng tên thư mục; rồi **Publish repository**, để đánh dấu **Keep this code private** [Giữ riêng tư] (trừ khi dùng GitHub Pages gói miễn phí, xem dưới).
5. Mỗi lần web được sửa xong và bạn đã duyệt: mở GitHub Desktop, xem danh sách thay đổi, gõ một dòng tóm tắt ở ô **Summary** (ví dụ "Đổi ngày khai giảng"), bấm **Commit to main**, rồi **Push origin**.

## Claude làm

- Chuẩn bị thư mục web đúng cấu trúc, có `.gitignore` chặn khoá bí mật, `node_modules`, `dist`.
- Chạy `tools/kiem-web.py` trước khi bạn commit; nhắc bạn commit khi một đợt sửa đã duyệt.
- Không tự commit, không tự đẩy lên, trừ khi bạn cho phép trong phiên đó.

## GitHub Pages (chỉ cho web cá nhân, tài liệu công khai, phi thương mại)

1. Kho phải là công khai (gói miễn phí). Claude tạo quy trình đưa lên: `python3 tools/dua-len.py <web> --noi github-pages` (tạo `.github/workflows/pages.yml`).
2. Trên github.com, vào kho > **Settings** > **Pages** > **Source**: chọn **GitHub Actions**.
3. Commit và Push. Sau 1-2 phút, web chạy ở `https://<tên-người-dùng>.github.io/<tên-kho>/`.

## Xong khi

- [ ] Tài khoản có xác thực hai lớp, mã khôi phục đã cất.
- [ ] Kho của web hiện trên github.com, đúng chế độ riêng tư hay công khai.

## Lỗi hay gặp

- Kho đang có mã truy cập trong địa chỉ remote (`https://github_pat_...@github.com/...`): đó là mã đã lộ. Thu hồi ở **Settings > Developer settings > Personal access tokens**, rồi trong GitHub Desktop: **Repository > Repository Settings > Remote**, đặt lại địa chỉ dạng `https://github.com/<tên>/<kho>.git`.
- Lỡ đẩy tệp khoá bí mật lên kho: xoá tệp chưa đủ (còn trong lịch sử). Thu hồi khoá ở dịch vụ gốc trước, tạo khoá mới, rồi nhờ Claude dọn.
- Tải tệp qua trang web GitHub (**Add file > Upload files**) tối đa 100 tệp một lần; web có nhiều tệp phông nên dùng GitHub Desktop.

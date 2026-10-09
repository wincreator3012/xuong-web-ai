---
name: web-ung-dung
description: "Tầng ứng dụng của xưởng web AI (repo xuong-web-ai): web có form ghi Google Sheets, thanh toán VietQR và đối soát, web nhiều trang và blog bằng Astro 7, web-app có đăng nhập Google và dữ liệu riêng từng người bằng Firebase (luật Firestore, quản trị, xuất CSV), trắc nghiệm, tra cứu dữ liệu, và rà an toàn web-app cũ. Kích hoạt khi người dùng nói làm web-app, có đăng nhập, lưu dữ liệu, quản lý học viên, bài thi online, chấm điểm, dashboard, form ghi vào Google Sheet, nhận đăng ký tự động, thu tiền, VietQR, blog, nhiều trang, Astro, Firebase, Firestore, Supabase, kiểm bảo mật app, app bị lộ khoá, kể cả khi người dùng không nhắc tên skill. Đi cùng web-thiet-ke (tư vấn, thiết kế, kiểm) và web-trien-khai (đưa lên)."
---

# Xưởng web AI: tầng ứng dụng (bậc 1-3)

Đọc `CLAUDE.md`, `docs/QUY-TRINH-KY-THUAT.md` của repo `xuong-web-ai`; chuẩn chính: `chuan/06-du-lieu-bao-mat.md`, `chuan/05-ky-thuat.md`, `chuan/01-tu-van-giai-phap.md` mục 3-5; bài học từ web-app cũ của tác giả xưởng: `nghien-cuu/E-bai-hoc-web-app.md`.

Chưa gắn thư mục "Web AI" vào phiên (không thấy `CLAUDE.md` của repo) thì nhờ người dùng gắn trước bằng nút thêm thư mục. Không gắn được (ví dụ người dùng đang dùng ứng dụng trên điện thoại) thì vẫn làm theo các bước dưới: bản skill có kèm `references/` (gói .zip của `tools/dong-goi-skill.py`) thì dựa vào bản chụp chuẩn và phong cách ở đó (danh sách, dấu gói: `references/DONG-GOI.md`); bản chỉ có SKILL.md (lưu qua thẻ đề xuất skill) thì dựa vào các bước và quy tắc cứng trong tệp này. Nói rõ với người dùng là đang làm khi chưa có xưởng, công cụ kiểm chưa chạy, khuôn chưa dùng được, và việc nào nên làm lại khi gắn được thư mục.

## Nguyên tắc chọn

Luôn bậc thấp nhất đủ dùng. Trước khi lên bậc 3, hỏi: một form nhúng, một bảng tính, một nền tảng có sẵn có làm được không? Bậc 3 thêm tài khoản phải giữ, thêm chỗ có thể lộ dữ liệu của nhiều người.

## Theo nhu cầu

### Form ghi vào Google Sheets, nhận đăng ký (bậc 1-2)

- Mặc định Web3Forms (`data-gui="web3forms"`); form phức tạp, tải tệp: Tally nhúng; cần ghi thẳng bảng tính với form tự thiết kế: Apps Script (mã mẫu chuan/06 mục 2, `data-gui="apps-script"`, chuỗi bí mật, LockService). Dẫn người dùng theo `huong-dan/09-form-va-du-lieu.md`.
- Luôn có ô đồng ý không đánh dấu sẵn, liên kết chính sách, bẫy rác; nen.js ghi bằng chứng đồng ý.

### Thu tiền (bậc 1-2)

- Mã VietQR có số tiền, mã đơn (`img[data-vietqr]`, `data-ma-don`); đối soát tay hoặc SePay vào Sheets (`huong-dan/10-thanh-toan-vietqr.md`). Webhook, link thanh toán PayOS cần hàm máy chủ (Cloudflare Worker): thiết kế, giải thích, để người dùng tạo khoá và đặt biến môi trường.
- Gắn cờ pháp lý trong BRIEF (chuan/08 mục 3, 7): thông báo website thương mại điện tử, thuế; khuyên hỏi luật sư, kế toán.

### Web nhiều trang, blog (khuôn `site-astro`)

- Astro 7 xuất tĩnh, Node 22.12+; viết theo docs.astro.build bản 7 (không cú pháp Astro 4-5); giữ `markdown.smartypants: false`.
- Bài viết là tệp `.md` trong `src/content/bai-viet/` (tiêu đề, mô tả dưới 155 ký tự, ngày); người biên tập dùng Pages CMS (`.pages.yml`).
- Kiểm: `npm run build` rồi `tools/kiem-web.py` (kiểm `dist/`).

### Web-app đăng nhập + dữ liệu (khuôn `app-firebase`, bậc 3)

1. Đặc tả trước: ai dùng, vai trò nào thấy gì, dữ liệu gì, giữ bao lâu; ghi BRIEF.md.
2. **Luật trước giao diện:** viết `firestore.rules` theo mẫu của khuôn (mặc định cấm; chủ sở hữu theo `uid`; kiểm từng trường; quản trị qua `quanTri/<email>` + `email_verified`); giải thích từng khối bằng lời thường cho người dùng.
3. Dựng giao diện: JS thuần + Firebase SDK module qua CDN, hiện dữ liệu bằng `textContent`; giữ lá chắn trình duyệt Zalo/Facebook; lưu ngầm với phiên làm việc dài.
4. Điểm, đáp án, tiền, gửi thư: tính ở máy chủ (Cloud Functions, gói Blaze có giới hạn chi), không trong trình duyệt.
5. Dẫn người dùng `huong-dan/05-firebase.md`; chạy `kiem-web.py --len`; làm `KIEM-BAO-MAT.md` cùng chủ web (hai tài khoản, thử khi chưa đăng nhập) trước khi mời người dùng thật.
6. Supabase chỉ khi cần SQL thật: RLS mọi bảng, không `sb_secret_` trong trình duyệt, lưu ý tạm dừng sau 7 ngày yên ắng.

### Rà an toàn web-app có sẵn

Đọc mã (không chạy) theo bảng lỗ hổng ở nghien-cuu/E mục 3 và cổng kiem-web: khoá bí mật trong mã và trong địa chỉ remote git, tệp riêng nằm trong thư mục đưa lên mạng, luật mở, phân quyền chỉ ở giao diện, đáp án, điểm gửi xuống trình duyệt. Báo người dùng theo mức độ, việc nào người dùng phải làm ngay (thu hồi khoá) và việc Claude vá được; không sửa web-app của người dùng khi người dùng chưa đồng ý.

## Quy tắc cứng

1. Bậc thấp nhất đủ dùng; lên bậc 3 phải nói rõ lý do và cái giá.
2. Khoá bí mật không bao giờ nằm trong mã gửi xuống trình duyệt hay trong kho git; khoá đã lộ thì thu hồi trước, dọn sau.
3. Luật bảo vệ dữ liệu viết và kiểm trước giao diện; không `if true` cho ghi, không `{document=**}`, không `request.auth != null` đứng một mình.
4. Không để trình duyệt chấm điểm, tính tiền, cấp quyền.
5. Dữ liệu tâm lý, sức khoẻ là dữ liệu nhạy cảm: mặc định không lưu (trắc nghiệm tính trên máy người dùng); muốn lưu thì xin đồng ý riêng và gắn cờ pháp lý.
6. Chưa làm `KIEM-BAO-MAT.md` cùng chủ web thì chưa mở cho người dùng cuối.

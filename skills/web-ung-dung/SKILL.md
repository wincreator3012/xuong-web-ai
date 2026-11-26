---
name: web-ung-dung
description: "Tầng ứng dụng của xưởng web AI (repo xuong-web-ai): web có form ghi Google Sheets, thanh toán VietQR và đối soát, web nhiều trang và blog bằng Astro 7, web-app có đăng nhập Google và dữ liệu riêng từng người bằng Firebase (luật Firestore, quản trị, xuất CSV), trắc nghiệm, tra cứu dữ liệu, và rà an toàn web-app cũ. Kích hoạt khi người dùng nói làm web-app, có đăng nhập, lưu dữ liệu, quản lý học viên, bài thi online, chấm điểm, dashboard, form ghi vào Google Sheet, nhận đăng ký tự động, thu tiền, VietQR, blog, nhiều trang, Astro, Firebase, Firestore, Supabase, kiểm bảo mật app, app bị lộ khoá, web-app có trí năng nhân tạo gọi Claude API (prompt, rào chắn, chi phí, đợt thử nghiệm người dùng), giao diện và trải nghiệm web-app nhiều bước, kể cả khi người dùng không nhắc tên skill. Đi cùng web-thiet-ke (tư vấn, thiết kế, kiểm) và web-trien-khai (đưa lên)."
---

# Xưởng web AI: tầng ứng dụng (bậc 1-4)

Đọc `CLAUDE.md`, `docs/QUY-TRINH-KY-THUAT.md` của repo `xuong-web-ai`; chuẩn chính: `chuan/06-du-lieu-bao-mat.md`, `chuan/05-ky-thuat.md`, `chuan/01-tu-van-giai-phap.md` mục 3-5; bài học từ web-app cũ của tác giả xưởng: `nghien-cuu/E-bai-hoc-web-app.md`. Web-app có trí năng nhân tạo (bậc 4): `chuan/10-ung-dung-ai.md`. Giao diện và trải nghiệm của mọi web-app: `chuan/11-giao-dien-trai-nghiem.md` (nền tảng: `nghien-cuu/G-giao-dien-trai-nghiem.md`).

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
2. **Luật trước giao diện:** viết `firestore.rules` theo mẫu của khuôn (mặc định cấm; chủ sở hữu theo `uid`; kiểm từng trường bằng `keys().hasOnly`, kiểu, độ dài; quản trị qua `quanTri/<email>` hoặc kiểm email chủ đã xác minh `email_verified == true` kèm `mods/{uid}`); giải thích từng khối bằng lời thường cho người dùng.
3. Dựng giao diện theo chuan/11 (trạng thái, bố cục theo khổ, luồng nhiều bước, lưu nháp, mẫu đang tải và lỗi ở mục 4, bộ token và theme tối ở mục 11, danh sách cấm mẫu lừa): JS thuần + Firebase SDK module qua CDN, hiện dữ liệu bằng `textContent`; giữ lá chắn trình duyệt Zalo/Facebook. Vì CSP khoá chặt (`script-src 'self' https://www.gstatic.com https://apis.google.com`), viết các mô-đun vẽ biểu đồ (SVG và Canvas 2D), xuất PDF khổ A4 và xuất Excel `.xlsx` chuẩn OpenXML ngay trong `public/assets/js/` thay vì gọi CDN lạ. Các khung đăng nhập email/mật khẩu hoặc bộ lọc quản trị dùng `<div class="bieu-mau" role="group">` kèm `<button type="button">` (không bọc `<form>` để tránh nhầm với biểu mẫu thu thông tin khách hàng).
4. Điểm, đáp án, tiền, gửi thư: bài thi có đáp án đúng sai hoặc tính tiền phải chấm ở máy chủ (Cloud Functions, gói Blaze có giới hạn chi). Với **bài tự đánh giá phản tư [self-assessment]** không có đúng sai, cho phép tính điểm trên trình duyệt để cả Khách chưa đăng nhập vẫn dùng trọn vẹn, nhưng khi trang quản trị hiển thị hoặc xuất Excel phải **tính lại điểm từ câu trả lời thô (`answers`)** bằng đúng công thức gốc.
5. Khi chạy trong **Antigravity** (hoặc trợ lý chạy trên máy người dùng đã đăng nhập `firebase login`), chủ động dùng `firebase-tools` tạo dự án, gắn tên miền `<mã-dự-án>.web.app`, khởi tạo Firestore `asia-southeast1`, đăng ký ứng dụng web điền `firebase-cau-hinh.js` và chạy `firebase deploy` (`huong-dan/05-firebase.md`); người dùng chỉ cần bật công tắc phương thức đăng nhập (Google, Email/Password) trong bảng điều khiển Firebase. Chạy `kiem-web.py --len`; làm `KIEM-BAO-MAT.md` cùng chủ web trước khi mời người dùng thật.
6. Supabase chỉ khi cần SQL thật: RLS mọi bảng, không `sb_secret_` trong trình duyệt, lưu ý tạm dừng sau 7 ngày yên ắng.

### Web-app có trí năng nhân tạo (bậc 4, `chuan/10-ung-dung-ai.md`)

1. Hỏi trước xem có thật cần bậc 4 (chuan/10 mục 1), và nói rõ cái giá: chi phí mỗi lượt gọi mô hình, gói Blaze, khóa API phải giữ, dữ liệu nhạy cảm, prompt là tài sản cần bảo vệ.
2. Đặc tả nghiệp vụ và tệp prompt riêng (có số phiên bản) trước khi viết mã; trong đặc tả giữ bảng quyết định đánh số, mỗi thay đổi người dùng duyệt thêm một dòng. Phương án lớn: trình phương án kèm các điểm cần người dùng quyết, chờ duyệt rồi mới dựng.
3. Kiến trúc mặc định (chuan/10 mục 3): lõi TypeScript thuần có mô hình giả lập để kiểm thử; Cloud Functions thế hệ 2 làm mọi thao tác ghi và mọi lời gọi mô hình; luật Firestore chỉ cho đọc dữ liệu của chính mình; React + Vite + TypeScript cho giao diện; khóa ở Secret Manager.
4. Gọi Claude bằng `output_config.format` (json_schema) và `effort` theo từng lời gọi; đo lời gọi thật rồi mới đặt trần `max_tokens` (tiếng Việt tốn gấp khoảng 3 lần ước lượng). Mỗi đầu ra qua rào chắn bằng mã (câu trích nguyên văn, số lượng, không khuyên chọn, chuẩn chữ, không lộ prompt, kiểm an toàn), viết lại có giới hạn rồi dùng phương án mặc định soạn sẵn.
5. Hạn mức theo gói, trần token mỗi lượt, ngân sách ngày tự tạm ngưng, ghi chi phí từng lời gọi; nhắc người dùng đặt hạn mức chi trên Anthropic Console và Google Cloud. Việc chạy nhiều phút thì chạy nền theo Firestore, có khóa chống chạy trùng (chuan/10 mục 8).
6. Kiểm ba tầng: kiểm thử lõi; máy giả lập Firebase và Playwright đi trọn luồng bằng nhiều vai; một lượt thật với Claude để đo chi phí, thời gian, chất lượng. Đưa lên tự động theo web-trien-khai (GitHub Actions và Workload Identity Federation).
7. Mời người dùng thật theo đợt thử nghiệm (chuan/10 mục 13): gói giới hạn, trang mời ẩn tự duyệt có số tài khoản tối đa và ngày đóng trang, góp ý theo nhịp ngắn, vị thế đồng kiến tạo.
8. Giao diện theo chuan/11 mục 5: người dùng nghĩ trước, máy soi sau; giọng máy tách khỏi lời người dùng; mỗi nhận xét kèm căn cứ; bản ghi chỉ gom lời người dùng; chờ trên 10 giây nói thời lượng.
9. Mọi chữ hiển thị, kể cả lời nhắn lỗi phía máy chủ, lời chào, câu hỏi khảo sát, qua cổng soát chữ (chuan/04, `tools/kiem-web.py`) và đọc to lại trước khi trình người dùng.

### Rà an toàn web-app có sẵn

Đọc mã (không chạy) theo bảng lỗ hổng ở nghien-cuu/E mục 3 và cổng kiem-web: khoá bí mật trong mã và trong địa chỉ remote git, tệp riêng nằm trong thư mục đưa lên mạng, luật mở, phân quyền chỉ ở giao diện, đáp án, điểm gửi xuống trình duyệt. Báo người dùng theo mức độ, việc nào người dùng phải làm ngay (thu hồi khoá) và việc Claude vá được; không sửa web-app của người dùng khi người dùng chưa đồng ý.

## Quy tắc cứng

1. Bậc thấp nhất đủ dùng; lên bậc 3 phải nói rõ lý do và cái giá.
2. Khoá bí mật không bao giờ nằm trong mã gửi xuống trình duyệt hay trong kho git; khoá đã lộ thì thu hồi trước, dọn sau.
3. Luật bảo vệ dữ liệu viết và kiểm trước giao diện; không `if true` cho ghi, không `{document=**}`, không `request.auth != null` đứng một mình.
4. Không để trình duyệt chấm bài có đáp án đúng sai, tính tiền, cấp quyền; bài tự đánh giá phản tư là ngoại lệ duy nhất (mục bậc 3, bước 4), và trang quản trị vẫn tính lại điểm từ câu trả lời thô.
5. Dữ liệu tâm lý, sức khoẻ là dữ liệu nhạy cảm: mặc định không lưu (trắc nghiệm tính trên máy người dùng); muốn lưu thì xin đồng ý riêng và gắn cờ pháp lý.
6. Chưa làm `KIEM-BAO-MAT.md` cùng chủ web thì chưa mở cho người dùng cuối.
7. Chữ của web-app (câu hỏi, lời diễn giải kết quả, khuyến nghị, thông báo) nằm trong JS nhưng là chữ hiển thị: viết câu đủ chủ ngữ, vị ngữ, gọi đúng tên chỉ số của mô hình, không xâu nhãn bằng dấu hai chấm, theo `chuan/04-ngon-tu-web.md` mục 9; đọc soát bằng mắt cả những màn chỉ hiện sau khi làm bài (kết quả, so sánh, đánh giá).
8. Bậc 4: khóa mô hình chỉ ở Secret Manager; prompt chỉ ở máy chủ, lên git chỉ khi đã mã hóa; danh tính người dùng không gửi cho mô hình; mọi đầu ra của mô hình qua rào chắn bằng mã trước khi tới người dùng.
9. Bậc 4: chưa có hạn mức chi (theo gói, theo ngày, trên Anthropic Console) thì chưa mở cho người dùng cuối.

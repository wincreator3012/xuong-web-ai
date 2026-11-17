# BÀI HỌC

Bài học đã chưng cất, mỗi dòng có nguồn (ngày, dự án hoặc thử nghiệm). Cách làm đúng từ nay đã sửa vào skill, chuan, khuôn, công cụ; ở đây giữ câu chuyện để hiểu vì sao. Thêm một dòng vào đúng chủ đề.

## An toàn dữ liệu

- 2026-10-07 (rà ba web-app cũ của tác giả xưởng) - Mã truy cập GitHub nằm trong địa chỉ remote của git; khoá Resend viết cứng trong mã trình duyệt và lưu ở tài liệu Firestore ai cũng đọc được; đáp án bài thi đóng gói vào mã gửi xuống máy thí sinh; Vercel và firebase.json đưa cả thư mục gốc (kế hoạch, biên bản họp) lên mạng. Sửa: web chỉ đưa `public/` lên; kiem-web quét khoá bí mật, tệp riêng trong `public/`, luật lỏng, dữ liệu đáp án; chuan/06 "trình duyệt là đất của người dùng". Chi tiết: nghien-cuu/E-bai-hoc-web-app.md.
- 2026-10-07 (nghiên cứu B, D) - Lỗ hổng lớn của ứng dụng làm cùng AI là thiếu luật bảo vệ (Lovable 2025, Tea 2025, Moltbook 2026). Sửa: khuôn app viết luật trước giao diện, có danh sách kiểm hai tài khoản.
- 2026-11-15 (web-app có trí năng nhân tạo) - Khóa Claude và các khóa khác được dán thẳng vào trò chuyện lúc dựng cho nhanh. Sửa: coi như đã lộ, tạo khóa mới, thay trong Secret Manager, xóa khóa cũ; chuan/10 mục 10.
- 2026-10-17 (dựng web-app tự đánh giá trên Firebase) - Bài tự đánh giá phản tư không có đáp án đúng sai nên tính điểm ngay trên trình duyệt để cả Khách (không đăng nhập) vẫn làm trọn bài và tải tệp về máy; nhưng khi trang quản trị xuất báo cáo Excel tổng hợp, phải tính lại điểm từ câu trả lời thô (`answers`) bằng đúng công thức gốc thay vì dùng trường `scores` đã lưu từ trình duyệt. Bộ quét khoá bí mật của `kiem-web` bắt mẫu `(apiKey|secret|password|mat_khau) : "..."` từ 12 ký tự trở lên: không đặt tên thuộc tính thông báo lỗi là `password: "..."` trong mã JS.

## Dựng và kiểm

- 2026-10-07 (thử khuôn site-astro) - Astro đổi dấu tự động trong Markdown: nháy thẳng thành nháy cong, ba chấm gõ tay thành ký tự ba chấm Unicode, vi phạm quy ước chữ; kiem-web bắt được. Sửa: `markdown.smartypants: false` trong khuôn.
- 2026-10-07 - Astro từ chối `site` không phải URL hợp lệ (`https://[[ten-mien]]`). Sửa: web-moi dùng `https://chua-dat-ten-mien.invalid` cho Astro; kiem-web nhận diện cả hai dạng là "chưa đặt tên miền".
- 2026-10-07 - Logo gốc của các thương hiệu nặng tới 400 KB, làm trang chậm. Sửa: web-moi thu logo về chiều cao 192 px (biểu tượng 512 px) khi chép vào web.
- 2026-10-07 - Thuộc tính `onsubmit`, `onclick` trong HTML bị chính sách bảo mật nội dung (`script-src 'self'`) chặn. Sửa: mọi hành vi gắn bằng tệp JS; khuôn không dùng thuộc tính sự kiện.
- 2026-10-07 - Hiệu ứng hiện dần làm axe-core đo sai tương phản (phần tử còn mờ). Sửa: kiem-web cho hiện hết `.hien` trước khi đo, chụp.
- 2026-10-07 - Sandbox đám mây chặn gstatic.com, img.vietqr.io: lỗi tải SDK Firebase là lỗi môi trường, không phải lỗi web. Sửa: kiem-web xếp lỗi tải tài nguyên ngoài vào CẢNH BÁO; app Firebase không ném lỗi khi chưa cấu hình hay mất mạng mà báo bằng chữ.
- 2026-10-07 - Tên riêng có học vị kèm họ tên bị nhận nhầm là Title Case. Sửa: chung.py bỏ qua chuỗi có học vị và tên khai trong brand.json.
- 2026-10-17 - Các lớp `.nut` (`display: inline-flex`), `.o` (`display: grid`) trong `nen.css` có độ ưu tiên cao hơn thuộc tính `[hidden]` mặc định của trình duyệt nên phần tử gắn `hidden` vẫn hiện trên ảnh chụp `kiem-web`. Sửa: thêm `[hidden] { display: none !important; }` vào `he-thong/nen.css`.
- 2026-10-17 - Cổng `kiem-web` coi mọi thẻ `<form>` có ô `email`, `ten`, `phone` là biểu mẫu thu thông tin khách hàng (đòi hỏi `.dong-y`, `.mat-ong`, `data-gui`). Với khung đăng nhập email/mật khẩu, đổi tên hồ sơ hay bộ lọc quản trị trong web-app, dùng `<div class="bieu-mau" role="group" aria-label="...">` kèm `<button type="button">` (mỗi ô nhập vẫn có `<label for="...">`). Với thanh chuyển thẻ `role="tablist"`, các nút con có `aria-selected` bắt buộc gắn `role="tab"` để đạt chuẩn `axe-core` WCAG 2.2 AA.
- 2026-10-17 - Chính sách bảo mật nội dung (`script-src 'self' https://www.gstatic.com https://apis.google.com`) của khuôn `app-firebase` chặn thư viện từ CDN lạ: vẽ biểu đồ (SVG và Canvas 2D), đóng gói PDF A4 nhiều trang từ Canvas và xuất tệp `.xlsx` nhiều sheet chuẩn OpenXML (ZIP STORE + CRC32) bằng mô-đun JS thuần trong `public/assets/js/` giúp trang nhẹ, không phụ thuộc bên thứ ba và qua thẳng cổng CSP.
- 2026-11-16 (web-app có trí năng nhân tạo) - Máy giả lập Firebase không gắn được hàm chạy nền theo Firestore khi máy làm việc có biến môi trường proxy. Sửa: chạy `firebase emulators:start` với proxy đã gỡ; Playwright vẫn đi qua proxy nhưng bỏ qua 127.0.0.1.
- 2026-11-17 (web-app có trí năng nhân tạo) - Playwright `text=` khớp chuỗi con không phân biệt hoa thường: bấm nhầm đoạn văn "mời bạn làm phần tổng kết" thay cho nút "Làm phần tổng kết"; `goto` tới địa chỉ chỉ khác phần sau dấu `#` không tải lại trang nên dữ liệu cũ vẫn hiện. Sửa: chọn theo thẻ (`button:has-text(...)`), dùng `reload()` khi cần dữ liệu mới.

## Ứng dụng có trí năng nhân tạo

- 2026-11-15 (web-app có trí năng nhân tạo) - Claude Sonnet 5.5, Opus 5.5 không nhận `tool_choice` ép công cụ; tiếng Việt tốn token gấp khoảng 3 lần ước lượng và phần suy nghĩ thích ứng ăn vào `max_tokens`, đầu ra bị cắt. Sửa: `output_config.format` (json_schema), `effort` theo từng lời gọi, đo lời gọi thật rồi đặt trần (chuan/10 mục 4).
- 2026-11-15 (web-app có trí năng nhân tạo) - Mô hình chép câu trích với kiểu đặt dấu thanh khác kiểu người học gõ, phép kiểm nguyên văn chấm sai. Sửa: chuẩn hóa kiểu đặt dấu khi so, tự sửa lời mô hình về kiểu cũ (chuan/10 mục 5).
- 2026-11-16 (web-app có trí năng nhân tạo) - Bảng mô thức gọi "lượt 1, lượt 2" trong khi người học không thấy số thứ tự này. Sửa: gửi kèm tên, ngày từng lượt và dặn mô hình gọi bằng tên (chuan/10 mục 4).
- 2026-11-16 (web-app có trí năng nhân tạo) - Lập bảng mô thức bằng Opus mất vài phút, quá sức một hàm gọi được và bắt người dùng chờ. Sửa: chạy nền theo Firestore, có khóa chống chạy trùng và mốc 20 phút coi là lỗi (chuan/10 mục 8).
- 2026-11-17 (web-app có trí năng nhân tạo) - Prompt là tài sản nhưng kho git cần đủ để máy dựng chạy. Sửa: mã hóa CMS bằng chứng chỉ công khai, khóa riêng ở Secret Manager, GitHub Actions giải mã trong lúc dựng (chuan/10 mục 6).
- 2026-11-17 (web-app có trí năng nhân tạo, đợt thử nghiệm) - Chủ dự án chốt: người tham gia thử nghiệm là người đồng kiến tạo, không phải người đánh giá; trang mời ẩn tự duyệt có số tài khoản tối đa và ngày đóng trang thay cho duyệt tay từng người, đội ngũ kiểm tra lại sau (chuan/10 mục 13).

## Chữ

- 2026-11-09 (web-app trắc nghiệm) - Chủ dự án hiệu đính 15 chỗ chữ của web-app sau khi đưa lên mạng: chuỗi nhãn nối bằng dấu hai chấm ở kết quả, khẩu ngữ rút gọn ở mô tả chia sẻ và ảnh chia sẻ, lối dịch từ tiếng Anh ("những gì được lưu", "nói rõ điều đó nghĩa là gì", "mức độ đúng"), từ mang nghĩa tốt đặt tên chiều đo quá tải ("Độ liền mạch"), câu tự hạ độ tin cậy ("ngưỡng là tạm thời"). Vài lỗi đã có luật từ trước ("đội ngũ" thay "đội", từ đơn âm cụt, "liền mạch" trong danh sách từ đẹp lời) mà vẫn sót, vì phần lớn chữ của web-app nằm trong JS nên kiem-web không quét, và Claude chỉ rà bằng mắt những màn đã chụp. Sửa: chuan/04 mục 9; kiem-web quét cả chuỗi chữ Việt trong tệp .js tự viết; chung.py bắt chuỗi nhãn hai chấm; tu-ngu.json thêm 9 mẫu. Chạy lại trên bản trước hiệu đính, kiem-web bắt được gần hết 15 chỗ đã sửa, và một chỗ còn sót ("Các ngưỡng này còn tạm thời" ở ghi chú cách phân mức trong ban-do.js).
- 2026-11-17 (web-app có trí năng nhân tạo) - Chủ dự án viết lại lời chào đợt thử nghiệm và vài câu hỏi góp ý vì còn giọng văn máy (câu đối xứng "không có cách dùng nào là sai", câu trấn an, chữ "khoảnh khắc", "chạm sâu"); máy soát chữ không bắt được kiểu lỗi này. Sửa: lời chào, lời mời, câu hỏi khảo sát luôn đọc to lại trước khi trình (chuan/10 mục 14).

## Nơi lưu trữ, dịch vụ

- 2026-10-07 (nghiên cứu A) - Vercel Hobby cấm thương mại theo nghĩa rộng (quảng bá bán dịch vụ cũng tính); Netlify Free từ 09/2025 tính theo tín dụng, hết là mọi web tạm dừng. Sửa: Cloudflare làm mặc định; dua-len cảnh báo khi đặt web thương mại lên Vercel, GitHub Pages.
- 2026-10-07 (nghiên cứu C) - Vercel đổi giá trị DNS cho dự án mới; Gmail bỏ "Send as" địa chỉ ngoài từ 01/2027; .edu.vn chỉ cho tổ chức giáo dục từ 10/02/2026. Sửa: thẻ huong-dan/06, 07, 08.
- 2026-10-17 - Khi dùng Antigravity (trợ lý AI của Google chạy trực tiếp trên máy), việc dựng và triển khai web-app lên các nền tảng của Google như Firebase (Firebase Hosting, Cloud Firestore, Firebase Authentication) rất liền mạch: sau một lần `firebase login`, trợ lý tự động tạo dự án, gắn tên miền `<mã-dự-án>.web.app`, bật API Firestore và Identity Toolkit, tạo cơ sở dữ liệu `asia-southeast1`, đăng ký ứng dụng web lấy cấu hình và chạy `firebase deploy` đưa cả luật, chỉ mục lẫn giao diện lên mạng; người dùng chỉ cần bật công tắc phương thức đăng nhập (Google, Email/Password) trong bảng điều khiển Firebase.
- 2026-11-15 đến 17 (web-app có trí năng nhân tạo) - Bốn cái bẫy khi đưa Cloud Functions lên: thiếu `https://<dự án>.web.app/__/auth/handler` trong redirect URI của cấu hình OAuth (Client ID); hàm lỗi ở lần tạo đầu không tự mở quyền gọi công khai (trình duyệt báo `internal`); lần đầu có hàm chạy nền theo Firestore, Eventarc cần vài phút cấp quyền; `firebase deploy --non-interactive` đòi giá trị mọi `defineString`. Sửa: chuan/10 mục 11.
- 2026-11-17 (web-app có trí năng nhân tạo) - GitHub Actions với Workload Identity Federation đưa web-app lên mỗi lần đẩy `main`, không giữ khóa tài khoản dịch vụ trên GitHub; gõ lệnh dài vào Cloud Shell qua trình duyệt từng làm treo thẻ, nên Cloud Shell chỉ còn là đường dự phòng chạy một tập lệnh. Sửa: chuan/07 mục 2, chuan/10 mục 11.

## Tổ chức xưởng

- 2026-10-07 (dựng xưởng) - Theo mẫu Xưởng thiết kế Claude: repo chỉ năng lực; hồ sơ ở `Du an/`, mã nguồn web ở `Web/` (mỗi web một kho git riêng, khác với "Thanh pham" của xưởng thiết kế vì web là thứ sống, sửa mãi); phong cách của người dùng tạo từ bản `*.mau.*` ở bước cài, nằm ngoài git chung, để cập nhật xưởng không đụng tới.

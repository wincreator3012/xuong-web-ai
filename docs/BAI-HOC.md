# BÀI HỌC

Bài học đã chưng cất, mỗi dòng có nguồn (ngày, dự án hoặc thử nghiệm). Cách làm đúng từ nay đã sửa vào skill, chuan, khuôn, công cụ; ở đây giữ câu chuyện để hiểu vì sao. Thêm một dòng vào đúng chủ đề.

## An toàn dữ liệu

- 2026-10-07 (rà ba web-app cũ của tác giả xưởng) - Mã truy cập GitHub nằm trong địa chỉ remote của git; khoá Resend viết cứng trong mã trình duyệt và lưu ở tài liệu Firestore ai cũng đọc được; đáp án bài thi đóng gói vào mã gửi xuống máy thí sinh; Vercel và firebase.json đưa cả thư mục gốc (kế hoạch, biên bản họp) lên mạng. Sửa: web chỉ đưa `public/` lên; kiem-web quét khoá bí mật, tệp riêng trong `public/`, luật lỏng, dữ liệu đáp án; chuan/06 "trình duyệt là đất của người dùng". Chi tiết: nghien-cuu/E-bai-hoc-web-app.md.
- 2026-10-07 (nghiên cứu B, D) - Lỗ hổng lớn của ứng dụng làm cùng AI là thiếu luật bảo vệ (Lovable 2025, Tea 2025, Moltbook 2026). Sửa: khuôn app viết luật trước giao diện, có danh sách kiểm hai tài khoản.

## Dựng và kiểm

- 2026-10-07 (thử khuôn site-astro) - Astro đổi dấu tự động trong Markdown: nháy thẳng thành nháy cong, ba chấm gõ tay thành ký tự ba chấm Unicode, vi phạm quy ước chữ; kiem-web bắt được. Sửa: `markdown.smartypants: false` trong khuôn.
- 2026-10-07 - Astro từ chối `site` không phải URL hợp lệ (`https://[[ten-mien]]`). Sửa: web-moi dùng `https://chua-dat-ten-mien.invalid` cho Astro; kiem-web nhận diện cả hai dạng là "chưa đặt tên miền".
- 2026-10-07 - Logo gốc của các thương hiệu nặng tới 400 KB, làm trang chậm. Sửa: web-moi thu logo về chiều cao 192 px (biểu tượng 512 px) khi chép vào web.
- 2026-10-07 - Thuộc tính `onsubmit`, `onclick` trong HTML bị chính sách bảo mật nội dung (`script-src 'self'`) chặn. Sửa: mọi hành vi gắn bằng tệp JS; khuôn không dùng thuộc tính sự kiện.
- 2026-10-07 - Hiệu ứng hiện dần làm axe-core đo sai tương phản (phần tử còn mờ). Sửa: kiem-web cho hiện hết `.hien` trước khi đo, chụp.
- 2026-10-07 - Sandbox đám mây chặn gstatic.com, img.vietqr.io: lỗi tải SDK Firebase là lỗi môi trường, không phải lỗi web. Sửa: kiem-web xếp lỗi tải tài nguyên ngoài vào CẢNH BÁO; app Firebase không ném lỗi khi chưa cấu hình hay mất mạng mà báo bằng chữ.
- 2026-10-07 - Tên riêng có học vị kèm họ tên bị nhận nhầm là Title Case. Sửa: chung.py bỏ qua chuỗi có học vị và tên khai trong brand.json.

## Nơi lưu trữ, dịch vụ

- 2026-10-07 (nghiên cứu A) - Vercel Hobby cấm thương mại theo nghĩa rộng (quảng bá bán dịch vụ cũng tính); Netlify Free từ 09/2025 tính theo tín dụng, hết là mọi web tạm dừng. Sửa: Cloudflare làm mặc định; dua-len cảnh báo khi đặt web thương mại lên Vercel, GitHub Pages.
- 2026-10-07 (nghiên cứu C) - Vercel đổi giá trị DNS cho dự án mới; Gmail bỏ "Send as" địa chỉ ngoài từ 01/2027; .edu.vn chỉ cho tổ chức giáo dục từ 10/02/2026. Sửa: thẻ huong-dan/06, 07, 08.

## Tổ chức xưởng

- 2026-10-07 (dựng xưởng) - Theo mẫu Xưởng thiết kế Claude: repo chỉ năng lực; hồ sơ ở `Du an/`, mã nguồn web ở `Web/` (mỗi web một kho git riêng, khác với "Thanh pham" của xưởng thiết kế vì web là thứ sống, sửa mãi); phong cách của người dùng tạo từ bản `*.mau.*` ở bước cài, nằm ngoài git chung, để cập nhật xưởng không đụng tới.

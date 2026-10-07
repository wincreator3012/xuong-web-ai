# Nghiên cứu gốc của xưởng web

Năm báo cáo làm nền cho mọi chuẩn trong `chuan/`. Mỗi dữ kiện có nguồn và ngày kiểm (07/10/2026); chỗ chưa chắc được đánh dấu ngay trong báo cáo. Chuẩn chỉ giữ phần đã chưng cất; khi một quyết định cần lý lẽ hay số liệu gốc, đọc báo cáo tương ứng.

| Báo cáo | Câu hỏi | Kết luận chính đã đưa vào chuẩn |
|---|---|---|
| `nghien-cuu/A-hosting.md` | Đặt web ở đâu? | Cloudflare (Workers, tệp tĩnh) làm mặc định: miễn phí, được dùng thương mại, băng thông tệp tĩnh không giới hạn, có máy chủ ở Hà Nội và TP.HCM. Vercel Hobby cấm thương mại. Netlify Free tính theo tín dụng, hết là mọi web tạm dừng. Firebase Hosting cho web-app Firebase. |
| `nghien-cuu/B-du-lieu-dich-vu.md` | Thêm biểu mẫu, dữ liệu, đăng nhập, thanh toán thế nào cho người không chuyên? | Web3Forms hoặc Tally cho biểu mẫu; Apps Script khi cần ghi thẳng Google Sheets; Firebase Spark khi thật cần đăng nhập; VietQR có mã đơn, SePay đối soát; Pages CMS cho người biên tập; Astro 7 cho web nhiều trang. Bốn vụ lộ dữ liệu của ứng dụng làm cùng AI. |
| `nghien-cuu/C-ten-mien-email-phap-ly.md` | Những việc người dùng phải tự tay làm, và pháp lý Việt Nam | .vn mua qua nhà đăng ký trong nước, khai số định danh; .edu.vn chỉ cho tổ chức giáo dục từ 10/02/2026; Vercel đổi giá trị DNS; Gmail bỏ "Send as" từ 01/2027; Luật Bảo vệ dữ liệu cá nhân 91/2025 và Nghị định 356/2025; Luật Thương mại điện tử 122/2025. |
| `nghien-cuu/D-loai-web-quy-trinh-chuan.md` | Người dùng hay cần loại web nào, tư vấn ra sao, chuẩn chất lượng 2026, làm web cùng AI thế nào cho đúng | 12 loại web, 4 bậc hạ tầng, 15 câu hỏi brief, cây quyết định "giải pháp đơn giản nhất"; Core Web Vitals, WCAG 2.2 AA, OG cho Zalo; AGENTS.md ngắn; năm cụm giao diện "văn AI"; bộ kiểm tự động Playwright, axe-core. |
| `nghien-cuu/E-bai-hoc-web-app.md` | Ba web-app Firebase thật, do một người không chuyên lập trình làm cùng AI, dạy gì? | Lá chắn trình duyệt Zalo/Facebook, luật Firestore kiểm từng trường; và các lỗ hổng (khoá trong mã, đáp án gửi xuống trình duyệt, đưa cả thư mục gốc lên mạng) thành cổng kiểm tự động. |

Giá, hạn mức miễn phí và giao diện các dịch vụ đổi nhanh. Trước khi tư vấn một con số cho người dùng, mở lại nguồn (đường dẫn có trong `chuan/kho-dich-vu.json`), và cập nhật báo cáo khi thấy khác.

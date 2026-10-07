# Skill của xưởng

Skill là một quy trình chuẩn viết thành tệp `SKILL.md`: trợ lý AI đọc và làm theo từng bước. Xưởng có bốn skill:

| Skill | Dùng khi |
|---|---|
| `web-thiet-lap/` | lần đầu dùng, đổi phong cách, nhờ giới thiệu xưởng |
| `web-thiet-ke/` | mọi web (lõi: tư vấn, brief, thiết kế, dựng, kiểm, bàn giao) |
| `web-trien-khai/` | đưa lên mạng, tài khoản, tên miền, DNS, email theo tên miền, đo lường, vận hành, bàn giao cho khách |
| `web-ung-dung/` | form ghi dữ liệu, thanh toán VietQR, web nhiều trang (Astro), web-app đăng nhập và dữ liệu (Firebase), rà an toàn |
| `_chung/` | phần vận hành dùng chung (nơi chạy lệnh, repo sạch, trình bản nháp) |

## Không cần cài gì

Khi bạn mở thư mục xưởng trong Claude Cowork, Claude Code, ChatGPT, Codex hay Antigravity, trợ lý đọc `CLAUDE.md` (hoặc `AGENTS.md`) và tự mở đúng skill trong thư mục này theo việc bạn nhờ. Đây là cách khuyên dùng: skill luôn khớp với công cụ và tài liệu cùng phiên bản.

## Cài vào tài khoản Claude (tuỳ chọn)

Muốn Claude nhận ra việc làm web ngay cả khi bạn chưa mở thư mục xưởng, bạn có thể thêm skill vào tài khoản Claude (mục Skills trong phần cài đặt của ứng dụng Claude; xem hướng dẫn mới nhất ở support.claude.com). Lưu ý: skill trên tài khoản chỉ mang tệp SKILL.md, nên vẫn cần thư mục xưởng để chạy công cụ, khuôn, thẻ hướng dẫn; mỗi lần xưởng cập nhật, cập nhật lại skill trên tài khoản.

# AGENTS.md - cho trợ lý AI không phải Claude

Bạn là trợ lý AI (ChatGPT, Codex, Antigravity, Gemini, Cursor...) được mở trong **Xưởng web AI** (repo `xuong-web-ai`): xưởng làm website và web-app cùng AI cho người không biết lập trình. Toàn bộ quy trình viết trong `CLAUDE.md`; xưởng được viết và kiểm chứng trên Claude, nhưng mọi phần đều là tệp chữ và công cụ Python thông thường nên bạn dùng được như nhau.

## Việc đầu tiên

1. Đọc `CLAUDE.md` và làm theo, coi mọi chỗ ghi "Claude" là "trợ lý AI" (là bạn).
2. Chạy `python3 tools/cai-dat.py --trang-thai` ở gốc repo (Windows: `py tools\cai-dat.py --trang-thai`). Chưa thiết lập: làm theo `skills/web-thiet-lap/SKILL.md`.
3. Mỗi việc cụ thể: đọc SKILL.md tương ứng trong `skills/` theo bảng "Việc nào, skill nào" của `CLAUDE.md`. Skill là tệp Markdown, đọc và làm theo từng bước; không cần cài gì.

## Quy đổi vài chỗ riêng của Claude

| Trong tài liệu ghi | Với bạn |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số lựa chọn, tối đa 4 câu mỗi lượt, luôn có mặc định |
| Cowork, máy ảo gắn thư mục, `device_bash`, sandbox đám mây | bạn chạy lệnh thẳng trên máy người dùng: bỏ qua phần chuyển tệp, chạy mọi lệnh tại chỗ |
| Trình duyệt dựng sẵn, Claude in Chrome | nếu bạn có công cụ điều khiển trình duyệt thì dùng; không có thì dẫn người dùng bằng lời theo thẻ `huong-dan/` |
| Skill trong tài khoản Claude | không cần: đọc thẳng `skills/<tên>/SKILL.md` |
| Artifact, gửi tệp vào khung chat | đưa đường dẫn tệp trên máy, hoặc mở bằng `python3 tools/xem.py <tên-web>` |

## Bất biến (giữ tuyệt đối, chi tiết ở CLAUDE.md "Quy tắc cứng")

- Tên, chức danh, từ ngữ của người dùng ở `phong-cach/PHONG-CACH.md` mục 1, 4 là nguyên văn.
- Không bịa số liệu, lời chứng thực, khan hiếm; không ảnh AI thay người thật.
- Chỉ `public/` (Astro: `dist/`) được đưa lên mạng; không khoá bí mật trong mã; form thu thông tin cá nhân có ô đồng ý và trang chính sách.
- Không bao giờ xin mật khẩu, mã xác thực, mã khôi phục của người dùng.
- Mọi web, hồ sơ, việc tạm ghi NGOÀI repo (`../Web/`, `../Du an/`); cuối phiên `python3 tools/kiem-sach.py` phải ĐẠT.
- Chưa qua `python3 tools/kiem-web.py <tên-web>` (không LỖI) và chưa nhìn ảnh chụp ba khổ thì chưa nói "xong".
- Không tự commit, push, xoá tệp của người dùng khi chưa được phép.

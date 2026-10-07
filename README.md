# Xưởng web AI

Xưởng làm website và web-app cùng trợ lý AI (Claude, ChatGPT, Codex, Antigravity...) dành cho chuyên gia, giảng viên, diễn giả, nhà chuyên môn và tổ chức nhỏ không biết lập trình. Bạn nói nhu cầu bằng lời thường; trợ lý tư vấn giải pháp đơn giản nhất đủ dùng, thiết kế theo phong cách của bạn, dựng, tự kiểm bằng máy, đưa lên mạng, và dẫn bạn từng bước ở những việc chỉ chủ web làm được (tạo tài khoản, mua tên miền, cấp quyền).

Làm được: trang một trang, hồ sơ cá nhân, trang liên kết cho tiểu sử mạng xã hội, thư viện tra cứu, trắc nghiệm tự soi chiếu, trang đích khoá học, sự kiện có form đăng ký và mã chuyển khoản VietQR, trang báo giá gửi link riêng, web nhiều trang có blog (Astro), web-app có đăng nhập Google và dữ liệu (Firebase).

## Bắt đầu

- **Người mới**: đọc [BAT-DAU.md](BAT-DAU.md) (10 phút đọc, 30-60 phút làm theo). Bạn gần như không phải gõ lệnh nào.
- **Dùng hằng ngày**: [HUONG-DAN.md](HUONG-DAN.md).
- **Trợ lý AI**: đọc `CLAUDE.md` (Claude) hoặc `AGENTS.md` (trợ lý khác).

## Xưởng khác gì một lời nhắc "làm cho tôi cái web"

- **Phong cách của bạn, giữ đều trên mọi web.** Tên, chức danh nguyên văn, màu, logo, liên hệ, từ ngữ bạn dùng và từ bạn không bao giờ dùng được thiết lập một lần, áp cho mọi trang.
- **Tư vấn trước khi dựng.** 15 câu hỏi lập bản tóm tắt yêu cầu [brief], bốn bậc hạ tầng (từ trang tĩnh tới web-app có dữ liệu), cây quyết định chọn giải pháp rẻ và bền nhất; nói thẳng khi bạn chưa cần web.
- **Chưa qua cổng kiểm thì chưa báo xong.** Máy chụp web ở ba khổ (điện thoại, máy tính bảng, máy tính), đo tràn chữ, tương phản, khả năng tiếp cận (axe-core, WCAG 2.2 AA), độ nặng trang, chữ văn AI, Title Case, khoá bí mật lọt vào mã, luật dữ liệu lỏng, form thiếu ô đồng ý.
- **Thẻ hướng dẫn cho mọi việc bạn tự tay làm**: GitHub, Cloudflare, Vercel, Netlify, Firebase, mua tên miền .vn hoặc .com, trỏ DNS, email theo tên miền, form ghi Google Sheets, VietQR, đo lượt xem, bàn giao web cho khách.
- **Chuẩn pháp lý Việt Nam cho web nhỏ** (cập nhật 10/2026): Luật Bảo vệ dữ liệu cá nhân 2025 và Nghị định 356/2025, thương mại điện tử, thông tin chủ quản ở chân trang. Là tài liệu tham khảo, không phải tư vấn pháp lý.
- **Nơi lưu trữ chọn bằng nghiên cứu**, không theo thói quen: mặc định Cloudflare (miễn phí, cho phép thương mại, có điểm phục vụ ở Hà Nội và TP.HCM); Vercel, Netlify, Firebase, GitHub Pages khi hợp hơn. Bảng so sánh và lý do ở `chuan/07-trien-khai.md`, `nghien-cuu/A-hosting.md`.

## Cấu trúc

```
CLAUDE.md, AGENTS.md      điểm vào cho trợ lý AI
BAT-DAU.md, HUONG-DAN.md  cho người dùng: cài lần đầu, dùng hằng ngày
phong-cach/               phong cách của bạn (tạo ở bước cài từ bản *.mau.*)
brand/                    chủ đề màu web theo vai (6 chủ đề khởi đầu), thương hiệu, nhân vật, liên hệ, logo
chuan/                    9 chuẩn nghề: tư vấn, loại web, thiết kế, chữ, kỹ thuật, dữ liệu, triển khai, pháp lý, nghiệm thu
huong-dan/                13 thẻ dẫn từng bước những việc chủ web tự tay làm
khuon/                    9 khuôn web, 3 tầng kỹ thuật (HTML tĩnh, Astro 7, Firebase)
he-thong/                 nền chung (nen.css, nen.js), mẫu hồ sơ dự án, tệp kèm web, trang dùng chung
fonts/                    Lora, Playfair Display, Be Vietnam Pro (tự lưu trữ, đủ dấu tiếng Việt)
tools/                    cai-dat, web-moi, kiem-web, anh-chia-se, dua-len, xem, tuong-phan, kiem-sach, kiem-tai-lieu
skills/                   4 skill: web-thiet-lap, web-thiet-ke, web-trien-khai, web-ung-dung
nghien-cuu/               báo cáo nghiên cứu gốc (10/2026): nơi lưu trữ, dữ liệu, tên miền, pháp lý, quy trình chuẩn
docs/                     quy trình kỹ thuật, bài học, cập nhật và đóng góp
```

Web và hồ sơ của bạn nằm NGOÀI repo, cạnh nó: `Web/` (mã nguồn từng web) và `Du an/` (brief, kế hoạch, hồ sơ vận hành, báo cáo kiểm). Nhờ vậy cập nhật xưởng không đụng tới web nào của bạn.

## Cần gì

Một máy Mac hoặc Windows, Python 3.9 trở lên, một ứng dụng AI làm việc được với thư mục trên máy (khuyên dùng Claude Desktop ở chế độ Cowork). Node.js chỉ cần khi làm web nhiều trang (Astro) hoặc đưa web lên từ máy. Các tài khoản miễn phí (GitHub, Cloudflare...) tạo khi cần, có thẻ hướng dẫn.

## Xưởng anh em

Cùng tác giả, cùng cách làm: **Xưởng thiết kế Claude** (repo `xuong-thiet-ke-ai`) làm ấn phẩm ảnh, đồ in, sơ đồ tri thức. Ảnh chia sẻ, sơ đồ đẹp cho web có thể làm ở đó rồi chép sang; hai xưởng có sáu họ màu cùng tên, cùng tinh thần, và cùng quy ước chữ.

## Tác giả, giấy phép

Xưởng do nhà giáo dục Lương Dũng Nhân (ldn.edu.vn) tạo ra và chia sẻ miễn phí. Mã nguồn theo MIT (`LICENSE`), tài liệu theo CC BY 4.0 (`LICENSE-TAI-LIEU.md`), cách ghi công ở `GHI-CONG.md`. Thành phần bên thứ ba: phông chữ SIL OFL 1.1, axe-core của Deque Systems (MPL 2.0). Cập nhật và đóng góp: `docs/DONG-GOP.md`.

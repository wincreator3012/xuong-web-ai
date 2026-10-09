# Xưởng web AI: bản vẽ để trợ lý AI dựng xưởng web riêng cho bạn

Xưởng làm website và web-app cùng trợ lý AI (Claude, ChatGPT, Codex, Antigravity...) dành cho chuyên gia, giảng viên, diễn giả, nhà chuyên môn và tổ chức nhỏ không biết lập trình. Bạn nói nhu cầu bằng lời thường; trợ lý tư vấn giải pháp đơn giản nhất đủ dùng, thiết kế theo phong cách của bạn, dựng, tự kiểm bằng máy, đưa lên mạng, và dẫn bạn từng bước ở những việc chỉ chủ web làm được (tạo tài khoản, mua tên miền, cấp quyền).

Làm được: trang một trang, hồ sơ cá nhân, trang liên kết cho tiểu sử mạng xã hội, thư viện tra cứu, trắc nghiệm tự soi chiếu, trang đích khoá học, sự kiện có form đăng ký và mã chuyển khoản VietQR, trang báo giá gửi link riêng, web nhiều trang có blog (Astro), web-app có đăng nhập Google và dữ liệu (Firebase).

## Đây là bản vẽ, không phải phần mềm để tải về

Trang GitHub này (gọi là repo) là **bản vẽ** [blueprint]. Bạn không cần bấm nút xanh **Code** hay **Download ZIP**, không cần tải về, không cần `git clone`, không cần biết GitHub. Bạn đưa đường dẫn bản vẽ cho trợ lý AI của mình; trợ lý đọc bản vẽ, hỏi bạn vài lượt, rồi tự dựng trên máy bạn **một xưởng riêng**:

- phần năng lực (công cụ, khuôn web, chuẩn nghề, thẻ hướng dẫn) giống hệt bản vẽ, được trợ lý chép nguyên vẹn và tự kiểm bằng máy;
- phần phong cách (tên, chức danh, màu, logo, liên hệ, giọng chữ) là của bạn, hỏi từ chính bạn;
- một **bộ skill riêng** mang cấu hình của bạn, để bạn lưu vào tài khoản AI (mục "Skill riêng" bên dưới).

Xưởng dựng xong không nối với bản vẽ: không có gì tự đổi sau lưng bạn. Khi bản vẽ có bản mới, bạn nói "cập nhật xưởng"; trợ lý đọc nhật ký thay đổi (`CHANGELOG.md`), kể bạn nghe điều gì mới, rồi áp những gì bạn đồng ý.

## Bắt đầu bằng một câu

Mở ứng dụng AI làm việc được với thư mục trên máy (khuyên dùng Claude Desktop ở chế độ Cowork), gắn một thư mục trống tên "Web AI", rồi nói:

> Đọc bản vẽ xưởng web ở https://github.com/wincreator3012/xuong-web-ai (bắt đầu từ AGENTS.md) rồi dựng xưởng web riêng cho tôi trong thư mục Web AI.

Từng bước cho người mới hoàn toàn, kể cả cài ứng dụng và xử lý khi có gì lạ: [BAT-DAU.md](BAT-DAU.md) (10 phút đọc, 45-75 phút làm theo, phần lớn là chờ máy).

## Ba cửa vào

- **Bạn, người dùng**: tệp này và [BAT-DAU.md](BAT-DAU.md). Sau khi có xưởng, việc hằng ngày ở `HUONG-DAN.md` trong xưởng của bạn.
- **Trợ lý AI**: [AGENTS.md](AGENTS.md) trước tiên (`CLAUDE.md`, `GEMINI.md` đều trỏ về đó), rồi [DUNG-XUONG.md](DUNG-XUONG.md) và danh mục `BAN-DUNG.json`.
- **Người đóng góp**: [docs/DONG-GOP.md](docs/DONG-GOP.md).

## Bạn sẽ có gì trên máy

```
Web AI/
  xuong-web-ai/   xưởng của bạn: năng lực từ bản vẽ + phong cách của bạn (không phải bản sao git)
  Du an/          hồ sơ từng dự án (brief, kế hoạch, báo cáo kiểm, hồ sơ vận hành); Du an/_skill/: gói skill riêng
  Web/            mã nguồn từng web, về sau mỗi web là một kho GitHub riêng của bạn
```

## Skill riêng cho tài khoản AI của bạn

Skill là một quy trình đã kiểm chứng, viết thành tệp chữ để trợ lý mở ra đúng lúc: khi bạn nói "làm trang đăng ký khoá học", trợ lý đi đúng các bước của xưởng thay vì nghĩ lại từ đầu. Khi dựng xưởng, trợ lý đóng gói bốn skill (`xuong-web-thiet-lap`, `xuong-web-thiet-ke`, `xuong-web-trien-khai`, `xuong-web-ung-dung`) mang tên bạn, cách trợ lý gọi bạn, thư mục làm việc và bản chụp phong cách của bạn, rồi dẫn bạn lưu chúng vào tài khoản (với Claude: Customize > Skills > + > Create skill > Upload a skill). Từ đó trợ lý nhận ra việc làm web ở mọi cuộc trò chuyện, kể cả khi bạn đang ở điện thoại. Giải thích đầy đủ, từng bước cho từng nền tảng, gỡ rối: [skills/README.md](skills/README.md).

## Xưởng khác gì một lời nhắc "làm cho tôi cái web"

- **Phong cách của bạn, giữ đều trên mọi web.** Tên, chức danh nguyên văn, màu, logo, liên hệ, từ ngữ bạn dùng và từ bạn không bao giờ dùng được thiết lập một lần, áp cho mọi trang.
- **Tư vấn trước khi dựng.** 15 câu hỏi lập bản tóm tắt yêu cầu [brief], bốn bậc hạ tầng (từ trang tĩnh tới web-app có dữ liệu), cây quyết định chọn giải pháp rẻ và bền nhất; nói thẳng khi bạn chưa cần web.
- **Chưa qua cổng kiểm thì chưa báo xong.** Máy chụp web ở ba khổ (điện thoại, máy tính bảng, máy tính), đo tràn chữ, tương phản, khả năng tiếp cận (axe-core, WCAG 2.2 AA), độ nặng trang, chữ văn AI, Title Case, khoá bí mật lọt vào mã, luật dữ liệu lỏng, form thiếu ô đồng ý.
- **Thẻ hướng dẫn cho mọi việc bạn tự tay làm**: GitHub, Cloudflare, Vercel, Netlify, Firebase, mua tên miền .vn hoặc .com, trỏ DNS, email theo tên miền, form ghi Google Sheets, VietQR, đo lượt xem, bàn giao web cho khách.
- **Chuẩn pháp lý Việt Nam cho web nhỏ** (cập nhật 10/2026): Luật Bảo vệ dữ liệu cá nhân 2025 và Nghị định 356/2025, thương mại điện tử, thông tin chủ quản ở chân trang. Là tài liệu tham khảo, không phải tư vấn pháp lý.
- **Nơi lưu trữ chọn bằng nghiên cứu**, không theo thói quen: mặc định Cloudflare (miễn phí, cho phép thương mại, có điểm phục vụ ở Hà Nội và TP.HCM); Vercel, Netlify, Firebase, GitHub Pages khi hợp hơn. Bảng so sánh và lý do ở `chuan/07-trien-khai.md`, `nghien-cuu/A-hosting.md`.

## Bản vẽ gồm gì (dành cho trợ lý AI và người tò mò)

```
AGENTS.md, CLAUDE.md, GEMINI.md   cửa vào cho trợ lý AI (hai tệp sau trỏ về AGENTS.md)
DUNG-XUONG.md                     quy trình dựng, cập nhật, gỡ rối (cho trợ lý)
BAN-DUNG.json                     danh mục từng tệp: chép vào xưởng, mẫu để điền, hay chỉ ở bản vẽ; vân tay sha256
CHANGELOG.md                      nhật ký thay đổi: trợ lý đọc khi cập nhật xưởng của bạn
README.md, BAT-DAU.md             cho người dùng ở bản vẽ
mau-xuong/                        mẫu điểm vào của xưởng được dựng (CLAUDE.md, AGENTS.md, XUONG.json)
HUONG-DAN.md                      hướng dẫn dùng hằng ngày (được chép vào xưởng)
phong-cach/, brand/               bản khởi đầu *.mau.* để tạo phong cách của bạn; 6 chủ đề màu web
chuan/                            9 chuẩn nghề: tư vấn, loại web, thiết kế, chữ, kỹ thuật, dữ liệu, triển khai, pháp lý, nghiệm thu
huong-dan/                        13 thẻ dẫn từng bước những việc chủ web tự tay làm
khuon/                            9 khuôn web, 3 tầng kỹ thuật (HTML tĩnh, Astro 7, Firebase)
he-thong/                         nền chung (nen.css, nen.js), mẫu hồ sơ dự án, tệp kèm web, trang dùng chung
fonts/                            Lora, Playfair Display, Be Vietnam Pro (tự lưu trữ, đủ dấu tiếng Việt)
tools/                            ban-dung, cai-dat, web-moi, kiem-web, anh-chia-se, dua-len, xem, tuong-phan, kiem-sach,
                                  kiem-tai-lieu, dong-goi-skill
skills/                           4 skill nguồn và hướng dẫn skill (skills/README.md)
nghien-cuu/                       báo cáo nghiên cứu gốc (10/2026): nơi lưu trữ, dữ liệu, tên miền, pháp lý, quy trình chuẩn
docs/                             quy trình kỹ thuật, bài học, đóng góp
```

## Cần gì

Một máy Mac hoặc Windows, Python 3.9 trở lên (trợ lý hướng dẫn cài nếu thiếu), một ứng dụng AI làm việc được với thư mục trên máy và có mạng để đọc bản vẽ. Node.js chỉ cần khi làm web nhiều trang (Astro) hoặc đưa web lên từ máy. Các tài khoản miễn phí (GitHub, Cloudflare...) tạo khi cần, có thẻ hướng dẫn.

## Xưởng anh em

Cùng tác giả, cùng cách làm: **Xưởng thiết kế Claude** (repo `xuong-thiet-ke-ai`) làm ấn phẩm ảnh, đồ in, sơ đồ tri thức. Ảnh chia sẻ, sơ đồ đẹp cho web có thể làm ở đó rồi chép sang; hai xưởng có sáu họ màu cùng tên, cùng tinh thần, và cùng quy ước chữ.

## Tác giả, giấy phép

Xưởng do nhà giáo dục Lương Dũng Nhân (ldn.edu.vn) tạo ra và chia sẻ miễn phí. Mã nguồn theo MIT (`LICENSE`), tài liệu theo CC BY 4.0 (`LICENSE-TAI-LIEU.md`), cách ghi công ở `GHI-CONG.md`. Thành phần bên thứ ba: phông chữ SIL OFL 1.1, axe-core của Deque Systems (MPL 2.0). Cập nhật lần cuối: 09/10/2026 (`CHANGELOG.md`).

Trang web đầu tiên bạn muốn người xem mở ra, sau khi có xưởng, sẽ nói thay bạn điều gì?

# Nhật ký thay đổi của bản vẽ

Trợ lý AI đọc tệp này khi người dùng nói "cập nhật xưởng": từ phiên bản ghi trong `XUONG.json` của xưởng tới bản mới nhất, để kể bằng lời thường điều gì mới và điều gì sẽ đổi. Mỗi mục ghi: phiên bản (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng, dữ kiện đã kiểm chứng lại.

## 2026.11.25

Bổ sung chuẩn giao diện và trải nghiệm từ lần học một bộ bàn giao thiết kế.

- **`chuan/11-giao-dien-trai-nghiem.md`**: mục 4 thêm 4 mẫu dùng lại (khung xương khi tải và báo mạng chậm sau 6 giây; băng mất kết nối trong đầu màn; 3 trang lỗi; cách phân biệt lỗi mạng với lỗi máy chủ của Firebase); mục 9 thêm hộp xác nhận nói rõ hệ quả trước việc tiêu hạn mức hay chia sẻ (câu chữ phải khớp mã) và viên chặng nổi; mục 10 thêm kiểm theme tối, mất mạng, mạng chậm; mục 11 mới về bộ token, thẻ không viền, theme tối, nhận diện chương trình và đơn vị chủ quản, phông tự lưu trữ; mục 12 mới về cách nhận bộ bàn giao thiết kế (Claude Design, Figma).
- **Skill**: `web-thiet-ke` làm theo chuan/11 mục 12 khi nhận bản mẫu hay bộ bàn giao, chụp kiểm cả theme tối và mất mạng; `web-ung-dung` dựng giao diện theo mục 4 và 11.
- **`docs/BAI-HOC.md`**: thêm 4 bài học về bộ bàn giao thiết kế, nhận diện, kiểm câu chữ với mã, kiểm bằng Playwright.

Việc trợ lý cần làm trong xưởng đã dựng: chép `chuan/11-giao-dien-trai-nghiem.md`, hai skill đã đổi; đóng gói lại `web-thiet-ke` và `web-ung-dung` bằng `python3 tools/dong-goi-skill.py` rồi hướng dẫn người dùng tải lại lên tài khoản AI.

## 2026.11.24

Thêm chuẩn giao diện và trải nghiệm cho web-app, kèm tổng quan tài liệu làm nền.

- **Chuẩn mới `chuan/11-giao-dien-trai-nghiem.md`**: cho web-app, công cụ nhiều bước, trắc nghiệm, ứng dụng có trí năng nhân tạo. Gồm: tinh thần (giao diện phục vụ suy nghĩ của người dùng, không giữ chân họ), hành trình và danh sách trạng thái, bố cục theo khổ màn hình (thanh bên từ 1024 px, khung phụ từ 1280 px, ngăn kéo trên điện thoại), luồng nhiều bước (tiến trình luôn hiện, từng ô một, thu gọn bước đã xong, lưu nháp và nói ra, chỉ bổ sung chứ không sửa đè lời đã gửi khi lời ấy là dữ liệu tư duy), phản hồi và chờ đợi theo ba ngưỡng 0,1, 1, 10 giây, giao diện có trí năng nhân tạo (người dùng nghĩ trước, máy soi sau; giọng máy tách khỏi lời người dùng; mỗi nhận xét kèm căn cứ), ma sát có chủ đích, an lành và an toàn tâm lý, danh sách cấm theo năm chiến lược mẫu lừa, chi tiết thực thi, kiểm.
- **Báo cáo mới `nghien-cuu/G-giao-dien-trai-nghiem.md`**: tổng quan 22 nguồn theo bảy cụm (khả dụng và thời gian chờ, tải nhận thức, bố cục đáp ứng và điều hướng, tương tác người và trí năng nhân tạo, phản tư và ma sát có chủ đích, động lực và an lành, đạo đức thiết kế), kèm ca thay giao diện một web-app phản tư và các chỗ vấp khi dựng.
- **Nối vào chuẩn và skill**: `chuan/03`, `chuan/09`, `chuan/10` trỏ sang chuan/11; skill `web-thiet-ke` thêm bước lập hành trình, trạng thái, bố cục cho web-app và tách giao diện khỏi đổi luồng khi nhận bản mẫu; skill `web-ung-dung` dựng giao diện theo chuan/11 và nói rõ ngoại lệ chấm điểm trên trình duyệt chỉ dành cho bài tự đánh giá phản tư; skill `web-trien-khai` nhận thêm lời gọi "đưa lên tự động bằng GitHub Actions". `docs/BAI-HOC.md` thêm mục "Giao diện và trải nghiệm".
- **Công cụ**: `tools/kho_tu_lieu.py` mới (tìm kho tư liệu dùng chung nếu có, không có thì dùng `brand/` của repo); `tools/chung.py`, `tools/web-moi.py`, `tools/kiem-tai-lieu.py`, `tools/dong-goi-skill.py` cập nhật theo.

Việc trợ lý cần làm trong xưởng đã dựng: chép `chuan/11-giao-dien-trai-nghiem.md`, `nghien-cuu/G-giao-dien-trai-nghiem.md`, các chuẩn và công cụ đã đổi; đóng gói lại hai skill `web-thiet-ke` và `web-ung-dung` bằng `python3 tools/dong-goi-skill.py` rồi hướng dẫn người dùng tải lại lên tài khoản AI.

Dữ kiện đã kiểm chứng lại ngày 24/11/2026: các lớp cửa sổ và bố cục chuẩn của Material Design 3 (Android Developers), số liệu điều hướng ẩn của Nielsen Norman Group (2016), ba ngưỡng thời gian đáp ứng, và thông tin xuất bản của các nghiên cứu Amershi và cộng sự (2019), Buçinca và cộng sự (2021), Lee và cộng sự (2025), Peters, Calvo và Ryan (2018), Chen và cộng sự (2022), Cox và cộng sự (2016), Fleck và Fitzpatrick (2010), Gray và cộng sự (2018), Passi và Vorvoreanu (2022).

## 2026.11.17

Thêm bậc 4 (web-app có trí năng nhân tạo) và cách soát chữ trong mã của web-app.

- **Chuẩn mới `chuan/10-ung-dung-ai.md`**: web-app mà máy chủ gọi mô hình Claude để viết phản hồi riêng cho từng người dùng. Gồm: khi nào cần, đặc tả và nhật ký quyết định, kiến trúc mặc định (lõi TypeScript thuần, Cloud Functions, luật Firestore chỉ cho đọc, React + Vite), gọi Claude bằng `output_config`, rào chắn bằng mã, bảo vệ prompt bằng mã hóa trong git, chi phí và hạn mức, việc chạy nền, quyền và đồng ý, bảo mật, đưa lên tự động bằng GitHub Actions và Workload Identity Federation, kiểm thử ba tầng, đợt thử nghiệm với người dùng thật.
- **Năm bậc hạ tầng** (`chuan/01`): thêm bậc 4 vào bảng và cây quyết định; bậc 4 là ngoại lệ có lý do của quy ước không dùng React.
- **`chuan/06`, `chuan/07`**: khóa Anthropic thuộc loại khóa bí mật; thêm cách đưa lên tự động cho web-app có Cloud Functions.
- **Chữ trong web-app** (`chuan/04` mục 9, `tools/kiem-web.py`, `tools/chung.py`): kiem-web quét cả chuỗi chữ Việt trong tệp .js tự viết và bắt chuỗi nhãn nối bằng dấu hai chấm.
- **Skill**: `web-ung-dung` thêm quy trình bậc 4 và 2 quy tắc cứng, tài liệu kèm có `chuan/10`; `web-trien-khai` thêm cách đưa lên tự động và 1 quy tắc cứng; `web-thiet-ke` nhận bậc hạ tầng 0 đến 4.
- **`docs/BAI-HOC.md`**: mục mới "Ứng dụng có trí năng nhân tạo", cùng các bài học về máy giả lập Firebase, Playwright và những cái bẫy khi đưa Cloud Functions lên.

Việc trong xưởng đã dựng: trợ lý chạy `python3 tools/ban-dung.py --so-ban-ve`, cập nhật các tệp năng lực theo `DUNG-XUONG.md` mục "Cập nhật xưởng", rồi đóng gói lại ba skill `web-ung-dung`, `web-trien-khai`, `web-thiet-ke` nếu người dùng đã lưu skill lên tài khoản.

Dữ kiện kiểm chứng lại: Claude Sonnet 5.5 và Opus 5.5 trả JSON qua `output_config.format` (json_schema) và không nhận `tool_choice` ép công cụ; GitHub Actions đăng nhập Google Cloud bằng Workload Identity Federation và đưa Cloud Functions thế hệ 2 lên (kiểm 17/11/2026 trên một dự án thật).

## 2026.10.17

Bổ sung kinh nghiệm dựng web-app tự đánh giá [self-assessment] và quy trình đưa lên Firebase tự động khi dùng Google Antigravity.

- **Quy trình Antigravity + Firebase**: cập nhật `huong-dan/05-firebase.md`, `chuan/07-trien-khai.md`, `docs/QUY-TRINH-KY-THUAT.md`, `skills/web-trien-khai/SKILL.md` và `skills/web-ung-dung/SKILL.md`. Khi dùng Antigravity (hoặc trợ lý chạy trực tiếp trên máy người dùng) đã đăng nhập `firebase login` một lần, trợ lý chủ động tạo dự án, gắn tên miền `<mã-dự-án>.web.app`, khởi tạo Firestore ở vùng `asia-southeast1`, đăng ký ứng dụng web, điền `firebase-cau-hinh.js` và chạy `firebase deploy` đưa thẳng cả luật bảo mật lẫn thư mục `public/` lên mạng; người dùng chỉ cần bật công tắc phương thức đăng nhập trong bảng điều khiển Firebase.
- **Nền chung (`he-thong/nen.css`)**: thêm `[hidden] { display: none !important; }` để các lớp có `display` riêng (như `.nut`, `.o`) luôn ẩn đúng khi gắn thuộc tính HTML `hidden` trong các luồng nhiều bước của web-app.
- **Chuẩn kỹ thuật và an toàn dữ liệu cho web-app (`chuan/05-ky-thuat.md`, `chuan/06-du-lieu-bao-mat.md`, `docs/BAI-HOC.md`)**:
  - Phân biệt bài thi có đáp án đúng sai (chấm ở máy chủ) với bài tự đánh giá phản tư [self-assessment] không có đúng sai (cho phép tính trên trình duyệt để cả Khách chưa đăng nhập vẫn dùng trọn vẹn, nhưng trang quản trị và tệp xuất Excel phải tính lại điểm từ mảng câu trả lời thô `answers`).
  - Mẫu mô-đun JS tự chủ (`public/assets/js/`) để vẽ biểu đồ SVG / Canvas 2D, xuất PDF khổ A4 nhiều trang và xuất tệp Excel `.xlsx` chuẩn OpenXML mà không cần gọi thư viện ngoài bị CSP chặn.
  - Quy ước dùng `<div class="bieu-mau" role="group">` kèm `<button type="button">` cho khung đăng nhập email/mật khẩu và bộ lọc quản trị (tránh nhầm với `<form>` thu thông tin khách hàng), và đặt `role="tab"` bên trong `role="tablist"`.

Việc trong xưởng đã dựng: trợ lý chạy `python3 tools/ban-dung.py --so-ban-ve` và cập nhật các tệp năng lực theo `DUNG-XUONG.md` mục "Cập nhật xưởng", rồi đóng gói lại skill nếu người dùng đã lưu skill lên tài khoản.

Dữ kiện kiểm chứng lại: `firebase-tools` CLI tạo dự án, khởi tạo cơ sở dữ liệu Firestore `asia-southeast1` và đưa web-app + luật Firestore lên `*.web.app` (kiểm 17/10/2026).

## 2026.10.09

Chuyển sang mô hình bản vẽ.

- Repo trở thành **bản vẽ**: người dùng không tải về hay `git clone`; trợ lý AI đọc bản vẽ rồi dựng xưởng riêng ở thư mục làm việc của người dùng. Cửa vào cho trợ lý: `AGENTS.md`; quy trình: `DUNG-XUONG.md`; danh mục tệp và vân tay: `BAN-DUNG.json`.
- Công cụ mới `tools/ban-dung.py`: lập danh mục (ở bản vẽ), đọc thô và kiểm vân tay khi dựng, kiểm xưởng còn nguyên, so xưởng với bản vẽ mới khi cập nhật; giữ nguyên tệp người dùng đã chủ ý sửa.
- Mẫu điểm vào của xưởng chuyển sang `mau-xuong/` (CLAUDE.md, AGENTS.md, XUONG.json); `CLAUDE.md`, `GEMINI.md` ở bản vẽ chỉ trỏ về `AGENTS.md`.
- **Skill riêng cho tài khoản AI**: công cụ mới `tools/dong-goi-skill.py` đóng gói bốn skill thành `xuong-web-*.zip` (khối cấu hình cá nhân, bản chụp phong cách và chuẩn nghề trong `references/`, kiểm tên, mô tả, khoá bí mật); mỗi skill nguồn có `kem.json`. Hướng dẫn skill đầy đủ: `skills/README.md`. Skill `web-thiet-lap` thêm bước 4 (skill riêng), giới thiệu xưởng thành bước 5; `tools/cai-dat.py` thêm dấu `--danh-dau skill`.
- `HUONG-DAN.md` thêm mục 13 (cập nhật xưởng theo mô hình mới), mục 14 (skill trên tài khoản). `BAT-DAU.md` viết lại theo cách đưa đường dẫn cho trợ lý.

Việc trong xưởng đã dựng trước ngày này (xưởng tải về theo cách cũ, có `.git` hoặc là bản ZIP): trợ lý giải thích mô hình mới; dựng xưởng mới cạnh đó theo `DUNG-XUONG.md`, dùng bản cũ làm nguồn đọc và chép sang phần của người dùng (`brand/brand.json`, logo trong `brand/logo/`, `phong-cach/PHONG-CACH.md`, `phong-cach/tu-ngu.json`, `cau-hinh.json`); kiểm `python3 tools/ban-dung.py --kiem`; rồi để người dùng quyết giữ hay bỏ bản cũ.

Dữ kiện kiểm chứng lại: các bước lưu skill vào tài khoản Claude theo trang trợ giúp "Use skills in Claude" và "How to create custom skills" (kiểm 09/10/2026).

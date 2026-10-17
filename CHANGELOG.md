# Nhật ký thay đổi của bản vẽ

Trợ lý AI đọc tệp này khi người dùng nói "cập nhật xưởng": từ phiên bản ghi trong `XUONG.json` của xưởng tới bản mới nhất, để kể bằng lời thường điều gì mới và điều gì sẽ đổi. Mỗi mục ghi: phiên bản (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng, dữ kiện đã kiểm chứng lại.

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

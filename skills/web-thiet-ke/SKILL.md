---
name: web-thiet-ke
description: "Lõi của xưởng web AI (repo xuong-web-ai): tư vấn nhu cầu, chọn giải pháp đơn giản nhất đủ dùng, lập brief, thiết kế, dựng, kiểm và bàn giao website hoặc web-app cho người dùng và các thương hiệu, đối tác họ làm cùng, theo phong cách và chuẩn ngôn ngữ của chính người dùng (phong-cach/PHONG-CACH.md). Kích hoạt khi người dùng nói làm web, làm website, tạo trang web, landing page cho khoá học, sự kiện, sách, trang báo giá, trang hồ sơ, trang liên kết, web tra cứu, trắc nghiệm online, web-app, sửa web, thêm trang, đổi giao diện web, biến nội dung này thành website, tôi muốn có web nhưng chưa biết bắt đầu từ đâu, kể cả khi người dùng không nhắc tên skill. Việc tài khoản, đưa lên mạng, tên miền, DNS, email dùng web-trien-khai; đăng nhập, dữ liệu, Astro, Firebase, thanh toán dùng thêm web-ung-dung. Không dùng cho việc chỉ viết một bài văn, làm ấn phẩm ảnh, slide."
---

# Xưởng web AI: lõi tư vấn, thiết kế, dựng, kiểm

Xưởng ở thư mục "Web AI" trên máy người dùng: repo `xuong-web-ai` (năng lực), `Du an/` (hồ sơ từng dự án), `Web/` (mã nguồn từng web). Đọc `CLAUDE.md` và `docs/QUY-TRINH-KY-THUAT.md` của repo trước; mọi đường dẫn dưới đây tính từ gốc repo. Skill chứa CÁCH LÀM; số liệu, chuẩn nằm ở `chuan/`, tên và chức danh ở `phong-cach/PHONG-CACH.md`, lệnh ở `docs/QUY-TRINH-KY-THUAT.md`.

Chưa gắn thư mục "Web AI" vào phiên (không thấy `CLAUDE.md` của repo) thì nhờ người dùng gắn trước bằng nút thêm thư mục. Không gắn được (ví dụ người dùng đang dùng ứng dụng trên điện thoại) thì vẫn làm theo các bước dưới: bản skill có kèm `references/` (gói .zip của `tools/dong-goi-skill.py`) thì dựa vào bản chụp chuẩn và phong cách ở đó (danh sách, dấu gói: `references/DONG-GOI.md`); bản chỉ có SKILL.md (lưu qua thẻ đề xuất skill) thì dựa vào các bước và quy tắc cứng trong tệp này. Nói rõ với người dùng là đang làm khi chưa có xưởng, công cụ kiểm chưa chạy, khuôn chưa dùng được, và việc nào nên làm lại khi gắn được thư mục.

## Bảy bước

### 1. Tiếp nhận

- Đọc tư liệu người dùng đưa (nội dung, outline khoá học, web cũ, ảnh). Dữ kiện cần kiểm chứng (số liệu, trích dẫn, lịch) thì kiểm trước bằng tìm kiếm hoặc tài liệu trong project; không bịa số, lời chứng thực, năng lực.
- Web đang có (sửa, mở rộng): đọc `xuong.json`, `README.md` của web và `BRIEF.md`, `SO-GOP-Y.md`, `VAN-HANH.md` của dự án; bỏ qua bước 2-4 nếu phạm vi không đổi.

### 2. Tư vấn (chuan/01-tu-van-giai-phap.md)

- Hỏi theo bộ 15 câu, tối đa 4 câu mỗi lượt, có phương án sẵn (AskUserQuestion); bỏ câu đã rõ.
- Xếp vào loại web (chuan/02-loai-web.md) và bậc hạ tầng 0-3. Đi theo cây quyết định "giải pháp đơn giản nhất": có khi câu trả lời đúng là không cần web, hoặc dùng nền tảng có sẵn.
- Trình 1-2 phương án: làm được gì, không làm gì, chi phí mỗi năm, việc người dùng phải tự tay làm, rủi ro, phương án khuyên.

### 3. Tạo dự án và chốt brief (chốt thứ nhất)

- `python3 tools/web-moi.py "<tên dự án>" --khuon <khuôn> [--thuong-hieu <th>] [--chu-de <cđ>]` (`--ds` để xem khuôn, chủ đề, thương hiệu). Công cụ tạo `Du an/<YYYY-MM tên>/` và `Web/<tên-web>/`.
- Điền `BRIEF.md` cùng người dùng; người dùng duyệt mới đi tiếp.

### 4. Kế hoạch thiết kế (chốt thứ hai)

- Viết `THIET-KE.md` 10-15 dòng theo chuan/03-thiet-ke-web.md mục 2: mood, chủ đề màu, khối tối, phông, bố cục từng phần, chất liệu đặc trưng, một điểm nhớ, những gì cố ý không dùng. Người dùng duyệt.

### 5. Dựng

- Sửa trong `Web/<tên-web>/public/` (Astro: `src/`). Dùng lớp của `nen.css`; phần riêng vào `assets/css/trang.css`; màu gọi theo vai, không mã màu rời.
- Chữ: theo `chuan/04-ngon-tu-web.md` và PHONG-CACH mục 1, 4. Trang đích chương trình, sách, sự kiện: cấu trúc theo khuôn `landing` (mười phần, mỗi phần một ý); bài viết dài: viết theo chuan/04 và skill viết riêng của người dùng nếu có; luôn rà tám tầng văn AI ở chuan/04 mục 2.
- Chỗ người dùng sẽ tự sửa (giá, ngày, link) đánh dấu `<!-- SỬA Ở ĐÂY: ... -->`. Thiếu ảnh thì để `.cho-anh` ghi cỡ khuyến nghị; ảnh, sơ đồ, ảnh chia sẻ có thể làm ở Xưởng thiết kế Claude (repo anh em, nếu người dùng có) rồi chép vào `public/assets/img/`.
- Form thu dữ liệu, thanh toán, đăng nhập: đọc thêm skill web-ung-dung và chuan/06.

### 6. Kiểm (chuan/09-nghiem-thu.md)

- `python3 tools/kiem-web.py <tên-web>` tới khi không còn LỖI; cảnh báo nào giữ lại phải có lý do.
- NHÌN tờ tổng thể và ảnh từng khổ (390, 768, 1280 px), đối chiếu THIET-KE.md và danh sách cấm (chuan/03 mục 9); đọc soát từng âm tiết.
- `python3 tools/anh-chia-se.py <tên-web>` khi nội dung đã chốt.

### 7. Trình và bàn giao

- Trình: tờ tổng thể + 3-6 dòng (lựa chọn chính, lý do, cảnh báo còn lại, điều cần người dùng chốt).
- Người dùng duyệt bản cuối: chuyển sang web-trien-khai để đưa lên mạng, gắn tên miền.
- Bàn giao: địa chỉ web, danh sách chỗ `SỬA Ở ĐÂY` (có trong BAO-CAO.md), `README.md` của web (cách sửa), giả định đã tự quyết.

## Quy tắc cứng

1. Tên, chức danh, từ ngữ ở PHONG-CACH mục 1, 4 là nguyên văn. Chữ trên web: thuần Việt có [English], sentence case hoặc FULL-CAP, không Title Case, không gạch dài, không emoji.
2. Không bịa số liệu, lời chứng thực, khan hiếm; không ảnh AI thay người, lớp, sự kiện thật; ghi tác giả mọi mô hình, công cụ.
3. Hai chốt (brief, kế hoạch thiết kế) trước khi dựng phần lớn.
4. Chưa qua `kiem-web.py` (không LỖI) và chưa NHÌN ảnh chụp thì chưa nói "xong".
5. Chỉ `public/` (hoặc `dist/`) được đưa lên mạng; không khoá bí mật trong mã; form thu thông tin cá nhân luôn có ô đồng ý không đánh dấu sẵn và trang chính sách.
6. Góp ý lặp lần hai: sửa nguồn mặc định (khuôn, nen.css, brand.json, chuan) và ghi sổ tay PHONG-CACH; đổi giá trị dùng chung trong brand.json: hỏi người dùng trước.
7. Repo sạch: web, hồ sơ, việc tạm ghi ngoài repo; cuối phiên `tools/kiem-sach.py` ĐẠT. Không tự commit; người dùng tự commit (hoặc cho phép trong phiên).

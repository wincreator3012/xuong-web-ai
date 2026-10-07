# Khuôn web

Mỗi khuôn là một web chạy được ngay, mang sẵn nền chung (`he-thong/nen.css`, `nen.js`), chỗ cần điền đánh dấu `[[...]]` trên trang và `<!-- SỬA Ở ĐÂY -->` trong mã. Tạo web từ khuôn bằng `tools/web-moi.py "Tên dự án" --khuon <id>`; không sửa khuôn để làm một web cụ thể.

Chọn khuôn theo loại web và bậc hạ tầng thấp nhất đủ dùng (chuan/01-tu-van-giai-phap.md, chuan/02-loai-web.md).

| Khuôn | Bậc | Dùng cho | Có sẵn |
|---|---|---|---|
| `trang-don` | 0 | trang giới thiệu một trang, thông báo, trang tạm cho tên miền mới | mở đầu, hai phần nội dung, liên hệ |
| `ho-so` | 0 | hồ sơ cá nhân, chuyên gia | điều hướng, khối mở đầu tối, các cửa theo đối tượng, triết lý, số liệu, đang diễn ra, cảm nhận, lời mời đọc bản tin |
| `lien-ket` | 0 | trang liên kết gắn ở tiểu sử mạng xã hội | ảnh, tên, 4-8 nút to |
| `tra-cuu` | 0 | thư viện, kho bài tập, danh mục tra cứu | dữ liệu JSON tách riêng, tìm không dấu, lọc nhóm, link chia sẻ từng mục |
| `trac-nghiem` | 0 | bài tự soi chiếu, tự đánh giá | câu hỏi JSON, tính điểm nhiều chiều trên máy người dùng, không lưu |
| `landing` | 1 | trang đích chương trình, sự kiện, sách | 10 phần theo cấu trúc trang đích chương trình, form đăng ký có ô đồng ý, mã VietQR có mã đơn, hỏi đáp, nút nổi trên điện thoại |
| `bao-gia` | 1 | báo giá, đề xuất cho tổ chức (gửi link riêng) | không lên Google, dịch vụ, cách làm việc, ba gói, điều khoản, đặt lịch |
| `site-astro` | 1 | web nhiều trang, blog | Astro 7 xuất tĩnh, bài viết Markdown, sơ đồ trang, Pages CMS cho người biên tập |
| `app-firebase` | 3 | ứng dụng có đăng nhập, dữ liệu riêng từng người | đăng nhập Google, luật Firestore viết sẵn, cảnh báo trình duyệt Zalo/Facebook, quản trị xuất CSV, danh sách kiểm bảo mật |

Trang dùng chung (`he-thong/trang-chung/`): `chinh-sach-bao-mat.html` (bản nháp theo Luật Bảo vệ dữ liệu cá nhân 2025, tự thêm vào khuôn có form) và `404.html`.

## Thêm khuôn mới

1. Tạo `khuon/<id>/khuon.json` (ten, bac, loai: tinh | astro | firebase, coForm, trangChung, loaiWeb) và `public/` (hoặc cấu trúc Astro).
2. Chỉ dùng lớp của `nen.css`; phần riêng của khuôn đặt trong `<style>` của trang, màu gọi theo vai.
3. Chữ mẫu viết đúng chuẩn (chuan/04-ngon-tu-web.md), chỗ cần điền dạng `[[...]]`, không bịa số liệu, lời chứng thực.
4. Thêm một dòng vào bảng trên; tạo thử một web từ khuôn và chạy `tools/kiem-web.py` tới khi chỉ còn cảnh báo chỗ trống.

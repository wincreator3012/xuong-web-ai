# 02. Mười hai loại web thường gặp

Bảng tổng hợp từ danh mục mẫu của Wix, Squarespace, Framer, Carrd, khảo sát doanh nghiệp nhỏ và đặc thù Việt Nam (nghien-cuu/D-loai-web-quy-trinh-chuan.md mục 1). Mỗi loại ghi việc người xem cần làm xong, các phần thường có, tính năng bắt buộc, bậc hạ tầng (chuan/01 mục 3) và khuôn khởi đầu.

| # | Loại | Người xem cần làm xong việc gì | Phần thường có | Bắt buộc | Bậc | Khuôn |
|---|---|---|---|---|---|---|
| 1 | Hồ sơ cá nhân, chuyên gia | tra cứu bạn trước khi hợp tác | giới thiệu, triết lý, việc đã làm, báo chí, liên hệ | OG đẹp, schema Person, nút Zalo, email | 0 | `ho-so` |
| 2 | Trang liên kết [link-in-bio] | tìm đúng một link từ tiểu sử mạng xã hội | ảnh, tên, 4-8 nút | tải rất nhanh, nút cao từ 44 px, gắn nguồn lượt đến [UTM] | 0 | `lien-ket` |
| 3 | Trang đích chương trình, sự kiện, sách | quyết định đăng ký, mua | vấn đề, lời hứa, nội dung, người hướng dẫn, cảm nhận, giá, hỏi đáp, kêu gọi | form có ô đồng ý, VietQR có mã đơn, OG, nút nổi trên điện thoại | 1 | `landing` |
| 4 | Dịch vụ cho tổ chức, báo giá | đánh giá năng lực và cơ chế phí, đặt lịch | định vị, dịch vụ, cách làm việc, gói, bằng chứng, điều khoản | gửi link riêng, không lên Google (noindex) | 1 | `bao-gia` |
| 5 | Web tổ chức, thương hiệu nhỏ | "căn cứ" chính thức trên Google | trang chủ, giới thiệu, dịch vụ, tin, liên hệ, chính sách | nhiều trang, sitemap, schema Organization, chân trang đủ thông tin | 0-1 | `site-astro` hoặc vài trang tĩnh từ `trang-don` |
| 6 | Blog, bản tin | đọc và theo dõi nội dung chuyên môn | danh sách bài, bài, đăng ký nhận thư | bài viết Markdown, schema Article, RSS hoặc dẫn sang Substack | 0-1 | `site-astro` |
| 7 | Microsite sự kiện có đăng ký | đăng ký, xem lịch trình, đường đi | lịch trình, diễn giả, địa điểm, vé, hỏi đáp | form + QR + thư xác nhận; schema Event; trang cảm ơn | 1-2 | `landing` |
| 8 | Thư viện, công cụ tra cứu | tìm nhanh một mục trong kho tri thức | ô tìm, bộ lọc, thẻ kết quả, chi tiết | dữ liệu JSON tách khỏi giao diện, tìm không dấu, link chia sẻ từng mục | 0 | `tra-cuu` |
| 9 | Trắc nghiệm, tự đánh giá | hiểu mình, biết bước tiếp theo | giới thiệu, câu hỏi, tiến độ, kết quả diễn giải | tính điểm trên máy người dùng; lưu kết quả là dữ liệu nhạy cảm nếu về tâm lý | 0 (không lưu) / 3 (có lưu) | `trac-nghiem` |
| 10 | Đặt lịch hẹn | chọn giờ tư vấn, coaching | dịch vụ, thời lượng, giá, lịch trống | nhúng Cal.com, Google Calendar; không tự xây | 1 | nhúng vào `ho-so`, `bao-gia` |
| 11 | Khu thành viên, cổng khoá học | vào học nội dung trả phí | đăng nhập, bài học, tài liệu, tiến độ | xác thực, phân quyền; ưu tiên nền tảng có sẵn | 3 | `app-firebase` (khi thật cần tự xây) |
| 12 | Bảng điều khiển nội bộ | nhóm theo dõi số liệu vận hành | chỉ số chính, biểu đồ, bảng, bộ lọc | không công khai, có đăng nhập; đọc từ Sheets hoặc Firestore | 2-3 | `app-firebase` |

Cố ý để ngoài: cửa hàng trực tuyến đầy đủ (giỏ hàng, kho, vận chuyển). Ở Việt Nam đã có sàn và nền tảng chuyên dụng; tự xây kéo theo nghĩa vụ thông báo với Bộ Công Thương (chuan/08) và rủi ro thanh toán. Khuyên: web giới thiệu sản phẩm, dẫn sang sàn hoặc Zalo.

## Đặc thù Việt Nam (áp cho mọi loại)

- Khoảng 68% lượt duyệt web là trên điện thoại (StatCounter 09/2026): thiết kế cho khổ 390 px trước.
- Người xem đến từ Facebook, Zalo nhiều hơn từ Google: ảnh chia sẻ 1200x630 (`tools/anh-chia-se.py`) và mô tả OG quan trọng ngang SEO. Sau khi sửa ảnh chia sẻ, làm mới bộ đệm Zalo tại developers.zalo.me/tools/debug-sharing.
- Kênh liên hệ ưu tiên là Zalo: `https://zalo.me/<số điện thoại>`.
- Thu tiền: mã VietQR có số tiền, mã đơn trong nội dung chuyển khoản (`nen.js` dựng sẵn).
- Người xem mở link trong trình duyệt của Zalo, Facebook: đăng nhập Google bị chặn ở đó, web-app phải có lá chắn hướng dẫn mở bằng Chrome, Safari.

# Nghiên cứu E: bài học từ ba web-app làm cùng AI trước khi có xưởng

Rà ngày 07/10/2026, đọc mã nguồn (không chạy) của ba web-app thật mà tác giả xưởng, một nhà giáo dục không chuyên lập trình, đã làm cùng trợ lý AI trước khi dựng xưởng. Tên ứng dụng và mọi dữ liệu thật được lược bỏ. Mục đích: giữ lại những gì đã chạy tốt thành mặc định của xưởng, và biến những lỗ hổng thành cổng kiểm tự động để người dùng xưởng không lặp lại. Hai loại lỗ hổng gặp ở đây (khoá bí mật nằm trong mã chạy trên trình duyệt, luật bảo vệ dữ liệu lỏng) cũng là nguyên nhân của các vụ lộ dữ liệu ở ứng dụng làm cùng AI được ghi nhận 2025-2026 (`nghien-cuu/B-du-lieu-dich-vu.md` mục các vụ lộ dữ liệu).

## 1. Ba ứng dụng

| Ứng dụng | Kiến trúc | Nơi chạy | Dùng cho |
|---|---|---|---|
| Quản lý lớp học | một tệp HTML, Tailwind qua CDN, Firebase bản compat qua CDN | Firebase Hosting | danh sách lớp, học viên |
| Bài thi cuối khoá | React + Vite + Tailwind, Firebase 12, dịch vụ gửi thư | Firebase Hosting | bài thi nhiều câu, có giờ, tạm dừng, xem lại, niêm phong kết quả |
| Lập lịch cá nhân | một tệp HTML lớn (vài nghìn dòng) + Firestore + tập lệnh Python đồng bộ lịch | Vercel và Firebase Hosting | lịch, việc trong ngày, hàng chờ xem lại |

Cả ba theo cùng một hướng: trang tĩnh, dữ liệu và đăng nhập giao cho Firebase, đăng nhập bằng Google. Đây chính là bậc 3 của xưởng (`chuan/01-tu-van-giai-phap.md`), và là hướng hợp lý cho người không chuyên kỹ thuật: không phải vận hành máy chủ.

## 2. Những điều đã làm tốt, nay thành mặc định của xưởng

- **Lá chắn trình duyệt nhúng.** Ứng dụng bài thi phát hiện trình duyệt bên trong Zalo, Facebook, Messenger, Instagram, TikTok và hướng dẫn mở bằng Chrome, Safari, tránh lỗi Google chặn đăng nhập `disallowed_useragent`. Với người dùng Việt Nam (link đi qua Zalo là chính) đây là điều bắt buộc. Đã đưa vào khuôn `app-firebase`.
- **Phân quyền ngay trong luật Firestore** (quản trị, điều phối viên, thí sinh), không chỉ ẩn hiện trên giao diện. Một phần luật còn kiểm từng trường dữ liệu (`keys().hasOnly`, kiểu, khoảng giá trị, `createdAt == request.time`): mức này là chuẩn của xưởng.
- **Lưu ngầm** đáp án và thời gian mỗi 15 giây và ngay khi chọn, có bản dự phòng trên máy: đúng cho mọi ứng dụng có phiên làm việc dài.
- **Đặc tả nghiệp vụ viết thành README trước** (thể thức, chấm điểm, phân quyền, mốc thời gian): khớp nguyên tắc "đặc tả trước, mã sau" của xưởng.
- **Tách các tệp bí mật bằng `.gitignore`**: khoá tài khoản dịch vụ, token Google không bị đưa vào git.

## 3. Lỗ hổng tìm thấy, và cổng kiểm tương ứng

| Lỗ hổng | Hậu quả | Cổng kiểm của xưởng |
|---|---|---|
| Mã truy cập GitHub [personal access token] viết thẳng vào địa chỉ remote của git | ai đọc được cấu hình git, nhật ký lệnh là có quyền vào tài khoản GitHub | `huong-dan/01-github.md`: đăng nhập bằng GitHub Desktop hoặc `gh auth login`, không dán mã vào URL; kiem-web quét mẫu `github_pat_` |
| Khoá API dịch vụ gửi thư viết cứng trong mã chạy trên trình duyệt, và lưu ở tài liệu Firestore cho mọi người đọc | ai mở trang cũng lấy được khoá để gửi thư dưới tên tổ chức | kiem-web quét mẫu khoá Resend, Stripe, Supabase secret, tài khoản dịch vụ; `chuan/06-du-lieu-bao-mat.md`: khoá gửi thư chỉ nằm ở máy chủ (Cloud Functions, Worker) |
| Đáp án và lời giải đóng gói vào mã gửi xuống máy thí sinh; bài làm, điểm do chính thí sinh ghi vào Firestore | thí sinh rành máy tính xem được đáp án, sửa được điểm | kiem-web cảnh báo dữ liệu đáp án trong mã công khai ở web bậc 2-3; chuan/06 mục "chấm điểm ở máy chủ"; `khuon/app-firebase/KIEM-BAO-MAT.md` |
| Đưa cả thư mục gốc lên mạng (`firebase.json` có `public: "."`; Vercel không có cấu hình đầu ra) | kế hoạch, biên bản họp, dữ liệu gốc có thể tải công khai qua đường dẫn | mọi web của xưởng chỉ đưa `public/` (hoặc `dist/`) lên; kiem-web báo LỖI khi `hosting.public` là thư mục gốc và khi tệp `.md`, `.json` dữ liệu, `.py` nằm trong thư mục công khai |
| Danh sách quản trị viết bằng email cụ thể ngay trong luật | đổi người phải sửa và đưa lại luật; email lộ trong kho mã | khuôn app dùng bộ sưu tập `quanTri/<email>` tạo tay trong Console, kiểm `email_verified` |
| Bộ sưu tập người dùng cho mọi người đã đăng nhập đọc (`allow read: if request.auth != null`) | bất kỳ ai có tài khoản Google, đăng nhập vào, đọc được danh sách người dùng | kiem-web cảnh báo mẫu `if request.auth != null` đứng một mình |
| Tailwind qua CDN và Firebase bản compat trong trang chạy thật | Tailwind CDN chỉ dành cho thử nghiệm, tải chậm; bản compat nặng | khuôn dùng nen.css của xưởng và Firebase bản module 12 |
| Emoji trong giao diện, tiêu đề Title Case | lệch chuẩn ngôn ngữ của chủ web | kiem-web bắt Title Case; `chuan/03-thiet-ke-web.md` danh sách cấm |

## 4. Hàm ý cho kiến trúc xưởng

1. Bậc 3 (đăng nhập + dữ liệu) giữ Firebase làm mặc định, vì Firebase Spark không tạm dừng dự án khi ít dùng (khác Supabase) và đăng nhập Google quen thuộc với người Việt. Phần cần bí mật (gửi thư, chấm điểm, thanh toán) đặt ở Cloud Functions hoặc Cloudflare Worker, không ở trình duyệt.
2. Mọi web tách rõ phần công khai (`public/`) và phần riêng (README, ghi chú, tập lệnh, dữ liệu gốc).
3. "Luật trước, giao diện sau": khuôn app đưa sẵn `firestore.rules` có kiểm từng trường, và danh sách kiểm hai tài khoản trước khi mở cho người dùng thật.
4. Đồng bộ và tự động hoá cá nhân (nối lịch, ghi chú) nằm ngoài phạm vi khuôn; xưởng hỗ trợ ở mức tư vấn kiến trúc và rà an toàn.

## 5. Bạn đã có web-app làm cùng AI?

Nhờ trợ lý: "Kiểm bảo mật web-app ở thư mục <tên>" (skill `web-ung-dung`, `khuon/app-firebase/KIEM-BAO-MAT.md`). Trợ lý đọc mã, rà theo bảng mục 3, báo theo mức nặng nhẹ. Thấy khoá bí mật lộ: thu hồi khoá ở trang của nhà cung cấp TRƯỚC, sửa mã sau; xoá khoá khỏi mã không làm khoá cũ hết hiệu lực.

# Cập nhật và đóng góp

## Xưởng được cập nhật thế nào

Tác giả (Lương Dũng Nhân, ldn.edu.vn) dùng một xưởng riêng hằng ngày cho web thật. Kinh nghiệm mới (công cụ sửa lỗi, khuôn mới, giá và giao diện dịch vụ đổi, luật mới, bài học từ dự án) được đưa sang repo chung này bằng một quy trình có cổng kiểm: phần kỹ thuật chép máy móc, phần tài liệu được khái quát hoá, và một cổng chặn để không mang theo bất cứ thứ gì riêng (tên, chức danh, thương hiệu, chương trình, đối tác, logo, web-app riêng). Vì vậy `tools/`, `he-thong/`, `khuon/`, `fonts/`, `chuan/`, `huong-dan/`, `nghien-cuu/`, `skills/` (trừ `web-thiet-lap`) và `docs/` có thể đổi qua từng bản.

## Cập nhật bản mới mà không mất phần của bạn

Phần của bạn không bao giờ bị bản mới ghi đè:

- ngoài repo: `Web/` (mã nguồn mọi web), `Du an/` (hồ sơ, báo cáo kiểm, hồ sơ vận hành);
- trong repo nhưng là của bạn: `brand/brand.json`, logo bạn thả vào `brand/logo/`, `phong-cach/PHONG-CACH.md`, `phong-cach/tu-ngu.json`, `cau-hinh.json`. Các tệp này được tạo trên máy bạn ở bước cài, từ bản khởi đầu cùng tên có thêm `.mau` (ví dụ `brand/brand.mau.json`); repo chung chỉ chứa bản khởi đầu, và `.gitignore` giữ bản của bạn ngoài git, nên bản cập nhật chỉ có thể thay bản khởi đầu, không đụng tới bản của bạn.

Cách cập nhật, chọn một:

1. **Nhờ trợ lý AI** (dễ nhất): tải bản mới (nút Code, Download ZIP trên GitHub), giải nén ra một thư mục tạm cạnh repo, rồi nói: "Cập nhật xưởng từ thư mục <tên thư mục tạm>, giữ nguyên brand, phong-cach, cau-hinh.json của tôi". Trợ lý chép phần năng lực mới vào repo, giữ phần của bạn, so `brand/brand.mau.json` bản mới với `brand/brand.json` của bạn để thêm chủ đề màu, khoá mới (nếu có) mà không đổi giá trị bạn đã đặt, rồi chạy `python3 tools/kiem-tai-lieu.py`, `python3 tools/tuong-phan.py`, `python3 tools/kiem-sach.py`, và tạo thử một web.
2. **Dùng git** (nếu bạn đã `git clone`): `git pull`. Phần của bạn nằm ngoài git nên không xung đột; sau đó nhờ trợ lý so bản khởi đầu mới với bản của bạn như cách 1.

**Web đã làm không tự đổi theo xưởng.** Mỗi web mang bản chép riêng của nền chung (`public/assets/css/nen.css`, `nen.js`) để chạy độc lập. Muốn một web cũ nhận bản sửa mới của nền chung (ví dụ một lỗi hiển thị đã được sửa), nói với trợ lý "cập nhật nền chung cho web <tên>"; trợ lý chép bản mới, kiểm lại web bằng `tools/kiem-web.py` rồi mới để bạn đưa lên.

## Đóng góp

Bạn làm được web tốt hơn nhờ một quy tắc mới, một khuôn mới, thấy một thẻ hướng dẫn đã cũ vì nhà cung cấp đổi giao diện, hay bắt được một lỗi? Mở issue hoặc pull request trên GitHub. Lưu ý:

- Không đưa thông tin riêng của bạn (tên, logo, nội dung khách hàng, khoá truy cập) vào pull request; nội dung mẫu của khuôn luôn là chỗ trống `[[...]]` hoặc giả định.
- Thay đổi ở `tools/`, `he-thong/`, `khuon/`, `chuan/`, `huong-dan/`, `skills/` sẽ được tác giả đưa về xưởng gốc trước rồi mới vào bản chung ở lần cập nhật sau, để hai bên không lệch nhau.
- Thẻ hướng dẫn, giá, hạn mức: ghi ngày bạn kiểm và đường dẫn trang chính thức.
- Trước khi gửi: `python3 tools/kiem-tai-lieu.py` và `python3 tools/tuong-phan.py` phải ĐẠT; sửa khuôn hay nền chung thì tạo thử web từ khuôn đó và `python3 tools/kiem-web.py` không LỖI.
- Mọi đóng góp được nhận theo cùng giấy phép của repo (MIT cho mã, CC BY 4.0 cho tài liệu).

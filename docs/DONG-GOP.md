# Bảo trì bản vẽ và đóng góp

Tệp này chỉ có ở bản vẽ. Người dùng xưởng không cần đọc: cập nhật xưởng của họ đi theo `DUNG-XUONG.md` mục "Cập nhật về sau".

## Bản vẽ được cập nhật thế nào

Tác giả (Lương Dũng Nhân, ldn.edu.vn) dùng một xưởng gốc hằng ngày cho web thật. Kinh nghiệm mới (công cụ sửa lỗi, khuôn mới, giá và giao diện dịch vụ đổi, luật mới, bài học từ dự án) được đưa sang bản vẽ bằng một quy trình có cổng kiểm: phần kỹ thuật chép máy móc, phần tài liệu được khái quát hoá, và một cổng chặn để không mang theo bất cứ thứ gì riêng (tên, chức danh, thương hiệu, chương trình, đối tác, logo, web-app riêng). Vì vậy `tools/`, `he-thong/`, `khuon/`, `fonts/`, `chuan/`, `huong-dan/`, `nghien-cuu/`, `skills/` (trừ `web-thiet-lap`) và `docs/` có thể đổi qua từng bản.

Mỗi lần bản vẽ đổi, người bảo trì làm đủ ba việc trước khi đẩy lên GitHub, để xưởng của mọi người cập nhật được đúng:

1. Ghi một mục mới ở đầu `CHANGELOG.md` (phiên bản năm.tháng.ngày, thay đổi, việc trợ lý cần làm trong xưởng đã dựng, dữ kiện đã kiểm chứng lại).
2. Lập lại danh mục: `python3 tools/ban-dung.py --lap` (đọc phiên bản từ mục đầu của `CHANGELOG.md`, ghi `BAN-DUNG.json`).
3. Chạy các cổng: `python3 tools/kiem-tai-lieu.py`, `python3 tools/tuong-phan.py`, `python3 tools/kiem-sach.py`; sửa khuôn hay nền chung thì dựng thử một xưởng từ bản vẽ trên máy (`DUNG-XUONG.md` với `--ban-ve <thư mục bản vẽ>`), tạo thử web từ khuôn đã đổi và `tools/kiem-web.py` không LỖI.

Tệp mới thêm vào bản vẽ mặc định là loại `chep` (được chép vào xưởng). Tệp chỉ có nghĩa ở bản vẽ thì thêm vào danh sách `CHI_BAN_VE` trong `tools/ban-dung.py`; mẫu điểm vào của xưởng đặt trong `mau-xuong/` và khai ở `MAU`.

## Đóng góp

Bạn làm được web tốt hơn nhờ một quy tắc mới, một khuôn mới, thấy một thẻ hướng dẫn đã cũ vì nhà cung cấp đổi giao diện, hay bắt được một lỗi? Mở issue hoặc pull request trên GitHub. Lưu ý:

- Không đưa thông tin riêng của bạn (tên, logo, nội dung khách hàng, khoá truy cập) vào pull request; nội dung mẫu của khuôn luôn là chỗ trống `[[...]]` hoặc giả định.
- Thay đổi ở `tools/`, `he-thong/`, `khuon/`, `chuan/`, `huong-dan/`, `skills/` sẽ được tác giả đưa về xưởng gốc trước rồi mới vào bản vẽ ở lần cập nhật sau, để hai bên không lệch nhau.
- Thẻ hướng dẫn, giá, hạn mức: ghi ngày bạn kiểm và đường dẫn trang chính thức.
- Trước khi gửi: `python3 tools/kiem-tai-lieu.py` và `python3 tools/tuong-phan.py` phải ĐẠT; sửa khuôn hay nền chung thì tạo thử web từ khuôn đó và `python3 tools/kiem-web.py` không LỖI.
- Mọi đóng góp được nhận theo cùng giấy phép của repo (MIT cho mã, CC BY 4.0 cho tài liệu).

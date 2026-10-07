# {{TIEU_DE}}

Mã nguồn web "{{TIEU_DE}}" của {{TEN}}, dựng bằng Xưởng web AI ngày {{NAM}}. Tệp này viết cho chủ web: sửa gì ở đâu, nhờ trợ lý AI thế nào.

## Cấu trúc

```
public/                 phần ĐƯA LÊN MẠNG (mọi thứ ngoài thư mục này không ai xem được)
  index.html            trang chính
  assets/css/tokens.css màu và phông của web (đổi màu ở đây)
  assets/css/nen.css    nền chung của xưởng (không sửa; chỉnh riêng thì viết vào trang.css)
  assets/css/trang.css  chỉnh riêng cho web này
  assets/js/nen.js      biểu mẫu, mã chuyển khoản, menu điện thoại, hiệu ứng hiện dần
  assets/img/           ảnh, logo, ảnh chia sẻ (chia-se.jpg 1200x630)
  assets/fonts/         phông tự lưu trữ, đủ dấu tiếng Việt
  _headers, robots.txt  lớp bảo vệ HTTP, chỉ dẫn cho máy tìm kiếm
README.md               tệp bạn đang đọc
xuong.json              hồ sơ máy đọc cho công cụ của xưởng
```

## Sửa nội dung

- Mở `public/index.html` bằng trình soạn văn bản (hoặc ngay trên GitHub: mở tệp, bấm biểu tượng bút chì). Chỗ cần điền có dấu `[[...]]` trên trang và chú thích `<!-- SỬA Ở ĐÂY: ... -->` trong mã.
- Nhờ trợ lý AI: mở thư mục web này (hoặc thư mục xưởng) trong ứng dụng AI và nói thẳng điều cần đổi, ví dụ "đổi ngày khai giảng thành 12/11, giá thành 4.500.000 đ". Trợ lý sửa, chạy kiểm, rồi đưa lên mạng theo cách đã thiết lập.
- Xem thử trên máy: bấm đúp `public/index.html`; hoặc chạy `python3 -m http.server -d public 8000` rồi mở http://localhost:8000.

## Đưa lên mạng và cập nhật

Nơi lưu trữ, tên miền, tài khoản và lịch gia hạn của web này ghi trong hồ sơ dự án (`VAN-HANH.md` ở thư mục dự án của xưởng). Khi web đã nối GitHub, mỗi lần lưu thay đổi [commit] lên nhánh chính là nơi lưu trữ tự đưa bản mới lên sau khoảng một phút.

## An toàn

Không bao giờ dán khoá bí mật (khoá API, mật khẩu, tệp tài khoản dịch vụ) vào bất kỳ tệp nào trong `public/`: mọi thứ trong đó ai cũng tải về được. Khoá cho biểu mẫu Web3Forms (access key) là loại công khai, đặt trong HTML được.

# PHONG CÁCH WEB CỦA [TÊN BẠN]

Bản đồ phong cách trợ lý AI đọc trước mỗi web trong xưởng. Một chỗ duy nhất giữ tên, chức danh nguyên văn, từ ngữ phải viết đúng, tông và các góp ý đã chốt; chỗ khác (skill, quy trình, chuẩn) chỉ trỏ về đây. Bạn sửa tay lúc nào cũng được, hoặc nói "từ nay đổi X thành Y" là trợ lý cập nhật tệp này và phần máy đọc tương ứng (`brand/brand.json`, `phong-cach/tu-ngu.json`).

Đây là bản khởi đầu: mọi chỗ trong ngoặc vuông là chỗ trống, skill `web-thiet-lap` hỏi bạn rồi điền dần. Mục 1 và 4 là nguyên văn, giữ tuyệt đối; các mục còn lại là tinh thần và điểm xuất phát. Bạn có dùng thêm Xưởng thiết kế Claude (cùng tác giả) thì giữ mục 1 và 4 ở hai xưởng giống nhau.

## 1. Tên và chức danh (nguyên văn, không rút gọn, không đổi chữ)

Dữ liệu máy đọc ở `brand/brand.json` > `nhanVat.chinh`.

- **Mặc định**: **[Tên hiển thị kèm học vị] - [Chức danh nguyên văn]**. Cách viết học vị: [ví dụ "TS" không dấu chấm, hay "TS."].
- **Bản thứ hai (nếu có)**: [ví dụ bản dễ hiểu cho người xem đại chúng, bản tiếng Anh; khi nào dùng].
- Quy tắc chọn: dự án nào bạn nói chức danh riêng thì dùng nguyên văn trong dự án đó, ghi vào BRIEF.md, không đưa ngược thành mặc định. Phân vân giữa hai bản thì trợ lý hỏi bạn.
- Web làm cho đối tác, khách hàng (không mang thương hiệu của bạn): dùng thương hiệu, liên hệ của họ (thêm vào `brand/brand.json` > `thuongHieu`), không chèn logo của bạn nếu không được yêu cầu.
- Nhân vật khác (khách mời, đồng giảng viên): lấy nguyên văn từ brief của dự án; chưa có thì hỏi bạn trước khi dựng.

## 2. Web bạn thường làm

[Danh sách loại web, ví dụ: trang đích khoá học, hồ sơ cá nhân, trang báo giá cho doanh nghiệp, thư viện tra cứu, web-app lớp học]. Người xem chính: [ai, đến từ đâu: Facebook, Zalo, email, mã QR trên tài liệu in]. Mặc định của xưởng: thiết kế cho điện thoại trước, ảnh chia sẻ và mô tả khi dán link vào Zalo, Facebook làm kỹ.

## 3. Tông và cảm giác

- **Ba từ tả cảm giác** muốn người xem nhận được: [ví dụ điềm tĩnh, tin cậy, ấm áp].
- **Chủ đề màu web** (chi tiết `brand/brand.json` > `chuDe`, đã kiểm tương phản):
  - Chủ đề chính: [tên chủ đề, ví dụ giay-muc], dùng cho [loại web].
  - Chủ đề phụ: [tên chủ đề cho sự kiện, chương trình đặc biệt, nếu có].
  - Sáu chủ đề khởi đầu: giay-muc (điềm tĩnh, sâu), than-dong (trầm ấm, cả trang tối), dem-vang (sang trọng cho sự kiện), dem-xanh (rõ ràng, hiện đại, cả trang tối), am-ap (gần gũi), trang-xanh (hiện đại, tin cậy). Chủ đề riêng pha từ màu logo được thêm vào brand.json và phải qua `tools/tuong-phan.py`.
- Một web một chủ đề, không pha. Web của một chiến dịch dùng cùng họ màu với ấn phẩm của chiến dịch đó.
- **Ảnh**: người thật, khoảnh khắc thật; chỉnh tự nhiên. Không ảnh AI thay người, lớp học, sự kiện thật.

## 4. Chữ trên web

Bản đầy đủ ở `chuan/04-ngon-tu-web.md`. `tools/kiem-web.py` tự bắt từ cấm và dấu hiệu văn AI (luật chung trong `tools/chung.py`, luật riêng của bạn trong `phong-cach/tu-ngu.json`), nhưng máy chỉ bắt được phần nổi: trợ lý vẫn đọc soát bằng mắt.

Quy ước mặc định của xưởng (giữ, hoặc đổi nếu bạn muốn khác):

- Tiêu đề: sentence case (chỉ viết hoa chữ đầu câu và tên riêng), hoặc FULL-CAP cho nhãn ngắn, tên chương trình. Không Title Case (Viết Hoa Mọi Chữ Đầu).
- Dấu gạch: gạch ngang thường (-) hoặc dấu hai chấm; không gạch dài. Dấu nháy thẳng "...", ba chấm gõ tay (...).
- Thuật ngữ tiếng Anh: viết thuần Việt, từ gốc trong ngoặc vuông, ví dụ "trí tuệ cảm xúc [emotional intelligence]"; ngoặc tròn cho chú thích thông tin. Hoặc viết thuần Anh; không trộn tuỳ tiện.
- Không emoji trên web, trừ khi bạn muốn.

Của riêng bạn:

- Xưng hô với người xem: [bạn, anh chị, quý phụ huynh...].
- Từ ngữ PHẢI viết đúng (tên chương trình, thuật ngữ nghề): [danh sách].
- Từ không bao giờ dùng: [danh sách; mỗi từ cũng được ghi vào `phong-cach/tu-ngu.json` để máy bắt].
- Mọi mô hình, công cụ của người khác: ghi tên tác giả. Dữ kiện (con số, năm, trích dẫn) có nguồn đối chiếu.
- Quảng bá: không doạ "bị bỏ lại phía sau"; không bịa khan hiếm, không nêu số ghế còn lại; cho chọn ngày cụ thể; kết bằng một câu hỏi mở thật.

## 5. Liên hệ và chân trang

Dữ liệu máy đọc ở `brand/brand.json` > `lienHe` (chủ quản, email, điện thoại, Zalo, địa chỉ). Dòng còn trống thì web tạo ra để chỗ `[[...]]` và `kiem-web.py --len` chặn đưa lên mạng tới khi điền. Logo: [có / chưa]; ghi chú dùng logo: [nền nào dùng bản nào].

## 6. Sổ tay góp ý đã chốt

Một góp ý lặp lại lần thứ hai là tín hiệu sửa nguồn mặc định (khuôn, `he-thong/nen.css`, `brand/brand.json`, `chuan/`), không chỉ sửa web đang làm. Mỗi dòng: ngày - điều đã góp ý - đã sửa ở đâu.

- [ngày] - Thiết lập xưởng lần đầu.

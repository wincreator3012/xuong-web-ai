# 08. Pháp lý Việt Nam cho web nhỏ

Tài liệu tóm lược để xưởng tư vấn đúng hướng và soạn nháp đúng chỗ; KHÔNG phải ý kiến pháp lý. Người dùng đọc, sửa và tự quyết; trường hợp bán hàng trực tuyến, thu dữ liệu sức khoẻ, tâm lý hoặc số lượng lớn thì hỏi luật sư, kế toán. Nguồn và mức tin cậy từng điểm: nghien-cuu/C-ten-mien-email-phap-ly.md phần 4 (kiểm 07/10/2026; phụ lục A liệt kê 10 điểm còn cần đối chiếu nguyên văn).

## 1. Dữ liệu cá nhân (áp cho mọi web có form)

Văn bản: Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Nghị định 356/2025/NĐ-CP, cùng hiệu lực 01/01/2026; Nghị định 13/2023 không còn hiệu lực. Hộ kinh doanh, doanh nghiệp siêu nhỏ được miễn lập hồ sơ đánh giá tác động và bố trí nhân sự chuyên trách, nhưng KHÔNG miễn các nghĩa vụ dưới đây; xử lý dữ liệu nhạy cảm (trong đó có sức khoẻ hiểu rộng) thì không được miễn.

Việc tối thiểu, đã có sẵn trong khuôn:
1. Chỉ hỏi ô thật cần (thường là họ tên, email, điện thoại).
2. Nói rõ mục đích ngay cạnh form.
3. Ô đồng ý không đánh dấu sẵn, mỗi mục đích một ô; "im lặng hoặc không phản hồi không được coi là sự đồng ý".
4. Lưu bằng chứng đồng ý (nen.js ghi nội dung câu đồng ý, thời điểm, phiên bản chính sách).
5. Trang chính sách bảo vệ dữ liệu (khuôn `he-thong/trang-chung/chinh-sach-bao-mat.html`): ai kiểm soát dữ liệu, thu gì, để làm gì, lưu ở đâu (nêu dịch vụ nước ngoài), giữ bao lâu, ai xem, quyền của người dùng và cách liên hệ, ngày cập nhật.
6. Rút lại đồng ý dễ như khi đồng ý (liên kết huỷ nhận trong mỗi thư, một địa chỉ email nhận yêu cầu).
7. Tài khoản chứa dữ liệu bật xác thực hai lớp; không chia sẻ bảng tính công khai; xoá dữ liệu khi hết mục đích.
8. Không mua bán, trao đổi danh sách.

Lưu ý riêng lĩnh vực tâm lý, giáo dục, coaching: câu hỏi về cảm xúc, sức khoẻ tâm thần trong form công khai có thể là dữ liệu nhạy cảm. Tách bảng hỏi sàng lọc khỏi form đăng ký; trắc nghiệm tự đánh giá mặc định không lưu kết quả (khuôn `trac-nghiem`). Lưu biểu mẫu trên dịch vụ nước ngoài (Google Sheets, Firebase, Web3Forms) về bản chất là chuyển dữ liệu ra nước ngoài; thu thập nhiều thì hỏi luật sư về hồ sơ chuyển dữ liệu xuyên biên giới.

## 2. Cookie và đo lường

Pháp luật Việt Nam không có quy định riêng tên "cookie", nhưng cookie theo dõi gắn với một người thuộc phạm vi Luật Bảo vệ dữ liệu cá nhân. Cách đơn giản nhất: không dùng cookie theo dõi (Cloudflare Web Analytics). Dùng Google Analytics, Meta Pixel thì cần hộp hỏi đồng ý có nút Đồng ý và Từ chối ngang hàng, chỉ tải mã theo dõi sau khi đồng ý; kiem-web cảnh báo khi thấy mã theo dõi. Phông chữ tự lưu trữ (xưởng đã làm) để không gửi địa chỉ IP người xem cho bên thứ ba.

## 3. Thông báo website thương mại điện tử với Bộ Công Thương

Văn bản: Luật Thương mại điện tử số 122/2025/QH15 và Nghị định 248/2026/NĐ-CP, hiệu lực 01/7/2026; web đã thông báo trước ngày này dùng tiếp tới 30/6/2027. Nền tảng có chức năng **đặt hàng trực tuyến** phải thông báo trên online.gov.vn trước khi hoạt động (người dùng tự làm: tạo tài khoản thương nhân, khai báo web, nhận biểu tượng "Đã thông báo").

| Loại web | Phải thông báo? |
|---|---|
| Hồ sơ cá nhân, blog, giới thiệu dịch vụ chỉ có nút liên hệ, Zalo | thường không |
| Đăng ký sự kiện miễn phí | nhiều khả năng không |
| Đăng ký có thanh toán trên trang, chọn gói, giỏ hàng | nhiều khả năng có |

Ranh giới chưa rõ (ví dụ form đăng ký kèm mã chuyển khoản): xưởng gắn cờ trong BRIEF.md và khuyên người dùng hỏi luật sư; không tự kết luận.

## 4. Giấy phép trang thông tin điện tử

Nghị định 147/2024/NĐ-CP khoản 2 Điều 24: trang cá nhân, trang nội bộ, trang cung cấp dịch vụ chuyên ngành không phải xin giấy phép. Web đăng lại, tổng hợp tin từ báo chí và nguồn khác theo kiểu trang tin thì cần giấy phép trang tổng hợp. Nguyên tắc dễ nhớ: viết nội dung của chính mình thì không cần giấy phép.

## 5. Thông tin ở chân trang

Nghị định 174/2026/NĐ-CP (hiệu lực 01/7/2026) phạt 10-20 triệu đồng khi trang thông tin điện tử thiếu hoặc sai thông tin chủ quản (tên, địa chỉ liên lạc, email, điện thoại, người chịu trách nhiệm nội dung); phạm vi áp cho mọi loại trang còn cần đối chiếu. Chi phí gần như bằng không, nên mọi khuôn đều có chân trang đủ các dòng này (`brand/brand.json` > `lienHe`).

## 6. Bản quyền, hình ảnh

- Phông Google Fonts, Fontsource: giấy phép SIL OFL, dùng thương mại được (xưởng giữ tệp OFL.txt kèm phông).
- Ảnh Unsplash: dùng thương mại miễn phí, không bắt ghi công; ảnh có người rõ mặt dùng quảng cáo thì cân nhắc quyền hình ảnh.
- Ảnh lấy từ Google Hình ảnh, Facebook, báo: mặc định có bản quyền, không dùng.
- Ảnh học viên, khách hàng: vừa là quyền hình ảnh vừa là dữ liệu cá nhân, cần sự đồng ý bằng văn bản hoặc dạng điện tử.
- Lời chứng thực: lời thật, tên thật, có sự đồng ý của người nói.
- Mô hình, công cụ, bảng hỏi, thang đo của người khác: ghi tác giả; thang đo có bản quyền thì xin phép trước khi đưa lên web.

## 7. Thu tiền và thuế

Từ 01/01/2026 bỏ thuế khoán với hộ kinh doanh; ngưỡng doanh thu không chịu thuế GTGT, TNCN nâng lên 1 tỷ đồng/năm (Nghị định 141/2026); hộ kinh doanh phải thông báo mọi tài khoản ngân hàng, ví điện tử dùng nhận tiền kinh doanh (Nghị định 68/2026, Thông tư 18/2026). Cá nhân chưa đăng ký kinh doanh có được nhận học phí vào tài khoản cá nhân không là câu hỏi thuế: hỏi kế toán. Web của tổ chức thì dùng tài khoản tổ chức.

## 8. Tiếp cận cho người khuyết tật

Thông tư 26/2020/TT-BTTTT khuyến khích (với đa số tổ chức, cá nhân) áp dụng tiêu chuẩn hỗ trợ người khuyết tật tiếp cận thông tin. Xưởng lấy WCAG 2.2 AA làm sàn cho mọi web (chuan/05). Bán khoá học, dịch vụ trực tuyến cho người tiêu dùng ở Liên minh châu Âu và không thuộc diện doanh nghiệp siêu nhỏ thì thuộc Đạo luật Tiếp cận châu Âu (2025).

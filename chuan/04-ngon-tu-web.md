# 04. Ngôn từ web

Chữ trên web là phần người đọc gặp trước tiên và nhớ lâu nhất. Chuẩn này gồm ba lớp: quy ước nền (bất biến), khung chống văn AI cho tiếng Việt rút gọn cho web, và quy tắc riêng từng vùng trang. Tên, chức danh, từ ngữ phải viết đúng của người dùng nằm ở `phong-cach/PHONG-CACH.md` mục 1 và 4; từ cấm máy tự bắt nằm ở `phong-cach/tu-ngu.json` (cùng luật chung trong `tools/chung.py`).


## 1. Quy ước nền (bất biến)

- Thuần Việt, thuật ngữ tiếng Anh quan trọng để trong ngoặc vuông ở lần đầu: an toàn tâm lý [psychological safety]. Hoặc viết thuần Anh cho web tiếng Anh. Không xen hai thứ tiếng tuỳ tiện.
- Ngoặc tròn cho chú thích thông tin (như thế này); ngoặc vuông cho thuật ngữ gốc hoặc dịch nghĩa.
- Không gạch dài (em dash); dùng gạch ngang thường (-) hoặc dấu hai chấm. Nháy thẳng "...", ba chấm gõ tay (...). Khoảng giá trị viết 12-15.
- Tiêu đề sentence case, hoặc FULL-CAP cho nhãn ngắn. Không Title Case.
- Không emoji trên trang.
- Web công khai kết bằng một câu hỏi mở thật hoặc một lời mời có chiều sâu, không "Hy vọng trang này hữu ích".
- Mọi mô hình, công cụ, bảng hỏi của người khác: ghi tên tác giả. Mọi con số, lời chứng thực, tên đơn vị: thật và kiểm chứng được. Không bịa.

## 2. Tám tầng dấu hiệu văn AI, bản cho web

| Tầng | Dấu hiệu cần gỡ | Sửa thành |
|---|---|---|
| Từ vựng | hành trình, kỷ nguyên, chìa khoá, bí quyết, lăng kính, cánh cửa; đột phá, vượt trội, liền mạch, toàn diện, then chốt; kiến tạo, vun đắp, chinh phục, khai phá, phát huy tối đa; vô cùng, cực kỳ | từ cụ thể chở thông tin: việc làm được, con số, tên |
| Cụm sáo | "Trong bối cảnh...", "Trong thời đại số...", "Hãy cùng...", "Đừng bỏ lỡ", "Người bạn đồng hành", "Mang lại trải nghiệm...", "Hơn bao giờ hết", "Tóm lại" | mở bằng quan sát, ví dụ, luận điểm; kết tại chỗ ý tự nhiên kết |
| Cú pháp | "không chỉ... mà còn" (tối đa một lần cả trang), câu mở bằng danh ngữ trừu tượng ("Việc ứng dụng..."), bị động kiểu Anh ("được xem là"), bộ ba cứng (ba tính từ, ba lợi ích, ba thẻ) | câu chủ vị rõ chủ ngữ; số lượng theo nội dung thật |
| Diễn ngôn | công thức định nghĩa, liệt kê, nhắc lại, tương lai mơ hồ; lặp một ý bằng lời khác; "Trong phần này..." | mỗi phần một ý mới; đoạn dài ngắn có nhịp |
| Dấu câu, định dạng | gạch dài, nháy cong, ba chấm Unicode; gạch đầu dòng + chữ đậm + hai chấm cho văn xuôi; in đậm mọi thuật ngữ | xem mục 4 |
| Giọng | lịch sự thái quá, khen quá, hùng biện rỗng, "các chuyên gia cho rằng" không nguồn, "chúng ta" mơ hồ | nói thẳng, có vị thế, dẫn nguồn thật |
| Chất liệu | khẳng định đúng với mọi chủ đề, thiếu ví dụ riêng, dàn trải năm ý nông | một hai ý sâu, chi tiết thật, câu chuyện thật |
| Diễn đạt Việt | kết hợp từ sai ("khép chương trình"), ràng buộc giả ("viết một từ"), từ đơn tiết cụt ("nhẹ" thay "nhẹ nhàng"), dịch sát tiếng Anh | đọc to: người Việt có nói câu này không? |

Máy (`tools/kiem-web.py`) chỉ bắt phần nổi (từ, cụm, dấu câu, Title Case). Claude vẫn đọc soát từng câu bằng mắt.

## 3. Giọng theo vùng trang

| Vùng | Giọng | Đúng | Sai |
|---|---|---|---|
| Mở đầu | ai, làm gì, cho ai trong 5 giây; danh xưng + một câu cụ thể | "Lớp kỹ năng lắng nghe cho quản lý cấp trung, hai ngày, học bằng tình huống của chính bạn." | "Khai phá tiềm năng lãnh đạo trong kỷ nguyên mới" |
| Thân trang | người thầy trò chuyện với người học, không phải bài báo khoa học | "Bạn đã có sẵn năng lực. Chương trình tạo điều kiện để bạn nhận ra nó." | "Chương trình mang lại giá trị vượt trội" |
| Số liệu, năng lực | dữ kiện, không tính từ | "Hơn 500 học viên từ 2019" (khi đúng) | "Hàng nghìn người đã thay đổi cuộc đời" |
| Nút | động từ cụ thể 2-5 từ, nói điều sẽ xảy ra | "Gửi đăng ký", "Đặt lịch trao đổi", "Đọc thử một chương" | "Submit", "Click vào đây", "ĐĂNG KÝ NGAY!!!" |
| Thông báo lỗi | ngắn, nói cách sửa, không đổ lỗi | "Số điện thoại cần 10 chữ số, ví dụ 0903 123 456." | "Dữ liệu không hợp lệ" |
| Trạng thái | báo điều đang xảy ra và điều tiếp theo | "Đã nhận đăng ký. Thư xác nhận gửi trong 24 giờ làm việc." | "Thành công!" |
| Chân trang | thông tin, không khẩu hiệu | tên chủ quản, email, điện thoại, người chịu trách nhiệm nội dung | |

## 4. Gạch đầu dòng hay văn xuôi

- Được dùng danh sách, thẻ khi nội dung là danh sách thật có cấu trúc song song: bảng giá, quyền lợi gói, các bước, thông số, lịch trình.
- Bắt buộc văn xuôi 2-3 đoạn khi là lập luận, câu chuyện: phần "vì sao", triết lý, mô tả vấn đề.
- Thẻ có tiêu đề + mô tả: tiêu đề là cụm danh từ thật, mô tả 1-3 câu trọn vẹn.

## 5. Chân thật cấu trúc [structural honesty]

- Khan hiếm chỉ khi có thật, kèm lý do ("Lớp giới hạn số người để mỗi người được thực hành 1-1"); không nêu số ghế còn lại; không đếm ngược giả.
- Không khung "đua tranh, bị bỏ lại"; không khơi cảm giác tội lỗi; không bán thêm lộ liễu trên trang đích.
- Minh bạch: dành cho ai, KHÔNG dành cho ai, giá bao nhiêu hoặc cơ chế tính giá, chính sách hoàn phí.
- Cho chọn ngày cụ thể thay vì tả tần suất lặp lại ("Khai giảng 12/11 hoặc 3/12" thay vì "khai giảng hằng tháng").

## 6. Chữ cho máy đọc (Google, Zalo, Facebook, trình đọc màn hình)

- `<title>` dưới 60 ký tự: "Tên trang | Tên thương hiệu". Mô tả dưới 155 ký tự, một câu nói rõ trang giúp ai làm gì. Hai dòng này hiện khi chia sẻ link qua Zalo, Facebook: viết như viết lời mời.
- `alt` của ảnh: tả điều ảnh cho thấy và vì sao nó ở đó ("Người hướng dẫn cùng nhóm học viên thực hành lắng nghe tại lớp tháng 9"); ảnh trang trí thì `alt=""`.
- Liên kết nói đích đến ("Đọc chính sách bảo vệ dữ liệu"), không "tại đây".
- Ảnh chia sẻ 1200x630: tiêu đề ngắn, một dòng phụ, tên thương hiệu (`tools/anh-chia-se.py`).

## 7. Câu đồng ý và chính sách dữ liệu

- Câu đồng ý nói rõ ai dùng, dùng làm gì, dẫn tới chính sách: "Tôi đồng ý để [tên] dùng thông tin trên để xác nhận đăng ký và gửi hướng dẫn tham gia, theo chính sách bảo vệ dữ liệu." Mỗi mục đích một ô; ô không đánh dấu sẵn.
- Chính sách dữ liệu viết bằng lời thường (khuôn: `he-thong/trang-chung/chinh-sach-bao-mat.html`), chủ web đọc và tự quyết.

## 8. Danh sách soát chữ trước khi trình

- [ ] Tên, chức danh đúng nguyên văn PHONG-CACH mục 1; từ ngữ phải viết đúng ở mục 4.
- [ ] Không còn `[[...]]`; không gạch dài, nháy cong, Title Case (máy kiểm).
- [ ] Đọc to từng phần: câu nào người Việt không nói như vậy thì viết lại.
- [ ] Mỗi con số, lời chứng thực, tên đơn vị, mô hình của người khác có nguồn, có ghi công.
- [ ] Mở đầu trả lời "ai, làm gì, cho ai" trong 5 giây; kết bằng câu hỏi mở thật hoặc lời mời.

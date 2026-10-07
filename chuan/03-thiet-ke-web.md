# 03. Thiết kế web

Chuẩn thiết kế chung cho mọi web của xưởng. Màu, phông cụ thể của từng thương hiệu nằm ở `brand/brand.json` > `chuDe` (đã kiểm tương phản bằng `tools/tuong-phan.py`); lớp giao diện dùng chung nằm ở `he-thong/nen.css`. Tài liệu này nói cách nghĩ và các bất biến.


## 1. Năm nguyên tắc bất biến

1. **Khoảng trống có chủ đích [ma].** Khoảng trống chiếm 40-50% mỗi màn hình đọc; nó định nhịp, cho từng ý được thấm. Ngoại lệ có chủ đích: trang công cụ, tra cứu (khoảng trống phục vụ việc quét, không để trình diễn).
2. **Mỗi phần một ý.** Phải nói hai điều thì tách hai phần.
3. **Chữ làm chủ đạo.** Sức mạnh thị giác đến từ chữ, cấu trúc, khoảng trống, ảnh thật; không đến từ hình trang trí.
4. **Tiết chế.** Mỗi yếu tố có lý do tồn tại; bỏ đi mà nghĩa không đổi thì bỏ. Muốn thêm thì hỏi: làm sao cho cái đang có tinh hơn?
5. **Tương tác êm [calm interaction].** Đòi lượng chú ý nhỏ nhất: không cửa sổ bật lên, không tự phát âm thanh, video, không đếm ngược giả, không biểu tượng nhấp nháy.

## 2. Kế hoạch trước, mã sau

Trước khi dựng, Claude viết `THIET-KE.md` 10-15 dòng cho người dùng duyệt (chốt thứ hai): mood và biến thể, chủ đề màu, khối tối đặt ở đâu, cặp phông, bố cục từng phần theo thứ tự, chất liệu đặc trưng của lĩnh vực (ảnh thật nào, sơ đồ nào), **một điểm nhớ duy nhất** (chỗ dồn sự táo bạo), những gì cố ý không dùng. Nguồn: skill frontend-design của Anthropic và hướng dẫn thực hành Claude Code (nghien-cuu/D mục 4.2).

## 3. Màu

- Nền sáng là mặc định (web đọc dài). Khối tối dùng tối đa 1-2 lần, ở vị trí có chủ đích (mở đầu trang hồ sơ, lời mời cuối trang, chân trang), không xen sáng tối liên tục như ngựa vằn. Chủ đề tối cả trang (`than-dong`, `dem-vang`) chỉ khi có lý do (sự kiện buổi tối, bộ nhận diện đã tối).
- Tỉ lệ 60-30-10: nền khoảng 60-70%, chữ và cấu trúc khoảng 30%, màu nhấn dưới 10% (nút chính, liên kết, 1-2 từ khoá, đường kẻ điểm nhấn).
- Một web một chủ đề. Đổi màu riêng cho một web: sửa `assets/css/tokens.css` của web đó, kiểm lại bằng `tools/kiem-web.py`.
- Vai màu (khai trong brand.json, nen.css dùng): `nen`, `nenPhu`, `nenO` (ô nhập), `chu`, `chuPhu`, `nhan` (nền nút chính), `nhanDam`, `nhanChu` (chữ trên nút), `lienKet` (liên kết, nhãn mục, chữ nhấn nhỏ), `cauTruc` (tiêu đề phụ, số liệu, bảng), `vien`, `vienO`, `loi`, nhóm `toi*` cho khối tối, `vang` (trích dẫn trên nền tối).
- Mức tương phản bắt buộc (WCAG 2.2 AA, xưởng nâng chữ chính lên 7:1): chữ chính 7:1, chữ phụ và liên kết 4.5:1, viền ô nhập 3:1. Màu tươi (vàng, xanh lá sáng) chỉ làm nền nút hoặc chữ trên nền tối, không làm chữ trên nền sáng.
- Không truyền thông tin chỉ bằng màu (lỗi form có chữ nói cách sửa, không chỉ viền đỏ).

## 4. Chữ

- Hai họ phông, đủ dấu tiếng Việt, tự lưu trữ trong `fonts/`: phông tiêu đề (Lora, Playfair Display) và Be Vietnam Pro cho nội dung. Không thêm họ thứ ba.
- Cỡ chữ thân 18 px (sàn 16 px), dòng 1.7 (sàn 1.6: dấu tiếng Việt hai tầng cần khoảng thở), tiêu đề lớn 1.2-1.3. Cột văn xuôi tối đa khoảng 68 ký tự (`.cot-van`).
- Không giãn chữ âm [negative letter-spacing] cho tiếng Việt; chữ in hoa có dấu không nhỏ hơn 14 px; không căn đều hai bên; văn bản căn trái (chỉ trích dẫn, lời mời cuối được căn giữa).
- Tiêu đề: sentence case, hoặc FULL-CAP cho nhãn nhỏ trên tiêu đề [eyebrow]. Tuyệt đối không Title Case.
- In đậm rất kiệm: 1-2 cụm mỗi khối, không đậm cả câu.
- Tiêu đề lớn tự cân dòng (`text-wrap: balance`); câu mở đầu có thể ngắt dòng chủ ý tại điểm ngắt tự nhiên.

## 5. Bố cục

- Thiết kế cho 390 px trước, mở rộng ở 640 px và 1024 px. Lề 20 px trên điện thoại, 40 px trở lên trên máy tính.
- Khung nhiều cột 1120 px (`.khung`), cột văn 720 px (`.cot-van`). Một cột là mặc định; 2-3 cột chỉ khi nội dung thật sự song song (bảng giá, thẻ dịch vụ).
- Mỗi phần: nhãn nhỏ, tiêu đề, nội dung. Phần liền kề đổi kiểu bố cục (văn một cột, hai cột lệch, thẻ, trích dẫn lớn); không lặp một kiểu ba lần liên tiếp; không căn giữa mọi phần.
- Không quá ba cỡ chữ chính trên một màn hình.
- Trang một mục tiêu (trang đích, báo giá): không thanh điều hướng, chỉ tên hoặc logo và một nút; nút nổi cuối màn hình điện thoại (`.nut-dinh`).
- Trang có điều hướng (hồ sơ, web nhiều trang): tối đa 6 mục, không menu khổng lồ.

## 6. Thành phần (đều có sẵn trong nen.css)

| Thành phần | Lớp | Quy tắc |
|---|---|---|
| Nút chính, phụ, dạng chữ | `.nut`, `.nut--phu`, `.nut--chu` | một hành động chính mỗi màn hình; cao từ 48 px; chữ là động từ cụ thể 2-5 từ, không VIẾT HOA, không "Bấm vào đây" |
| Thẻ | `.the`, `.the--phu` | phẳng, viền 1 px hoặc nền phụ; bo 8 px (tối đa 12 px); không bóng nặng |
| Lưới | `.luoi--2/3/4`, `.hai-cot` | số thẻ theo nội dung thật (2, 4, 5 đều được, không ép về 3) |
| Số liệu | `.so-lieu` | chỉ số liệu thật, kiểm chứng được |
| Trích dẫn lớn | `.trich` | phông tiêu đề nghiêng, không biểu tượng ngoặc kép khổng lồ |
| Cảm nhận | `.cam-nhan` | trích nguyên văn 2-4 câu, tên đầy đủ, vai trò thật, có sự đồng ý của người nói; không ảnh đại diện minh hoạ |
| Các bước | `ol.buoc` | danh sách thật, đánh số |
| Gói, giá | `.goi`, `.goi--chon` | tối đa 7 dòng mỗi gói; dấu "được chọn nhiều" chỉ khi đúng |
| Hỏi đáp | `.hoi-dap details` | mở sẵn câu đầu |
| Biểu mẫu | `.bieu-mau`, `.o`, `.dong-y`, `.mat-ong` | nhãn luôn hiện (không thay bằng placeholder), ô cao từ 48 px, lỗi nói cách sửa, ô đồng ý không đánh dấu sẵn, bẫy rác |
| Mã chuyển khoản | `.qr` + `img[data-vietqr]` | có số tiền, nội dung có mã đơn, nút chép |
| Khung ảnh chờ | `.cho-anh` | chỉ trong bản nháp; kiem-web chặn khi đưa lên mạng |

## 7. Chuyển động

- 200-400 ms, êm dần [ease-out]; chỉ hai kiểu: hiện dần và dịch lên 10 px khi cuộn tới (`.hien`), mỗi phần một lần.
- Hiện dần chỉ áp khi JS chạy (`html.js`), nên tắt JS, in, trình đọc màn hình vẫn thấy đủ nội dung.
- Luôn tôn trọng `prefers-reduced-motion`. Cấm: thị sai [parallax], hoạt ảnh lặp vô tận, con trỏ tuỳ biến, hiệu ứng gõ chữ, số nhảy đếm.

## 8. Hình ảnh

- Thứ tự ưu tiên: khoảng trống và chữ; sơ đồ khi diễn đạt được bằng cấu trúc; ảnh thật của người, lớp học, sự kiện (tông ấm, không bão hoà cao); không có gì cả còn hơn ảnh kho [stock].
- Cấm ảnh kho chung chung (người cầm máy tính mỉm cười), cấm ảnh AI thay cho người thật, lớp thật, sự kiện thật, cấm ảnh lấy trên mạng không có quyền dùng.
- Ảnh WebP (hoặc AVIF), rộng tối đa 1600 px, luôn khai `width` `height`, `loading="lazy"` cho ảnh dưới màn hình đầu (không cho ảnh lớn nhất màn đầu), `alt` mô tả thật.
- Ảnh và sơ đồ có thể làm ở xưởng thiết kế (khổ ảnh web, ảnh chia sẻ 1200x630, sơ đồ tri thức) rồi chép vào `public/assets/img/`.
- Biểu tượng: một bộ nét mảnh 1.5 px (như Lucide), 20-24 px, màu `cauTruc` hoặc `chuPhu`; không biểu tượng nhiều màu, không emoji.

## 9. Danh sách cấm (dấu hiệu "web làm bằng AI" và "web rẻ tiền")

1. Nền chuyển sắc tím xanh và mọi chuyển sắc nền mặc định; kính mờ [glassmorphism], phát sáng neon.
2. Đường gạch ngắn màu nhấn dưới tiêu đề.
3. Ba thẻ biểu tượng đều tăm tắp lặp suốt trang; biểu tượng 3D bóng bẩy; emoji ở tiêu đề, gạch đầu dòng.
4. Bóng đổ nặng trên mọi thẻ; bo góc quá 12 px; một bán kính bo và một bóng xám cho mọi thứ.
5. Đồng hồ đếm ngược, cửa sổ giữ chân khi rời trang, khung chat nhấp nháy, thông báo "X người vừa mua".
6. Huy hiệu "AI-powered", ngôi sao lấp lánh.
7. Sáng tối xen kẽ máy móc; mọi phần đều căn giữa.
8. Chữ xám nhạt "cho đẹp" rớt chuẩn tương phản.
9. Title Case tiếng Việt ở bất cứ đâu.
10. Năm cụm giao diện mặc định của mô hình AI (skill frontend-design của Anthropic, 2025-2026): nền kem + serif tương phản cao + nhấn đất nung; nền gần đen + một màu nhấn chói; kiểu báo giấy kẻ mảnh, bo 0; bộ thẻ SaaS giống hệt nhau; "khung mẫu" với nhãn monospace VIẾT HOA giãn chữ trên mọi khối, dấu chấm giữa ngăn cách, mũi tên sau mọi liên kết (nhãn mục `.nhan-muc` của nen.css vẫn được dùng: một nhãn mỗi phần, phông nội dung, không kèm dấu chấm giữa). Cùng họ: nhấn một từ trong mọi tiêu đề bằng nghiêng hoặc đậm, hiệu ứng trượt hiện và di chuột cho mọi thứ.


## 10. Biến thể theo loại trang

| Loại | Mood | Cách pha |
|---|---|---|
| Báo giá, dịch vụ cho tổ chức | tin cậy | `cauTruc` làm chủ (tiêu đề phụ, bảng giá, số liệu); khối tối ở mở đầu; không vàng kim |
| Trang đích sản phẩm tri thức | ấm và mời gọi | nhấn làm chủ; nền phụ cho khối trích đoạn; một khối tối duy nhất ở lời mời cuối |
| Hồ sơ cá nhân | chiêm nghiệm | mở đầu hoặc chân trang nền tối với trích dẫn màu `vang`; thân trang sáng |
| Công cụ, tra cứu, ứng dụng | trung tính | gần như đơn sắc; nhấn chỉ cho trạng thái tương tác; không khối tối, không mở đầu lớn |

Nếu Claude tự chọn mood, bố cục thay người dùng: ghi lý do vào THIET-KE.md và nói khi trình.

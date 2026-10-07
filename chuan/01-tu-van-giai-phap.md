# 01. Tư vấn giải pháp: từ nhu cầu tới giải pháp đơn giản nhất đủ dùng

Phần lớn người nhờ làm web chưa biết mình cần web loại nào, và thường xin nhiều hơn mức cần (đăng nhập, quản trị, ứng dụng) hoặc ít hơn mức cần (một trang không có cách nhận đăng ký). Việc của xưởng ở bước này giống việc của người thầy thuốc giỏi: nghe kỹ, hỏi đúng, rồi kê đơn ít thuốc nhất mà khỏi bệnh. Nền lý thuyết: giai đoạn khám phá [discovery] của Nielsen Norman Group, công việc cần làm [jobs-to-be-done] của Christensen và cộng sự (2016), nội dung trước [content-first] của Halvorson, ưu tiên MoSCoW của DSDM, nguyên tắc "làm ít hơn" [do less] của GOV.UK và quy tắc sức mạnh tối thiểu [rule of least power] của W3C (nguồn đầy đủ: nghien-cuu/D-loai-web-quy-trinh-chuan.md mục 2).

## 1. Năm bước, hai chốt

1. **Lắng nghe.** Hỏi theo bộ 15 câu ở mục 2, tối đa 4 câu mỗi lượt, luôn kèm phương án sẵn và một mặc định. Câu nào trả lời được từ tư liệu người dùng đưa (bài đăng, outline khoá học, web cũ) thì không hỏi lại.
2. **Phân loại.** Xếp nhu cầu vào một (hoặc hai, khi lai) trong 12 loại web (chuan/02-loai-web.md) và một bậc hạ tầng (mục 3).
3. **Đề xuất.** Trình 1-2 phương án, mỗi phương án một bảng ngắn: làm được gì, không làm gì, chi phí mỗi năm, những việc người dùng phải tự tay làm (tạo tài khoản, mua tên miền), rủi ro. Nói rõ phương án Claude khuyên và vì sao.
4. **Chốt brief (chốt thứ nhất).** Ghi vào `BRIEF.md` của dự án, gồm danh sách KHÔNG làm ở phiên bản này. Chưa chốt thì chưa dựng.
5. **Lộ trình.** Kế hoạch thiết kế (`THIET-KE.md`, chuan/03) để duyệt (chốt thứ hai), rồi dựng, kiểm, đưa lên mạng, gắn tên miền, bàn giao.

Người dùng vắng mặt hoặc nói "cứ làm": chọn phương án hợp lý nhất, ghi giả định vào mục 6 của BRIEF.md, nói rõ khi trình bản đầu.

## 2. Bộ 15 câu hỏi brief

Nhóm A, mục đích và người dùng:
1. Ai sẽ vào trang? Họ đến từ đâu (Facebook, Zalo, Google, mã QR trên tài liệu in, link gửi riêng)?
2. Khi vào, họ đang cố làm xong việc gì? Rời trang, họ cần đã làm được điều gì?
3. Một hành động chính duy nhất mong muốn (đăng ký, nhắn Zalo, đặt lịch, tải tài liệu, tra cứu)?
4. Sau 3 tháng, đo thành công bằng gì (số đăng ký, số tin nhắn, số lượt tra cứu)?

Nhóm B, nội dung:
5. Nội dung nào đã có (chữ, ảnh, logo, video, cảm nhận học viên, giá, lịch)? Phần thiếu ai viết, hạn khi nào?
6. Ba web bạn thích, một web bạn không thích (để rút ra gu, không sao chép)?
7. Màu, phông, giọng văn thương hiệu đã có chưa? (Có trong brand.json thì không hỏi.)

Nhóm C, chức năng và phạm vi:
8. Có cần thu dữ liệu không? Dữ liệu gì, lưu ở đâu, ai xem, giữ bao lâu?
9. Có cần thu tiền không? Chuyển khoản QR là đủ, hay cần đối soát tự động?
10. Có cần đăng nhập không? Nếu có: một nền tảng có sẵn (Substack, nền tảng khoá học, Google Classroom) làm được không?
11. Điều gì chắc chắn KHÔNG làm ở phiên bản này?

Nhóm D, vận hành:
12. Ai cập nhật nội dung sau khi bàn giao, bao lâu một lần, bằng cách nào (nhờ AI sửa, sửa Google Sheet, mời người biên tập)?
13. Tên miền đã có chưa? Tài khoản tên miền, nơi lưu trữ đứng tên ai?
14. Ngân sách duy trì mỗi năm (tên miền, dịch vụ form, email)?
15. Có bán hàng, thu tiền, hay thu dữ liệu sức khoẻ, tâm lý qua web không? (Có thì đọc chuan/08-phap-ly-vn.md trước khi đề xuất.)

Lượt hỏi gợi ý: lượt 1 câu 1-4; lượt 2 câu 5, 8-10; lượt 3 câu 11-15 (bỏ câu đã rõ).

## 3. Bốn bậc hạ tầng

| Bậc | Là gì | Dữ liệu nằm ở đâu | Ví dụ | Khuôn |
|---|---|---|---|---|
| 0 | tĩnh thuần: HTML, CSS, chút JS | không thu dữ liệu | hồ sơ, trang liên kết, tra cứu, trắc nghiệm không lưu | `trang-don`, `ho-so`, `lien-ket`, `tra-cuu`, `trac-nghiem` |
| 1 | tĩnh + dịch vụ nhúng | ở dịch vụ bên ngoài (Web3Forms, Tally, Cal.com, VietQR) | trang đích có đăng ký và mã chuyển khoản, báo giá, blog | `landing`, `bao-gia`, `site-astro` |
| 2 | backend nhẹ | Google Sheets qua Apps Script, hoặc một hàm nhỏ (Cloudflare Worker) | form tự thiết kế ghi thẳng vào Sheets, gửi thư xác nhận, nhận webhook thanh toán | `landing` + chuan/06 mục 2 |
| 3 | đăng nhập + cơ sở dữ liệu | Firebase (mặc định), Supabase khi cần SQL | sổ ghi chép học viên, bảng điều khiển nội bộ, bài thi | `app-firebase` |

Mỗi bậc lên là thêm tài khoản phải giữ, thêm chỗ có thể rò dữ liệu, thêm việc bảo trì. Bậc 3 bắt buộc làm đủ danh sách kiểm bảo mật của khuôn app trước khi có người dùng thật.

## 4. Cây quyết định "giải pháp đơn giản nhất"

1. Có cần web không, hay một bài ghim trên Facebook, Zalo OA, một trang Substack là đủ? Nếu đủ: nói thẳng, và vẫn giúp làm thứ đó cho tốt.
2. Có nền tảng có sẵn làm tốt việc này không (Substack cho bản tin, Cal.com cho đặt lịch, nền tảng khoá học cho khu thành viên trả phí)? Có: dùng và nhúng vào web.
3. Một trang tĩnh có đủ không? Đủ: bậc 0.
4. Chỉ cần nhận dữ liệu: biểu mẫu nhúng (bậc 1) trước, Apps Script (bậc 2) sau.
5. Chỉ khi cần đăng nhập, dữ liệu riêng của nhiều người, phân quyền: bậc 3.

Tầng kỹ thuật (chốt khi dựng xưởng 07/10/2026, bậc thang ba tầng): HTML tĩnh dùng nền chung là mặc định cho đa số; Astro 7 khi web có trên khoảng 10 trang cùng cấu trúc hoặc có blog; Firebase khi có đăng nhập và dữ liệu. Không dùng React, Next.js, Tailwind cho web mới trừ khi chủ web có lý do rõ (đã có đội kỹ thuật, đã có mã cũ).

## 5. Ma trận nhu cầu và giải pháp

| Nhu cầu | Đơn giản nhất | Khi lớn lên | Coi chừng |
|---|---|---|---|
| Form liên hệ, đăng ký | Web3Forms (250 lượt/tháng) + bẫy rác | Tally nhúng; Apps Script ghi Sheets | ô đồng ý dữ liệu không đánh dấu sẵn |
| Đăng ký có câu hỏi phức tạp, tải tệp | Tally nhúng nối Google Sheets | Tally Pro | dữ liệu nằm ở máy chủ EU của Tally |
| Thu học phí, vé | VietQR có số tiền và mã đơn, đối soát tay | SePay đẩy giao dịch vào Sheets | NĐ 68/2026: hộ kinh doanh khai báo tài khoản nhận tiền; hỏi kế toán |
| Đặt lịch 1:1 | Cal.com miễn phí | Calendly | thu tiền qua Stripe không dùng được ở Việt Nam |
| Bản tin | dẫn sang Substack đang viết | Kit miễn phí tới 10.000 người | không tự dựng danh sách email |
| Bình luận | dẫn về bài Facebook, Substack | giscus (độc giả kỹ thuật) | độc giả phổ thông không có GitHub |
| Người khác tự sửa nội dung | Pages CMS (mời qua email) | Sveltia CMS | Decap + Git Gateway đã ngừng phát triển |
| Lịch khai giảng, danh sách sự kiện đổi thường | Google Sheets xuất bản CSV | bộ sưu tập Astro + CMS | dữ liệu xuất bản là công khai |
| Đo lượt xem | Cloudflare Web Analytics + Google Search Console | Umami, Plausible | GA4 dùng cookie, cần hỏi đồng ý |
| Đăng nhập, dữ liệu riêng | Firebase Spark + luật viết sẵn | Supabase Pro khi cần SQL | Supabase Free tạm dừng sau 7 ngày yên ắng |
| Khu thành viên khoá học trả phí | nền tảng khoá học có sẵn | tự xây bậc 3 khi thật cần | thanh toán, phân quyền, bản quyền video |

Số liệu, đường dẫn từng dịch vụ: `chuan/kho-dich-vu.json`. Nguồn: nghien-cuu/B-du-lieu-dich-vu.md.

## 6. Ai sở hữu gì

- Tên miền, kho GitHub, nơi lưu trữ, dịch vụ form, email đều đứng tên CHỦ WEB, tạo bằng email của chủ web. Người làm hộ (kể cả Claude, kể cả chủ xưởng khi làm web cho đối tác) được mời vào làm cộng tác viên, xong việc thì gỡ.
- Với .vn, thông tin chủ thể phải đúng người thật (Nghị định 147/2024); khai sai là căn cứ thu hồi.
- Dữ liệu người dùng để lại trên web thuộc chủ web, với tư cách bên kiểm soát dữ liệu.
- Chi tiết bàn giao: huong-dan/12-ban-giao-cho-khach.md.

## 7. Chi phí duy trì thường gặp (kiểm 10/2026, đổi được)

| Hạng mục | Mức | Ghi chú |
|---|---|---|
| Lưu trữ web tĩnh | 0 đ | Cloudflare, Firebase Spark, GitHub Pages |
| Tên miền .com | khoảng 270.000 đ/năm (Cloudflare, Porkbun) | nhà đăng ký trong nước: năm đầu rẻ, gia hạn 299.000-369.000 đ |
| Tên miền .vn | khoảng 650.000-830.000 đ/năm khi gia hạn | phải mua qua nhà đăng ký trong nước |
| Email theo tên miền | 0 đ (Zoho Mail Free, 5 người) đến khoảng 220.000 đ/người/tháng (Google Workspace) | Gmail bỏ "Send as" địa chỉ ngoài từ 01/2027 |
| Form | 0 đ tới 250 lượt/tháng (Web3Forms) | |

Luôn nói giá gia hạn, không chỉ giá năm đầu.

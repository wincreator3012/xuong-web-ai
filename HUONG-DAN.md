# HƯỚNG DẪN SỬ DỤNG XƯỞNG WEB

Tài liệu cho việc hằng ngày, sau khi trợ lý AI đã dựng và thiết lập xưởng cho bạn. Đọc lướt một lần; về sau tra mục cần.

## 1. Một web đi qua những bước nào

1. **Bạn nói nhu cầu bằng lời thường**, kèm tư liệu nếu có (nội dung khoá học, bài đăng, ảnh, link web cũ, bảng giá).
2. **Trợ lý tư vấn**: hỏi vài lượt ngắn (ai xem, đến từ đâu, cần làm xong việc gì, có thu thông tin, thu tiền không, ai sẽ sửa web về sau), rồi đề xuất giải pháp đơn giản nhất đủ dùng, chi phí mỗi năm, những việc bạn phải tự tay làm. Có khi câu trả lời là "chưa cần web, một bài ghim hay một Google Form là đủ".
3. **Bạn duyệt bản tóm tắt yêu cầu** [brief] (chốt thứ nhất). Trợ lý tạo hồ sơ dự án trong `Du an/` và mã nguồn web trong `Web/`.
4. **Bạn duyệt kế hoạch thiết kế** 10-15 dòng (chốt thứ hai): chủ đề màu, phông, bố cục từng phần, điểm nhớ của trang.
5. **Trợ lý dựng, tự kiểm bằng máy, nhìn ảnh chụp ba khổ** (điện thoại, máy tính bảng, máy tính) rồi gửi bạn tờ tổng thể kèm vài dòng giải thích. Bạn góp ý bằng lời; muốn bấm thử thì mở `Xem web` (mục 5).
6. **Đưa lên mạng**: trợ lý chuẩn bị mọi thứ; bạn làm những bước chỉ bạn làm được (mục 4), trợ lý dẫn từng bước một.
7. **Bàn giao**: địa chỉ web, cách tự sửa những chỗ hay đổi (giá, ngày, link), hồ sơ vận hành `VAN-HANH.md` (web chạy ở đâu, tài khoản nào, khi nào gia hạn tên miền).

Sửa sẵn trong brief rẻ nhất; sửa sau khi đã lên mạng vẫn được, chỉ mất thêm một vòng kiểm.

## 2. Đặt yêu cầu thế nào

Một câu tốt có ba ý: **làm gì, cho ai, họ đến từ đâu và cần làm xong việc gì trên trang**.

| Bạn cần | Câu mẫu | Xưởng dùng |
|---|---|---|
| Trang giới thiệu bản thân, gửi đối tác | "Làm trang hồ sơ để gửi đối tác doanh nghiệp, có các chương trình tôi đang dạy và nút đặt lịch trao đổi" | khuôn `ho-so` |
| Một chỗ gom mọi đường dẫn ở tiểu sử Facebook, TikTok | "Làm trang liên kết: khoá học, bản tin, Zalo, kênh YouTube" | `lien-ket` |
| Quảng bá và nhận đăng ký khoá học, sự kiện | "Làm trang đăng ký hội thảo 20/12, có form và mã chuyển khoản học phí" | `landing` |
| Báo giá cho một tổ chức | "Làm trang báo giá chương trình đào tạo cho công ty X, gửi link riêng, không lên Google" | `bao-gia` |
| Thư viện bài tập, tài liệu cho học viên | "Học viên cần tra cứu 60 bài tập theo chủ đề và độ khó" | `tra-cuu` |
| Bài tự đánh giá | "Làm bài trắc nghiệm 20 câu để người đọc tự soi chiếu phong cách giao tiếp, không lưu kết quả" | `trac-nghiem` |
| Web nhiều trang, viết bài thường xuyên | "Tôi muốn có web có blog, tự viết bài được mà không cần biết code" | `site-astro` + Pages CMS |
| Ứng dụng có đăng nhập, dữ liệu riêng | "Học viên đăng nhập bằng Google để ghi nhật ký thực hành hằng tuần, tôi xem tổng hợp" | `app-firebase` |
| Thông báo ngắn, trang tạm | "Làm một trang thông báo lịch nghỉ Tết, có số điện thoại" | `trang-don` |

Đưa **chữ, số liệu, giá, lịch thật**. Chưa có thì để trợ lý đề xuất chữ, bạn duyệt. Không có số liệu, lời cảm nhận thật thì trợ lý để chỗ trống `[[...]]`, không bịa; web chưa điền hết chỗ trống thì không được đưa lên mạng.

## 3. Bốn bậc web và chi phí

| Bậc | Là gì | Ví dụ | Chi phí thường gặp mỗi năm |
|---|---|---|---|
| 0 | trang tĩnh, không thu thông tin | hồ sơ, trang liên kết, tra cứu, trắc nghiệm không lưu | 0 đ (chưa tính tên miền) |
| 1 | trang tĩnh + dịch vụ nhúng | form đăng ký, mã VietQR, đặt lịch, blog | 0 đ ở mức dùng nhỏ |
| 2 | có một phần chạy ngầm nhẹ | form ghi thẳng vào Google Sheets, thư xác nhận tự động | 0 đ ở mức dùng nhỏ |
| 3 | đăng nhập + cơ sở dữ liệu | sổ ghi chép học viên, bảng điều khiển nội bộ, bài thi | 0 đ ở gói miễn phí của Firebase; cần làm kỹ phần bảo vệ dữ liệu |

Tên miền: khoảng 270.000 đ một năm cho .com, 650.000-830.000 đ cho .vn (giá gia hạn, kiểm 10/2026). Email theo tên miền: từ 0 đ (Zoho Mail Free). Trợ lý luôn nói giá gia hạn, không chỉ giá năm đầu. Chi tiết và nguồn: `chuan/01-tu-van-giai-phap.md` mục 7.

Bậc càng cao càng nhiều việc phải giữ gìn. Trợ lý chọn bậc thấp nhất làm được việc, và nói rõ khi nào nên lên bậc.

## 4. Những việc chỉ bạn làm được

Trợ lý không làm thay được, và không bao giờ xin bạn mật khẩu hay mã xác thực:

- tạo tài khoản (GitHub, Cloudflare, Firebase, nhà đăng ký tên miền), bật xác thực hai lớp, cất mã khôi phục;
- thanh toán (tên miền, dịch vụ trả phí), khai thông tin chủ tên miền (.vn cần thông tin định danh đúng người thật);
- bấm cho phép kết nối (Cloudflare đọc kho GitHub, Google cấp quyền cho Apps Script);
- đưa mã lên GitHub (Commit, Push) bằng GitHub Desktop, hoặc cho phép trợ lý làm trong phiên;
- quyết định nội dung pháp lý (chính sách dữ liệu, câu đồng ý), và thủ tục với cơ quan nhà nước nếu web bán hàng.

Mỗi việc có một thẻ trong `huong-dan/` (danh mục: `huong-dan/README.md`). Trợ lý đọc thẻ và dẫn bạn từng bước, theo đúng màn hình bạn đang thấy; giao diện nhà cung cấp đổi thì trợ lý tra tài liệu chính thức và dẫn theo màn hình thật.

**Mọi tài khoản đứng tên bạn**, tạo bằng email của bạn. Người làm hộ (kể cả trợ lý, kể cả một người bạn rành kỹ thuật) được mời vào làm cộng tác viên, xong việc thì gỡ. Làm web cho khách: `huong-dan/12-ban-giao-cho-khach.md`.

## 5. Xem web trên máy bạn

- **Bấm đúp `Xem web`** trong thư mục xưởng `xuong-web-ai` (Mac: `Xem web.command`, Windows: `Xem web.bat`), gõ tên web khi được hỏi (hoặc Enter để chọn web làm gần nhất). Trình duyệt mở web; giữ cửa sổ đen mở trong lúc xem, đóng khi xong.
- Web một trang đơn giản: bấm đúp `Web/<tên-web>/public/index.html` cũng xem được. Trang tra cứu, trắc nghiệm, web nhiều trang thì cần cách thứ nhất.
- Xem trên điện thoại: chờ web lên mạng (thường là địa chỉ tạm miễn phí trước khi có tên miền), mở link trên điện thoại thật, bấm thử mọi nút, gửi thử form.

## 6. Phong cách của bạn

Tên, chức danh nguyên văn, chủ đề màu, logo, liên hệ, từ ngữ được thiết lập một lần, áp cho mọi web:

- `phong-cach/PHONG-CACH.md`: bản bạn đọc và sửa tay được.
- `brand/brand.json`: bản máy đọc (màu theo vai, thương hiệu, nhân vật, liên hệ); `phong-cach/tu-ngu.json`: từ bạn không bao giờ dùng, máy tự bắt.
- Muốn đổi: nói "đổi phong cách: ..." hoặc "từ nay ...". Trợ lý sửa cả hai bản, tạo thử một trang để bạn xem.
- Làm web cho đối tác, khách hàng: trợ lý thêm thương hiệu của họ (tên, logo, màu, liên hệ) vào `brand/brand.json`, không trộn với của bạn.
- Sáu chủ đề màu khởi đầu đều đã kiểm tương phản (chữ đọc êm trên điện thoại ngoài nắng). Chủ đề riêng pha từ màu logo cũng phải qua bộ kiểm đó.

## 7. Chữ và ảnh

- **Chữ là phần người đọc gặp trước tiên.** Trợ lý viết theo `chuan/04-ngon-tu-web.md`: thuần Việt có từ gốc trong ngoặc vuông khi cần, không Title Case, không sáo ngữ văn AI, không doạ "bị bỏ lại phía sau", không bịa khan hiếm. Máy bắt được phần nổi; trợ lý vẫn đọc soát từng chữ.
- **Ảnh thật**: chân dung, lớp học, sự kiện gửi bản gốc (không ảnh chụp màn hình, không ảnh đã nén qua ứng dụng nhắn tin). Xưởng không dùng ảnh do AI tạo thay người, lớp, sự kiện thật.
- **Ảnh chia sẻ** (ảnh hiện ra khi dán link vào Zalo, Facebook): xưởng tạo tự động một bản gọn từ tiêu đề và chủ đề màu; muốn đẹp hơn thì làm ở Xưởng thiết kế Claude (nếu bạn có) rồi chép vào web.
- Mọi mô hình, công cụ, thang đo của người khác nhắc trên web đều ghi tên tác giả; trợ lý sẽ nhắc nếu bạn quên.

## 8. Thư mục

Trong "Web AI": `xuong-web-ai/` (xưởng của bạn, dựng từ bản vẽ; đừng để gì khác vào đây), `Du an/` (hồ sơ từng dự án: `BRIEF.md`, `THIET-KE.md`, `SO-GOP-Y.md`, `VAN-HANH.md`, báo cáo kiểm và ảnh chụp trong `kiem/`), `Web/` (mã nguồn từng web; phần đưa lên mạng nằm trong `public/`, web nhiều trang thì trong `dist/` sau khi dựng). Gói skill để lưu vào tài khoản AI nằm ở `Du an/_skill/`. Muốn đổi chỗ đặt hai thư mục kia: nói với trợ lý ở đầu cuộc trò chuyện.

## 9. Dùng xưởng hiệu quả nhất

1. **Bắt đầu nhỏ và thật.** Một trang bạn cần trong tháng này, làm trọn một vòng tới lúc lên mạng, rồi mới làm web lớn.
2. **Nói ai xem, từ đâu tới**: "phụ huynh bấm link từ nhóm Zalo lớp", "phòng nhân sự nhận link qua email". Hai câu đó dẫn tới hai trang rất khác nhau.
3. **Một hành động chính mỗi trang**: đăng ký, nhắn Zalo, đặt lịch, tra cứu. Trang muốn người xem làm năm việc thường không được việc nào.
4. **Đưa chữ, giá, lịch thật sớm.** Thiết kế đẹp trên chữ mẫu hay vỡ khi chữ thật vào.
5. **Dành sức cho brief.** Đổi đối tượng, hành động chính, bậc web ở brief mất một câu; đổi sau khi dựng mất cả buổi.
6. **Góp ý cụ thể theo khổ**: "trên điện thoại nút đăng ký nằm thấp quá", "máy tính: ảnh to quá".
7. **Chê một lần rồi dặn "từ nay"** để xưởng ghi vào sổ tay và các web sau không lặp lại.
8. **Tên miền mua sớm, đứng tên bạn**, bật tự gia hạn. Mất tên miền là mất mọi đường dẫn đã chia sẻ.
9. **Giữ hồ sơ vận hành** (`VAN-HANH.md`): một năm sau bạn sẽ cần biết web chạy ở đâu, tài khoản nào.
10. **Thử web như người xem thật** trước khi gửi: điện thoại, mạng di động, bấm link từ Zalo.

## 10. Xưởng không làm gì

- Không tự tạo tài khoản, không thanh toán, không giữ mật khẩu thay bạn.
- Không làm cửa hàng trực tuyến đầy đủ (giỏ hàng, kho, cổng thanh toán thẻ), khu thành viên khoá học trả phí có video bảo vệ, ứng dụng điện thoại cài từ App Store: những việc này nên dùng nền tảng chuyên dụng; trợ lý nói thẳng và gợi ý cách gần nhất.
- Không bảo đảm thứ hạng Google; xưởng làm đúng phần kỹ thuật (tốc độ, cấu trúc, mô tả), phần còn lại là nội dung và thời gian.
- Không thay luật sư, kế toán: chuẩn pháp lý trong xưởng là tài liệu tham khảo cập nhật tới 10/2026.
- Web-app có dữ liệu nhạy cảm (sức khoẻ, trẻ em, tài chính) cần người có chuyên môn bảo mật rà lại trước khi dùng thật; xưởng có danh sách kiểm nhưng không thay được một lần rà độc lập.
- Windows ít được kiểm hơn Mac.

## 11. Câu nói nhanh

| Muốn | Nói |
|---|---|
| Làm web mới | "Làm [loại trang] cho [ai], họ đến từ [đâu] để [làm gì]" |
| Sửa web đang có | "Sửa web [tên]: đổi giá thành ..., thêm phần hỏi đáp" |
| Xem lại web | "Gửi tôi ảnh chụp web [tên] trên điện thoại" |
| Đưa lên mạng | "Đưa web [tên] lên mạng" |
| Gắn tên miền | "Tôi đã mua tên miền ..., gắn vào web [tên]" |
| Web không vào được | "Web [tên] không vào được, báo lỗi ..." |
| Kiểm an toàn web-app | "Kiểm bảo mật web-app [tên]" |
| Đổi phong cách | "Từ nay chức danh của tôi là ...", "đổi chủ đề màu mặc định sang ..." |
| Nghe lại giới thiệu | "Giới thiệu lại xưởng" |
| Kiểm toàn bộ xưởng | "Kiểm tra xưởng" |
| Nhận bản mới của xưởng | "Cập nhật xưởng" |
| Lưu skill vào tài khoản AI | "Lưu skill vào tài khoản" |
| Sau khi đổi phong cách | "Đóng gói lại skill" |

## 12. Sự cố thường gặp

| Bạn thấy | Thường do | Làm gì |
|---|---|---|
| Dán link vào Zalo, Facebook không hiện ảnh, tiêu đề, hoặc hiện bản cũ | web chưa gắn tên miền thật, hoặc Zalo, Facebook còn nhớ bản cũ | nói với trợ lý; trợ lý kiểm thẻ chia sẻ và chỉ bạn làm mới bộ nhớ bằng công cụ gỡ lỗi chia sẻ của Zalo, Facebook (`chuan/05-ky-thuat.md`) |
| Web lên mạng nhưng tên miền chưa vào được | bản ghi DNS chưa lan truyền (vài phút tới 48 giờ) hoặc trỏ sai | chờ, rồi nói trợ lý kiểm theo `huong-dan/07-dns.md` |
| Trình duyệt báo "không an toàn" | chứng chỉ bảo mật chưa cấp xong cho tên miền mới | thường tự hết sau 15-60 phút; quá lâu thì báo trợ lý |
| Form gửi không thấy thư | khoá truy cập dịch vụ form chưa điền, hoặc thư vào hộp thư rác | kiểm hộp thư rác; báo trợ lý |
| Đăng nhập Google trong Zalo, Facebook báo lỗi | trình duyệt cài sẵn trong ứng dụng chặn đăng nhập Google | web-app của xưởng hiện lời nhắc "mở bằng trình duyệt"; hướng dẫn người dùng bấm ba chấm, chọn mở bằng trình duyệt |
| Sửa xong mà web trên mạng chưa đổi | chưa Commit, Push; hoặc trình duyệt còn nhớ bản cũ | mở GitHub Desktop kiểm; tải lại trang có giữ phím Shift |
| `Xem web` không mở | máy chưa có Python, hoặc Mac chặn tệp lần đầu | Mac: mở System Settings [Cài đặt hệ thống] > Privacy & Security [Quyền riêng tư và bảo mật], kéo xuống cuối, bấm Open Anyway [Vẫn mở]; Windows: bấm More info rồi Run anyway; chưa có Python thì nhờ trợ lý hướng dẫn cài |

## 13. Cập nhật xưởng

Xưởng của bạn được trợ lý AI dựng từ bản vẽ Xưởng web AI và không nối với bản vẽ: không có gì tự đổi sau lưng bạn. Tác giả cập nhật bản vẽ định kỳ (khuôn mới, công cụ sửa lỗi, giá và luật mới). Muốn nhận bản mới, nói "cập nhật xưởng": trợ lý đọc nhật ký thay đổi của bản vẽ, kể bạn nghe điều gì mới, điều gì sẽ đổi trong xưởng, hỏi ý bạn, rồi chép phần năng lực mới vào xưởng. Phong cách, cấu hình, web và hồ sơ của bạn không bị đụng tới; tệp năng lực bạn đã chủ ý sửa được giữ lại để cùng quyết. Web đã làm không tự đổi theo: muốn một web nhận nền chung mới thì nói "cập nhật nền chung cho web <tên>".

## 14. Skill của xưởng trên tài khoản AI

Bốn skill của xưởng (những quy trình trợ lý làm theo) có bản gốc trong `skills/`. Lưu bản đóng gói của chúng vào tài khoản AI thì trợ lý nhận ra việc làm web ở mọi cuộc trò chuyện, kể cả khi bạn quên mở thư mục, và vẫn nói đúng phong cách của bạn khi đang ở điện thoại. Skill là gì, lưu thế nào, khi nào đóng gói lại, gỡ rối: `skills/README.md`.

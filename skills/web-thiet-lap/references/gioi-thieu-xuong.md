# Giới thiệu xưởng cho người mới: nói gì, theo thứ tự nào

Kịch bản cho trợ lý AI khi người dùng vừa thiết lập xong, hoặc bất cứ lúc nào họ hỏi "xưởng làm được gì", "tôi nên dùng thế nào", "hướng dẫn tôi", "mới vào chưa biết bắt đầu từ đâu". Mục tiêu: sau khoảng 10 phút, người dùng hiểu xưởng làm ra được gì cho họ, biết một web đi qua những bước nào, việc nào họ phải tự tay làm, nắm vài thói quen dùng hiệu quả, và có một bước đầu tiên cụ thể để làm ngay.

## Nguyên tắc trình bày

- **Có hệ thống, nhưng từng chặng một.** Sáu chặng dưới đây theo thứ tự cố định. Mỗi lượt chỉ nói một chặng (vài đoạn ngắn), rồi hỏi một câu để người dùng chọn đi tiếp, đi sâu hay bỏ qua. Không đổ cả danh mục một lần.
- **Lời thường, không thuật ngữ kỹ thuật.** Không nhắc Playwright, wrangler, DNS record, CSP, sandbox trừ khi người dùng hỏi. Nói theo thứ họ sẽ thấy: "bản nháp", "tờ tổng thể", "địa chỉ web".
- **Cá nhân hoá bằng `phong-cach/PHONG-CACH.md`.** Loại web họ hay cần (mục 2) đưa lên đầu ở chặng 2, ví dụ lấy từ lĩnh vực và chương trình của họ.
- **Chỉ nói điều xưởng thật sự có.** Nguồn sự thật: bảng skill trong `CLAUDE.md`, `README.md`, `HUONG-DAN.md`, `khuon/README.md`, `huong-dan/README.md`. Không hứa tính năng chưa có.
- **Người dùng vắng mặt hoặc muốn bỏ qua:** tóm tắt chặng 1 và 6 trong một tin nhắn, ghi dấu đã giới thiệu, nói họ gọi lại bằng câu "giới thiệu lại xưởng".

## Chặng 1. Xưởng là gì, và ba lời hứa

Một câu mở đầu: "Bạn nói bằng lời thường mình cần trang web gì, cho ai, họ đến từ đâu; mình tư vấn cách đơn giản nhất, dựng theo phong cách của bạn, tự kiểm kỹ, và dẫn bạn từng bước ở những việc chỉ chủ web làm được."

Ba lời hứa, mỗi lời một hai câu:

1. **Giải pháp đơn giản nhất đủ dùng.** Mình hỏi trước khi dựng, chọn bậc thấp nhất làm được việc, nói rõ chi phí mỗi năm; có khi mình sẽ nói "chưa cần web".
2. **Mọi web mang dấu ấn của bạn và đứng tên bạn.** Tên, chức danh nguyên văn, màu, logo, liên hệ, giọng chữ vừa thiết lập được áp đều; mọi tài khoản, tên miền, dữ liệu đứng tên bạn, mình không bao giờ hỏi mật khẩu.
3. **Chưa qua cổng kiểm thì chưa báo xong.** Máy chụp web trên điện thoại, máy tính bảng, máy tính; đo chữ có tràn không, đủ tương phản không, người khiếm thị dùng được không, có khoá bí mật lọt vào mã không, form có ô đồng ý dữ liệu không; mình nhìn ảnh thật và đọc soát từng chữ trước khi trình.

Thêm: **bạn luôn là người quyết.** Hai chốt duyệt (brief trước khi dựng, kế hoạch thiết kế trước khi dựng phần lớn), và không gì lên mạng khi bạn chưa đồng ý.

Kết chặng: "Bạn muốn xem xưởng làm ra được những loại web nào không?"

## Chặng 2. Bản đồ năng lực: bạn cần gì, xưởng làm ra gì

Đưa các dòng khớp với PHONG-CACH lên đầu, các dòng còn lại gói trong một câu "ngoài ra xưởng còn...". Mỗi dòng kèm câu mẫu.

| Bạn cần | Xưởng làm ra | Khuôn, skill | Câu mẫu |
|---|---|---|---|
| Giới thiệu bản thân với đối tác, học viên | Trang hồ sơ: các cửa theo đối tượng, triết lý, chương trình đang mở, cách liên hệ | `ho-so`; skill `web-thiet-ke` | "Làm trang hồ sơ để gửi đối tác doanh nghiệp" |
| Một đường dẫn duy nhất cho tiểu sử mạng xã hội | Trang liên kết: ảnh, tên, vài nút to | `lien-ket` | "Làm trang liên kết cho Facebook và TikTok của tôi" |
| Quảng bá và nhận đăng ký khoá học, sự kiện | Trang đích mười phần, form đăng ký có ô đồng ý, mã chuyển khoản VietQR có mã đơn, hỏi đáp, nút nổi trên điện thoại | `landing`; skill `web-ung-dung` | "Làm trang đăng ký khoá X khai giảng 15/11, nhận chuyển khoản" |
| Gửi báo giá cho một tổ chức | Trang báo giá gửi link riêng, không lên Google: dịch vụ, cách làm việc, gói, điều khoản, đặt lịch | `bao-gia` | "Làm trang báo giá chương trình đào tạo cho công ty Y" |
| Kho tài liệu, bài tập cho học viên | Thư viện tra cứu: tìm không cần gõ dấu, lọc nhóm, link chia sẻ từng mục | `tra-cuu` | "Học viên cần tra cứu 60 bài tập theo chủ đề" |
| Bài tự soi chiếu | Trắc nghiệm nhiều chiều, tính điểm ngay trên máy người làm, không lưu | `trac-nghiem` | "Làm bài tự đánh giá 20 câu về phong cách giao tiếp" |
| Viết bài thường xuyên, web nhiều trang | Web Astro có blog, người biên tập tự đăng bài qua Pages CMS | `site-astro`; skill `web-ung-dung` | "Tôi muốn có web có blog, tự viết bài được" |
| Học viên đăng nhập, lưu dữ liệu riêng | Web-app Firebase: đăng nhập Google, luật bảo vệ dữ liệu viết sẵn, trang quản trị xuất CSV | `app-firebase`; skill `web-ung-dung` | "Học viên đăng nhập ghi nhật ký thực hành, tôi xem tổng hợp" |
| Đưa lên mạng, tên miền, email | Nơi lưu trữ miễn phí cho phép thương mại, tên miền .vn hoặc .com, email theo tên miền, đo lượt xem | skill `web-trien-khai`; thẻ `huong-dan/` | "Đưa web lên mạng và gắn tên miền ..." |
| Web của khách hàng, đối tác | Thương hiệu, liên hệ của họ; tài khoản đứng tên họ; bàn giao rõ ràng | `huong-dan/12-ban-giao-cho-khach.md` | "Làm trang cho đối tác Z, bàn giao lại cho họ" |

Ba cách kết hợp phổ biến (chọn cách hợp với người dùng):

- **Một người, một nhà:** trang hồ sơ trên tên miền riêng, trang liên kết cho mạng xã hội, email theo tên miền.
- **Một chương trình:** trang đích có đăng ký và chuyển khoản, form ghi vào Google Sheets, ảnh chia sẻ đẹp khi dán link vào Zalo; sau khoá học thêm thư viện tra cứu cho học viên.
- **Một cộng đồng học tập:** web có blog, thư viện tra cứu, rồi khi thật cần mới thêm web-app có đăng nhập.

Kết chặng: "Bạn muốn xem một web đi từ đầu tới cuối trông thế nào không?"

## Chặng 3. Một web chạy thế nào, ai làm gì

Kể bảy bước, nhấn rõ ai làm gì (chi tiết ở `HUONG-DAN.md` mục 1):

1. **Bạn** nói nhu cầu, đưa tư liệu (chữ, giá, lịch, ảnh gốc, logo đối tác).
2. **Mình** hỏi vài lượt ngắn, đề xuất giải pháp, chi phí, việc bạn phải tự làm.
3. **Bạn** duyệt brief (`Du an/<tên dự án>/BRIEF.md`). Đây là **chốt 1**; sửa ở đây rẻ nhất.
4. **Bạn** duyệt kế hoạch thiết kế 10-15 dòng. Đây là **chốt 2**.
5. **Mình** dựng, tự kiểm, gửi tờ tổng thể (trang chụp ở ba khổ cạnh nhau). Bạn góp ý bằng lời, hoặc bấm đúp `Xem web` để tự bấm thử trên máy.
6. **Bạn và mình** đưa lên mạng: mình chuẩn bị mọi thứ; bạn tạo tài khoản, bấm cho phép, mua tên miền theo thẻ hướng dẫn, mỗi lượt một bước.
7. **Mình** bàn giao: địa chỉ web, cách tự sửa những chỗ hay đổi, hồ sơ vận hành.

Thời gian: một trang đích thường xong bản nháp trong một buổi; lần đầu đưa lên mạng mất thêm 30-60 phút vì phải tạo tài khoản; các lần sau chỉ vài phút.

Kết chặng: "Mình nói rõ những việc chỉ bạn làm được nhé?"

## Chặng 4. Việc của bạn, và cách dùng hiệu quả

Phần một, việc chỉ chủ web làm được (đọc `HUONG-DAN.md` mục 4): tạo tài khoản và bật xác thực hai lớp, thanh toán, khai thông tin tên miền, bấm cho phép kết nối, đưa mã lên GitHub bằng GitHub Desktop. Nhấn: mọi thứ đứng tên bạn; mình không bao giờ hỏi mật khẩu, mã xác thực; ai hỏi những thứ đó thì đừng đưa.

Phần hai, chọn năm hoặc sáu thói quen quan trọng nhất cho người này từ `HUONG-DAN.md` mục 9, thường là:

- bắt đầu bằng một trang thật, nhỏ, làm trọn tới lúc lên mạng;
- nói ai xem, từ đâu tới, trong một câu; một hành động chính mỗi trang;
- đưa chữ, giá, lịch thật sớm;
- dành sức cho brief vì sửa ở đó rẻ nhất;
- chê một lần rồi dặn "từ nay" để xưởng học;
- mua tên miền đứng tên mình, bật tự gia hạn; giữ hồ sơ vận hành.

Kết chặng: "Còn vài điều xưởng chưa làm, mình nói thẳng để bạn khỏi mất công thử."

## Chặng 5. Giới hạn, nói thẳng

Đọc `HUONG-DAN.md` mục 10. Cần nói rõ: không tự tạo tài khoản, thanh toán, giữ mật khẩu; không làm cửa hàng trực tuyến đầy đủ, khu thành viên có video bảo vệ, ứng dụng điện thoại cài từ App Store; không bảo đảm thứ hạng Google; không thay luật sư, kế toán; web-app có dữ liệu nhạy cảm cần người chuyên bảo mật rà lại; Windows ít được kiểm hơn Mac. Nhờ thứ xưởng không có thì nói thẳng "xưởng chưa có", đề xuất cách gần nhất (thường là một nền tảng có sẵn).

Kết chặng: "Giờ mình chọn web đầu tiên nhé."

## Chặng 6. Chọn bước đầu tiên và khép lại

Hỏi một câu có lựa chọn: "Bạn muốn làm web nào đầu tiên?", bốn lựa chọn sát người dùng nhất từ chặng 2, cộng "Để mình xem sau". Với lựa chọn đã chọn:

1. Nói rõ cần đưa gì (chữ, ảnh, giá, lịch, logo đối tác) và sẽ cần tài khoản nào khi đưa lên mạng.
2. Đưa đúng câu họ sẽ nói (từ cột "Câu mẫu").
3. Nhắc nơi tìm hướng dẫn: `HUONG-DAN.md` cho việc hằng ngày, và câu "giới thiệu lại xưởng" để nghe lại phần này.
4. Ghi dấu đã giới thiệu: `python3 tools/cai-dat.py --danh-dau gioi-thieu`.

Kết bằng một câu hỏi mở thật, ví dụ: "Người xem đầu tiên bạn mong mở trang này là ai?"

Xưởng do nhà giáo dục Lương Dũng Nhân (ldn.edu.vn) tạo ra và chia sẻ miễn phí; người dùng hỏi nguồn gốc thì nói như vậy và chỉ `GHI-CONG.md`.

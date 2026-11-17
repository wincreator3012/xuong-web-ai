# 10. Web-app có trí năng nhân tạo (bậc 4)

Bậc 4 là web-app mà máy chủ gọi một mô hình ngôn ngữ (Claude) để đọc lời người dùng rồi viết phản hồi riêng cho họ: người đồng hành phản tư, trợ lý soạn thảo, máy chấm bài tự luận có giải thích, bảng phân tích cá nhân. Chuẩn này chưng cất từ một ca thật làm trọn vòng: web-app giúp học viên suy xét một quyết định có thật qua nhiều chặng, dựng và đưa vào vận hành trong 3 ngày (11/2026). Mọi điều ở chuan/06 về bậc 3 vẫn áp dụng; chuẩn này thêm phần riêng của việc đặt một mô hình vào giữa ứng dụng.

## 1. Khi nào cần bậc 4

- Chỉ lên bậc 4 khi người dùng cần một phản hồi viết riêng cho chính lời của họ, lặp lại nhiều lần, có dữ liệu tích lũy và phân quyền. Nếu chỉ cần một lần trò chuyện, một dự án Claude hay một trang Claude chia sẻ có thể đủ; nếu phản hồi có thể soạn sẵn theo mẫu, bậc 0 đến 3 rẻ và an toàn hơn.
- Cái giá phải nói rõ với chủ dự án trước khi dựng: chi phí mỗi lượt gọi mô hình (đo thật; ở ca gốc khoảng 0,33 USD và 100 giây cho một lượt sáu chặng), gói Blaze có thẻ, khóa API phải giữ, dữ liệu nhạy cảm, prompt là tài sản trí tuệ cần bảo vệ, rủi ro mô hình viết sai hay viết điều có hại.

## 2. Đặc tả trước, và giữ nhật ký quyết định

- Viết đặc tả nghiệp vụ trước khi viết mã (ca gốc: một tệp đặc tả riêng): vai trò và quyền, hành trình người dùng, từng chặng ai viết gì, nguyên tắc hành vi của trí năng nhân tạo, mô hình dữ liệu, hạn mức và chi phí, màn hình, chuẩn chữ.
- Prompt là một tệp riêng (ca gốc: một tệp prompt riêng): khối dùng chung, khối nhiệm vụ cho từng lời gọi, cấu trúc đầu ra, các phép kiểm bằng mã, bộ tình huống mẫu để thử. Có số phiên bản và ngày sửa.
- Đặc tả có bảng "các quyết định đã chốt", đánh số tăng dần; mỗi thay đổi chủ dự án duyệt thêm một dòng (vấn đề, quyết định). Bảng này giúp phiên làm việc sau hiểu vì sao hệ thống như hiện nay mà không phải lục lại trò chuyện.
- Phương án lớn hay tốn công làm lại (gói mới, vai trò mới, luồng thử nghiệm): trình phương án kèm những điểm cần chủ dự án quyết và đề xuất của Claude, chờ duyệt rồi mới dựng.

## 3. Kiến trúc mặc định

| Tầng | Lựa chọn | Lý do |
|---|---|---|
| Lõi nghiệp vụ | TypeScript thuần trong `core/`, không nhập thư viện Firebase: luồng các chặng, prompt, rào chắn, hạn mức, giao diện kho dữ liệu | kiểm thử nhanh không cần mạng; đổi nơi lưu (PostgreSQL, Zalo Mini App) không đụng lõi |
| Máy chủ | Cloud Functions thế hệ 2, hàm gọi được [callable], vùng `asia-southeast1` | mọi thao tác ghi và mọi lời gọi mô hình đi qua đây; khóa API chỉ sống ở đây |
| Dữ liệu | Firestore (Singapore); luật chỉ cho người dùng ĐỌC dữ liệu của chính mình, cấm mọi lệnh GHI từ trình duyệt | quyền kiểm một chỗ, ở máy chủ |
| Đăng nhập | Firebase Authentication với Google; vai trò gắn vào thẻ đăng nhập [custom claims] | một nút, không giữ mật khẩu |
| Giao diện | React + Vite + TypeScript, dùng chung kiểu dữ liệu với lõi | luồng nhiều chặng, nhiều trạng thái; ngoại lệ có lý do của chuan/01 mục 4 |
| Bí mật | Secret Manager (`ANTHROPIC_API_KEY`, khóa giải mã prompt) | không nằm trong mã, kho git, tệp cấu hình |

Một kho git cho mỗi ứng dụng: `app/` (core, functions, web), tài liệu đặc tả ở gốc kho, `prompt/` chứa prompt đã mã hóa.

## 4. Gọi mô hình cho đúng

- **Đầu ra có cấu trúc.** Claude Sonnet 5.5 và Opus 5.5 không nhận `tool_choice` ép công cụ; lấy JSON bằng `output_config.format` (json_schema). Đặt `output_config.effort` theo từng lời gọi: việc tóm gọn, sắp xếp để mức thấp; việc soi xét sâu để mức vừa.
- **Chọn mô hình theo việc.** Sonnet cho lời gọi nhẹ, nhiều lần; Opus cho phần cần suy xét sâu mà người dùng đọc kỹ (phiếu tổng hợp, câu hỏi phản tư, bảng phân tích nhiều lượt).
- **Trần token rộng tay với tiếng Việt.** Tiếng Việt tốn token gấp khoảng 3 lần ước lượng ban đầu, và phần suy nghĩ thích ứng ăn vào `max_tokens`: đo trên lời gọi thật rồi đặt trần, ghi ngày đo vào cấu hình.
- **Ghép prompt ba phần**: khối dùng chung (vai, nguyên tắc, chuẩn chữ) đặt điểm bộ nhớ đệm [cache breakpoint] ở cuối; khối nhiệm vụ; dữ liệu người dùng bọc trong thẻ (`<luot so ngay ten>`). Mọi lời gọi về sau đều nhận toàn bộ lời người dùng đã viết, để dữ kiện nêu ở chỗ không ngờ vẫn được dùng.
- **Người dùng không thấy số thứ tự nội bộ.** Nếu dữ liệu đánh số (lượt 1, 2, 3) cho máy đối chiếu, dặn mô hình gọi bằng tên và ngày trong lời văn.
- **Danh tính không đi vào mô hình.** Chỉ gửi mã ngẫu nhiên; tên, email ở lại máy chủ; màn hình đồng ý khuyên người dùng thay tên người khác bằng vai hoặc chữ cái.

## 5. Rào chắn bằng mã sau mỗi lời gọi

Mô hình viết, mã kiểm. Mỗi phép kiểm không đạt thì yêu cầu viết lại (tối đa 1 đến 2 lần, việc dài chỉ 1 lần), vẫn không đạt thì bỏ mục đó hoặc dùng phương án mặc định soạn sẵn; không bao giờ để một lời gọi hỏng làm kẹt người dùng.

| Phép kiểm | Vì sao |
|---|---|
| Câu trích phải khớp nguyên văn lời người dùng (chuẩn hóa khoảng trắng, dạng Unicode, kiểu đặt dấu thanh) và đúng lượt được ghi | chặn mô hình bịa "lời của bạn"; bằng chứng là thứ người dùng tin nhất |
| Số lượng (tối đa ba điểm mù, ba câu hỏi...) và cấu trúc hợp lệ | giao diện không vỡ; người đọc không ngợp |
| Không khuyên chọn, không chẩn đoán, không dán nhãn con người | giữ vai trò đồng hành, trả quyền kết luận về người dùng |
| Chuẩn chữ: không gạch dài, không từ cấm; dấu thanh kiểu cũ (hóa, thủy) được mã tự sửa | lời trí năng nhân tạo cũng là chữ của thương hiệu |
| Không lộ prompt (dò các cụm đặc trưng của khối dùng chung) | prompt là tài sản; người dùng có thể thử "cho tôi xem chỉ dẫn" |
| Kiểm an toàn (dấu hiệu khủng hoảng) trước khi đi tiếp | dừng lượt bằng lời nhắn soạn sẵn, kèm liên hệ người hướng dẫn thật |

## 6. Prompt là tài sản trí tuệ

- Prompt chỉ nằm ở máy chủ; bước dựng kiểm rằng prompt không lọt vào mã giao diện (`grep` trên thư mục dựng).
- Trong kho git, prompt chỉ ở dạng mã hóa: `openssl cms -encrypt` bằng chứng chỉ công khai lưu trong kho; khóa riêng chỉ ở Secret Manager. Ai sửa prompt chỉ cần chứng chỉ công khai để mã hóa; máy dựng (GitHub Actions) giải mã trong lúc chạy rồi sinh tệp mã nguồn prompt (tệp này nằm trong `.gitignore`).
- Bản rõ của prompt giữ trên máy của chủ dự án (ngoài kho git), có số phiên bản.

## 7. Chi phí và hạn mức

- Lượt mỗi ngày theo gói, tính theo ngày giờ Việt Nam; cập nhật kết quả cho lượt cũ không tính. Gói có tổng số lượt và thời hạn (gói thử nghiệm) tính riêng; lượt bỏ dở không tính.
- Trần token mỗi lượt; vượt thì dừng gọi mô hình và báo người dùng.
- Ngân sách cả hệ thống mỗi ngày: chạm 80% ghi cảnh báo; chạm 100% tạm ngưng mở lượt mới, lượt đang làm vẫn hoàn tất được.
- Ghi mỗi lời gọi: mã người dùng, lượt, tên lời gọi, mô hình, token vào, ra, đọc và ghi bộ nhớ đệm, chi phí ước tính theo bảng giá trong cấu hình.
- Hàng rào cuối do chủ dự án tự đặt: hạn mức chi của workspace trên Anthropic Console, trần chi và cảnh báo ngân sách của Google Cloud.
- Khi hết hạn mức, lời nhắn nói rõ khi nào có lượt mới; không thúc mua gói cao hơn.

## 8. Việc chạy lâu: chạy nền, không bắt người dùng chờ

Lời gọi nhiều phút (bảng phân tích từ nhiều lượt): hàm gọi được chỉ ghi một tài liệu trạng thái `generating`; một hàm chạy nền theo Firestore [onDocumentWritten] làm phần việc tốn thời gian. Chống chạy trùng bằng số lần yêu cầu (`attempt`) và dấu giữ chỗ (`runningAttempt`) trong giao dịch; quá 20 phút chưa xong thì coi là lỗi để người dùng yêu cầu lại; giao diện hỏi lại mỗi 15 giây. Trong một lượt, khóa lượt (`busyUntil`) khi đang gọi mô hình để bấm liên tiếp cũng chỉ gọi mô hình một lần.

## 9. Dữ liệu, quyền, đồng ý

- Vai trò kiểm ở máy chủ: người học, giảng viên, điều phối viên, quản trị viên. Điều phối viên vận hành (duyệt tài khoản, gói, lớp) mà không đọc nội dung, không thấy chi tiêu riêng từng người; tài khoản thử có thể ẩn để chỉ quản trị viên thấy.
- Nội dung người dùng viết là riêng tư mặc định. Chia sẻ từng mục do chính họ bật và rút lại được; ai đọc mục được chia sẻ đều ghi vào nhật ký truy cập; quản trị viên cũng chỉ đọc mục được chia sẻ.
- Lưu trữ có thời hạn và tự xóa theo lịch (ca gốc: mục không chia sẻ xóa sau 5 năm); người dùng tải về, xóa từng mục hay toàn bộ dữ liệu bất cứ lúc nào.
- Màn hình đồng ý có số phiên bản; đổi cách dùng dữ liệu thì tăng số, người dùng cũ được mời đồng ý lại một lần. Viết rõ: nội dung được gửi tới nhà cung cấp mô hình nào, ở đâu, ai xem được gì.
- Dữ liệu tâm lý, sức khỏe, cơ thể là dữ liệu nhạy cảm (chuan/08): gắn cờ pháp lý, khuyên chủ dự án nhờ luật sư rà màn hình đồng ý.

## 10. Bảo mật thêm cho bậc 4

- App Check (reCAPTCHA Enterprise): chạy chế độ theo dõi 1 đến 2 tuần, khi gần như mọi lời gọi đều có chứng nhận thì bật bắt buộc.
- CORS chỉ cho tên miền của sản phẩm; giới hạn tần suất mỗi tài khoản (ví dụ 60 thao tác mỗi phút); trần kích thước dữ liệu gửi lên; kiểm mã lượt, mã người dùng bằng biểu thức chính quy trước khi ghép vào đường dẫn dữ liệu.
- Firestore: chống xóa cơ sở dữ liệu, khôi phục theo thời điểm 7 ngày, sao lưu hằng ngày.
- Hai chủ dự án (một tài khoản dự phòng), cả hai bật xác thực hai lớp; danh sách email quản trị viên đầu tiên đặt trong mã có mặc định, không đặt trong giao diện.
- Khóa dán vào trò chuyện, ảnh chụp, tin nhắn là khóa đã lộ: tạo khóa mới, thay trong Secret Manager, xóa khóa cũ.

## 11. Đưa lên tự động: GitHub Actions + Workload Identity Federation

- Kho riêng tư trên GitHub; mỗi lần đẩy lên `main` (chỉ khi đổi `app/` hoặc `prompt/`) thì Actions chạy: cài gói, đăng nhập Google Cloud, giải mã prompt, kiểm thử, kiểm kiểu, dựng, kiểm prompt không lọt xuống trình duyệt, `firebase deploy` (thử lại 3 lần), mở quyền gọi công khai cho hàm phía trình duyệt, gọi thử trang chủ.
- Đăng nhập bằng Workload Identity Federation: pool và provider chỉ nhận đúng kho và đúng nhánh `main`; đóng vai một tài khoản dịch vụ riêng cho việc đưa lên với đúng các vai trò cần (khoảng 11). Không có khóa tài khoản dịch vụ nào lưu trên GitHub.
- Cloud Shell với một tập lệnh đưa lên là đường dự phòng.
- Năm cái bẫy đã gặp: hàm lỗi ở lần tạo đầu thì lần sau không tự mở quyền gọi công khai (trình duyệt báo `internal`, gọi thẳng nhận 403); lần đầu có hàm chạy nền theo Firestore, Eventarc cần vài phút cấp quyền; `firebase deploy --non-interactive` đòi giá trị mọi `defineString` (dùng `process.env` có mặc định); đăng nhập trên `*.web.app` cần thêm `https://<dự án>.web.app/__/auth/handler` vào redirect URI trong cấu hình OAuth (Client ID) của dự án; hàm chạy theo lịch và hàm chạy nền không được mở quyền gọi công khai.

## 12. Kiểm thử ba tầng

1. **Lõi với mô hình giả lập** (`MockLlm`, kho dữ liệu trong bộ nhớ): mỗi tính năng có kiểm thử chạy vài giây, kể cả luật gói, thời hạn, câu trích.
2. **Máy giả lập Firebase + Playwright** đi trọn luồng bằng nhiều tài khoản và nhiều vai (quản trị, điều phối, người học), chụp màn hình để Claude nhìn. Dữ liệu mồi (đủ 3 hay 10 lượt) bằng tập lệnh tạm, xóa sau khi dùng.
3. **Một lượt thật với Claude** để đo thời gian, chi phí, chất lượng; chạy bộ tình huống mẫu của tệp prompt trước khi mời người thật.

## 13. Đợt thử nghiệm với người dùng thật

- Gói riêng có giới hạn (ví dụ 3 lượt, 1 lượt mỗi ngày, 14 ngày, hẹn kết quả tối đa 30 ngày).
- Trang mời ẩn theo đợt: đăng nhập là được duyệt và vào đúng gói, đúng lớp; mỗi đợt có số tài khoản tối đa và ngày đóng trang, quá thì chuyển sang chờ duyệt; đội ngũ kiểm tra lại sau và loại người không có trong danh sách mời.
- Góp ý theo nhịp ngắn ngay sau khoảnh khắc đáng hỏi (sau khi chốt, sau khi nhìn lại kết quả, tổng kết đợt), lưu riêng khỏi nội dung, không chặn lượt sau.
- Vị thế đồng kiến tạo, không phải người đánh giá: câu hỏi đi từ trải nghiệm của họ, thang số dùng ít, có câu "nếu được sửa theo ý mình"; đội ngũ viết lại cho họ "đã thay đổi gì nhờ góp ý của bạn"; trang cảm ơn ghi tên ai đồng ý.

## 14. Làm việc cùng chủ dự án

- Mọi chữ hiển thị (giao diện, lời nhắn lỗi phía máy chủ, lời chào, câu hỏi) qua cổng soát chữ của chuan/04 và `tools/kiem-web.py` trước khi gửi chủ dự án duyệt; lời mời, lời chào dễ mang giọng văn máy nhất, đọc to lại.
- Mỗi lần đưa lên: đồng bộ các tệp đã đổi về thư mục dự án trên máy của chủ dự án, cập nhật `VAN-HANH.md` của dự án.
- Chủ dự án tự bấm những việc gắn với danh tính và quyền: đồng ý điều khoản, cấp quyền OAuth, nhập khóa vào Secret Manager, chấp nhận lời mời chủ dự án.

# B. Dữ liệu và dịch vụ: thêm tính năng động cho web tĩnh khi làm web cùng trợ lý AI

Báo cáo nghiên cứu cho Xưởng web AI. Người đọc mục tiêu: người không chuyên kỹ thuật ở Việt Nam, dựng web bằng cách trò chuyện với trợ lý AI.

- Ngày kiểm: 07/10/2026 (mọi số liệu dưới đây được đọc trực tiếp từ trang chính thức hoặc nguồn ghi kèm vào ngày này, trừ chỗ ghi khác).
- Quy ước: thuật ngữ tiếng Anh để trong [ngoặc vuông] ở lần đầu xuất hiện. Chỗ nào chưa chắc được đánh dấu **[cần kiểm lại]**.
- Giá và hạn mức miễn phí [free tier] thay đổi thường xuyên. Trước khi cam kết với khách hàng, hãy mở lại đường dẫn nguồn.

---

## 0. Khuyến nghị mặc định (đọc phần này trước)

| Nhu cầu | Mặc định nên chọn | Lý do ngắn |
|---|---|---|
| Biểu mẫu liên hệ, đăng ký | Web3Forms (250 lượt/tháng miễn phí) hoặc Tally nhúng | Không cần máy chủ, không cần thẻ tín dụng, AI viết đúng ngay lần đầu |
| Ghi dữ liệu vào Google Sheets | Tally nhúng (tích hợp Sheets sẵn) ; khi cần form tự thiết kế: Google Apps Script | Dữ liệu nằm ngay trong Sheets người dùng đã quen |
| Đăng nhập và cơ sở dữ liệu | Tạm thời tránh. Nếu thật cần: Firebase gói Spark, có quy tắc bảo mật viết sẵn và kiểm tra | Rủi ro rò dữ liệu khi AI viết code là có thật và đã xảy ra hàng loạt |
| Sửa nội dung không cần code | Pages CMS (miễn phí, mời qua email) | Không cần máy chủ, không cần tài khoản GitHub cho người biên tập |
| Thu tiền khoá học, vé sự kiện | Mã VietQR có số tiền và mã đơn trong nội dung chuyển khoản, đối soát bằng SePay (gói miễn phí 50 giao dịch/tháng) hoặc thủ công | Không cần giấy phép kinh doanh để bắt đầu, phí thấp |
| Đặt lịch hẹn | Cal.com gói miễn phí hoặc lịch hẹn của Google Calendar | Miễn phí, nhúng được |
| Bản tin | Kit (miễn phí tới 10.000 người đăng ký) hoặc nhúng Substack nếu đã viết Substack | Hạn mức miễn phí rộng nhất |
| Đo lường truy cập | Cloudflare Web Analytics + Google Search Console | Miễn phí, không cookie, không cần banner đồng ý |
| Web nhiều trang, blog | Astro (bản 7.x) xuất tĩnh | AI viết Astro tốt, nội dung là file Markdown dễ hiểu |

---

## 1. Biểu mẫu không cần máy chủ [serverless forms]

### 1.1. So sánh dịch vụ nhận biểu mẫu [form backend]

| Dịch vụ | Miễn phí | Ghi chú quan trọng | Gói trả phí thấp nhất | Nguồn |
|---|---|---|---|---|
| **Web3Forms** | 250 lượt gửi/tháng, không giới hạn số form và tên miền | Chống rác [spam] có sẵn, hỗ trợ hCaptcha, bẫy ẩn [honeypot]; **không** có tải tệp ở gói miễn phí | Pro khoảng 12 USD/tháng (trả năm 149 USD), 10.000 lượt | https://web3forms.com/pricing |
| **Formspree** | 50 lượt/tháng, không giới hạn số form | Lưu trữ 30 ngày, không tải tệp, không thư tự động trả lời, chỉ 2 email nhận | Personal 10 USD/tháng (200 lượt) | https://formspree.io/plans |
| **Netlify Forms** | Miễn phí và không giới hạn trên gói tính theo tín dụng [credit-based] | Chỉ dùng khi web đặt trên Netlify. Lọc rác Akismet tự động, có honeypot và reCAPTCHA | (gói Netlify) | https://docs.netlify.com/manage/forms/usage-and-billing/ ; https://docs.netlify.com/manage/forms/spam-filters/ |
| **Basin** | 1 form, 50 lượt/tháng, lưu 30 ngày | Phù hợp thử nghiệm | Starter 12,50 USD/tháng (trả năm) | https://usebasin.com/pricing |
| **Getform** | 100 lượt/tháng | Vẫn hoạt động | Pro 14 USD/tháng | https://getform.com/pricing |
| **Tally** (nhúng form) | Không giới hạn form và lượt gửi (theo nguyên tắc dùng hợp lý), có tải tệp, logic điều kiện, thu tiền, tích hợp Google Sheets, Notion; webhook miễn phí có khoá ký [signing secret] | Có logo Tally ở gói miễn phí | Pro 24 USD/tháng | https://tally.so/pricing ; https://tally.so/help/webhooks |
| **Google Forms** nhúng | Miễn phí | Nhúng bằng khung `iframe`, giao diện khó tuỳ biến, dữ liệu tự vào Sheets | Không có | (kiến thức chung) |

Lưu ý về Netlify:
- Từ 04/09/2025, tài khoản Netlify mới dùng gói tính theo tín dụng. Gói Free có 300 tín dụng/tháng, mỗi lần triển khai bản chính [production deploy] tốn 15 tín dụng, băng thông 20 tín dụng/GB. Khi hết tín dụng, **toàn bộ web trong nhóm bị tạm dừng** (khách thấy trang "Site not available", form cũng ngừng nhận) cho tới chu kỳ sau, và gói Free không mua thêm tín dụng được. Nguồn: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans ; https://www.netlify.com/pricing/
- Hệ quả thực tế: người mới hay bảo AI "sửa nhỏ rồi đẩy lên" hàng chục lần một ngày. 20 lần triển khai = 300 tín dụng = hết hạn mức tháng. Đây là cái bẫy lớn nhất của Netlify cho người dùng AI.

### 1.2. Mẫu Google Apps Script ghi vào Google Sheets

Cách làm: tạo Google Sheet, mở Extensions > Apps Script, viết hàm `doPost(e)` ghi một dòng mới, rồi triển khai dạng ứng dụng web [web app] với "Execute as: Me" và "Who has access: Anyone". Trang web tĩnh gửi dữ liệu tới đường dẫn `.../exec`.

Hạn mức với tài khoản Gmail cá nhân (nguồn: https://developers.google.com/apps-script/guides/services/quotas):
- Mỗi lần chạy tối đa 6 phút.
- Tối đa 30 lần chạy đồng thời mỗi người dùng.
- Gửi email: 100 người nhận/ngày (quan trọng nếu muốn tự gửi email xác nhận).
- Gọi URL ra ngoài [UrlFetch]: 20.000 lần/ngày.
- Trình kích hoạt [triggers]: tổng 90 phút/ngày.

Những cái bẫy thường gặp:
1. **CORS và chuyển hướng.** Nội dung trả về từ Apps Script luôn bị chuyển hướng [redirect] sang một đường dẫn dùng một lần ở `script.googleusercontent.com`; trình gọi phải đi theo chuyển hướng (nguồn: https://developers.google.com/apps-script/guides/content). Kinh nghiệm cộng đồng: gửi bằng `fetch` với `Content-Type: text/plain` (hoặc `FormData`/`URLSearchParams`) để trình duyệt không gửi yêu cầu kiểm tra trước [preflight], vì Apps Script không trả lời được yêu cầu `OPTIONS`. Nếu dùng `mode: "no-cors"` thì gửi được nhưng không đọc được phản hồi. **[cần kiểm lại khi thử thực tế; đây là kinh nghiệm cộng đồng, tài liệu chính thức không nói về CORS]**. Nguồn tham khảo cộng đồng: https://dev.to/allenarduino/how-to-connect-your-html-form-to-google-sheets-without-a-backend-31bo
2. **Sửa code nhưng web vẫn chạy bản cũ.** Phải tạo phiên bản [version] mới và vào Deploy > Manage deployments > Edit để trỏ triển khai cũ sang phiên bản mới; làm vậy thì **giữ nguyên URL**. Nếu bấm "New deployment" sẽ ra URL mới và phải sửa lại web. Nguồn: https://developers.google.com/apps-script/concepts/deployments
3. **Không đọc được tiêu đề HTTP [headers].** Đối tượng sự kiện `e` chỉ có `parameter`, `queryString`, `postData`... không có headers (nguồn: https://developers.google.com/apps-script/guides/web). Hệ quả: dịch vụ webhook nào xác thực bằng header (như SePay gửi `Authorization: Apikey ...`) thì Apps Script không kiểm được. Cách vá: đặt một chuỗi bí mật trong URL webhook (`.../exec?token=...`) và kiểm `e.parameter.token`.
4. **Ghi đồng thời.** Dùng `LockService.getScriptLock()` để hai lượt gửi cùng lúc không đè dòng nhau. Nguồn: https://dev.to/bs_tales/tutorial-add-forms-to-static-sites-with-google-sheets-1c3a
5. **URL "Anyone" là công khai.** Ai có URL đều ghi được vào Sheet. Cần honeypot và kiểm dữ liệu trong script.

### 1.3. Chống rác

- **Bẫy ẩn [honeypot]:** một ô nhập bị ẩn; máy điền vào thì loại. Netlify có thuộc tính `netlify-honeypot` (nguồn: https://docs.netlify.com/manage/forms/spam-filters/); Web3Forms có sẵn. Rẻ nhất, nên luôn bật.
- **Cloudflare Turnstile:** miễn phí, tối đa 20 widget/tài khoản, 10 tên miền/widget, không giới hạn số lần thử thách, dùng được mà không cần chuyển tên miền sang Cloudflare (nguồn: https://developers.cloudflare.com/turnstile/plans/). **Bắt buộc** kiểm token phía máy chủ qua API Siteverify; token sống 5 phút và chỉ dùng một lần. Chỉ gắn widget ở giao diện thì **không** bảo vệ gì (nguồn: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/). Với web tĩnh thuần, người dùng cần dịch vụ form có hỗ trợ Turnstile hoặc một hàm nhỏ trên Cloudflare Workers.
- **hCaptcha:** gói Basic miễn phí; Pro 99 USD/tháng (trả năm) (nguồn: https://www.hcaptcha.com/pricing). Web3Forms tích hợp sẵn ở gói miễn phí.

---

## 2. Dịch vụ backend có sẵn [Backend-as-a-Service, BaaS] cho ứng dụng nhỏ có đăng nhập và cơ sở dữ liệu

### 2.1. So sánh hạn mức miễn phí

| Dịch vụ | Miễn phí | Điểm cần biết | Nguồn |
|---|---|---|---|
| **Firebase gói Spark** | Auth 50.000 người dùng hoạt động/tháng [MAU]; Firestore 1 GiB, 50.000 lượt đọc/ngày, 20.000 lượt ghi/ngày, 20.000 lượt xoá/ngày; Hosting 10 GB, 360 MB/ngày | **Không cần thẻ**. Cloud Storage (lưu ảnh, tệp) và Cloud Functions **không có** ở Spark. Gói Blaze trả theo dùng, **cần thẻ tín dụng**, có thể được 300 USD tín dụng thử | https://firebase.google.com/pricing |
| **Firebase Cloud Storage** | Phải lên Blaze mới truy cập được bucket, kể cả bucket mặc định; dự án Spark gặp lỗi 402/403 | Thay đổi công bố từ 09/2024 | https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024 |
| **Supabase Free** | 2 dự án; 500 MB CSDL/dự án; 50.000 MAU; 1 GB tệp; 5 GB băng thông ra; 500.000 lượt gọi Edge Function | **Tạm dừng sau 1 tuần không hoạt động**. Không cần thẻ. Pro 25 USD/tháng | https://supabase.com/pricing |
| **Appwrite Cloud Free** | 2 dự án; 75.000 MAU; 2 GB lưu trữ; 5 GB băng thông; 500.000 đọc và 250.000 ghi CSDL/tháng; 2 function/dự án | Tạm dừng sau 1 tuần không phát triển; **dự án tạm dừng bị xoá sau 90 ngày** (chính sách 06/2026). Trang giá chính thức không hiển thị rõ gói Free khi kiểm, số liệu lấy từ trang tổng hợp **[cần kiểm lại]** | https://agentdeals.dev/vendor/appwrite ; https://appwrite.io/pricing |
| **Turso** (SQLite trên mây) | 100 CSDL, 5 GB, 500 triệu dòng đọc, 10 triệu dòng ghi/tháng | Chỉ là cơ sở dữ liệu, **không có đăng nhập**, cần một lớp máy chủ để giữ khoá | https://turso.tech/pricing |
| **PocketBase** | Mã nguồn mở, miễn phí | Một tệp chạy duy nhất gồm CSDL, đăng nhập, tệp, trang quản trị. Bản v0.40.4, **chưa đạt 1.0** nên có thể đổi không tương thích. **Phải tự thuê máy chủ** | https://pocketbase.io/ |
| **Cloudflare Workers + D1** | 100.000 lượt gọi/ngày; D1 5 GB, 5 triệu dòng đọc/ngày, 100.000 dòng ghi/ngày | Không có đăng nhập dựng sẵn | https://developers.cloudflare.com/workers/platform/pricing/ |

### 2.2. Nên chọn gì cho người mới làm cùng AI

- **Firebase (Spark)** là lựa chọn ít bất ngờ nhất cho người không chuyên: không tạm dừng vì ít dùng, không cần thẻ, đăng nhập Google một nút, tài liệu dày nên AI viết code khá chuẩn. Điểm yếu: muốn lưu ảnh hoặc chạy hàm phía máy chủ là phải lên Blaze (cần thẻ, có rủi ro hoá đơn bất ngờ nếu bị lạm dụng).
- **Supabase** mạnh hơn (SQL thật, quan hệ bảng), nhưng hai cái bẫy với người mới: dự án bị tạm dừng sau 1 tuần yên ắng (web của một khoá học mở đăng ký theo đợt rất dễ rơi vào), và bảo mật dựa vào chính sách cấp dòng [Row Level Security, RLS] mà người mới khó đọc hiểu.
- **PocketBase** chỉ khi đã có người kỹ thuật lo máy chủ.
- **Khuyến nghị thực tế:** với đa số web của người làm giáo dục, chưa cần đăng nhập. Đăng ký khoá học, khảo sát, danh sách chờ... nên dùng form + Google Sheets. Chỉ lên BaaS khi người dùng thật sự cần xem lại dữ liệu riêng của họ.

### 2.3. Lỗi bảo mật thường gặp khi AI viết code Firebase, Supabase

Nguyên lý: khoá công khai trong trình duyệt **không phải** là lỗ hổng; lỗ hổng là **thiếu luật kiểm soát quyền**.

- Firebase: khoá API Firebase (đã giới hạn cho dịch vụ Firebase) không cần giữ bí mật và để trong code được; quyền truy cập do **Security Rules** và **App Check** quyết định. Tuyệt đối không để khoá tài khoản dịch vụ [service account key] hay khoá Gemini API trong code giao diện. Nguồn: https://firebase.google.com/docs/projects/api-keys
- Supabase: khoá `sb_publishable_...` (bản cũ là `anon`) để trong trình duyệt được, chỉ truy cập được những gì RLS cho phép. Khoá `sb_secret_...` (bản cũ là `service_role`) **vượt qua RLS hoàn toàn**, không bao giờ để trong trình duyệt. Supabase sẽ ngừng khoá `anon`/`service_role` kiểu cũ trước cuối năm 2026. Nguồn: https://supabase.com/docs/guides/api/api-keys
- Supabase: "bảng trong schema được công khai mà không bật RLS thì vai trò nào có quyền cũng đọc và ghi được"; bật RLS mà chưa có chính sách thì không đọc được gì; view do `postgres` tạo mặc định **bỏ qua RLS** trừ khi đặt `security_invoker = true`. Nguồn: https://supabase.com/docs/guides/database/postgres/row-level-security
- Firebase: ba mẫu luật nguy hiểm là mở toàn bộ (chế độ thử nghiệm [test mode]), chỉ kiểm `request.auth != null` (ai đăng nhập cũng xem được hết), và không đối chiếu chủ sở hữu (`request.auth.uid == resource.data.<trường chủ>`). Nguồn: https://firebase.google.com/docs/rules/insecure-rules
- App Check (web dùng reCAPTCHA Enterprise hoặc v3) giảm lạm dụng nhưng **không thay thế** Security Rules. Nguồn: https://firebase.google.com/docs/app-check

Sự cố có thật (để người dùng hiểu đây không phải lo xa):

| Thời điểm | Sự cố | Nguyên nhân gốc | Nguồn |
|---|---|---|---|
| 03-05/2025 | CVE-2025-48757: hơn 170 ứng dụng dựng bằng Lovable, 303 điểm truy cập lộ email, số điện thoại, trạng thái thanh toán, khoá API | Thiếu hoặc sai chính sách RLS; khoá `anon` trong trình duyệt truy vấn thẳng Supabase. Người phát hiện: Matt Palmer | https://www.superblocks.com/blog/lovable-vulnerabilities |
| 25/07/2025 | Ứng dụng Tea (Mỹ) lộ khoảng 72.000 ảnh, gồm khoảng 13.000 ảnh chân dung và giấy tờ tuỳ thân | Bucket Firebase Storage để mở (hệ lưu trữ cũ) | https://securityaffairs.com/180539/data-breach/hackers-leak-images-and-comments-from-women-dating-safety-app-tea.html |
| 31/01-01/02/2026 | Moltbook (mạng xã hội cho tác tử AI, dựng theo lối "vibe coding") lộ 1,5 triệu token API, hơn 35.000 email, tin nhắn riêng; có quyền đọc và ghi toàn bộ CSDL | Khoá Supabase trong JavaScript phía trình duyệt + RLS tắt. Wiz phát hiện | https://wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys |
| 09/2026 | UpGuard tìm thấy 16.326 CSDL Supabase có bảng đọc công khai, hơn một nửa chứa thông tin cá nhân | Cấu hình sai của người dựng, thường qua công cụ AI | https://cybernews.com/news/16000-supabase-databases-exposed/ (ngày đăng bài ghi 26/09/2026 **[cần kiểm lại ngày chính xác]**) |

Danh sách kiểm tra tối thiểu khi để AI viết phần đăng nhập và dữ liệu:
1. Yêu cầu AI viết luật bảo mật **trước** khi viết giao diện, và giải thích từng dòng bằng tiếng Việt.
2. Thử bằng tài khoản thứ hai: có xem được dữ liệu của tài khoản thứ nhất không.
3. Thử khi chưa đăng nhập: mở công cụ nhà phát triển, gọi thẳng API.
4. Tìm trong code: không có chuỗi `service_role`, `sb_secret_`, `private_key`.
5. Supabase: mở Security Advisor trong bảng điều khiển trước khi công bố **[chưa đối chiếu tài liệu chính thức về Security Advisor trong lần kiểm này]**.

---

## 3. Sửa nội dung cho người không viết code (web tĩnh, Astro)

| Công cụ | Cách hoạt động | Chi phí | Hợp với ai | Nguồn |
|---|---|---|---|---|
| **Pages CMS** | Ứng dụng GitHub, cấu hình bằng một tệp `.pages.yml`; có trình soạn trực quan, quản lý ảnh kéo thả; **mời người biên tập qua email, không cần tài khoản GitHub** | 100% miễn phí, mã nguồn mở MIT | Mặc định cho khách hàng không chuyên. Hỗ trợ Astro, Hugo, Eleventy, Jekyll | https://pagescms.org/ |
| **Sveltia CMS** | Viết lại từ Netlify/Decap CMS, tương thích cấu hình cũ, tự nhận là đã đủ tính năng để thay Decap | Miễn phí | Ai đang dùng Decap hoặc cần đa ngôn ngữ. Gói npm vẫn ở 0.230.0 (chưa 1.0) | https://github.com/sveltia/sveltia-cms ; npm `@sveltia/cms` |
| **Decap CMS** | Giao diện React chạy trên Git; nhiều phương thức đăng nhập | Miễn phí, bản 3.16.3 | Web cũ đã dùng. Lưu ý: Git Gateway (cách đăng nhập phổ biến nhất trên Netlify) **đã bị ngừng phát triển**, chỉ vá lỗi bảo mật; Netlify Identity thì được giữ lại từ 19/02/2026 | https://decapcms.org/docs/intro/ ; https://answers.netlify.com/t/netlify-identity-is-staying-feb-2026-reversal-what-changed-whos-affected-and-how-to-proceed/162733 |
| **TinaCMS** | Sửa trực quan ngay trên trang, cần TinaCloud | Miễn phí 2 người dùng; Team 24 USD/tháng/dự án | Khi cần soạn trực quan mạnh | https://tina.io/pricing |
| **Sửa Markdown trên giao diện web GitHub** | Mở tệp `.md`, bấm biểu tượng bút chì, lưu [commit]; web tự dựng lại | Miễn phí | Người chịu học chút cú pháp Markdown | (kiến thức chung) |
| **Google Sheets làm CMS** | File > Share > Publish to web, chọn định dạng CSV; web đọc CSV lúc dựng (Astro) hoặc lúc chạy | Miễn phí | Danh sách sự kiện, lịch khai giảng, bảng giá | https://support.google.com/docs/answer/183965 |

Lưu ý với Google Sheets xuất bản:
- Bản xuất bản cập nhật trễ "vài phút".
- Nội dung xuất bản là **công khai** với mọi người; không để cột email, số điện thoại trong trang tính được xuất bản.
- Tài khoản tổ chức (Workspace) có thể bị quản trị viên tắt chức năng xuất bản.
- Với Astro xuất tĩnh, đọc CSV lúc dựng nghĩa là sửa Sheet xong phải dựng lại web (có thể đặt lịch dựng lại hằng ngày); đọc lúc chạy bằng JavaScript thì cập nhật ngay nhưng SEO kém hơn.

---

## 4. Thanh toán cho cá nhân, hộ kinh doanh Việt Nam

### 4.1. Bối cảnh pháp lý 2026 (quan trọng trước khi chọn công cụ)

- Từ 01/01/2026 bỏ thuế khoán với hộ kinh doanh. Nguồn: https://daibieunhandan.vn/cach-tinh-thue-doi-voi-ho-kinh-doanh-ban-hang-online-sau-khi-bo-thue-khoan-10396920.html
- Nghị định 141/2026/NĐ-CP (ban hành 29/04/2026, hiệu lực từ 01/01/2026) nâng ngưỡng doanh thu không chịu thuế GTGT và TNCN của hộ kinh doanh, cá nhân kinh doanh từ 500 triệu lên **1 tỷ đồng/năm**. Nguồn: https://lsvn.vn/chinh-thuc-nang-nguong-chiu-thue-voi-ho-kinh-doanh-len-1-ti-dong-nam-a172198.html
- Nghị định 68/2026/NĐ-CP và Thông tư 18/2026/TT-BTC yêu cầu hộ kinh doanh thông báo **mọi tài khoản ngân hàng và ví điện tử dùng để nhận tiền kinh doanh** cho cơ quan thuế (mẫu 01/BK-STK), kể cả khi doanh thu dưới 1 tỷ; hạn chót gia hạn 31/07/2026. Nguồn: https://lsvn.vn/doanh-thu-duoi-1-ti-ho-kinh-doanh-co-phai-thong-bao-so-tai-khoan-a176691.html
- MoMo đã yêu cầu hộ kinh doanh cập nhật thông tin khớp giấy phép kinh doanh, theo Thông tư 25/2025/TT-NHNN và Nghị định 68/2026 (thông báo 20/03/2026). Nguồn: https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-cap-nhat-moi-nhat-ve-giai-phap-nhan-tien-8587
- Với người bán khoá học, vé sự kiện qua công ty thì dùng tài khoản công ty; câu hỏi "cá nhân không đăng ký kinh doanh có được nhận tiền khoá học vào tài khoản cá nhân không" là câu hỏi thuế, **nên hỏi kế toán**, báo cáo này không kết luận.

### 4.2. Các công cụ

| Công cụ | Là gì | Yêu cầu | Phí | Nguồn |
|---|---|---|---|---|
| **VietQR tĩnh/động qua img.vietqr.io** | Tạo ảnh mã QR chuyển khoản bằng một đường link: `https://img.vietqr.io/image/<NGÂN_HÀNG>-<SỐ_TK>-<MẪU>.png?amount=<SỐ_TIỀN>&addInfo=<NỘI_DUNG>&accountName=<TÊN>`. Nội dung tối đa 50 ký tự, không ký tự đặc biệt. Mẫu: `compact2`, `compact`, `qr_only`, `print` | Chỉ cần số tài khoản | Miễn phí, không cần khoá API | https://www.vietqr.io/danh-sach-api/link-tao-ma-nhanh/ |
| **SePay** | Theo dõi biến động số dư tài khoản ngân hàng (cá nhân hoặc doanh nghiệp), bắn webhook về web trong khoảng 10 giây, đẩy vào Google Sheets, Telegram, Lark | Liên kết tài khoản bằng OTP; cá nhân dùng được | Free: 50 giao dịch/tháng; Startup từ 120.000 đ/tháng. Gói miễn phí liệt kê 11 ngân hàng (Vietcombank, BIDV, VietinBank, MB, ACB, VPBank, TPBank, Sacombank, MSB, OCB, KienlongBank) | https://sepay.vn/bang-gia.html ; https://sepay.vn/ |
| **PayOS** (sản phẩm của Casso) | Cổng thanh toán dựa trên tài khoản ngân hàng, tạo VietQR động có mã đơn, trang thanh toán dựng sẵn, webhook | Trang chủ ghi "không giấy phép kinh doanh", đăng ký bằng CCCD khoảng 5 phút | Trang chủ ghi miễn phí giao dịch, miễn phí cài đặt và duy trì; có gói theo ngân hàng đối tác (ví dụ BIDV-1K: 1.000 giao dịch/năm). **Không mở được trang bảng giá chi tiết khi kiểm [cần kiểm lại]** | https://payos.vn/ |
| | Tạo link thanh toán **cần máy chủ** để ký yêu cầu bằng khoá checksum và nhận webhook | | | https://payos.vn/docs/ |
| **Casso** | Kết nối ngân hàng và tự động hoá (Casso Flow), webhook, xác nhận đơn | Doanh nghiệp là chính | Tính theo năm, dùng thử 14 ngày hoặc 100 giao dịch; không công bố giá chi tiết | https://www.casso.vn/bang-gia/ |
| **MoMo Business** | QR nhận tiền cho hộ kinh doanh; cổng thanh toán cho doanh nghiệp | Hộ kinh doanh phải khớp GPKD theo quy định 2026 | Từ 20/09/2023: miễn phí thu, rút miễn phí tới 30 triệu/tháng, vượt mức tính 0,5%. Phí cổng thanh toán doanh nghiệp **[không tìm thấy công bố chính thức]** | https://www.momo.vn/tin-tuc/thong-bao/quan-trong-cap-nhat-cac-chinh-sach-phi-va-quyen-4904 |
| **VNPAY cổng thanh toán** | Thẻ nội địa, quốc tế, QR | Thường yêu cầu pháp nhân (doanh nghiệp hoặc hộ kinh doanh) và hồ sơ ký hợp đồng | **Không kiểm được trang chính thức (lỗi 404) [cần kiểm lại]** | https://vnpay.vn |
| **Stripe** | | **Không hỗ trợ** doanh nghiệp đăng ký tại Việt Nam (Đông Nam Á chỉ có Singapore, Malaysia, Thái Lan, Hồng Kông; Indonesia ở dạng xem trước) | | https://stripe.com/global |

### 4.3. Luồng đơn giản nhất để bán khoá học hoặc vé từ web tĩnh

**Bậc 0 (không code, đối soát tay):**
1. Form đăng ký (Tally hoặc Google Forms) ghi vào Google Sheets, mỗi lượt có mã đơn ngắn (ví dụ `KH25A7`).
2. Trang cảm ơn hiện ảnh VietQR với `amount` và `addInfo=KH25A7` tạo bằng link img.vietqr.io.
3. Người tổ chức đối chiếu sao kê với Sheet, gửi email xác nhận.
Hợp với sự kiện dưới khoảng 50 người.

**Bậc 1 (tự động, gần như không code):**
1. Như trên, nhưng liên kết tài khoản nhận tiền với SePay.
2. Bật tích hợp Google Sheets sẵn của SePay để mọi giao dịch đổ vào một trang tính; dùng công thức `REGEXEXTRACT`/`XLOOKUP` khớp mã đơn với danh sách đăng ký và đánh dấu "đã trả".
3. Nếu cần gửi email xác nhận tự động: Apps Script chạy theo lịch 5 phút quét các dòng mới đã khớp (giới hạn 100 người nhận email/ngày với Gmail cá nhân).

**Bậc 2 (webhook thẳng):** SePay hoặc PayOS bắn webhook tới một điểm nhận. Cảnh báo khi điểm nhận là Apps Script:
- Apps Script không đọc được header, nên không kiểm được `Authorization: Apikey`; phải đặt token bí mật trong URL (nguồn: https://developers.google.com/apps-script/guides/web ; https://docs.sepay.vn/tich-hop-webhooks.html).
- Phản hồi Apps Script luôn đi qua chuyển hướng 302 sang `script.googleusercontent.com` (nguồn: https://developers.google.com/apps-script/guides/content). SePay coi thành công khi nhận HTTP 200/201 kèm `{"success": true}` và thử lại tối đa 7 lần trong 5 giờ (nguồn: https://docs.sepay.vn/tich-hop-webhooks.html). Nếu bên gửi không đi theo chuyển hướng, mỗi giao dịch có thể bị gửi lặp. **[chưa thử thực tế; cần chạy thử và khử trùng lặp bằng trường `id`]**.
- Cách chắc hơn: một Cloudflare Worker nhỏ (miễn phí 100.000 lượt/ngày) nhận webhook, kiểm header, rồi ghi sang Sheets hoặc D1.

Những cái bẫy khi đối soát bằng nội dung chuyển khoản:
- Người mua sửa hoặc xoá nội dung, chuyển thiếu, chuyển hai lần. Luôn có cột "cần xử lý tay".
- Mã đơn nên ngắn, chỉ chữ in hoa và số, có tiền tố cố định (ví dụ `KHT`), để dễ tách bằng biểu thức chính quy.
- Một số ngân hàng tự chèn thêm chữ vào nội dung; khớp theo "chứa mã" chứ không khớp toàn bộ chuỗi.

---

## 5. Đặt lịch, bản tin, bình luận, đo lường

### 5.1. Đặt lịch

| Công cụ | Miễn phí | Ghi chú | Nguồn |
|---|---|---|---|
| **Cal.com** | Không giới hạn loại sự kiện và lịch, nhắc qua email/SMS, thu tiền qua Stripe và PayPal | Stripe không mở được cho tài khoản Việt Nam nên phần thu tiền gần như vô dụng với người ở VN | https://cal.com/pricing |
| **Calendly** | 1 loại sự kiện, 1 lịch, có logo Calendly, không thu tiền | Standard 10 USD/người/tháng | https://calendly.com/pricing |
| **Google Calendar lịch hẹn [appointment schedules]** | Dùng được với tài khoản Google cá nhân | Một số tính năng cần Google Workspace hoặc Google One. Trang so sánh tính năng cao cấp trả lỗi 404 khi kiểm **[cần kiểm lại tính năng nào mất phí]** | https://support.google.com/calendar/answer/10729749 |

### 5.2. Bản tin

| Công cụ | Miễn phí | Nguồn |
|---|---|---|
| **Kit** (trước là ConvertKit) | Tới 10.000 người đăng ký, không giới hạn trang đích, form, thư; tự động hoá cần gói Creator 33 USD/tháng | https://kit.com/pricing |
| **MailerLite** | 250 người đăng ký, 2.500 email/tháng, 3 tự động hoá, 1 trang đích (hạn mức đã giảm so với các năm trước) | https://www.mailerlite.com/pricing |
| **Buttondown** | 100 người đăng ký | https://buttondown.com/pricing |
| **Substack nhúng** | Lấy mã ở Settings > Growth features; nhúng bằng iframe; **không tuỳ biến giao diện được** | https://support.substack.com/hc/en-us/articles/360041759232-Can-I-embed-a-signup-form-for-my-Substack-publication |

Với người đã viết Substack, nhúng form Substack là đơn giản nhất và giữ một danh sách độc giả duy nhất.

### 5.3. Bình luận

- **giscus:** miễn phí, không quảng cáo, dựa trên GitHub Discussions; cần kho mã công khai và **người bình luận phải có tài khoản GitHub**. Hợp với blog kỹ thuật, **không hợp** với độc giả phổ thông Việt Nam. Nguồn: https://giscus.app/
- Với độc giả phổ thông: thường tốt hơn là dẫn về bài đăng Facebook/Substack để thảo luận, thay vì nhúng hệ bình luận riêng (nhận định của người viết báo cáo).

### 5.4. Đo lường truy cập

| Công cụ | Miễn phí | Ghi chú | Nguồn |
|---|---|---|---|
| **Cloudflare Web Analytics** | Miễn phí, không thu dữ liệu cá nhân | Chỉ cần dán một đoạn JavaScript, **không** phải chuyển DNS sang Cloudflare. Thời gian lưu dữ liệu và việc lấy mẫu chưa được ghi trên trang kiểm **[cần kiểm lại]** | https://developers.cloudflare.com/web-analytics/about/ |
| **Umami Cloud** | Hobby: 100.000 sự kiện/tháng, 1 web, lưu 6 tháng; tự cài thì miễn phí | Pro 20 USD/tháng | https://umami.is/pricing |
| **Plausible** | Dùng thử 30 ngày, không cần thẻ | 9 USD/tháng cho 10.000 lượt xem trang | https://plausible.io/#pricing |
| **GA4** | Miễn phí, lưu dữ liệu sự kiện tối đa 14 tháng (chọn 2 hoặc 14) | Dùng cookie; cần banner đồng ý nếu có khách EU; giao diện khó với người mới | https://support.google.com/analytics/answer/11202874 |
| **Google Search Console** | Miễn phí | Xem từ khoá đưa khách tới, lỗi lập chỉ mục. Nên luôn cài | (kiến thức chung) |

---

## 6. Astro làm khung web bậc hai

### 6.1. Phiên bản hiện tại

- Bản mới nhất trên npm: **astro 7.3.6** (kiểm 07/10/2026). Mốc lớn: 5.0 (03/12/2024), 6.0 (10/03/2026), 7.0 (22/06/2026). Yêu cầu Node.js 22.12.0 trở lên. Nguồn: https://registry.npmjs.org/astro
- Astro 7.0 mang Vite 8, trình biên dịch mới viết bằng Rust, Advanced Routing; 7.2 thử nghiệm dựng tĩnh tăng dần [incremental static builds]; 7.3 phát hành 03/09/2026. Nguồn: https://astro.build/blog/
- Cloudflare mua lại Astro (thông cáo 16/01/2026). Nguồn: https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-astro-to-accelerate-the-future-of-high-performance-web-development/
- Lưu ý: kiến thức huấn luyện của nhiều mô hình AI dừng ở Astro 4 hoặc 5. Khi làm việc, nên dặn AI "dùng Astro 7, đọc docs.astro.build" để tránh code kiểu cũ.

### 6.2. Vì sao hợp với người mới làm cùng AI

- Mặc định xuất HTML tĩnh, không gửi JavaScript nếu không cần: web nhanh, đặt miễn phí ở Cloudflare Pages, Netlify, GitHub Pages.
- **Bộ sưu tập nội dung [content collections]:** khai báo trong `src/content.config.ts`, dùng bộ nạp `glob()` để đọc thư mục Markdown/MDX/YAML/JSON, `file()` để đọc một tệp dữ liệu; lược đồ kiểm dữ liệu bằng Zod, nên khi người dùng quên điền ngày hay tiêu đề bài viết thì lỗi hiện ra rõ ràng lúc dựng. Có "live collections" (`src/live.config.ts`) để lấy dữ liệu lúc chạy, nhưng cần chế độ dựng theo yêu cầu [on-demand rendering]. Nguồn: https://docs.astro.build/en/guides/content-collections/
- Một bài viết là một tệp `.md`: hợp với Pages CMS, Sveltia CMS và sửa trên GitHub.
- Cấu trúc tệp `.astro` gần với HTML thuần nên người không chuyên vẫn đọc hiểu được khi AI giải thích.

### 6.3. Các lựa chọn khác

| Khung | Phiên bản (kiểm 07/10/2026) | Khi nào chọn | Nguồn |
|---|---|---|---|
| **Eleventy (11ty)** | Ổn định 3.1.6 trên npm; trang chủ nói có v4.0.0 và dự án đổi tên thành "Build Awesome" từ 03/2026 **[cần kiểm lại trạng thái v4]** | Thích tối giản, ít phụ thuộc | https://www.11ty.dev/ ; npm `@11ty/eleventy` |
| **Hugo** | v0.167.0 (28/09/2026) | Web rất nhiều trang, cần dựng cực nhanh; nhưng cú pháp mẫu Go khó với người mới và AI hay viết sai | https://gohugo.io/news/ |

---

## 7. Ma trận quyết định

| Nhu cầu | Đơn giản nhất | Bước tiếp theo khi lớn lên | Cần coi chừng |
|---|---|---|---|
| Form liên hệ | Web3Forms (250/tháng) + honeypot | Formspree trả phí, hoặc Netlify Forms nếu đã ở Netlify | Không tải tệp ở gói miễn phí; email báo có thể vào thư rác |
| Form đăng ký có câu hỏi phức tạp | Tally nhúng, nối Google Sheets | Tally Pro (bỏ logo, tên miền riêng) | Dữ liệu nằm ở máy chủ EU của Tally |
| Ghi dữ liệu form tự thiết kế vào Sheets | Google Apps Script `doPost` | Cloudflare Worker + Sheets API hoặc D1 | CORS, sửa code phải "Edit deployment", URL công khai, 100 email/ngày |
| Chống rác | Honeypot | Cloudflare Turnstile (kiểm phía máy chủ) | Turnstile chỉ ở giao diện là vô dụng |
| Đăng nhập + dữ liệu riêng | Firebase Spark + Security Rules | Supabase Pro (25 USD) khi cần SQL | Luật mở, `auth != null`, khoá bí mật trong code; Supabase Free tạm dừng sau 7 ngày; Cloud Storage cần Blaze |
| Lưu ảnh người dùng tải lên | Tránh; dùng Tally (có tải tệp) hoặc Google Drive | Firebase Blaze / Supabase Storage | Vụ Tea 2025: bucket mở |
| Người khác tự sửa nội dung | Pages CMS | Sveltia CMS, TinaCMS | Decap + Git Gateway đã ngừng phát triển |
| Lịch khai giảng, danh sách sự kiện | Google Sheets xuất bản CSV | Content collections + CMS | Dữ liệu công khai, trễ vài phút |
| Thu tiền khoá học, vé | VietQR link + mã đơn + đối soát tay | SePay → Google Sheets tự động; PayOS link thanh toán qua Worker | Thông báo tài khoản với thuế (NĐ 68/2026); người mua sửa nội dung CK; Stripe không có ở VN |
| Đặt lịch 1:1 | Cal.com miễn phí | Calendly Standard | Thu tiền qua Stripe không dùng được ở VN |
| Bản tin | Nhúng Substack (nếu đã có) hoặc Kit Free | Kit Creator (tự động hoá) | MailerLite Free còn 250 người |
| Bình luận | Dẫn về Facebook/Substack | giscus (độc giả kỹ thuật) | Độc giả phổ thông không có GitHub |
| Đo lường | Cloudflare Web Analytics + Search Console | Umami Cloud / Plausible | GA4 dùng cookie, phức tạp |
| Web nhiều trang, blog | Astro 7 xuất tĩnh | Astro + live collections, Eleventy | Dặn AI dùng đúng phiên bản; Node ≥ 22.12 |
| Nơi đặt web | Cloudflare Pages / GitHub Pages | Netlify | Netlify Free: 300 tín dụng, 15 tín dụng/lần triển khai, hết là tạm dừng mọi web |

---

## 8. Những điểm chưa chắc chắn

1. Bảng giá chi tiết PayOS (trang `/bang-gia/` trả 404); chỉ có thông tin "miễn phí" ở trang chủ.
2. Phí và hồ sơ cổng thanh toán VNPAY và MoMo cho doanh nghiệp: không tìm được trang chính thức đọc được.
3. Hạn mức Appwrite Cloud Free lấy từ trang tổng hợp, không phải trang chính thức.
4. Cách Apps Script trả chuyển hướng 302 có làm SePay/PayOS coi là thất bại hay không: chưa thử.
5. Tính năng nào của lịch hẹn Google Calendar cần trả phí.
6. Trạng thái Eleventy v4 / "Build Awesome".
7. Thời gian lưu dữ liệu của Cloudflare Web Analytics.
8. Câu hỏi thuế khi cá nhân chưa đăng ký kinh doanh nhận tiền khoá học: cần ý kiến kế toán.

---

## 9. Danh sách nguồn (kiểm 07/10/2026)

Biểu mẫu và chống rác
- https://formspree.io/plans
- https://web3forms.com/pricing
- https://docs.netlify.com/manage/forms/usage-and-billing/
- https://docs.netlify.com/manage/forms/spam-filters/
- https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans
- https://www.netlify.com/pricing/
- https://usebasin.com/pricing
- https://getform.com/pricing
- https://tally.so/pricing
- https://tally.so/help/webhooks
- https://developers.google.com/apps-script/guides/services/quotas
- https://developers.google.com/apps-script/guides/web
- https://developers.google.com/apps-script/guides/content
- https://developers.google.com/apps-script/concepts/deployments
- https://dev.to/bs_tales/tutorial-add-forms-to-static-sites-with-google-sheets-1c3a
- https://dev.to/allenarduino/how-to-connect-your-html-form-to-google-sheets-without-a-backend-31bo
- https://developers.cloudflare.com/turnstile/plans/
- https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
- https://www.hcaptcha.com/pricing

Backend và bảo mật
- https://firebase.google.com/pricing
- https://firebase.google.com/docs/storage/faqs-storage-changes-announced-sept-2024
- https://firebase.google.com/docs/rules/insecure-rules
- https://firebase.google.com/docs/app-check
- https://firebase.google.com/docs/projects/api-keys
- https://supabase.com/pricing
- https://supabase.com/docs/guides/api/api-keys
- https://supabase.com/docs/guides/database/postgres/row-level-security
- https://agentdeals.dev/vendor/appwrite
- https://turso.tech/pricing
- https://pocketbase.io/
- https://developers.cloudflare.com/workers/platform/pricing/
- https://www.superblocks.com/blog/lovable-vulnerabilities
- https://securityaffairs.com/180539/data-breach/hackers-leak-images-and-comments-from-women-dating-safety-app-tea.html
- https://wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
- https://cybernews.com/news/16000-supabase-databases-exposed/

Quản lý nội dung
- https://pagescms.org/
- https://github.com/sveltia/sveltia-cms
- https://decapcms.org/docs/intro/
- https://answers.netlify.com/t/netlify-identity-is-staying-feb-2026-reversal-what-changed-whos-affected-and-how-to-proceed/162733
- https://tina.io/pricing
- https://support.google.com/docs/answer/183965

Thanh toán và pháp lý
- https://www.vietqr.io/danh-sach-api/link-tao-ma-nhanh/
- https://sepay.vn/bang-gia.html
- https://sepay.vn/
- https://docs.sepay.vn/tich-hop-webhooks.html
- https://payos.vn/
- https://payos.vn/docs/
- https://www.casso.vn/bang-gia/
- https://www.momo.vn/tin-tuc/thong-bao/quan-trong-cap-nhat-cac-chinh-sach-phi-va-quyen-4904
- https://www.momo.vn/tin-tuc/thong-cao-bao-chi/momo-cap-nhat-moi-nhat-ve-giai-phap-nhan-tien-8587
- https://stripe.com/global
- https://daibieunhandan.vn/cach-tinh-thue-doi-voi-ho-kinh-doanh-ban-hang-online-sau-khi-bo-thue-khoan-10396920.html
- https://lsvn.vn/chinh-thuc-nang-nguong-chiu-thue-voi-ho-kinh-doanh-len-1-ti-dong-nam-a172198.html
- https://lsvn.vn/doanh-thu-duoi-1-ti-ho-kinh-doanh-co-phai-thong-bao-so-tai-khoan-a176691.html

Đặt lịch, bản tin, bình luận, đo lường
- https://cal.com/pricing
- https://calendly.com/pricing
- https://support.google.com/calendar/answer/10729749
- https://kit.com/pricing
- https://www.mailerlite.com/pricing
- https://buttondown.com/pricing
- https://support.substack.com/hc/en-us/articles/360041759232-Can-I-embed-a-signup-form-for-my-Substack-publication
- https://giscus.app/
- https://developers.cloudflare.com/web-analytics/about/
- https://umami.is/pricing
- https://plausible.io/#pricing
- https://support.google.com/analytics/answer/11202874

Khung web
- https://registry.npmjs.org/astro
- https://astro.build/blog/
- https://docs.astro.build/en/guides/content-collections/
- https://www.cloudflare.com/press/press-releases/2026/cloudflare-acquires-astro-to-accelerate-the-future-of-high-performance-web-development/
- https://www.11ty.dev/
- https://gohugo.io/news/

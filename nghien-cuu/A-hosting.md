# Nghiên cứu A: chọn nền tảng lưu trữ web cho xưởng web AI

Ngày kiểm tra toàn bộ nguồn: 07/10/2026 (trừ khi ghi khác). Mọi con số lấy từ trang tài liệu hoặc trang giá chính thức tại thời điểm kiểm tra; các nền tảng này đổi giá khá thường xuyên, nên trước khi ra quyết định lớn nên mở lại đường dẫn nguồn.

Ký hiệu: **[Chưa chắc]** = thông tin chưa kiểm chứng được trực tiếp từ nguồn chính thức, hoặc nguồn mâu thuẫn.

---

## 1. Tóm tắt điều hành

- **Mặc định đề xuất: Cloudflare Workers (tài nguyên tĩnh [static assets])** - miễn phí, cho phép dùng thương mại, băng thông [bandwidth] và lượt truy cập vào file tĩnh **không giới hạn và không tính phí**, có trung tâm dữ liệu tại **Hà Nội và TP.HCM**, không cần thẻ tín dụng, triển khai bằng `wrangler` với token nên rất hợp cho Claude tự động hóa. Cloudflare cũng đã mua lại Astro (01/2026).
- **Vercel Hobby** dễ dùng nhất cho người mới nhưng **chỉ được dùng phi thương mại** - không dùng cho trang bán khóa học.
- **Netlify Free** đã chuyển sang **tính theo tín dụng [credit]** từ 04/09/2025: 300 tín dụng/tháng, mỗi lần triển khai bản chính thức [production deploy] tốn 15 tín dụng, tức tối đa khoảng 20 lần đẩy bản chính thức mỗi tháng nếu không có lưu lượng. Hết tín dụng thì **toàn bộ** trang bị tạm dừng. Bù lại, biểu mẫu [Netlify Forms] miễn phí và không giới hạn.
- **GitHub Pages** hợp cho trang cá nhân/tài liệu, không phù hợp cho trang bán hàng, không có hàm máy chủ, không hỗ trợ định tuyến SPA chuẩn.
- **Firebase Hosting (Spark)** chỉ nên dùng khi web-app đã dùng Firestore/Auth của Firebase; giới hạn truyền dữ liệu chỉ 360 MB/ngày (khoảng 10 GB/tháng); muốn dùng Cloud Functions phải lên gói Blaze trả theo dùng.

---

## 2. Bảng so sánh tổng hợp

| Tiêu chí | Cloudflare Workers / Pages | Vercel Hobby | Netlify Free (gói tín dụng) | GitHub Pages | Firebase Hosting (Spark) | Render (static site) |
|---|---|---|---|---|---|---|
| Giá | $0 | $0 | $0 | $0 (kèm tài khoản GitHub) | $0 | $0 |
| Dùng thương mại | Được (không thấy điều khoản cấm) [Chưa chắc ở mức điều khoản] | **Không** - chỉ phi thương mại | Được | **Không** cho trang chủ yếu phục vụ giao dịch thương mại | Không thấy điều khoản cấm | Được |
| Băng thông miễn phí | File tĩnh: không giới hạn, miễn phí | 100 GB Fast Data Transfer/tháng | ~15 GB nếu không đẩy bản nào (20 tín dụng/GB, trần 300 tín dụng) | 100 GB/tháng (giới hạn mềm) | 10 GB/tháng (360 MB/ngày) | 5 GB/tháng [Chưa chắc - thấp bất thường] |
| Lượt build | Pages: 500 build/tháng; Workers Builds: 3.000 phút/tháng | 100 lần triển khai/ngày; 1 build đồng thời | Mỗi lần đẩy bản chính thức = 15 tín dụng; bản xem trước miễn phí | 10 build/giờ (mềm, không áp dụng khi dùng GitHub Actions) | Không nêu giới hạn build (build tại máy) | 500 phút build/tháng |
| Số dự án | 100 Workers / 100 dự án Pages | 200 dự án | Không giới hạn | Mỗi kho 1 trang | 36 trang/dự án Firebase | Không nêu |
| Kéo-thả không cần git | Có (cloudflare.com/drop, giữ 1 giờ rồi phải nhận về tài khoản; và tải trực tiếp trên bảng điều khiển) | Có (vercel.com/drop) | Có (app.netlify.com/drop) | Không (phải dùng kho GitHub) | Không (chỉ CLI) | Không (chỉ git) |
| Bản xem trước [preview deploy] | Có | Có | Có, miễn phí tín dụng | Không | Có (kênh xem trước [preview channels]) | Có (theo pull request) |
| HTTPS tự động | Có | Có | Có | Có (Let's Encrypt) | Có | Có (Let's Encrypt) |
| Tên miền riêng | Workers: tên miền phải nằm trên Cloudflare (đổi nameserver); Pages: cho phép tên miền ngoài | 50 tên miền/dự án | Có | Có | Có | 2 tên miền (Hobby) |
| Biểu mẫu tích hợp | Không (tự viết bằng Worker hoặc dịch vụ ngoài) | Không | **Có, miễn phí, không giới hạn** | Không | Không (ghi trực tiếp vào Firestore) | Không |
| Hàm máy chủ [serverless functions] | Có: 100.000 lượt/ngày, 10 ms CPU/lượt | Có: 1 triệu lượt/tháng, 4 giờ CPU | Có (tính 10 tín dụng/GB-giờ) | Không | **Không** (Cloud Functions cần Blaze) | Không (cho static site) |
| Biến môi trường [environment variables] | Có (64/Worker) | Có | Có | Không (chỉ lúc build qua Actions) | Không áp dụng cho Hosting | Có (lúc build) |
| Kho riêng tư [private repo] | Có [Chưa chắc chi tiết với kho tổ chức] | Có với kho cá nhân; **không** kết nối kho của tổ chức GitHub | Kho riêng tư của **tổ chức** chỉ có ở Pro; kho cá nhân [Chưa chắc] | Chỉ với GitHub Pro/Team trở lên | Không áp dụng (deploy từ máy) | Có [Chưa chắc] |
| Cần thẻ tín dụng | Không | Không | Không | Không | Không | Có thể bị yêu cầu (xác minh $1) [Chưa chắc] |
| Khi vượt hạn mức | File tĩnh không bị chặn; hàm vượt 100.000 lượt/ngày trả lỗi 429 | Tạm dừng (503 DEPLOYMENT_PAUSED), chờ khoảng 30 ngày; không tính tiền | **Tạm dừng toàn bộ trang** đến chu kỳ sau; không mua thêm được | Có thể bị giới hạn tốc độ (429) | Ân hạn ngắn rồi **tắt trang** | Tạm dừng nếu không có thẻ; có thẻ thì tính tiền thêm |
| Máy chủ biên gần Việt Nam | **Hà Nội (HAN), TP.HCM (SGN)**, Singapore | Singapore (sin1), Hong Kong (hkg1) và 126 PoP | Singapore | Fastly: Singapore, Bangkok, Kuala Lumpur, Manila; không có Việt Nam | Fastly (như GitHub Pages) [Chưa chắc] | Không rõ |
| Astro | Có (Cloudflare sở hữu Astro) | Có | Có | Có (qua GitHub Actions) | Có | Có |
| Định tuyến SPA | `not_found_handling = "single-page-application"` | `rewrites` trong vercel.json | `/* /index.html 200` | Không hỗ trợ chuẩn (mẹo dùng 404.html) | `rewrites` trong firebase.json | Quy tắc rewrite |
| Lệnh cho Claude triển khai | `npx wrangler deploy` + `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID` | `vercel deploy --prod --yes --token` | `netlify deploy --prod` + `NETLIFY_AUTH_TOKEN`, `NETLIFY_SITE_ID` | `git push` + GitHub Actions, hoặc gói `gh-pages` | `firebase deploy --only hosting` + tài khoản dịch vụ | Chỉ qua git push |

---

## 3. Chi tiết từng nền tảng

### 3.1. Vercel (gói Hobby)

**Hạn mức miễn phí** (nguồn: https://vercel.com/docs/plans/hobby, cập nhật 14/09/2026; https://vercel.com/docs/limits, cập nhật 16/09/2026 - kiểm tra 07/10/2026)
- Fast Data Transfer: 100 GB/tháng; Fast Origin Transfer: 10 GB; CDN Requests: 1.000.000; lượt gọi hàm [function invocations]: 1.000.000; Active CPU: 4 giờ; 5.000 lượt biến đổi ảnh.
- 200 dự án; 50 tên miền/dự án; 100 lần triển khai/ngày; 1 build đồng thời; tối đa 45 phút/build; tải lên qua CLI tối đa 100 MB mã nguồn.
- Khi vượt hạn mức: "In most cases, if you exceed your usage limits on the Hobby plan, you will have to wait until 30 days have passed before you can use the feature again." Bản chính thức có thể bị tạm dừng với lỗi `503 DEPLOYMENT_PAUSED` (https://vercel.com/kb/guide/why-is-my-account-deployment-blocked). Không có chu kỳ tính tiền nên không có hóa đơn bất ngờ.

**Hạn chế thương mại - đã xác minh** (https://vercel.com/docs/limits/fair-use-guidelines, cập nhật 14/09/2026)
- "Hobby teams are restricted to non-commercial personal use only."
- Định nghĩa thương mại rất rộng: bất kỳ triển khai nào phục vụ lợi ích tài chính của **bất kỳ ai** tham gia sản xuất, kể cả người được trả tiền để viết mã. Ví dụ: nhận thanh toán từ khách, **quảng bá bán sản phẩm hoặc dịch vụ**, được trả tiền để làm/lưu trữ trang, trang chủ yếu để gắn liên kết tiếp thị liên kết [affiliate], gắn quảng cáo. Kêu gọi quyên góp [donations] **không** bị coi là thương mại.
- Hệ quả: trang giới thiệu khoá học có nút đăng ký trả phí của một công ty giáo dục **không được** đặt trên Hobby. Trang hồ sơ cá nhân có giới thiệu dịch vụ coaching cũng có rủi ro bị coi là "advertising the sale of a service".

**Dễ dùng cho người mới**
- Hobby: "Free forever", không cần thẻ (https://vercel.com/pricing).
- Kéo-thả: vercel.com/drop - kéo file, thư mục hoặc .zip, Vercel tự nhận khung [framework] và build; cần chọn nhóm và đặt tên dự án; sau đó có thể nối với kho git (https://vercel.com/kb/guide/vercel-drop-vs-cloudflare-direct-upload, cập nhật 30/06/2026). Lưu ý: mỗi lần kéo-thả tạo dự án mới.
- **Không kết nối được kho của tổ chức GitHub [GitHub organization] trên Hobby**: "Vercel does not support connecting a project on your Hobby team to Git repositories owned by Git organizations." (https://vercel.com/docs/limits). Kho cá nhân (kể cả riêng tư) thì được.
- Có bản xem trước cho mỗi nhánh, HTTPS tự động, biến môi trường.

**Biểu mẫu, hàm, biến môi trường**: không có biểu mẫu tích hợp; có hàm máy chủ (1 triệu lượt/tháng, tối đa 300 giây/lượt); có biến môi trường.

**Hiệu năng gần Việt Nam** (https://vercel.com/docs/regions, cập nhật 11/08/2026): 126 điểm hiện diện [PoP] tại 94 thành phố, 51 quốc gia; vùng tính toán gần nhất là Singapore (sin1) và Hong Kong (hkg1). Trang không liệt kê PoP cụ thể theo thành phố nên **[Chưa chắc]** có PoP tại Việt Nam hay không. Hàm mặc định chạy ở Washington (iad1) - nên chuyển sang sin1 nếu dùng hàm.

**Gói trả phí**: Pro $20/tháng, gồm $20 tín dụng sử dụng; thêm thành viên phát triển $20/người/tháng (https://vercel.com/pricing).

### 3.2. Netlify (gói Free, mô hình tín dụng)

**Thay đổi giá 2025 - đã xác minh**
- Từ 04/09/2025, mọi tài khoản **mới** dùng gói tín dụng; tài khoản tạo trước ngày này giữ gói cũ [legacy] và có thể tự chọn chuyển (https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/). Thông báo chính thức ngày 05/09/2025 (https://www.netlify.com/changelog/netlify-pricing-update-introducing-credit-based-plans/).
- Gói hiện tại (trang tài liệu cập nhật 01/09/2026, https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/credit-based-pricing-plans/): Free 300 tín dụng/tháng (**trần cứng, không mua thêm được**); Personal $9/tháng, 1.000 tín dụng; Pro từ $20/tháng, 3.000 tín dụng, không giới hạn thành viên. **[Chưa chắc]**: thông báo 09/2025 ghi Pro "$20/member/month, 5.000 credits"; trang tài liệu 2026 ghi "starts at $20/month, 3.000 credits, unlimited members" - có vẻ Netlify đã điều chỉnh gói Pro trong 2026.

**Cách tiêu tín dụng** (nguồn như trên)
- Mỗi lần đẩy bản chính thức thành công: 15 tín dụng. Bản xem trước và triển khai nhánh: 0 tín dụng. Bản lỗi và thao tác quay lui [rollback] không tốn.
- Băng thông: 20 tín dụng/GB. Lượt truy cập web: 2 tín dụng/10.000 lượt. Tính toán: 10 tín dụng/GB-giờ. AI: 180 tín dụng cho mỗi $1.
- Biểu mẫu: **miễn phí cho mọi gói tín dụng**, "Forms are free and unlimited" (https://docs.netlify.com/manage/forms/usage-and-billing/).
- Phép tính thực tế: 300 tín dụng = 20 lần đẩy bản chính thức **hoặc** 15 GB băng thông, hoặc kết hợp (ví dụ 10 lần đẩy + 7,5 GB). Với cách làm việc cùng Claude (sửa - đẩy nhiều lần), con số 20 lần/tháng rất dễ chạm. **[Chưa chắc]**: tài liệu không nói rõ đẩy thủ công bằng CLI (`netlify deploy --prod`) hay kéo-thả có bị tính 15 tín dụng hay không; nên giả định là có.
- Hết tín dụng: "all of your web projects (sites/apps) are paused and visitors ... will find a `Site not available` page". Nghĩa là **một trang bị dùng nhiều sẽ kéo sập cả các trang khác** trong cùng tài khoản.

**Dùng thương mại**: không bị cấm trên Free (https://www.netlify.com/pricing/). Không cần thẻ tín dụng.

**Dễ dùng**: Netlify Drop (app.netlify.com/drop) cho phép kéo thư mục để xuất bản, kể cả khi chưa đăng nhập; với CLI có `netlify deploy --allow-anonymous`, trang tạm phải được nhận về tài khoản trong 1 giờ (https://docs.netlify.com/deploy/create-deploys/). Có bản xem trước không giới hạn, tên miền riêng kèm SSL, 1 build đồng thời.

**Kho riêng tư**: kho riêng tư thuộc tổ chức GitHub chỉ có ở Pro (https://www.netlify.com/pricing/pro-vs-free.md). Bản tóm tắt tài liệu gói còn ghi "No private repo support" cho Free - **[Chưa chắc]** điều này có áp dụng cho kho riêng tư cá nhân hay không.

**Hiệu năng**: CDN thông thường có điểm tại Singapore cho khu vực châu Á - Thái Bình Dương; nhân viên Netlify xác nhận trên diễn đàn (cập nhật gần nhất 03/2025, https://answers.netlify.com/t/is-there-a-list-of-where-netlifys-cdn-pops-are-located/855). Không có bằng chứng về điểm tại Việt Nam.

**Định tuyến SPA**: tệp `_redirects` với dòng `/* /index.html 200` (https://docs.netlify.com/manage/routing/redirects/rewrites-proxies/).

### 3.3. Cloudflare Pages và Cloudflare Workers (tài nguyên tĩnh)

**Tình trạng hợp nhất Pages vào Workers - đã xác minh**
- Trang tài liệu Pages hiện có thông báo: "Workers supports most Pages use cases and offers a broader feature set. It is Cloudflare's primary platform for building applications. **Start new projects with Workers.**" (https://developers.cloudflare.com/pages/).
- Pages **chưa bị khai tử**, không có lịch ngừng; hướng dẫn chuyển từ Pages sang Workers cập nhật 22/09/2026 (https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/).
- Khác biệt quan trọng cho người mới: Pages cho phép **tên miền nằm ngoài Cloudflare** (chỉ cần trỏ CNAME); Workers yêu cầu tên miền là "active Cloudflare zone" (https://developers.cloudflare.com/workers/configuration/routing/custom-domains/), trên gói miễn phí thực tế là phải chuyển nameserver của tên miền sang Cloudflare. Với tên miền .vn mua ở nhà đăng ký trong nước, việc đổi nameserver vẫn làm được nhưng là một bước kỹ thuật cần hướng dẫn.

**Hạn mức miễn phí**
- Workers tài nguyên tĩnh: "Requests to static assets are free and unlimited." (https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/). 20.000 file/phiên bản, tối đa 25 MiB/file, 100 quy tắc `_headers`, 2.000 chuyển hướng tĩnh (https://developers.cloudflare.com/workers/platform/limits/).
- Hàm Worker (phần mã chạy): 100.000 lượt/ngày, 10 ms CPU/lượt, 100 Worker/tài khoản, 64 biến môi trường/Worker. Lưu ý: nếu cấu hình `run_worker_first`, khi vượt hạn mức lượt gọi thì yêu cầu nhận lỗi 429 thay vì file tĩnh.
- Workers Builds (build từ git): 3.000 phút/tháng, 1 build đồng thời, 20 phút/build (https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).
- Pages: 500 build/tháng, 1 build đồng thời, 100 dự án, 100 tên miền/dự án, 20.000 file, 25 MiB/file; người dùng mới bị hạn chế tạo dự án trong 48 giờ đầu (https://developers.cloudflare.com/pages/platform/limits/).
- Gói Workers trả phí: $5/tháng (https://www.cloudflare.com/plans/developer-platform/).

**Dễ dùng**
- Cloudflare Drop (ra mắt 08/07/2026): kéo thư mục hoặc .zip vào cloudflare.com/drop, **không cần tài khoản**, có bản xem trước sống 1 giờ, sau đó đăng nhập để nhận về (https://developers.cloudflare.com/changelog/post/2026-07-08-cloudflare-drag-and-drop/).
- Tải trực tiếp trên bảng điều khiển: tối đa 1.000 file, 25 MiB/file; tải trực tiếp không chuyển sang git được về sau (https://vercel.com/kb/guide/vercel-drop-vs-cloudflare-direct-upload - nguồn của Vercel, nên đọc với độ dè dặt).
- Bảng điều khiển Cloudflare nhiều sản phẩm, dễ gây rối cho người mới hơn Vercel/Netlify (nhận định, không có nguồn định lượng).

**Biểu mẫu**: không có biểu mẫu tích hợp. Cách làm: viết một Worker nhận dữ liệu (lưu vào D1/KV hoặc gửi email), hoặc dùng dịch vụ ngoài. **[Chưa chắc]**: chưa nghiên cứu chi tiết các dịch vụ biểu mẫu bên thứ ba trong báo cáo này.

**Hiệu năng tại Việt Nam - bằng chứng mạnh nhất trong các nền tảng**
- Cloudflare công bố trung tâm dữ liệu thứ 160 và 161 tại **Hà Nội và TP.HCM** từ 20/12/2018 (https://blog.cloudflare.com/ten-new-data-centers/). Trang theo dõi độc lập openstatus vẫn liệt kê "Cloudflare Workers Ho Chi Minh City, Vietnam (SGN)" (https://www.openstatus.dev/status/cloudflare-workers/ho-chi-minh-city-vietnam-sgn).
- **[Chưa chắc]**: việc người dùng Việt Nam có thực sự được phục vụ từ HAN/SGN hay bị chuyển sang Singapore/Hong Kong phụ thuộc vào kết nối giữa Cloudflare và từng nhà mạng (Viettel, VNPT, FPT). Có ý kiến trên diễn đàn LowEndTalk (04/2020) cho rằng gói miễn phí bị định tuyến kém hơn ở châu Á (https://lowendtalk.com/discussion/comment/3097347/), nhưng đây là nguồn cũ, không chính thức. Nên kiểm tra thực tế bằng cách mở `https://<tên-trang>/cdn-cgi/trace` từ mạng Việt Nam và xem dòng `colo=`.

**Astro**: Cloudflare mua lại công ty Astro ngày 16/01/2026, cam kết Astro vẫn mã nguồn mở và triển khai được ở mọi nơi (https://www.nasdaq.com/press-release/cloudflare-acquires-astro-accelerate-future-high-performance-web-development-2026-01).

**Định tuyến SPA**: trong `wrangler.jsonc`/`wrangler.toml`, đặt `assets.not_found_handling = "single-page-application"` (https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/).

### 3.4. GitHub Pages

Nguồn: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (kiểm tra 07/10/2026)
- Trang xuất bản tối đa 1 GB; kho nguồn khuyến nghị dưới 1 GB; băng thông giới hạn mềm 100 GB/tháng; 10 build/giờ (mềm, không áp dụng khi dùng GitHub Actions); triển khai quá 10 phút sẽ hết thời gian; có thể bị giới hạn tốc độ (lỗi 429).
- **Cấm** dùng làm "free web-hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS)". Trang bán khóa học thuộc diện rủi ro.
- Kho riêng tư chỉ dùng được với GitHub Pro, Team, Enterprise; GitHub Free bắt buộc kho công khai.
- HTTPS tự động qua Let's Encrypt cho cả tên miền riêng, có tùy chọn "Enforce HTTPS"; GitHub cảnh báo không dùng Pages cho giao dịch nhạy cảm như mật khẩu, thẻ tín dụng (https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).
- Không có hàm máy chủ, không có biến môi trường lúc chạy, không có biểu mẫu, không có bản xem trước.
- SPA: chỉ hỗ trợ trang `404.html` tùy chỉnh, không có cơ chế viết lại URL (https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site).
- Astro: cần cấu hình GitHub Actions làm nguồn xuất bản (https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site; https://docs.astro.build/en/guides/deploy/).
- CDN: Fastly; bản đồ mạng Fastly có Singapore, Bangkok, Kuala Lumpur, Manila, Hong Kong, **không có Việt Nam** (https://www.fastly.com/network-map). Việc GitHub Pages dùng Fastly là hiểu biết phổ biến, **[Chưa chắc]** vì không tìm thấy trang tài liệu GitHub nói thẳng.

### 3.5. Firebase Hosting (gói Spark)

- Lưu trữ 10 GB; truyền dữ liệu 360 MB/ngày (trang giá, https://firebase.google.com/pricing) hay 10 GB/tháng (trang hạn mức, https://firebase.google.com/docs/hosting/usage-quotas-pricing) - hai cách diễn đạt gần tương đương.
- Vượt lưu trữ: không đẩy được bản mới; vượt truyền dữ liệu: "a short grace period but then your sites will be disabled".
- Tối đa 36 trang/dự án Firebase; file tối đa 2 GB; Spark chặn tải lên file thực thi như `.exe`, `.apk` (https://firebase.google.com/docs/hosting/faq-and-troubleshooting).
- Spark: "No payment method needed". **Cloud Functions và App Hosting không có trên Spark**, phải lên Blaze.
- Rủi ro hóa đơn trên Blaze: "Budget alerts do not pause services" - cảnh báo ngân sách không tự dừng dịch vụ; Firebase có thêm cơ chế "spend cap budgets" cho Cloud Functions và App Hosting (https://firebase.google.com/docs/projects/billing/avoid-surprise-bills).
- Dễ dùng: chỉ triển khai qua Firebase CLI (`firebase deploy`), không có kéo-thả; có kênh xem trước, SSL tự động, tích hợp GitHub cho pull request (https://firebase.google.com/docs/hosting). Với ứng dụng render phía máy chủ (Next.js, Angular SSR), Firebase khuyên dùng App Hosting thay vì Hosting.
- SPA: khai báo `rewrites` trong `firebase.json` để mọi đường dẫn trả về `index.html` (https://firebase.google.com/docs/hosting/full-config).
- CDN: theo netify.ai, Firebase chạy trên hạ tầng Fastly (https://www.netify.ai/resources/platforms/firebase) - **[Chưa chắc]**, không phải nguồn chính thức; Fastly không có điểm tại Việt Nam.
- Điều khoản thương mại: không tìm thấy điều khoản cấm dùng thương mại cho Hosting trên Spark.

### 3.6. Render (static site, tùy chọn)

- Static site miễn phí; Hobby: 2 tên miền riêng; bản xem trước theo pull request; quy tắc chuyển hướng/viết lại; TLS tự động; **chỉ triển khai qua git** (https://render.com/docs/static-sites).
- Trang giá ghi băng thông Hobby "5 GB included per month then $0.15 per GB", 500 phút build/tháng, và có xác minh thẻ $1 (https://render.com/pricing). **[Chưa chắc]**: mức 5 GB thấp hơn nhiều so với hiểu biết trước đây; trang không nói rõ thẻ là bắt buộc khi đăng ký hay chỉ khi dùng dịch vụ trả phí.
- Khi vượt: không có thẻ thì dịch vụ bị tạm ngưng; có thẻ thì bị tính tiền thêm (https://render.com/docs/free).
- Kết luận: không có lợi thế nào so với Cloudflare cho trang tĩnh; không đề xuất.

---

## 4. Claude và các tác tử AI triển khai thế nào

Nguyên tắc chung: để Claude tự triển khai mà không cần mở trình duyệt đăng nhập, cần một **mã truy cập [token]** lưu trong biến môi trường, không bao giờ ghi vào kho mã.

| Nền tảng | Lệnh | Biến môi trường/xác thực | Nguồn |
|---|---|---|---|
| Cloudflare Workers | `npx wrangler deploy` | `CLOUDFLARE_API_TOKEN` (mẫu quyền "Edit Cloudflare Workers"), `CLOUDFLARE_ACCOUNT_ID` | https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/ |
| Vercel | `vercel deploy --prod --yes --token=$VERCEL_TOKEN`; có `--prebuilt`, `--non-interactive` | Token cá nhân; có thể kèm phạm vi nhóm qua `--scope` | https://vercel.com/docs/cli/deploy (cập nhật 18/09/2026) |
| Netlify | `netlify deploy --prod`; `--allow-anonymous` cho trang tạm | `NETLIFY_AUTH_TOKEN`, `NETLIFY_SITE_ID` | https://docs.netlify.com/api-and-cli-guides/cli-guides/get-started-with-cli/ |
| Firebase | `firebase deploy --only hosting` | Tài khoản dịch vụ [service account] + `GOOGLE_APPLICATION_CREDENTIALS`; cách cũ `firebase login:ci` / `FIREBASE_TOKEN` đã bị **đánh dấu lỗi thời** và sẽ bị gỡ | https://github.com/firebase/firebase-tools |
| GitHub Pages | `git push` kèm quy trình GitHub Actions, hoặc gói npm `gh-pages` | Token GitHub (`gh auth`) | https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site |

Ngoài CLI, Netlify có máy chủ MCP chính thức cho tác tử AI triển khai (https://docs.netlify.com/welcome/build-with-ai/netlify-mcp-server); tài liệu Vercel gợi ý plugin `npx plugins add vercel/vercel-plugin` cho tác tử. **[Chưa chắc]**: chưa kiểm tra mức độ hoạt động của các MCP này với Claude Code.

Lưu ý riêng cho mô hình làm việc với Claude: Vercel có trang "fast static deployment" cho trang chỉ gồm HTML/Markdown, tối đa 10 file và 5 MB, không cần build (https://vercel.com/docs/cli/deploy) - rất hợp cho trang một tệp Claude sinh ra, nhưng vẫn vướng giới hạn phi thương mại.

---

## 5. Đề xuất

### (a) Trang cá nhân, phi thương mại
**Mặc định: Cloudflare Workers (tài nguyên tĩnh).** Lý do: băng thông file tĩnh không giới hạn, có máy chủ tại Hà Nội và TP.HCM, không cần thẻ, triển khai bằng token rất gọn cho Claude, và quan trọng nhất là **một nền tảng dùng chung cho cả trang cá nhân lẫn trang thương mại** - không phải chuyển nhà khi trang cá nhân bắt đầu giới thiệu dịch vụ.
**Thay thế:** Vercel Hobby nếu cần trải nghiệm đơn giản nhất và chắc chắn trang không có yếu tố bán hàng/quảng bá dịch vụ. GitHub Pages cho trang tài liệu công khai.

### (b) Trang thương mại, ví dụ trang đăng ký khóa học
**Mặc định: Cloudflare Workers (miễn phí).** Lý do: được dùng thương mại, không có trần băng thông cho file tĩnh nên một đợt chạy quảng cáo không làm trang bị tạm dừng.
**Không dùng:** Vercel Hobby (cấm thương mại, https://vercel.com/docs/limits/fair-use-guidelines), GitHub Pages (cấm trang phục vụ giao dịch thương mại).
**Khi cần trả phí:** Vercel Pro $20/tháng nếu dùng Next.js và cần sự tiện lợi của Vercel; hoặc Cloudflare Workers Paid $5/tháng nếu cần nhiều lượt gọi hàm.
**Thận trọng với Netlify Free:** được dùng thương mại nhưng trần 300 tín dụng cứng; một chiến dịch kéo 15 GB lưu lượng hoặc 20 lần sửa trang trong tháng sẽ làm **mọi trang** trong tài khoản hiển thị "Site not available".

### (c) Trang cần biểu mẫu
**Mặc định: Netlify Free** cho trang đơn giản, ít thay đổi, cần thu đăng ký/liên hệ: biểu mẫu tích hợp miễn phí, không giới hạn, chỉ cần thêm thuộc tính `data-netlify="true"` vào thẻ form. Điều kiện: dùng bản xem trước (miễn phí) để Claude sửa thử, chỉ đẩy bản chính thức khi đã chốt, để giữ số lần đẩy dưới khoảng 15 lần/tháng; bật chống thư rác (honeypot, reCAPTCHA) theo khuyến nghị của Netlify.
**Thay thế:** Cloudflare Workers + một Worker nhỏ nhận dữ liệu biểu mẫu (kèm Turnstile chống thư rác) hoặc dịch vụ biểu mẫu bên ngoài - phù hợp khi trang thương mại có lưu lượng lớn. **[Chưa chắc]**: chi tiết dịch vụ biểu mẫu bên thứ ba cần một nghiên cứu riêng.

### (d) Web-app dùng Firebase (Firestore, Auth)
**Mặc định: Firebase Hosting (Spark)** khi ứng dụng đã dùng Firestore/Auth: cùng một dự án, cùng bảng điều khiển, tên miền xác thực Auth khớp sẵn, `firebase deploy` một lệnh. Giới hạn cần nhớ: 360 MB/ngày truyền dữ liệu; Cloud Functions bắt buộc Blaze.
**Khi lên Blaze:** đặt cảnh báo ngân sách và spend cap cho Cloud Functions, vì cảnh báo ngân sách không tự dừng dịch vụ.
**Thay thế khi lưu lượng lớn:** đặt phần giao diện trên Cloudflare Workers, phần dữ liệu vẫn dùng Firebase SDK từ trình duyệt - tách hạ tầng giao diện khỏi giới hạn 10 GB/tháng của Spark (cần thêm tên miền Cloudflare vào danh sách tên miền được phép của Firebase Auth).

---

## 6. Rủi ro cần theo dõi

1. **Giá thay đổi nhanh**: Netlify đổi mô hình 09/2025 và tiếp tục điều chỉnh gói Pro trong 2026; Vercel chuyển Pro sang tín dụng; Render có vẻ đã hạ băng thông miễn phí. Nên kiểm tra lại mỗi 6 tháng.
2. **Phụ thuộc Cloudflare**: một nhà cung cấp cho cả DNS lẫn hosting; nếu tài khoản bị khóa thì mất cả hai. Nên giữ mã nguồn trên GitHub và giữ thông tin đăng nhập nhà đăng ký tên miền.
3. **Tạm dừng toàn tài khoản trên Netlify Free**: tách trang thương mại quan trọng sang tài khoản/nền tảng khác.
4. **Định nghĩa "thương mại" của Vercel rất rộng**: kể cả trang cá nhân có giới thiệu dịch vụ coaching trả phí.
5. **Hiệu năng thực tế tại Việt Nam** chưa được đo; nên kiểm tra bằng `/cdn-cgi/trace` (Cloudflare) và công cụ đo tốc độ từ mạng Viettel/VNPT/FPT trước khi chốt.
6. **Token triển khai** là chìa khóa vào tài khoản: chỉ cấp quyền tối thiểu (ví dụ mẫu "Edit Cloudflare Workers"), lưu trong biến môi trường, không đưa vào kho mã.

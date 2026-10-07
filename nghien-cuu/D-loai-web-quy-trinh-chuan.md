# Nghiên cứu D: các loại web thường gặp, quy trình tư vấn và bộ chuẩn chất lượng cho xưởng web AI

Tổng quan tài liệu [literature review] phục vụ thiết kế repo "xưởng web AI": bộ khung giúp người không chuyên kỹ thuật (nhà giáo dục, coach, tư vấn, doanh nghiệp nhỏ ở Việt Nam) dựng website và ứng dụng web nhỏ cùng trợ lý lập trình AI (Claude Cowork/Claude Code, Codex, Antigravity) một cách nhất quán, đạt chuẩn chuyên nghiệp.

- Ngày kiểm tra nguồn: 2026-10-07 (mọi URL dưới đây đều được truy cập ngày này, trừ khi ghi khác).
- Quy ước: [thuật ngữ tiếng Anh] trong ngoặc vuông ở lần đầu xuất hiện; (chú thích) trong ngoặc tròn.
- Mức tin cậy: **[chắc]** = nguồn gốc chính thức/nguồn sơ cấp; **[khá]** = nguồn thứ cấp uy tín hoặc nhiều nguồn khớp nhau; **[cần kiểm]** = nguồn đơn lẻ, nguồn có lợi ích thương mại, hoặc tôi chưa đọc được văn bản gốc.

---

## 0. Tóm lược điều hành

1. Nhu cầu web của cá nhân và tổ chức nhỏ hội tụ về khoảng 12 loại. Phần lớn (8/12) chạy được bằng **trang tĩnh** [static site] cộng dịch vụ nhúng (form, lịch hẹn, mã QR thanh toán). Chỉ khu thành viên, bảng điều khiển nội bộ và một phần microsite sự kiện thật sự cần máy chủ [backend].
2. Bối cảnh Việt Nam: 68% lưu lượng web là di động; người dùng đến từ Facebook, Zalo, TikTok nhiều hơn từ tìm kiếm. Vì vậy thẻ Open Graph, nút Zalo và tốc độ trên di động quan trọng ngang SEO.
3. Chuẩn kỹ thuật 2026 đã khá ổn định: Core Web Vitals (LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1), WCAG 2.2 AA (nay là ISO/IEC 40500:2025). Google khẳng định không cần tệp hay schema riêng cho tìm kiếm AI; llms.txt hầu như không được AI đọc.
4. Pháp lý Việt Nam mới: Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và Nghị định 356/2025 có hiệu lực từ 01/01/2026; Luật Thương mại điện tử 122/2025/QH15 có hiệu lực từ 01/07/2026. Mọi form thu thập dữ liệu phải có ô đồng ý không đánh dấu sẵn.
5. Rủi ro lớn nhất của web làm cùng AI không nằm ở giao diện mà ở **bảo mật** (45% tác vụ sinh mã có lỗ hổng OWASP; commit có Claude Code hỗ trợ rò bí mật 3,2% so với nền 1,5%) và **khả năng tiếp cận** (WebAIM 2026 ghi nhận lỗi tăng trở lại, nêu đích danh "vibe coding").
6. Vòng kiểm chứng tự động chạy không giao diện [headless] làm được hoàn toàn bằng Python + Node: Playwright (ảnh chụp), axe-core (tiếp cận), Lighthouse (hiệu năng/SEO), html-validate (HTML), lychee hoặc linkinator (liên kết).

---

## 1. Phân loại các loại web thường gặp

### 1.1. Bằng chứng từ các nền tảng dựng web

Danh mục mẫu [template categories] của các nền tảng dựng web phản ánh khá trung thực những gì người dùng thật sự cần, vì các nền tảng tối ưu danh mục theo hành vi.

| Nền tảng | Danh mục theo loại/mục đích | Nguồn |
|---|---|---|
| Wix | One Page, eCommerce, Portfolio & CV, Blog; ngành: Business, Health & Wellness, Events, Education, Communities, Restaurants & Food... | https://www.wix.com/website/templates **[chắc]** |
| Squarespace | 15 danh mục: Portfolios, Photography, Online Stores, Blogs & Podcasts, Professional Services, Local Business, Community & Non-Profits, Events, Weddings, Entertainment, Memberships, Restaurants, Personal & CV, Real Estate, Launch Pages | https://www.tooltester.com/en/blog/squarespace-templates **[khá]** (trang gốc squarespace.com/templates trả lỗi 429 khi truy cập) |
| Framer | Portfolio, Software, Agency, Ecommerce, Services (Consulting, Education, Legal...), Health (Therapy, Wellness...), Publishing, Real Estate, Hospitality, Events | https://www.framer.com/marketplace/templates/ **[chắc]** |
| Carrd | "simple, fully responsive one-page sites for pretty much anything": hồ sơ cá nhân, trang đích thu email; bản Pro thêm form, thanh toán, nhúng | https://carrd.co/ **[chắc]** |
| Linktree | khoảng 50 triệu người dùng (05/2024): loại "link-in-bio" là nhu cầu đại trà | https://www.statista.com/statistics/1468835/linktree-global-users **[khá]** |

Điểm chung qua bốn nền tảng: (a) hồ sơ cá nhân/portfolio, (b) trang một trang/trang ra mắt, (c) dịch vụ chuyên nghiệp, (d) doanh nghiệp địa phương, (e) blog, (f) sự kiện, (g) thành viên/cộng đồng, (h) cửa hàng. Các nhóm ngành "Education", "Health & Wellness/Therapy", "Consulting/Coaching" xuất hiện ở cả Wix và Framer, khớp đúng nhóm người dùng mục tiêu của xưởng.

### 1.2. Bằng chứng từ khảo sát doanh nghiệp nhỏ

- Clutch (08/2025, Mỹ): 83% doanh nghiệp nhỏ có website (2018: 64%); 41% dùng công cụ tự dựng [DIY builders] như Wix/Squarespace, 34% dùng WordPress/Shopify, 12% làm riêng. Trong 17% chưa có website, hơn 1/3 cho rằng website "không liên quan" vì đã bán qua mạng xã hội hoặc sàn. https://www.businesswire.com/news/home/20250821848152/en/ **[khá]** (không công bố cỡ mẫu trong thông cáo).
- Hàm ý: khách hàng nhỏ cần website như "căn cứ" đáng tin cậy bên cạnh mạng xã hội, chứ không thay thế mạng xã hội.

### 1.3. Đặc thù thị trường Việt Nam

| Chỉ số | Giá trị | Nguồn |
|---|---|---|
| Người dùng internet | 85,6 triệu (84,2% dân số), 10/2025 | https://datareportal.com/reports/digital-2026-vietnam **[chắc]** |
| Facebook | 79,0 triệu người dùng | như trên |
| Zalo | 78,3 triệu người dùng hoạt động tháng | như trên |
| TikTok (18+) | 76,1 triệu | như trên |
| YouTube | 62,1 triệu | như trên |
| Tốc độ di động trung vị | 152 Mbps (08/2025) | như trên |
| Thị phần nền tảng duyệt web | Di động 68,05%, máy tính 30,93%, máy tính bảng 1,02% (09/2026) | https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/viet-nam **[chắc]** |
| Văn hóa landing page | LadiPage: hơn 300.000 khách hàng, hơn 3,5 triệu landing page (số liệu khoảng 2020-2021) | https://theleader.vn/startup-ladipage-nhan-von-tu-shark-binh-giua-dai-dich-d16897.html **[khá, số liệu cũ]** |

Hệ quả thiết kế cho xưởng:

1. **Thiết kế cho di động trước** [mobile-first]: 2/3 lượt xem là điện thoại. Google cũng đã chuyển hẳn sang lập chỉ mục ưu tiên di động; trang không truy cập được trên di động có thể bị loại khỏi chỉ mục sau 05/07/2024. https://ppc.land/google-search-completes-transition-to-mobile-first-indexing-by-july-5-2024 **[khá]**
2. **Lưu lượng đến từ mạng xã hội và nhắn tin**: Facebook và Zalo đọc thẻ Open Graph để hiện ảnh/tiêu đề khi chia sẻ link; Zalo có công cụ làm mới bộ đệm tại developers.zalo.me/tools/debug-sharing; ảnh khuyến nghị 1200×630. https://helpv3.ladipage.vn/cac-tinh-nang-mo-rong/sua-loi-chia-se-tren-facebook-va-zalo **[khá]**. Facebook: tối thiểu 200×200, tỉ lệ gần 1,91:1, tối đa 8 MB. https://developers.facebook.com/docs/sharing/webmasters/images/ **[chắc]**
3. **Kênh liên hệ ưu tiên là Zalo**: link `https://zalo.me/<số điện thoại>` mở trò chuyện Zalo. https://dienthoaivui.com.vn/cach-lay-link-zalo **[khá]**
4. **Thanh toán không cần backend**: VietQR Quick Link tạo ảnh QR chuyển khoản miễn phí, không cần khóa API: `https://img.vietqr.io/image/<BANK_ID>-<ACCOUNT_NO>-<TEMPLATE>.png?amount=&addInfo=&accountName=`. https://www.vietqr.io/danh-sach-api/link-tao-ma-nhanh/ **[chắc]**. Lưu ý: QR tĩnh không tự xác nhận đã thanh toán; muốn đối soát tự động phải dùng dịch vụ có webhook (cần backend).

### 1.4. Bảng phân loại đề xuất (12 loại)

Phân bậc hạ tầng:
- **Bậc 0, tĩnh thuần**: HTML/CSS/JS, không thu dữ liệu.
- **Bậc 1, tĩnh + dịch vụ nhúng**: form (Google Forms, Tally...), lịch hẹn, QR VietQR, phân tích truy cập. Dữ liệu nằm ở dịch vụ bên thứ ba.
- **Bậc 2, backend nhẹ**: Google Apps Script/Sheets hoặc hàm không máy chủ [serverless function] để nhận form, gửi email xác nhận.
- **Bậc 3, backend thật**: cơ sở dữ liệu + xác thực người dùng (ví dụ Supabase). Bắt buộc có người có chuyên môn rà soát bảo mật.

| # | Loại | Mục đích chính (công việc cần làm) | Các phần thường có | Tính năng bắt buộc | Bậc |
|---|---|---|---|---|---|
| 1 | Hồ sơ cá nhân / portfolio [personal profile/portfolio] | Tạo niềm tin, để người khác "tra" mình trước khi hợp tác | Giới thiệu, chuyên môn, dự án/tác phẩm, báo chí, chứng nhận, liên hệ | OG, schema Person/ProfilePage, nút Zalo/email, ảnh tối ưu | 0 |
| 2 | Trang liên kết [link-in-bio] | Một link duy nhất gắn trên bio mạng xã hội | Ảnh đại diện, tên, 5-10 nút, mạng xã hội | Tải cực nhanh, nút lớn (≥ 24px, nên 44px), UTM | 0 |
| 3 | Trang đích cho chương trình/sự kiện/sách [landing page] | Chuyển người xem thành người đăng ký/mua | Vấn đề, lời hứa, nội dung chương trình, người hướng dẫn, cảm nhận, giá, câu hỏi thường gặp, kêu gọi hành động | Form đăng ký, ô đồng ý dữ liệu, QR thanh toán, OG đẹp | 1 |
| 4 | Dịch vụ B2B và yêu cầu báo giá [B2B services & quote] | Doanh nghiệp tìm hiểu năng lực, gửi yêu cầu | Dịch vụ, quy trình, khách hàng tiêu biểu, nghiên cứu tình huống, đội ngũ, form yêu cầu | Form nhiều trường, tải hồ sơ năng lực (PDF), schema Organization | 1 |
| 5 | Website doanh nghiệp nhỏ / thương hiệu [small business/brand site] | "Căn cứ" chính thức, xuất hiện trên Google | Trang chủ, giới thiệu, sản phẩm/dịch vụ, tin tức, liên hệ, bản đồ, chính sách | Nhiều trang, sitemap, LocalBusiness, chính sách bảo mật; thông báo Bộ Công Thương nếu bán hàng (mục 3.6) | 0-1 |
| 6 | Blog / bản tin [blog/newsletter] | Xây uy tín chuyên môn bằng nội dung | Danh sách bài, bài viết, chuyên mục, đăng ký nhận tin, RSS | Bộ sinh trang tĩnh hoặc nền tảng có sẵn (Substack), schema Article, RSS | 0-1 |
| 7 | Microsite sự kiện có đăng ký [event microsite] | Bán vé/nhận đăng ký, cung cấp thông tin hậu cần | Lịch trình, diễn giả, địa điểm, vé, câu hỏi thường gặp, đếm ngược | Form + QR + email xác nhận; schema Event; trang cảm ơn | 1-2 |
| 8 | Thư viện tài nguyên / công cụ tra cứu [resource library/lookup tool] | Tra cứu nhanh một kho tri thức | Ô tìm kiếm, bộ lọc, thẻ kết quả, trang chi tiết | Dữ liệu JSON/CSV tách khỏi giao diện, tìm kiếm phía trình duyệt, URL chia sẻ được | 0 |
| 9 | Trắc nghiệm / công cụ tự đánh giá [quiz/self-assessment] | Giúp người dùng hiểu mình, đồng thời là "mồi" thu khách tiềm năng | Giới thiệu, câu hỏi, thanh tiến độ, kết quả diễn giải, gợi ý bước tiếp | Tính điểm phía trình duyệt; nếu lưu kết quả thì cần đồng ý rõ ràng, coi là dữ liệu nhạy cảm nếu liên quan sức khỏe tâm lý | 0 (không lưu) / 2 (có lưu) |
| 10 | Đặt lịch hẹn [booking] | Khách tự chọn giờ tư vấn/coaching | Dịch vụ, thời lượng, giá, lịch trống, xác nhận | Nhúng dịch vụ lịch có sẵn (không tự xây); nhắc lịch; múi giờ | 1 |
| 11 | Khu thành viên / cổng khóa học [member area/course portal] | Phân phối nội dung trả phí, theo dõi tiến độ | Đăng nhập, bài học, tài liệu, tiến độ, cộng đồng | Xác thực, phân quyền, thanh toán; ưu tiên nền tảng có sẵn | 3 |
| 12 | Bảng điều khiển nội bộ [internal dashboard] | Theo dõi số liệu vận hành của nhóm | Chỉ số chính, biểu đồ, bảng, bộ lọc thời gian | Đọc dữ liệu từ Google Sheets/CSV; không công khai; xác thực | 2-3 |

Ghi chú về cách phân loại:
- Loại 1-6 tương ứng trực tiếp với danh mục của Wix/Squarespace/Framer/Carrd (mục 1.1). Loại 7, 10, 11 tương ứng "Events", "Memberships/Scheduling". Loại 8, 9, 12 là ứng dụng web nhỏ [small web-apps], không xuất hiện trong danh mục mẫu nhưng là nhu cầu điển hình của nhà giáo dục và tư vấn; mẫu "HTML tools" một tệp của Simon Willison (hơn 150 công cụ do LLM viết) cho thấy loại này phù hợp nhất để AI dựng. https://simonwillison.net/2025/Dec/10/html-tools/ **[chắc]**
- Thương mại điện tử đầy đủ (giỏ hàng, kho, vận chuyển) **cố ý để ngoài** bộ 12 loại: ở Việt Nam đã có sàn và nền tảng chuyên dụng; tự xây kéo theo nghĩa vụ pháp lý (mục 3.6) và rủi ro bảo mật thanh toán. Đề xuất: website giới thiệu sản phẩm + link sang sàn/Zalo.
- Loại 10 và 11: khuyến nghị **tích hợp, không tự xây**. Đây là đề xuất thiết kế dựa trên nguyên tắc "do less" của GOV.UK (mục 2.4), không phải số liệu.

---

## 2. Quy trình khám phá và tư vấn với khách hàng không chuyên kỹ thuật

### 2.1. Khung lý thuyết nền

| Khung | Nội dung cốt lõi | Ứng dụng trong xưởng | Nguồn |
|---|---|---|---|
| Giai đoạn khám phá [discovery phase] (NN/g) | Mục tiêu là "đạt đồng thuận về vấn đề cần giải quyết và kết quả mong muốn"; cần khi "có nhiều điều chưa biết khiến nhóm không tiến lên được"; đầu ra: phát biểu vấn đề có bằng chứng, hành trình người dùng, phát biểu nhu cầu | Bước 1 của quy trình: buổi phỏng vấn 30-45 phút trước khi viết dòng code nào | https://www.nngroup.com/articles/discovery-phase/ (2020, rà soát 08/2024) **[chắc]** |
| Công việc cần làm [jobs-to-be-done, JTBD] | Khách hàng "thuê" sản phẩm để hoàn thành một việc; việc luôn có chiều chức năng, xã hội và cảm xúc; hoàn cảnh quan trọng hơn nhân khẩu học | Hỏi: "Khi người ta vào trang này, họ đang cố làm xong việc gì?" | Christensen, Hall, Dillon & Duncan, HBR 09/2016: https://hbr.org/2016/09/know-your-customers-jobs-to-be-done **[chắc]** |
| Nội dung trước [content-first] | "Nội dung hầu như luôn là thứ được nghĩ tới sau cùng và giao sau cùng" (Halvorson); người dùng đến website vì nội dung | Thu nội dung thật (chữ, ảnh, giá) trước khi thiết kế; cấm lorem ipsum trong bản giao | Jeremy Keith ghi lại bài nói của Kristina Halvorson, 06/2009: https://adactio.com/journal/1587 **[chắc]** |
| MoSCoW (DSDM) | Must/Should/Could/Won't; phép thử Must: "Điều gì xảy ra nếu yêu cầu này không đạt?" Nếu còn cách vòng, dù thủ công, thì không phải Must; Must không quá 60% công sức, Could khoảng 20% | Chốt phạm vi phiên bản 1; ghi rõ danh sách "Won't" để tránh phình | https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html **[chắc]** |
| Nguyên tắc thiết kế GOV.UK | "Start with user needs", "Do less", "Do the hard work to make it simple", "Iterate. Then iterate again"; nguyên tắc 11 mới (04/2025): giảm tác động môi trường | Kim chỉ nam chọn giải pháp tối giản | https://www.gov.uk/guidance/government-design-principles (cập nhật 02/04/2025) **[chắc]** |
| Quy tắc sức mạnh tối thiểu [rule of least power] (W3C TAG) | "Dùng ngôn ngữ ít sức mạnh nhất đủ để biểu đạt thông tin"; HTML/CSS dễ tái sử dụng và phân tích hơn ngôn ngữ Turing-đầy-đủ | Cơ sở lý luận cho "HTML tĩnh trước, framework sau" | Berners-Lee & Mendelsohn, 2006: https://www.w3.org/2001/tag/doc/leastPower.html **[chắc]** |
| Để AI phỏng vấn mình | Anthropic khuyên với tính năng lớn, cho Claude phỏng vấn chi tiết rồi viết SPEC.md, sau đó mở phiên mới để thực thi | Biến bộ câu hỏi brief thành lệnh/skill để AI tự phỏng vấn khách | https://code.claude.com/docs/en/best-practices **[chắc]** |

### 2.2. Bộ câu hỏi brief đề xuất (tổng hợp từ các khung trên)

Nhóm A, mục đích và người dùng (JTBD, NN/g):
1. Ai sẽ vào trang? Họ đến từ đâu (Facebook, Zalo, Google, danh thiếp, QR in trên tài liệu)?
2. Khi vào, họ đang cố làm xong việc gì? Sau khi rời trang, họ cần đã làm được điều gì?
3. Một hành động chính duy nhất mong muốn là gì (đăng ký, nhắn Zalo, đặt lịch, tải tài liệu)?
4. Làm sao biết trang thành công sau 3 tháng (số đăng ký, số tin nhắn, số lượt tra cứu)?

Nhóm B, nội dung (content-first):
5. Nội dung nào đã có sẵn (chữ, ảnh, logo, video, cảm nhận học viên, giá)? Ai chịu trách nhiệm viết phần còn thiếu, hạn khi nào?
6. Ba website bạn thích và một website bạn không thích (để rút ra gu, không phải để sao chép)?
7. Màu, phông, giọng văn thương hiệu đã có chưa?

Nhóm C, chức năng và phạm vi (MoSCoW):
8. Có cần thu dữ liệu không? Dữ liệu gì, lưu ở đâu, ai được xem, giữ bao lâu?
9. Có cần thanh toán không? Chuyển khoản QR là đủ hay cần cổng thanh toán tự đối soát?
10. Có cần đăng nhập không? (Nếu "có", hỏi tiếp: có thể dùng nền tảng có sẵn không?)
11. Điều gì chắc chắn **không** làm ở phiên bản 1?

Nhóm D, vận hành và bảo trì:
12. Ai cập nhật nội dung sau khi bàn giao, bao lâu một lần, bằng công cụ gì (sửa tệp với AI, sửa Google Sheet, nhờ người khác)?
13. Tên miền đã có chưa, ai sở hữu tài khoản tên miền và hosting?
14. Ngân sách duy trì hằng năm (tên miền, dịch vụ form, lịch)?
15. Có bán hàng hoặc thu tiền qua website không? (Kích hoạt kiểm tra pháp lý mục 3.6.)

### 2.3. Cây quyết định "giải pháp đơn giản nhất"

Đề xuất (tổng hợp từ GOV.UK "Do less", W3C rule of least power, MoSCoW):

1. Có cần website không, hay một bài ghim Facebook/Zalo OA là đủ? (Clutch: hơn 1/3 doanh nghiệp không có website vì thấy mạng xã hội đủ dùng.)
2. Có nền tảng có sẵn làm tốt việc này không (Substack cho bản tin, dịch vụ lịch cho đặt hẹn, nền tảng khóa học cho khu thành viên)? Nếu có: dùng và nhúng.
3. Một trang HTML tĩnh có đủ không? Nếu đủ: Bậc 0.
4. Chỉ cần nhận dữ liệu? Dùng form nhúng (Bậc 1) trước khi nghĩ tới Apps Script (Bậc 2).
5. Chỉ khi cần đăng nhập, phân quyền, dữ liệu riêng tư của nhiều người dùng: Bậc 3, có người rà soát bảo mật.

Lưu ý về Apps Script làm backend: một bài hướng dẫn (của bên bán dịch vụ form, nên có thiên lệch) liệt kê nhược điểm: phải tự xử lý CORS, không có chống spam, không có thông báo email nếu không tự viết. https://dev.to/allenarduino/how-to-connect-your-html-form-to-google-sheets-without-a-backend-31bo **[cần kiểm]**. Bài này cũng nói mỗi lần sửa script sẽ ra URL mới; theo hiểu biết của tôi, sửa một bản triển khai có sẵn (Manage deployments, chọn phiên bản mới) thì giữ nguyên URL. **[cần kiểm trước khi đưa vào hướng dẫn]**

### 2.4. Cân nhắc bảo trì

- **Hosting miễn phí có điều khoản hạn chế**:
  - GitHub Pages: site tối đa 1 GB, băng thông mềm 100 GB/tháng, 10 lần build/giờ; **không** được dùng làm hosting miễn phí cho kinh doanh trực tuyến/thương mại điện tử, không dùng cho giao dịch nhạy cảm (mật khẩu, thẻ). https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits **[chắc]**. Hệ quả: website doanh nghiệp bán hàng không nên đặt trên GitHub Pages.
  - GitHub Pages không hỗ trợ tự đặt HTTP header (kể cả HSTS cho tên miền riêng); thảo luận mở từ 2021, bình luận mới nhất 07/2026 nói phải liên hệ bộ phận hỗ trợ. https://github.com/orgs/community/discussions/4444 **[khá]**
  - Cloudflare Pages miễn phí: 500 lần build/tháng, 20.000 tệp/site, tệp tối đa 25 MiB, tệp `_headers` tối đa 100 quy tắc. https://developers.cloudflare.com/pages/platform/limits/ **[chắc]**
- **Quyền sở hữu tài khoản**: tên miền, hosting, form, analytics phải đứng tên khách hàng (đề xuất thực hành, không có nguồn định lượng).
- **Tách nội dung khỏi mã**: dữ liệu thay đổi thường xuyên (lịch sự kiện, danh mục tài nguyên) đặt trong tệp JSON/CSV hoặc Google Sheet, để người không chuyên sửa mà không đụng HTML.
- **Sổ tay bàn giao**: một trang "Cách sửa website này" viết cho chủ sở hữu, kèm câu lệnh mẫu để nhờ AI sửa.

---

## 3. Bộ chuẩn chất lượng 2026

### 3.1. Hiệu năng: Core Web Vitals

| Chỉ số | Đo gì | Tốt | Kém | Nguồn |
|---|---|---|---|---|
| LCP [Largest Contentful Paint] | Tốc độ hiện nội dung chính | ≤ 2,5 s | > 4 s | https://web.dev/articles/defining-core-web-vitals-thresholds **[chắc]** |
| INP [Interaction to Next Paint] | Độ nhạy phản hồi khi tương tác | ≤ 200 ms | > 500 ms | như trên |
| CLS [Cumulative Layout Shift] | Độ ổn định bố cục | ≤ 0,1 | > 0,25 | như trên |

- INP chính thức thay FID [First Input Delay] từ **12/03/2024**. https://web.dev/blog/inp-cwv-march-12 **[chắc]**
- Đánh giá theo **phân vị thứ 75** lượt tải trang, tách riêng di động và máy tính. https://web.dev/articles/vitals **[chắc]**
- Hàm ý cho xưởng: trang tĩnh không framework gần như mặc nhiên đạt INP; rủi ro chính là LCP (ảnh hero quá nặng, phông chữ chặn hiển thị) và CLS (ảnh không khai báo kích thước, phông thay thế lệch cỡ).

### 3.2. Khả năng tiếp cận: WCAG 2.2 AA

- WCAG 2.2 công bố 05/10/2023; được phê duyệt thành **ISO/IEC 40500:2025** ngày 21/10/2025. https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ và https://www.w3.org/WAI/news/2025-10-21/wcag22-iso **[chắc]**
- 9 tiêu chí mới, trong đó 6 tiêu chí thuộc mức A/AA (bắt buộc với mục tiêu AA):

| Mã | Tên | Mức | Ý nghĩa thực hành |
|---|---|---|---|
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Phần tử đang được focus bằng bàn phím không bị header dính [sticky header], banner cookie, nút chat che hoàn toàn |
| 2.5.7 | Dragging Movements | AA | Mọi thao tác kéo thả phải có cách làm bằng một lần chạm/nhấp |
| 2.5.8 | Target Size (Minimum) | AA | Vùng bấm tối thiểu **24×24 CSS px** (có ngoại lệ về khoảng cách, liên kết trong dòng chữ...) |
| 3.2.6 | Consistent Help | A | Kênh trợ giúp (nút Zalo, số điện thoại) nằm ở cùng vị trí trên mọi trang |
| 3.3.7 | Redundant Entry | A | Không bắt nhập lại thông tin đã nhập trong cùng quy trình |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Đăng nhập không bắt giải câu đố nhận thức; cho phép dán mật khẩu, dùng trình quản lý mật khẩu |

- Tiêu chí 4.1.1 Parsing bị loại bỏ vì lỗi thời. (cùng nguồn W3C) **[chắc]**
- Thực trạng: WebAIM Million 2026 cho thấy 95,9% trang chủ có lỗi WCAG phát hiện được, trung bình 56,1 lỗi/trang (tăng 10,1%), đảo chiều sau sáu năm cải thiện. Sáu lỗi phổ biến nhất: chữ tương phản thấp (83,9%), ảnh thiếu văn bản thay thế (53,1%), ô nhập thiếu nhãn (51%), link rỗng (46,3%), nút rỗng (30,6%), thiếu khai báo ngôn ngữ (13,5%). Báo cáo nêu đích danh việc dựa vào framework bên thứ ba và "lập trình có AI hỗ trợ ('vibe coding')". https://webaim.org/projects/million/ **[chắc]**
- Hàm ý: sáu lỗi này đều phát hiện được bằng công cụ tự động (axe-core); đưa chúng thành cổng chặn [gate] bắt buộc. Riêng `lang="vi"` là lỗi rẻ nhất nhưng ảnh hưởng lớn tới trình đọc màn hình tiếng Việt.

**Đạo luật Tiếp cận châu Âu [European Accessibility Act, EAA]**:
- Áp dụng từ 28/06/2025; yêu cầu tuân thủ EN 301 549 (tương đương WCAG 2.1 A/AA); phạm vi: thương mại điện tử, ngân hàng, đặt chỗ trực tuyến, vận tải hành khách, sách điện tử; doanh nghiệp siêu nhỏ (dưới 10 người và doanh thu dưới 2 triệu euro) **được miễn** đối với dịch vụ; áp dụng cả với doanh nghiệp ngoài EU bán cho người tiêu dùng EU. https://www.accessibility-developer-guide.com/knowledge/legal/eaa/ **[khá]**. Trang của Ủy ban châu Âu xác nhận danh mục sản phẩm/dịch vụ nhưng trang tôi đọc không nêu chi tiết miễn trừ. https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en **[chắc về phạm vi; cần kiểm điều khoản miễn trừ trong văn bản Chỉ thị (EU) 2019/882]**
- Mức liên quan với khách hàng Việt Nam: thấp, trừ khi bán khóa học/dịch vụ trực tuyến cho người tiêu dùng ở EU và không thuộc diện siêu nhỏ. Dù vậy, WCAG 2.2 AA vẫn nên là chuẩn mặc định vì là thực hành tốt và nay là chuẩn ISO.

**Việt Nam**: Thông tư 26/2020/TT-BTTTT (hiệu lực 01/01/2021) về áp dụng tiêu chuẩn hỗ trợ người khuyết tật tiếp cận thông tin; bắt buộc với một số cơ quan báo chí, **khuyến khích** với tổ chức, cá nhân khác. https://hoatieu.vn/phap-luat/thong-tu-26-2020-tt-btttt-ho-tro-nguoi-khuyet-tat-su-dung-dich-vu-thong-tin-va-truyen-thong-203640 **[khá; chưa đọc được phụ lục kỹ thuật để xác định phiên bản WCAG được viện dẫn]**

### 3.3. SEO cơ bản và tìm kiếm AI

**Nền tảng (Google Search Central):**
- Sitemap: tối đa 50.000 URL hoặc 50 MB; URL tuyệt đối; `lastmod` chỉ có ích khi chính xác; Google **bỏ qua** `priority` và `changefreq`; khai báo trong robots.txt hoặc Search Console. https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap **[chắc]**
- Dữ liệu có cấu trúc [structured data]: hơn 30 loại được hỗ trợ, gồm Article, Breadcrumb, Event, Organization, Local Business, Profile Page, Course List, Review Snippet, Video (trang cập nhật 15/06/2026). https://developers.google.com/search/docs/appearance/structured-data/search-gallery **[chắc]**
- Kết quả nhiều định dạng dạng FAQ [FAQ rich results] ngừng hiển thị từ 07/05/2026; schema FAQPage vẫn hợp lệ, Google vẫn dùng để hiểu trang. https://www.techwyse.com/news/ai-search/google-faq-rich-results-deprecated-2026 **[khá]**
- Open Graph: bốn thuộc tính bắt buộc `og:title`, `og:type`, `og:image`, `og:url`; nên thêm `og:description`, `og:site_name`, `og:locale` (với tiếng Việt: `vi_VN`). https://ogp.me/ **[chắc]**

**Tìm kiếm AI / "tối ưu cho công cụ tạo sinh" [generative engine optimization, GEO]:**
- Google (trang cập nhật 10/12/2025): "Không có yêu cầu bổ sung nào để xuất hiện trong AI Overviews hay AI Mode, cũng không cần tối ưu đặc biệt"; "Bạn không cần tạo tệp đọc-được-bằng-máy mới, tệp văn bản AI hay markup... không có schema.org riêng nào cần thêm". Các thực hành SEO cơ bản vẫn giữ nguyên giá trị. https://developers.google.com/search/docs/appearance/ai-features **[chắc]**
- llms.txt: theo dõi của Originality.ai và phân tích nhật ký máy chủ của Ahrefs (công bố 02/07/2026), số site có llms.txt tăng 8,8 lần trong 12 tháng (36.120 site), nhưng **97% tệp không nhận yêu cầu nào** trong 05/2026; trong số yêu cầu có được, bot truy xuất AI chỉ chiếm 1,1%, còn công cụ kiểm tra SEO chiếm 21,7%. https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/ **[khá]**
- Lighthouse 13.3 (07/05/2026) thêm nhóm kiểm tra "Agentic Browsing", có mục kiểm tra llms.txt (trả "Không áp dụng" nếu 404, chỉ báo lỗi khi máy chủ lỗi). John Mueller giải thích đây là phục vụ tác tử AI trong trình duyệt, không phải yếu tố xếp hạng; với site không dành cho lập trình viên, ông "không nghĩ việc này có nhiều ý nghĩa". https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit **[khá; nên đối chiếu changelog Lighthouse chính thức]**
- Kết luận cho xưởng: không đưa llms.txt vào danh sách bắt buộc. Ưu tiên HTML ngữ nghĩa, tiêu đề rõ, nội dung thật, schema chuẩn, trang tải nhanh. Có thể để llms.txt là tùy chọn cho site tài liệu/tra cứu (loại 8).

### 3.4. Bảo mật cho trang tĩnh: HTTP header

Theo OWASP HTTP Headers Cheat Sheet https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html **[chắc]**:

| Header | Giá trị khuyến nghị | Ghi chú |
|---|---|---|
| Strict-Transport-Security | `max-age=63072000; includeSubDomains; preload` | Chỉ thêm `preload` khi chắc chắn mọi tên miền con đều HTTPS |
| Content-Security-Policy | Tùy site; tốt nhất không cho JS nội tuyến | Phức tạp nhất; xem CSP Cheat Sheet |
| X-Content-Type-Options | `nosniff` | |
| Referrer-Policy | `strict-origin-when-cross-origin` | |
| Permissions-Policy | `geolocation=(), camera=(), microphone=()` | |
| X-Frame-Options / CSP `frame-ancestors` | `DENY` | Chống clickjacking |
| Cross-Origin-Opener-Policy | `same-origin` | |
| X-XSS-Protection | `0` (đã lỗi thời) | Thay bằng CSP |

Triển khai trên hosting tĩnh:
- Cloudflare Pages: tệp `_headers` (tối đa 100 quy tắc, mỗi dòng ≤ 2.000 ký tự); không áp dụng cho phản hồi từ Pages Functions. https://developers.cloudflare.com/pages/configuration/headers/ **[chắc]**
- GitHub Pages: không đặt được header (mục 2.4). CSP có thể đặt qua `<meta http-equiv>` nhưng MDN lưu ý cách này "không hỗ trợ mọi tính năng CSP" và không dùng được cho chế độ report-only. https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP **[chắc]**. Theo hiểu biết chung, `frame-ancestors` không hiệu lực trong thẻ meta **[cần kiểm trong đặc tả CSP3]**.
- Mâu thuẫn cần giải quyết trong thiết kế xưởng: trang một tệp (JS/CSS nội tuyến) tiện cho người mới nhưng xung đột với CSP nghiêm ngặt. Phương án dung hòa: CSP cho phép `'unsafe-inline'` với style nhưng dùng hash/nonce cho script, hoặc tách `app.js` khi trang có form/thu dữ liệu.

### 3.5. Hình ảnh và phông chữ tiếng Việt

**Ảnh:**
- web.dev: "WebP và AVIF thường nén tốt hơn định dạng cũ, nên dùng khi có thể"; cả hai được mọi trình duyệt hiện đại hỗ trợ; dùng kèm JPEG/PNG dự phòng qua `<picture>`. https://web.dev/articles/choose-the-right-image-format **[chắc]**
- AVIF đã đạt mức Baseline sau khi Edge 121 hỗ trợ; thời điểm "widely available" (30 tháng sau) tôi chưa xác minh được ngày chính xác. https://dev.to/maxgeris/avif-achieves-baseline-availability-edge-121-support-completes-browser-adoption-simplifying-web-3778 **[cần kiểm]**
- Đề xuất cho xưởng: ảnh hero AVIF/WebP + JPEG dự phòng, luôn khai báo `width`/`height` (chống CLS), `loading="lazy"` cho ảnh dưới màn hình đầu, **không** lazy-load ảnh LCP. Ảnh OG dùng JPEG 1200×630 (Zalo/Facebook đọc ổn định nhất với JPG theo LadiPage).

**Phông chữ:**
- web.dev: chỉ dùng WOFF2; chia nhỏ phông bằng `unicode-range`; chọn `font-display: swap` (hiện chữ nhanh) hoặc `optional` (ưu tiên hiệu năng); dùng `size-adjust` cho phông dự phòng để giảm CLS; preconnect tới máy chủ phông; tránh icon font, thay bằng SVG. https://web.dev/articles/font-best-practices **[chắc]**
- Google Fonts CSS2 API: tham số `display=swap`; tham số `text=` có thể giảm kích thước tệp tới 90% khi chỉ cần vài ký tự (hợp với logo chữ, tiêu đề cố định). https://developers.google.com/fonts/docs/css2 **[chắc]**
- Tiếng Việt: Google Fonts tách phông thành các tập con [subsets], trong đó có tập `vietnamese` khai báo bằng `unicode-range`, nên trình duyệt chỉ tải phần chứa dấu tiếng Việt khi trang có ký tự đó. **[cần kiểm: tôi không truy xuất được CSS gốc của Google Fonts trong môi trường này để trích dải unicode chính xác]**. Hai điểm thực hành quan trọng: (1) chỉ chọn phông có hỗ trợ tiếng Việt (lọc theo ngôn ngữ trên Google Fonts), nếu không dấu sẽ rơi về phông hệ thống, chữ bị "lệch phông" giữa chừng; (2) khi tự lưu trữ phông [self-host] hoặc dùng `text=`/subset tùy chỉnh, phải giữ đủ các ký tự tổ hợp dấu tiếng Việt, kể cả dấu kết hợp U+0300-U+0323.
- Gợi ý phông có hỗ trợ tiếng Việt phổ biến: Be Vietnam Pro (do người Việt thiết kế) **[khá, cần kiểm danh sách đầy đủ trên Google Fonts]**.

### 3.6. Pháp lý Việt Nam về dữ liệu và thương mại điện tử

| Văn bản | Hiệu lực | Điểm chính với website nhỏ | Nguồn |
|---|---|---|---|
| Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 | 01/01/2026 | Phạt hành chính tới 5% doanh thu năm trước; doanh nghiệp nhỏ, siêu nhỏ, khởi nghiệp được chọn chưa áp dụng một số quy định (đánh giá tác động, nhân sự chuyên trách) trong 5 năm (Điều 38), **trừ** khi kinh doanh dịch vụ xử lý dữ liệu, thương mại điện tử, fintech, tiếp thị số | https://vcci.com.vn/tin-tuc/luat-bao-ve-du-lieu-ca-nhan-luu-y-ve-hanh-lang-phap-ly-moi-cho-doanh-nghiep ; https://luatvietnam.vn/dan-su/tai-toan-van-luat-bao-ve-du-lieu-ca-nhan-2025-pdf-word-568-103646-article.html **[khá; nên đọc toàn văn Điều 38]** |
| Nghị định 356/2025/NĐ-CP (thay Nghị định 13/2023) | 01/01/2026 | Đồng ý phải rõ ràng bằng văn bản, giọng nói hoặc **ô đánh dấu**; cấm ô đánh dấu sẵn; bên xử lý phải chứng minh có sự đồng ý; xử lý tự động/AI phải công khai; báo cáo sự cố dữ liệu nhạy cảm trong 72 giờ | https://lsvn.vn/mot-so-thay-doi-can-luu-y-trong-xu-ly-du-lieu-ca-nhan-tu-01-01-2026-a167892.html ; https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html **[khá]** |
| Nghị định 52/2013/NĐ-CP, sửa đổi bởi 85/2021/NĐ-CP; Thông tư 47/2014/TT-BCT | đang hiệu lực | Website thương mại điện tử bán hàng phải **thông báo** với Bộ Công Thương (online.gov.vn); áp dụng cả cá nhân có mã số thuế; theo một hãng luật, cả website chỉ giới thiệu sản phẩm (không đặt hàng) cũng có thể bị coi là xúc tiến thương mại và cần thông báo | https://luatvietan.vn/thong-bao-website-thuong-mai-dien-tu.html **[cần kiểm: đây là diễn giải của hãng luật]** |
| Luật Thương mại điện tử 122/2025/QH15 | 01/07/2026 | Chủ yếu nhắm sàn: định danh người bán, kiểm duyệt hàng, lưu thông tin sản phẩm 1 năm; người bán phải công bố thông tin đầy đủ, trung thực | https://baolaocai.vn/tu-hom-nay-172026-ban-hang-online-khong-the-an-danh-nguoi-ban-can-lam-gi-post902924.html **[khá; cần kiểm luật mới có thay đổi thủ tục thông báo website hay không]** |

Hàm ý cho bộ khung:
- Mọi form có thu họ tên/email/số điện thoại phải có: ô đồng ý **không đánh dấu sẵn**, liên kết chính sách xử lý dữ liệu, nêu mục đích và thời hạn lưu. Trắc nghiệm tâm lý (loại 9) lưu kết quả cần cân nhắc như dữ liệu nhạy cảm.
- Phân tích truy cập nên ưu tiên công cụ không dùng cookie (mục 3.7) để giảm nghĩa vụ đồng ý.
- Website bán hàng: bật cờ "cần tư vấn pháp lý" trong brief; xưởng không tự kết luận nghĩa vụ thông báo.

### 3.7. Phân tích truy cập tôn trọng quyền riêng tư

So sánh (bài của nhóm Nuxt Scripts, 03/2026) https://scripts.nuxt.com/learn/privacy-first-analytics-compared **[khá]**:

| Công cụ | Kích thước script | Tự lưu trữ | Ghi chú |
|---|---|---|---|
| Plausible | 1,9 KB | Có | Không cookie, không lưu IP; bản Community Edition giấy phép AGPLv3, script theo dõi MIT (https://github.com/plausible/analytics **[chắc]**; bài Nuxt ghi "không mã nguồn mở" là **sai**) |
| Umami | 3,2 KB | Có | MIT |
| Cloudflare Web Analytics | 10,7 KB | Không | Miễn phí, có đo Core Web Vitals |
| Vercel Analytics | 1,6 KB | Không | Chỉ dùng trên Vercel |

Đề xuất mặc định: Cloudflare Web Analytics nếu đã host trên Cloudflare Pages (miễn phí, có số liệu CWV thực tế); Umami tự lưu trữ hoặc Plausible nếu khách cần dashboard riêng. Tránh Google Analytics 4 làm mặc định vì kéo theo cookie và nghĩa vụ đồng ý (đề xuất, không có nguồn định lượng).

---

## 4. Thực hành tốt khi dựng web cùng AI

### 4.1. Tệp hướng dẫn cho tác tử: AGENTS.md và CLAUDE.md

| Công cụ | Tệp đọc | Cơ chế | Nguồn |
|---|---|---|---|
| Chuẩn chung | AGENTS.md | Định dạng mở, do OpenAI ra mắt 08/2025, hơn 60.000 dự án dùng; tặng cho Agentic AI Foundation (Linux Foundation) ngày 09/12/2025 cùng MCP (Anthropic) và goose (Block); hơn 30 công cụ hỗ trợ; tệp gần thư mục làm việc nhất được ưu tiên | https://openai.com/index/agentic-ai-foundation/ ; https://agents.md/ **[chắc]** |
| OpenAI Codex | AGENTS.md, AGENTS.override.md | Ghép từ `~/.codex` rồi từ gốc Git xuống thư mục hiện tại; tệp gần hơn ghi đè; giới hạn tổng **32 KiB** mặc định (`project_doc_max_bytes`) | https://learn.chatgpt.com/docs/agent-configuration/agents-md **[chắc]** |
| Claude Code | CLAUDE.md; đọc AGENTS.md khi không có CLAUDE.md (từ v2.1.277) | Khuyến nghị **dưới 200 dòng** mỗi tệp; nhập tệp bằng `@path` (tối đa 4 cấp); cách chia sẻ một tệp cho mọi công cụ: CLAUDE.md chứa dòng `@AGENTS.md`; quy tắc theo đường dẫn trong `.claude/rules/` | https://code.claude.com/docs/en/memory **[chắc]** |
| Google Antigravity | GEMINI.md, AGENTS.md (từ bản IDE 1.20.5), `.agents/rules/` | Giới hạn 12.000 ký tự mỗi tệp; thứ tự ưu tiên khi có cả hai tệp chưa được Google xác định | https://thepromptshelf.dev/blog/google-antigravity-agents-md-rules-guide-2026 **[cần kiểm với tài liệu chính thức của Google]** |

Hướng dẫn nội dung (Anthropic best practices) https://code.claude.com/docs/en/best-practices **[chắc]**:
- Giữ ngắn; với mỗi dòng hỏi "Bỏ dòng này có khiến Claude làm sai không?"; tệp phình to khiến Claude bỏ qua chính các chỉ dẫn quan trọng.
- Nên ghi: lệnh Claude không tự đoán được, quy ước khác mặc định, cách chạy kiểm thử, quyết định kiến trúc riêng, điểm dễ vấp. Không nên ghi: điều đọc code là biết, tài liệu API dài, mô tả từng tệp, câu sáo kiểu "viết code sạch".
- Tri thức chỉ cần đôi lúc thì đưa vào skill (nạp khi cần); việc phải xảy ra 100% thì dùng hook (tất định), không dùng chỉ dẫn (khuyến nghị).

Hàm ý thiết kế repo: **một AGENTS.md gốc ngắn** (dưới khoảng 150 dòng để lọt cả ba giới hạn: 32 KiB của Codex, 12.000 ký tự của Antigravity, 200 dòng của Claude Code), CLAUDE.md chỉ chứa `@AGENTS.md` cộng phần riêng của Claude; chi tiết theo từng loại web đặt trong thư mục con hoặc skill để nạp khi cần.

### 4.2. Tránh giao diện "AI slop" bằng hệ thống thiết kế

- Anthropic (12/11/2025) gọi nguyên nhân là **hội tụ phân phối** [distributional convergence]: mô hình chọn lựa chọn "an toàn" phổ biến nhất trong dữ liệu. Phông bị lạm dụng: Inter, Roboto, Open Sans, Lato, phông hệ thống; hình mẫu điển hình: **gradient tím trên nền trắng**. Bốn trục cần chỉ đạo: chữ, màu và chủ đề (dùng biến CSS), chuyển động, nền. https://claude.com/blog/improving-frontend-design-through-skills **[chắc]**
- Bản hiện hành của skill frontend-design (kho anthropics/skills) mở rộng danh sách "dấu hiệu AI" thành năm cụm mặc định: (1) nền kem #F4F1EA + serif tương phản cao + điểm nhấn đất nung #D97757; (2) nền gần đen + một màu nhấn chói (xanh axit, đỏ son); (3) kiểu báo giấy: kẻ mảnh, bo góc 0, cột dày đặc; (4) bộ thẻ SaaS: thẻ bo tròn giống hệt nhau, một bán kính bo cho mọi thứ, cùng một bóng xám nhạt; (5) "khung mẫu": nhãn VIẾT HOA giãn chữ, dấu chấm giữa ngăn cách, nhãn monospace, mũi tên gắn sau link. Thêm: nhấn một từ trong tiêu đề bằng nghiêng/đậm; hiệu ứng trượt-hiện cho mọi section và hover cho mọi thẻ. Nguyên tắc: "Dồn sự táo bạo vào một chỗ"; quy trình hai lượt: lập kế hoạch thiết kế ngắn (màu, chữ, bố cục) rồi đối chiếu với brief trước khi code; dòng chữ thân bài dưới 80 ký tự. https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md **[chắc; nội dung skill thay đổi theo thời gian]**
- Các dấu hiệu người dùng hay nhắc (emoji làm icon, lưới ba thẻ đều nhau) khớp với cụm (4) và (5); tôi không tìm thấy nguồn chính thức liệt kê riêng "emoji" như một dấu hiệu **[cần kiểm]**.
- Hàm ý cho xưởng:
  1. Mỗi dự án có tệp **token thiết kế** [design tokens] (`tokens.css` với biến màu, chữ, khoảng cách, bo góc) sinh từ bước phỏng vấn thương hiệu, không để AI tự chọn.
  2. Quy trình "kế hoạch thiết kế trước, code sau": AI viết `DESIGN.md` 10-15 dòng (chất liệu đặc trưng của lĩnh vực khách, cặp phông có hỗ trợ tiếng Việt, bảng màu, một "điểm nhớ" duy nhất), người dùng duyệt rồi mới dựng.
  3. Danh sách kiểm "dấu hiệu AI" dùng ở bước rà soát.

### 4.3. Vòng kiểm chứng

- Anthropic: "Cho Claude một phép kiểm tra nó chạy được: test, build, ảnh chụp để so sánh. Đó là khác biệt giữa một phiên bạn phải canh và một phiên bạn có thể rời đi"; yêu cầu đưa **bằng chứng** (đầu ra test, ảnh chụp) thay vì tự khẳng định; "nếu không kiểm chứng được thì đừng giao"; thêm bước rà soát đối nghịch bằng tác tử con với ngữ cảnh mới, nhưng chỉ sửa lỗi ảnh hưởng tính đúng hoặc yêu cầu, tránh rơi vào làm quá. https://code.claude.com/docs/en/best-practices **[chắc]**
- Có thể biến phép kiểm thành cổng tất định bằng Stop hook (chặn kết thúc lượt cho tới khi kiểm tra đạt). (cùng nguồn)
- Giới hạn của kiểm tra tự động: Playwright nhấn mạnh công cụ tự động chỉ bắt được một phần lỗi tiếp cận; nhiều lỗi chỉ phát hiện qua kiểm thử thủ công. https://playwright.dev/docs/accessibility-testing **[chắc]**. Vì vậy cần thêm danh sách kiểm thủ công ngắn (thử Tab qua toàn trang, thử trên điện thoại thật, đọc to nội dung).

### 4.4. Bảo mật của ứng dụng do AI sinh

| Bằng chứng | Số liệu | Nguồn |
|---|---|---|
| Veracode GenAI Code Security Report 2025 | 45% mã sinh ra có lỗ hổng thuộc OWASP Top 10; hơn 100 LLM, 80 tác vụ; thất bại chống XSS 86%, log injection 88%; JavaScript 38-45%; an toàn không cải thiện theo kích cỡ mô hình | https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ **[chắc]** |
| GitGuardian State of Secrets Sprawl 2026 | 28,65 triệu bí mật mới lộ trên GitHub công khai năm 2025 (+34%); khóa dịch vụ AI lộ 1,28 triệu (+81%); commit có Claude Code hỗ trợ lộ bí mật **3,2%** so với nền **1,5%** | https://dev.to/gitguardian/the-state-of-secrets-sprawl-2026-ai-service-leaks-surge-81-and-29m-secrets-hit-public-github-2bgj **[khá; nên đối chiếu báo cáo gốc gitguardian.com]** |
| CVE-2025-48757 (Lovable/Supabase) | Matt Palmer báo riêng 21/03/2025, công bố CVE 29/05/2025; hơn 170 ứng dụng, 303 endpoint thiếu RLS; lộ email, số điện thoại, thông tin thanh toán, khóa API; nguyên nhân: khóa công khai trong trình duyệt + thiếu/lỏng chính sách bảo mật mức dòng [Row Level Security, RLS] | https://www.superblocks.com/blog/lovable-vulnerabilities ; https://blog.pluto.security/p/cve-202548757-what-happened-why-it-b22 **[khá]** |
| Supabase docs | "Bật RLS trên mọi bảng trong schema được phơi ra"; khi đã bật RLS thì khóa công khai không đọc được gì cho tới khi có policy; "Không bao giờ dùng khóa bí mật trong trình duyệt" | https://supabase.com/docs/guides/database/postgres/row-level-security **[chắc]** |

Hàm ý cho bộ khung (danh sách bắt buộc):
1. Không bao giờ đặt khóa bí mật trong HTML/JS gửi xuống trình duyệt; dùng biến môi trường phía máy chủ; `.gitignore` sẵn `.env`; quét bí mật trước khi commit (ví dụ gitleaks/ggshield, đề xuất công cụ chưa được đánh giá trong báo cáo này).
2. Bậc 3 chỉ được triển khai khi: RLS bật cho mọi bảng, có test truy cập ẩn danh trả rỗng, có người rà soát.
3. Mọi dữ liệu người dùng hiển thị lại phải được thoát ký tự (chống XSS, lỗi AI hay mắc nhất theo Veracode).
4. Ưu tiên Bậc 0-1 để không có gì để rò.

### 4.5. Mã dễ đọc cho người mới; một tệp HTML hay framework

- Mẫu "HTML tools" (Simon Willison, 12/2025): một tệp HTML chứa JS và CSS nội tuyến, "ít phiền nhất khi lưu trữ và phân phối"; chủ động yêu cầu "no react", không bước build; thư viện lấy từ CDN; giữ ở mức vài trăm dòng; lưu trạng thái trong URL hoặc localStorage; host GitHub Pages. https://simonwillison.net/2025/Dec/10/html-tools/ **[chắc]**
- W3C rule of least power ủng hộ cùng hướng (mục 2.1).
- WebAIM 2026 liên hệ việc tăng phụ thuộc framework, số phần tử trang tăng 14,3%/năm với số lỗi tiếp cận tăng. https://webaim.org/projects/million/ **[chắc về số liệu; mối quan hệ là tương quan, không phải nhân quả]**
- Đề xuất phân ngưỡng cho xưởng:
  - **Một tệp HTML**: loại 2, 9 (không lưu), công cụ nhỏ của loại 8.
  - **Nhiều tệp HTML tĩnh dùng chung `tokens.css` + `site.css`**: loại 1, 3, 4, 5, 7.
  - **Bộ sinh trang tĩnh** [static site generator] (ví dụ Eleventy/Astro) chỉ khi có trên khoảng 10 trang lặp cấu trúc hoặc blog (loại 6).
  - **Framework + backend**: chỉ loại 11, 12, và nên cân nhắc nền tảng có sẵn trước.
  - Ngưỡng "10 trang" là đề xuất kinh nghiệm, không có nguồn định lượng.
- Quy ước dễ đọc: chú thích tiếng Việt ở đầu mỗi khối; tên lớp CSS mô tả nội dung; không tối ưu sớm; một tệp README "cách sửa" cho chủ sở hữu.

---

## 5. Công cụ kiểm tra chất lượng tự động chạy không giao diện

| Công cụ | Kiểm gì | Cài đặt | Phụ thuộc | Mức nhẹ | Nguồn |
|---|---|---|---|---|---|
| Playwright (Python hoặc Node) | Ảnh chụp toàn trang (`full_page=True`), ảnh theo phần tử, nhiều khổ màn hình | `pip install playwright` + `playwright install` | Trình duyệt Chromium tải về (khoảng vài trăm MB) | Trung bình; là "xương sống" cho các công cụ khác | https://playwright.dev/python/docs/screenshots **[chắc]** |
| axe-core qua `@axe-core/playwright` (Node) | Lỗi tiếp cận tự động theo thẻ WCAG (`wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`, có thể thêm `wcag22aa`) | `npm i -D @axe-core/playwright` | Playwright | Nhẹ khi đã có Playwright | https://playwright.dev/docs/accessibility-testing **[chắc]** |
| axe-playwright-python | Như trên, cho Python | `pip install axe-playwright-python` | Python ≥ 3.8, Playwright ≥ 1.25; bản 0.1.8 (24/07/2026), Pamela Fox duy trì | Nhẹ | https://pypi.org/project/axe-playwright-python/ **[chắc]** |
| Lighthouse CLI | Hiệu năng, tiếp cận, best practices, SEO; xuất JSON/HTML; `--only-categories`, `--preset desktop`, `--chrome-flags="--headless"` | `npm i -g lighthouse` | **Node 22 LTS trở lên**, Chrome/Chromium | Trung bình; điểm dao động giữa các lần chạy | https://github.com/GoogleChrome/lighthouse **[chắc]** |
| Lighthouse CI (`@lhci/cli`) | Chạy nhiều lần, khẳng định ngưỡng [assertions], ngân sách hiệu năng [budgets], so hồi quy | `npm i -g @lhci/cli@0.15.x`; `lhci autorun` | Như Lighthouse | Nặng hơn; hợp CI | https://github.com/GoogleChrome/lighthouse-ci **[chắc]** |
| html-validate | Lỗi HTML, có preset `recommended`, `standard`, `a11y`, `document`; chạy hoàn toàn offline | `npm i -D html-validate`; `npm exec html-validate file.html` | Node, **không cần Java** | Rất nhẹ | https://html-validate.org/ ; https://html-validate.org/usage/index.html **[chắc]** |
| Nu HTML Checker (vnu) | Trình kiểm chính thức của W3C cho HTML/CSS | `npm i vnu-jar`, Docker, Homebrew, hoặc bản nhị phân kèm Java | Java 17+ (trừ bản nhị phân/Docker) | Nặng hơn html-validate | https://github.com/validator/validator **[chắc]** |
| lychee | Link hỏng trong HTML/Markdown, kiểm tệp cục bộ offline, có GitHub Action | Bản nhị phân tĩnh, Docker, Homebrew, Cargo... | Không (nhị phân Rust) | Rất nhẹ, nhanh | https://github.com/lycheeverse/lychee **[chắc]** |
| linkinator | Link hỏng; tự dựng máy chủ tĩnh khi trỏ vào thư mục; `--recurse`, `--skip`, xuất JSON/CSV | npm, nhị phân, Docker | Node | Nhẹ | https://github.com/JustinBeckwith/linkinator **[chắc]** |

Đề xuất bộ tối thiểu cho xưởng (một lệnh `kiem-tra`):
1. **html-validate** (preset `recommended` + `a11y`): nhanh, offline, bắt lỗi cấu trúc trước khi mở trình duyệt.
2. **Playwright** chụp ảnh ở 3 khổ (390px di động, 768px, 1280px) để AI và người dùng tự nhìn; đồng thời kiểm vùng bấm ≥ 24px, ảnh có `width/height`, có `lang="vi"`, có đủ thẻ OG.
3. **axe-core** qua Playwright với thẻ WCAG 2.2 AA; chặn nếu có lỗi mức "serious/critical".
4. **Lighthouse** chế độ di động một lần chạy, báo điểm và LCP/CLS mô phỏng (không chặn cứng vì điểm dao động; chỉ chặn tiếp cận và SEO dưới ngưỡng).
5. **lychee** offline cho link nội bộ; link ngoài chạy ở chế độ cảnh báo.

Lựa chọn ngôn ngữ: nếu bộ khung chọn Python làm chủ, dùng Playwright Python + axe-playwright-python; vẫn cần Node cho Lighthouse và html-validate. Phương án tránh hai hệ sinh thái: viết toàn bộ bằng Node (Playwright, @axe-core/playwright, lighthouse, html-validate, linkinator là gói npm). Đây là cân nhắc thiết kế, chưa có số liệu so sánh thời gian chạy.

---

## 6. Đề xuất kiến trúc repo xưởng (rút ra từ nghiên cứu)

Phần này là đề xuất tổng hợp, không phải dữ kiện có nguồn.

```
xuong-web-ai/
├── AGENTS.md                # ngắn, dùng chung Codex/Antigravity/Claude
├── CLAUDE.md                # @AGENTS.md + phần riêng của Claude
├── quy-trinh/
│   ├── 01-phong-van-brief.md     # bộ câu hỏi mục 2.2
│   ├── 02-chon-giai-phap.md      # cây quyết định mục 2.3
│   ├── 03-ke-hoach-thiet-ke.md   # mẫu DESIGN.md, danh sách dấu hiệu AI
│   └── 04-ban-giao.md            # sổ tay bảo trì cho chủ sở hữu
├── loai-web/                # 12 thư mục, mỗi loại: cấu trúc phần, tính năng bắt buộc, bậc hạ tầng, ví dụ
├── chuan/                   # danh sách kiểm CWV, WCAG 2.2 AA, SEO/OG, header bảo mật, pháp lý VN
├── mau/                     # tokens.css, khung HTML có sẵn lang="vi", meta OG, form có ô đồng ý, _headers
└── kiem-tra/                # script QA một lệnh (mục 5)
```

---

## 7. Những điểm còn bất định

1. Dải `unicode-range` chính xác của tập con `vietnamese` trên Google Fonts: chưa trích được từ nguồn gốc.
2. Điều khoản miễn trừ doanh nghiệp siêu nhỏ của EAA: mới kiểm qua nguồn thứ cấp.
3. Phạm vi nghĩa vụ thông báo website với Bộ Công Thương sau khi Luật Thương mại điện tử 122/2025/QH15 có hiệu lực (01/07/2026), và các nghị định hướng dẫn mới: chưa xác minh; diễn giải "website chỉ giới thiệu sản phẩm cũng phải thông báo" là của một hãng luật.
4. Chi tiết hỗ trợ AGENTS.md của Antigravity: nguồn bên thứ ba.
5. Lighthouse 13.3 và mục kiểm llms.txt: nguồn tin tức, chưa đối chiếu changelog chính thức.
6. Số liệu GitGuardian về Claude Code: lấy từ bản đăng lại trên dev.to của chính GitGuardian, chưa đọc báo cáo PDF gốc; tỉ lệ 3,2% có thể chịu ảnh hưởng của việc commit có dòng "Co-Authored-By" chỉ chiếm một phần các commit có AI hỗ trợ.
7. Số liệu LadiPage là số cũ (khoảng 2020-2021).
8. Khảo sát Clutch là thị trường Mỹ; chưa tìm được khảo sát tương đương đáng tin cậy về tỉ lệ doanh nghiệp nhỏ Việt Nam có website.

---

## 8. Danh mục nguồn (truy cập 2026-10-07)

Thị trường và phân loại
- DataReportal, Digital 2026: Vietnam. https://datareportal.com/reports/digital-2026-vietnam
- StatCounter, Platform market share Viet Nam. https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/viet-nam
- Wix templates. https://www.wix.com/website/templates
- Tooltester, Squarespace templates. https://www.tooltester.com/en/blog/squarespace-templates
- Framer Marketplace templates. https://www.framer.com/marketplace/templates/
- Carrd. https://carrd.co/
- Statista, Linktree global users. https://www.statista.com/statistics/1468835/linktree-global-users
- Clutch qua Business Wire (21/08/2025). https://www.businesswire.com/news/home/20250821848152/en/
- The Leader, LadiPage. https://theleader.vn/startup-ladipage-nhan-von-tu-shark-binh-giua-dai-dich-d16897.html
- Q&Me, Vietnam mobile app usage trends 2026. https://qandme.net/en/report/vietnam-mobile-app-usage-trends-2026.html (mẫu 100 người dùng iPhone, chỉ tham khảo)
- LadiPage help, chia sẻ Facebook và Zalo. https://helpv3.ladipage.vn/cac-tinh-nang-mo-rong/sua-loi-chia-se-tren-facebook-va-zalo
- VietQR Quick Link. https://www.vietqr.io/danh-sach-api/link-tao-ma-nhanh/
- Link Zalo cá nhân. https://dienthoaivui.com.vn/cach-lay-link-zalo

Quy trình
- NN/g, Discovery phase. https://www.nngroup.com/articles/discovery-phase/
- HBR, Know your customers' jobs to be done. https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- Jeremy Keith, Content first. https://adactio.com/journal/1587
- Agile Business Consortium, MoSCoW. https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html
- GOV.UK, Government design principles. https://www.gov.uk/guidance/government-design-principles
- W3C TAG, The rule of least power. https://www.w3.org/2001/tag/doc/leastPower.html
- GitHub Pages limits. https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- GitHub community discussion #4444. https://github.com/orgs/community/discussions/4444
- Cloudflare Pages limits. https://developers.cloudflare.com/pages/platform/limits/
- Dev.to, HTML form to Google Sheets. https://dev.to/allenarduino/how-to-connect-your-html-form-to-google-sheets-without-a-backend-31bo

Chuẩn kỹ thuật
- web.dev, Web Vitals. https://web.dev/articles/vitals
- web.dev, Defining Core Web Vitals thresholds. https://web.dev/articles/defining-core-web-vitals-thresholds
- web.dev, INP becomes a Core Web Vital on March 12. https://web.dev/blog/inp-cwv-march-12
- W3C, What's new in WCAG 2.2. https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- W3C, WCAG 2.2 approved as ISO standard. https://www.w3.org/WAI/news/2025-10-21/wcag22-iso
- WebAIM Million 2026. https://webaim.org/projects/million/
- Accessibility Developer Guide, EAA. https://www.accessibility-developer-guide.com/knowledge/legal/eaa/
- European Commission, European Accessibility Act. https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
- Hoatieu, Thông tư 26/2020/TT-BTTTT. https://hoatieu.vn/phap-luat/thong-tu-26-2020-tt-btttt-ho-tro-nguoi-khuyet-tat-su-dung-dich-vu-thong-tin-va-truyen-thong-203640
- Google, AI features and your website. https://developers.google.com/search/docs/appearance/ai-features
- Google, Structured data search gallery. https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Google, Build a sitemap. https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- TechWyse, FAQ rich results deprecated. https://www.techwyse.com/news/ai-search/google-faq-rich-results-deprecated-2026
- TechWyse, Google AI search guide và Lighthouse llms.txt audit. https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit
- PPC Land, llms.txt adoption. https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/
- PPC Land, Mobile-first indexing. https://ppc.land/google-search-completes-transition-to-mobile-first-indexing-by-july-5-2024
- Open Graph protocol. https://ogp.me/
- Meta, Sharing images. https://developers.facebook.com/docs/sharing/webmasters/images/
- OWASP, HTTP Headers Cheat Sheet. https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
- Cloudflare Pages, Headers. https://developers.cloudflare.com/pages/configuration/headers/
- MDN, Content Security Policy. https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP
- web.dev, Choose the right image format. https://web.dev/articles/choose-the-right-image-format
- Dev.to, AVIF Baseline. https://dev.to/maxgeris/avif-achieves-baseline-availability-edge-121-support-completes-browser-adoption-simplifying-web-3778
- web.dev, Font best practices. https://web.dev/articles/font-best-practices
- Google Fonts CSS2 API. https://developers.google.com/fonts/docs/css2
- Nuxt Scripts, Privacy-first analytics compared. https://scripts.nuxt.com/learn/privacy-first-analytics-compared
- Plausible Analytics GitHub. https://github.com/plausible/analytics

Pháp lý Việt Nam
- VCCI, Luật Bảo vệ dữ liệu cá nhân. https://vcci.com.vn/tin-tuc/luat-bao-ve-du-lieu-ca-nhan-luu-y-ve-hanh-lang-phap-ly-moi-cho-doanh-nghiep
- LuatVietnam, toàn văn Luật 91/2025/QH15. https://luatvietnam.vn/dan-su/tai-toan-van-luat-bao-ve-du-lieu-ca-nhan-2025-pdf-word-568-103646-article.html
- LSVN, thay đổi xử lý dữ liệu cá nhân từ 01/01/2026. https://lsvn.vn/mot-so-thay-doi-can-luu-y-trong-xu-ly-du-lieu-ca-nhan-tu-01-01-2026-a167892.html
- PwC Việt Nam, bản tin 28/01/2026. https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html
- Luật Việt An, thông báo website thương mại điện tử. https://luatvietan.vn/thong-bao-website-thuong-mai-dien-tu.html
- Báo Lào Cai, Luật Thương mại điện tử từ 01/07/2026. https://baolaocai.vn/tu-hom-nay-172026-ban-hang-online-khong-the-an-danh-nguoi-ban-can-lam-gi-post902924.html

AI và quy trình dựng
- OpenAI, Agentic AI Foundation. https://openai.com/index/agentic-ai-foundation/
- AGENTS.md. https://agents.md/
- OpenAI Codex, AGENTS.md. https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Claude Code, Memory (CLAUDE.md). https://code.claude.com/docs/en/memory
- Claude Code, Best practices. https://code.claude.com/docs/en/best-practices
- The Prompt Shelf, Antigravity AGENTS.md. https://thepromptshelf.dev/blog/google-antigravity-agents-md-rules-guide-2026
- Anthropic, Improving frontend design through skills. https://claude.com/blog/improving-frontend-design-through-skills
- Anthropic skills, frontend-design SKILL.md. https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Simon Willison, Useful patterns for building HTML tools. https://simonwillison.net/2025/Dec/10/html-tools/
- Veracode, GenAI Code Security Report. https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- GitGuardian, State of Secrets Sprawl 2026. https://dev.to/gitguardian/the-state-of-secrets-sprawl-2026-ai-service-leaks-surge-81-and-29m-secrets-hit-public-github-2bgj
- Superblocks, Lovable vulnerability. https://www.superblocks.com/blog/lovable-vulnerabilities
- Pluto Security, CVE-2025-48757. https://blog.pluto.security/p/cve-202548757-what-happened-why-it-b22
- Supabase, Row Level Security. https://supabase.com/docs/guides/database/postgres/row-level-security

Công cụ QA
- Playwright, Screenshots (Python). https://playwright.dev/python/docs/screenshots
- Playwright, Accessibility testing. https://playwright.dev/docs/accessibility-testing
- axe-playwright-python. https://pypi.org/project/axe-playwright-python/
- Lighthouse. https://github.com/GoogleChrome/lighthouse
- Lighthouse CI. https://github.com/GoogleChrome/lighthouse-ci
- html-validate. https://html-validate.org/ ; https://html-validate.org/usage/index.html
- Nu HTML Checker. https://github.com/validator/validator
- lychee. https://github.com/lycheeverse/lychee
- linkinator. https://github.com/JustinBeckwith/linkinator

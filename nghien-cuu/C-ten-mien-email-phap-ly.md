# Đưa website lên tên miền riêng tại Việt Nam năm 2026: những việc người không chuyên phải tự tay làm, email theo tên miền và yêu cầu pháp lý

Báo cáo nghiên cứu C - ngày kiểm tra nguồn: 07/10/2026 (mọi nguồn dưới đây được truy cập ngày này, trừ khi ghi khác).

Quy ước đánh dấu độ tin cậy:

- **[Đã kiểm]**: đối chiếu trực tiếp trên trang chính thức (cơ quan nhà nước, tài liệu của nhà cung cấp dịch vụ) hoặc trang tra cứu văn bản luật uy tín.
- **[Nguồn thứ cấp]**: lấy từ công ty luật, báo, trang tổng hợp giá; chưa đối chiếu nguyên văn văn bản gốc.
- **[Chưa chắc]**: thông tin chưa xác minh đủ, cần kiểm lại trước khi dùng cho tư vấn chính thức.
- **[Kinh nghiệm thực hành]**: nhận định từ thực tế vận hành, không có văn bản làm căn cứ.

Lưu ý chung: đây là tài liệu nghiên cứu, không phải ý kiến pháp lý. Với các quyết định có hệ quả pháp lý (bán hàng trực tuyến, thu thập dữ liệu quy mô lớn, xin giấy phép), nên hỏi luật sư.

---

## Phần 0. Bức tranh tổng quát: vì sao trợ lý AI không làm thay được

Một trợ lý trí năng nhân tạo [AI] có thể viết mã, dựng trang, soạn chính sách bảo mật, hướng dẫn từng bước. Nhưng có một nhóm việc **bắt buộc chủ website tự làm**, vì chúng gắn với căn tính pháp lý, tiền, hoặc quyền sở hữu tài khoản:

1. **Định danh pháp lý**: khai thông tin cá nhân/tổ chức thật, số định danh cá nhân, ký hoặc xác thực bản khai đăng ký tên miền.
2. **Thanh toán**: nhập thẻ Visa/Mastercard, chuyển khoản, xác nhận OTP từ ngân hàng.
3. **Tạo và giữ tài khoản**: tạo tài khoản GitHub, Vercel/Netlify/Cloudflare, nhà đăng ký tên miền, Google Workspace; bật xác thực hai lớp [two-factor authentication - 2FA]; cất mã khôi phục [recovery codes].
4. **Bấm nút trong bảng điều khiển [dashboard]**: thêm bản ghi DNS, đổi máy chủ tên miền [nameserver], xác minh tên miền, mở khóa chuyển tên miền.
5. **Xác nhận qua email/điện thoại**: bấm liên kết xác minh, nhận mã SMS.
6. **Thủ tục hành chính**: thông báo website thương mại điện tử với Bộ Công Thương (nếu thuộc diện), quyết định chấp nhận rủi ro pháp lý.
7. **Quyết định nội dung pháp lý**: chọn mục đích thu thập dữ liệu, cam kết với người dùng, chịu trách nhiệm về nội dung.

Phần còn lại của báo cáo đi qua từng nhóm.

---

## Phần 1. Mua tên miền

### 1.1. Khung pháp lý hiện hành cho tên miền ".vn"

**Nghị định 147/2024/NĐ-CP** về quản lý, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng, ký ngày 09/11/2024, hiệu lực từ 25/12/2024, là văn bản chính quy định đăng ký, sử dụng tên miền ".vn". [Đã kiểm]

- Điều 9 có tiêu đề "Đăng ký, sử dụng, thay đổi thông tin đăng ký, tạm ngừng, thu hồi, hoàn trả tên miền". Khoản 2 cho phép mọi chủ thể (cơ quan, tổ chức, doanh nghiệp, cá nhân) đăng ký; khoản 3 quy định đăng ký qua Nhà đăng ký chính thức và phải nộp phí trước khi được cấp quyền sử dụng; khoản 4 nêu nguyên tắc "đăng ký trước được quyền sử dụng trước". [Đã kiểm, qua trang hethongphapluat.com]
  Nguồn: https://hethongphapluat.com/nghi-dinh-147-2024-nd-cp-quan-ly-cung-cap-su-dung-dich-vu-internet-va-thong-tin-tren-mang/dieu-9
- **Thông tin cá nhân phải khai** (điểm b khoản 7 Điều 9): "Họ và tên cá nhân; số định danh cá nhân hoặc số chứng minh nhân dân [hoặc số hộ chiếu]; địa chỉ thường trú đầy đủ tới số nhà", kèm ngày sinh, số điện thoại, email; với tổ chức: tên, mã số thuế/mã số doanh nghiệp, địa chỉ trụ sở, người quản lý tên miền và người quản lý kỹ thuật. [Đã kiểm]
  Nguồn: https://thuvienphapluat.vn/hoi-dap-phap-luat/thong-tin-nao-phai-cung-cap-khi-dang-ky-su-dung-ten-mien-tu-25122024-138038198.html
- Khoản 8 Điều 9 đề cập xác thực thông tin qua chữ ký số hoặc định danh điện tử. [Chưa chắc]: tôi chỉ đọc được bản tóm tắt, chưa xem nguyên văn khoản 8 để biết bắt buộc hay khuyến khích, và có đối chiếu với Cơ sở dữ liệu quốc gia về dân cư hay không.
- Có các trường hợp tạm ngừng và thu hồi tên miền (khoản 13 đến 16 Điều 9), trong đó có trường hợp thông tin đăng ký không chính xác. [Nguồn thứ cấp]
  Nguồn: https://tapchicongthuong.vn/6-truong-hop-se-bi-thu-hoi-ten-mien---vn--tu-ngay-25-12-2024-129681.htm

**Thông tư 48/2025/TT-BKHCN** của Bộ Khoa học và Công nghệ hướng dẫn quản lý, sử dụng tài nguyên Internet (hướng dẫn Nghị định 147/2024 và Nghị định 115/2025), **hiệu lực từ 10/02/2026**. [Nguồn thứ cấp, trang phổ biến pháp luật TP Cần Thơ]
Nguồn: https://pbgdpl.cantho.gov.vn/bo-truong-bo-khoa-hoc-va-cong-nghe-ban-hanh-thong-tu-so-482025tt-bkhcn-huong-dan-ve-quan-ly-va-su-dung-tai-nguyen-internet

Ghi chú: quản lý nhà nước về tên miền đã chuyển từ Bộ Thông tin và Truyền thông sang Bộ Khoa học và Công nghệ sau hợp nhất bộ năm 2025; VNNIC vẫn là đơn vị vận hành. [Nguồn thứ cấp]

### 1.2. Ai được đăng ký ".edu.vn"

- Từ **10/02/2026**, theo thông báo của nhà đăng ký quốc tế WebNIC: "Only organizations operating within the education sector are eligible to register and maintain .edu.vn domain names" (chỉ tổ chức hoạt động trong lĩnh vực giáo dục được đăng ký và duy trì tên miền .edu.vn); cá nhân không còn được đăng ký hoặc gia hạn. Ngày này trùng ngày hiệu lực Thông tư 48/2025/TT-BKHCN. [Nguồn thứ cấp]
  Nguồn: https://faq.webnic.cc/kb/vn/
- Dự thảo thông tư (đưa tin trên báo Luật sư Việt Nam) yêu cầu tên miền dưới ".edu.vn" "sử dụng đúng lĩnh vực theo quy định"; tổ chức không còn đủ điều kiện phải hoàn trả hoặc chuyển nhượng. [Nguồn thứ cấp]
  Nguồn: https://lsvn.vn/du-kien-quy-dinh-moi-ve-trinh-tu-dang-ky-ten-mien-a162536.html
- [Chưa chắc]: tôi **chưa đọc được nguyên văn điều khoản** trong Thông tư 48/2025 quy định đối tượng ".edu.vn" và giấy tờ chứng minh (giấy phép hoạt động giáo dục, quyết định thành lập, giấy chứng nhận đăng ký doanh nghiệp có ngành nghề giáo dục?). Khuyến nghị: gọi nhà đăng ký trong nước hỏi danh mục giấy tờ cụ thể trước khi mua.

**Hệ quả thực tế**: một cá nhân (nhà giáo, nhà tâm lý, coach làm độc lập) **không nên chọn ".edu.vn"** cho website cá nhân. Một công ty giáo dục có đăng ký ngành nghề giáo dục thì có thể, nhưng cần hồ sơ tổ chức.

### 1.3. Lệ phí nhà nước cho ".vn" (Thông tư 10/2025/TT-BTC, hiệu lực 03/5/2025)

[Nguồn thứ cấp, hai nguồn khớp nhau]

| Loại tên miền | Lệ phí đăng ký (1 lần) | Phí duy trì/năm |
|---|---|---|
| Tên miền cấp 2 ".vn" (vd: tenban.vn), loại thường | 100.000 đ | 350.000 đ |
| ".vn" 1 ký tự / 2 ký tự | 100.000 đ | 40.000.000 đ / 10.000.000 đ |
| .com.vn, .net.vn, .biz.vn, .ai.vn | 100.000 đ | 250.000 đ |
| .edu.vn, .gov.vn, .org.vn, .ac.vn, .health.vn, .int.vn, tên miền địa giới | 100.000 đ | 100.000 đ |
| .info.vn, .pro.vn, .id.vn | | 50.000 đ |
| .name.vn, .io.vn | | 20.000 đ |
| Tên miền tiếng Việt | | 20.000 đ |

Nguồn: https://luatvietan.vn/quy-dinh-ve-phi-le-phi-su-dung-ten-mien-theo-thong-tu-10-2025-tt-btc.html ; https://thuvienphapluat.vn/ma-so-thue/phap-luat-thue/le-phi-dang-ky-su-dung-ten-mien-quoc-gia-vn-tu-ngay-1932025-201771.html

[Chưa chắc]: hai nguồn thứ cấp lệch nhau ở phí duy trì ".edu.vn" (một nguồn ghi 50.000 đ, một nguồn ghi 100.000 đ). Bảng trên theo luatvietan.vn có bảng đầy đủ hơn; cần đối chiếu nguyên văn Thông tư 10/2025/TT-BTC.

Giá bán lẻ của nhà đăng ký = lệ phí nhà nước + phí dịch vụ của nhà đăng ký.

### 1.4. Nhà đăng ký ".vn" chính thức trong nước

Trang VNNIC liệt kê 10 nhà đăng ký trong nước: Bạch Kim (Back Kim Network Solution), GMO-Z.com RUNSYSTEM (thương hiệu Tenten), PA Việt Nam, Mắt Bão, Nhân Hòa, iNET, Online Solution, Vinahost, Tino Group, Long Vân. [Đã kiểm, trang VNNIC bản tiếng Anh]
Nguồn: https://vnnic.vn/en/domain-name-vn/registras/registras-system

- [Chưa chắc]: **Viettel IDC không xuất hiện** trong danh sách tôi đọc được; có thể Viettel bán ".vn" với tư cách đại lý của một nhà đăng ký. Kiểm tra danh sách cập nhật tại nhadangky.vn trước khi mua.
- Người dùng ở Việt Nam đăng ký ".vn" **phải qua nhà đăng ký trong nước** (nhà đăng ký quốc tế như WebNIC ghi rõ không nhận người đăng ký Việt Nam cho ".vn"). [Nguồn thứ cấp] Nguồn: https://faq.webnic.cc/kb/vn/
- Cloudflare Registrar **không bán ".vn"** (không có trong danh sách hỗ trợ). [Chưa chắc: tôi không thấy ".vn" trong tài liệu Cloudflare; nên kiểm trực tiếp trên trang tìm tên miền của Cloudflare]

### 1.5. Giá tham khảo tại nhà đăng ký Việt Nam (tháng 10/2026)

[Nguồn thứ cấp, giá trên trang bán hàng, có thể chưa gồm VAT, thay đổi theo khuyến mãi]

| Nhà đăng ký | .vn năm đầu | .vn gia hạn | .com.vn năm đầu / gia hạn | .com năm đầu / gia hạn |
|---|---|---|---|---|
| Mắt Bão | 750.000 đ | 830.000 đ | 630.000 / 700.000 đ | 109.000 / 299.000 đ |
| Nhân Hòa | 450.000 đ (khuyến mãi đến 31/10, giá gốc 650.000) | 650.000 đ | không thấy trên trang | 145.000 (khi mua từ 3 năm) / 369.000 đ |

Nguồn: https://www.matbao.net/ten-mien/bang-gia-ten-mien.html ; https://nhanhoa.com/ten-mien/bang-gia-ten-mien.html

Mắt Bão niêm yết ".edu.vn" năm đầu 400.000 đ. Cùng nguồn.

**Bài học**: giá ".com" năm đầu 109.000 đ đến 145.000 đ là giá khuyến mãi; năm thứ hai trở đi là 299.000 đ đến 369.000 đ. Luôn hỏi "giá gia hạn" trước khi mua.

### 1.6. Nhà đăng ký quốc tế cho ".com" và các đuôi quốc tế

| Nhà đăng ký | .com đăng ký / gia hạn | Ghi chú |
|---|---|---|
| Cloudflare Registrar | 10,46 USD / 10,46 USD | Bán đúng giá gốc, không lời; **bắt buộc dùng nameserver Cloudflare** |
| Porkbun | 11,08 USD (khuyến mãi 10,08) / 11,08 USD | Riêng tư WHOIS miễn phí |
| Namecheap | (không kiểm được giá tại thời điểm này) | Chấp nhận Visa, Mastercard, PayPal |
| Squarespace Domains | (không kiểm) | Tiếp nhận khách Google Domains từ 2023 |

- Cloudflare: "Cloudflare Registrar sells domains at cost: you pay the registry and ICANN list price with no markup" và "All domains on Cloudflare Registrar use Cloudflare nameservers". Muốn dùng nameserver khác thì phải chuyển tên miền đi nơi khác. Tên miền mặc định có ẩn thông tin WHOIS và tự động gia hạn. [Đã kiểm]
  Nguồn: https://developers.cloudflare.com/registrar/faq/ ; https://developers.cloudflare.com/registrar/
- Giá Cloudflare ".com" 10,46 USD, ổn định từ 28/11/2025. [Nguồn thứ cấp] Nguồn: https://domainoffer.net/tld/com/cloudflare
- Giá Porkbun. [Nguồn thứ cấp] Nguồn: https://domainoffer.net/tld/com/porkbun
- **Giá ".com" sắp tăng**: Verisign tăng giá bán buôn ".com" từ 10,26 USD lên **10,97 USD/năm từ 01/11/2026** (công bố 23/4/2026). Do đó giá ở Cloudflare/Porkbun sẽ tăng tương ứng khoảng 0,7 USD. [Nguồn thứ cấp, Domain Name Wire]
  Nguồn: https://domainnamewire.com/2026/04/23/breaking-verisign-raising-wholesale-com-prices/
- Google Domains đã bán cho Squarespace (công bố 15/6/2023); Squarespace cam kết giữ giá gia hạn của Google Domains trong 12 tháng sau giao dịch. Cam kết này đã hết hạn. [Nguồn thứ cấp]
  Nguồn: https://www.techradar.com/news/google-domains-shuts-down-assets-sold-to-squarespace
- Namecheap: chân trang có biểu tượng Visa, Mastercard, PayPal, Bitcoin. [Nguồn thứ cấp] Nguồn: https://www.namecheap.com

**Người Việt có trả tiền được không?** [Kinh nghiệm thực hành, chưa có nguồn chính thức]
- Thẻ Visa/Mastercard (tín dụng hoặc ghi nợ quốc tế) do ngân hàng Việt Nam phát hành **thường thanh toán được**, với điều kiện đã bật "thanh toán trực tuyến/quốc tế" trong ứng dụng ngân hàng. Thẻ ghi nợ nội địa Napas **không dùng được**.
- Ngân hàng thu phí chuyển đổi ngoại tệ (thường khoảng 1% đến 3%, tùy ngân hàng). Theo Luật Quản lý thuế, giao dịch với nhà cung cấp nước ngoài có thể đã bao gồm thuế do nhà cung cấp kê khai; điểm này tôi chưa kiểm.
- Một số giao dịch bị ngân hàng chặn vì nghi gian lận; người dùng phải tự gọi tổng đài ngân hàng.
- Cloudflare chỉ dùng phương thức thanh toán chính cho giao dịch tên miền ("Cloudflare Registrar only uses the primary payment method"). [Đã kiểm] Nguồn: https://developers.cloudflare.com/registrar/faq/

### 1.7. Nên chọn ".vn" hay ".com"

- **".vn"**: tín hiệu "Việt Nam", được nhà nước khuyến khích, nhưng phí cao (khoảng 650.000 đ đến 830.000 đ/năm khi gia hạn), phải khai số định danh cá nhân, thủ tục theo pháp luật Việt Nam, chỉ mua qua nhà đăng ký trong nước.
- **".com"**: rẻ (khoảng 270.000 đ/năm qua Cloudflare/Porkbun theo tỷ giá khoảng 26.000 đ/USD [Chưa chắc về tỷ giá]), quản lý dễ, nhưng phải có thẻ quốc tế.
- **".com.vn"**: rẻ hơn ".vn" một chút; phù hợp doanh nghiệp.
- Lưu ý: tên miền là **tài sản cần bảo vệ thương hiệu**. Nếu thương hiệu quan trọng, cân nhắc giữ cả ".vn" và ".com", trỏ một cái về cái còn lại.

### 1.8. Bẫy thường gặp khi mua tên miền

1. **Giá năm đầu thấp, gia hạn cao** (xem bảng 1.5). Hỏi giá gia hạn, tính tổng chi phí 3 đến 5 năm.
2. **Tự động gia hạn [auto-renew]**: bật lên và đảm bảo thẻ còn hạn. Tên miền hết hạn có thể bị người khác mua và đòi tiền chuộc. [Kinh nghiệm thực hành]
3. **Ẩn thông tin WHOIS [WHOIS privacy]**: miễn phí ở Cloudflare và Porkbun. Với ".vn", thông tin chủ thể vẫn khai với nhà đăng ký theo luật; mức hiển thị công khai phụ thuộc chính sách VNNIC. [Chưa chắc]
4. **Khóa chuyển tên miền [domain lock / transfer lock]**: bật để chống chuyển trái phép. Theo quy định của ICANN cho tên miền quốc tế, sau khi đăng ký mới hoặc chuyển nhà đăng ký, tên miền thường bị khóa chuyển **60 ngày**. Cloudflare cũng ghi khóa 60 ngày sau khi đổi thông tin chủ thể. [Đã kiểm với Cloudflare; nguồn thứ cấp cho quy định chung]
   Nguồn: https://developers.cloudflare.com/registrar/faq/ ; https://nicenic.com/hy/support/What-Is-the-60-Day-Domain-Transfer-Lock-4853
5. **Mã chuyển tên miền [auth code / EPP code]**: chỉ chủ tên miền lấy được. Freelancer hoặc đại lý giữ tài khoản thì chủ thật không chuyển đi được.
6. **Đứng tên sai người**: tên miền phải đứng tên **chủ thật** (người hoặc tổ chức sở hữu thương hiệu), không đứng tên người làm web hộ. Với ".vn", Nghị định 147/2024 yêu cầu thông tin chính xác; thông tin sai là căn cứ thu hồi. [Nguồn thứ cấp]
7. **Gói kèm không cần thiết**: hosting, email, SSL trả phí. Với website tĩnh trên Vercel/Netlify/Cloudflare, SSL miễn phí và tự cấp; **không cần mua SSL**. [Đã kiểm qua tài liệu Vercel, mục 2]
8. **Dùng email cá nhân dễ mất** để đăng ký tên miền: nếu mất email thì mất quyền khôi phục.

---

## Phần 2. Trỏ tên miền về nơi lưu trữ [hosting]

### 2.1. Khái niệm tối thiểu cần hiểu

- **Tên miền gốc [apex / root domain]**: `tenban.vn` (không có www). Bản ghi ký hiệu `@`.
- **Tên miền phụ [subdomain]**: `www.tenban.vn`, `blog.tenban.vn`.
- **Bản ghi A [A record]**: trỏ tên tới một địa chỉ IP.
- **Bản ghi CNAME**: trỏ tên tới một tên khác. Theo chuẩn DNS, **không đặt CNAME ở tên miền gốc** được; nhiều nhà cung cấp có giải pháp "làm phẳng CNAME" [CNAME flattening] hoặc bản ghi ALIAS/ANAME.
- **Máy chủ tên miền [nameserver]**: nơi giữ toàn bộ bản ghi DNS. Đổi nameserver = giao toàn bộ quyền quản lý DNS cho nơi khác.
- **TTL [time to live]**: thời gian các máy chủ khác được phép nhớ bản ghi cũ. Đặt thấp (300 giây) trước khi đổi để thay đổi lan nhanh.
- **Thời gian lan truyền [propagation]**: thường vài phút đến vài giờ, tối đa khoảng 24 đến 48 giờ.

### 2.2. Giá trị bản ghi cho từng nền tảng (kiểm ngày 07/10/2026)

**Vercel** [Đã kiểm]
- Tên miền gốc: bản ghi A `76.76.21.21` là giá trị chung; **dự án mới có thể nhận IP khác** từ một dải IP anycast, ví dụ `216.198.79.1`. Nguyên văn: "Newer projects draw a value from a pool of anycast IPs matched to the plan and project, so your card may show a different address such as `216.198.79.1`." và "The card is the source of truth, so use whatever it displays."
- Tên miền phụ (www): CNAME. Tài liệu hiện ghi giá trị chung `cname.vercel-dns-0.com` (không còn là `cname.vercel-dns.com` như các hướng dẫn cũ) và nhấn mạnh: "Your project may have specific values."
- Chứng chỉ SSL tự cấp sau khi xác minh DNS, thường trong vài phút. Nếu có bản ghi CAA không cho phép Let's Encrypt thì việc cấp chứng chỉ bị chặn.
- **Kết luận**: không chép giá trị từ bài hướng dẫn trên mạng; mở **Settings → Domains** của dự án trên Vercel và chép đúng giá trị hiện ra.
  Nguồn: https://vercel.com/docs/domains/set-up-custom-domain (cập nhật 11/8/2026) ; https://vercel.com/kb/guide/a-record-and-caa-with-vercel

**Netlify** [Đã kiểm]
- www: CNAME tới `tensite.netlify.app`.
- Tên miền gốc: ưu tiên ALIAS/ANAME/CNAME làm phẳng tới `apex-loadbalancer.netlify.com`; nếu nhà cung cấp DNS không hỗ trợ thì dùng bản ghi A `75.2.60.5`.
- Netlify khuyên dùng tên miền phụ (www) làm tên chính khi quản lý DNS bên ngoài. Lan truyền có thể tới 24 giờ.
  Nguồn: https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/

**GitHub Pages** [Đã kiểm]
- Tên miền gốc: bốn bản ghi A `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`; tùy chọn AAAA `2606:50c0:8000::153` đến `2606:50c0:8003::153`.
- www: CNAME tới `tentaikhoan.github.io`.
- Nên **xác minh tên miền** trong cài đặt tài khoản trước khi gắn vào repo để chống chiếm quyền [domain takeover]; **không dùng bản ghi đại diện** `*.tenban.vn`. Bật "Enforce HTTPS" sau khi DNS lan xong.
  Nguồn: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

**Cloudflare Pages và Cloudflare Workers** [Đã kiểm]
- Pages: tên miền phụ dùng CNAME tới `tenduan.pages.dev`; **tên miền gốc bắt buộc chuyển nameserver sang Cloudflare**.
- Workers (hướng Cloudflare đang đẩy mạnh cho trang tĩnh lẫn động): "Unlike Pages, Workers does not support any domain whose nameservers are not managed by Cloudflare."
  Nguồn: https://developers.cloudflare.com/pages/configuration/custom-domains/ ; https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/

**Firebase Hosting** [Đã kiểm]
- Bảng điều khiển Firebase cấp bản ghi A riêng; thêm bản ghi TXT xác minh dạng `hosting-site=<site_id>` và **phải giữ bản ghi TXT này vĩnh viễn** để Firebase gia hạn chứng chỉ.
- Cấp SSL: "may take up to 24 hours", thường vài giờ.
  Nguồn: https://firebase.google.com/docs/hosting/custom-domain

### 2.3. Kiểm tra DNS đã đúng chưa

- **dnschecker.org**: xem bản ghi từ nhiều nơi trên thế giới. https://dnschecker.org
- **Google Admin Toolbox Dig**: https://toolbox.googleapps.com/apps/dig/
- Dòng lệnh (cho người dùng máy Mac/Linux): `dig tenban.vn A +short`, `dig www.tenban.vn CNAME +short`, `dig tenban.vn NS +short`.
- Tín hiệu thành công: trang quản lý tên miền của Vercel/Netlify chuyển sang "Valid Configuration", có ổ khóa HTTPS khi mở trang.
[Kinh nghiệm thực hành; các công cụ đều đang hoạt động ngày 07/10/2026]

### 2.4. Chuyển nameserver sang Cloudflare: lợi và hại cho người dùng Việt Nam

[Kinh nghiệm thực hành, trừ chỗ có ghi nguồn]

Lợi:
- Gói miễn phí có DNS nhanh, giao diện quản lý DNS tốt hơn đa số bảng điều khiển của nhà đăng ký trong nước.
- Hỗ trợ làm phẳng CNAME ở tên miền gốc, nên trỏ apex về Vercel/Netlify dễ.
- Bắt buộc nếu dùng Cloudflare Pages với tên miền gốc, Cloudflare Workers, hoặc Cloudflare Email Routing (xem mục 3).
- Có thể bật DNSSEC một chạm, miễn phí. Nguồn: https://developers.cloudflare.com/registrar/

Hại:
- Thêm một tài khoản phải bảo vệ; mất tài khoản Cloudflare = mất quyền điều khiển DNS.
- Chế độ "proxy" (đám mây màu cam) có thể xung đột với Vercel/Netlify (lỗi chuyển hướng vòng lặp, lỗi cấp SSL). Với Vercel/Netlify, thường nên để bản ghi ở chế độ "DNS only" (đám mây xám).
- Phải nhập lại thủ công **tất cả** bản ghi đang có (đặc biệt MX của email) trước khi đổi nameserver; quên là mất email.
- Tên miền ".vn" vẫn đổi được nameserver sang Cloudflare trong thực tế; [Chưa chắc] tôi không tìm thấy văn bản cấm, cũng không tìm thấy văn bản xác nhận rõ ràng.

### 2.5. Lỗi thường gặp ở bảng điều khiển DNS của nhà đăng ký Việt Nam

[Kinh nghiệm thực hành]

1. **Ô "Host/Tên"**: có nơi nhập `@`, có nơi để trống, có nơi tự nối thêm tên miền. Nhập `www.tenban.vn` vào ô host ở các bảng tự nối sẽ thành `www.tenban.vn.tenban.vn`. Chỉ nhập `www`.
2. **Bản ghi mặc định còn sót**: nhà đăng ký thường tạo sẵn A record trỏ về trang "đỗ" [parking page] hoặc hosting của họ. Phải **xóa** bản ghi A cũ ở `@` và `www` trước khi thêm bản ghi mới, nếu không trang sẽ lúc hiện lúc không.
3. **Đặt CNAME ở tên miền gốc**: đa số bảng điều khiển trong nước không hỗ trợ; dùng bản ghi A thay thế.
4. **Dùng "chuyển hướng URL" [URL forwarding]** thay vì A/CNAME: làm SSL không cấp được.
5. **Không thấy nút sửa bản ghi** vì tên miền đang dùng nameserver của dịch vụ khác; phải chuyển về "DNS của nhà đăng ký" hoặc sửa ở nơi giữ nameserver.
6. **Dấu chấm cuối**: một số bảng yêu cầu `cname.vercel-dns-0.com.` (có dấu chấm cuối), một số không chấp nhận.
7. **Bản ghi CAA** cũ chỉ cho phép một nhà phát hành chứng chỉ khác làm Let's Encrypt bị chặn (Vercel, Netlify, GitHub đều dùng Let's Encrypt).
8. **Tên miền chưa kích hoạt** vì bản khai chưa duyệt (với ".vn"): DNS không hoạt động dù đã nhập đúng.

---

## Phần 3. Email theo tên miền riêng

### 3.1. Các lựa chọn và chi phí (kiểm ngày 07/10/2026)

| Giải pháp | Chi phí | Gửi và nhận | Ghi chú |
|---|---|---|---|
| Google Workspace Business Starter | 220.000 đ/người/tháng giá niêm yết qua đại lý Tenten; khuyến mãi 90.000 đ/người/tháng (20 người đầu, cam kết 1 năm), chưa gồm 10% VAT | Có | 30 GB/người, tối đa 300 người |
| Microsoft 365 Business Basic | 3,50 USD/người/tháng (cam kết năm), theo trang Microsoft Việt Nam | Có | Bản web của Word, Excel, PowerPoint |
| Zoho Mail Forever Free | Miễn phí, tối đa 5 người, 5 GB/người, 1 tên miền | Có (qua web và ứng dụng di động) | **Không có IMAP/POP/ActiveSync**; "Available only in select data centers" |
| Cloudflare Email Routing | Miễn phí | **Chỉ nhận và chuyển tiếp** | Cần tên miền dùng DNS Cloudflare |

Nguồn:
- Google Workspace qua Tenten [Nguồn thứ cấp]: https://tenten.vn/en/email-server/gsuite ; trang giá chính thức không hiện số khi tôi truy cập: https://workspace.google.com/intl/vi/pricing.html
- Microsoft [Đã kiểm, nhưng con số thấp hơn mức tôi kỳ vọng; nên kiểm lại khi mua]: https://www.microsoft.com/vi-vn/microsoft-365/business/microsoft-365-plan-chooser
- Zoho [Đã kiểm]: https://www.zoho.com/mail/zohomail-pricing.html
- Cloudflare [Đã kiểm phần miễn phí và chức năng; yêu cầu nameserver là kinh nghiệm thực hành, vì thiết lập "partial/CNAME" của Cloudflare chỉ dành cho gói trả phí cao]: https://developers.cloudflare.com/email-routing/ ; https://developers.cloudflare.com/dns/zone-setups/partial-setup

### 3.2. Cảnh báo quan trọng năm 2026: Gmail bỏ "Send mail as" cho địa chỉ bên thứ ba từ tháng 01/2027

- Trang trợ giúp Gmail: "Starting January 2027, Gmail will no longer support the 'Send as' feature for third-party email addresses, such as @yahoo.com or @outlook.com." Không ảnh hưởng Google Workspace và địa chỉ Gmail của chính bạn. [Đã kiểm]
  Nguồn: https://support.google.com/mail/answer/22370?hl=en
- Theo Android Authority (công bố 05/8/2026) và ImprovMX, phạm vi **bao gồm cả địa chỉ tên miền riêng** gửi qua SMTP bên ngoài; Gmailify và việc lấy thư POP trên web cũng bị bỏ. [Nguồn thứ cấp]
  Nguồn: https://androidauthority.com/gmail-killing-third-party-send-as-feature-3694659 ; https://improvmx.com/guides/gmail-send-as-alternatives

**Hệ quả**: mô hình "Cloudflare Email Routing chuyển thư về Gmail + Gmail 'Send as' để gửi đi" mà nhiều hướng dẫn miễn phí đề xuất **sẽ không còn dùng được từ tháng 01/2027**. Không nên xây quy trình mới dựa trên mô hình này. Lựa chọn thay thế: Zoho Mail miễn phí (gửi và nhận ngay trong Zoho), hoặc trả phí Google Workspace/Microsoft 365.

### 3.3. Các bản ghi bắt buộc cho email

| Bản ghi | Vai trò | Ai tạo giá trị |
|---|---|---|
| MX | Chỉ nơi nhận thư | Nhà cung cấp email (Google, Zoho, Microsoft, Cloudflare) |
| SPF (TXT, bắt đầu `v=spf1`) | Liệt kê máy chủ được phép gửi thư thay tên miền | Nhà cung cấp email; **mỗi tên miền chỉ một bản ghi SPF**, gộp nếu dùng nhiều dịch vụ |
| DKIM (TXT) | Chữ ký số trên thư | Sinh trong bảng quản trị của nhà cung cấp email; người dùng phải tự chép vào DNS |
| DMARC (TXT tại `_dmarc`) | Chính sách khi thư không qua SPF/DKIM | Tự đặt; bắt đầu bằng `v=DMARC1; p=none; rua=mailto:...` |

**Quy định người gửi của Gmail** (hiệu lực từ 01/02/2024) [Đã kiểm]:
- Mọi người gửi tới Gmail: có SPF **hoặc** DKIM; DNS thuận và ngược hợp lệ; dùng TLS; tỉ lệ thư rác dưới 0,3%.
- Người gửi số lượng lớn (từ 5.000 thư/ngày tới Gmail): bắt buộc **cả** SPF và DKIM, có DMARC (tối thiểu `p=none`), tên miền ở dòng From phải khớp [alignment] với SPF hoặc DKIM, có hủy đăng ký một chạm cho thư tiếp thị.
  Nguồn: https://support.google.com/mail/answer/81126?hl=en
- Yahoo áp dụng yêu cầu tương tự từ 2024; Microsoft Outlook áp dụng cho người gửi trên 5.000 thư/ngày từ tháng 5/2025. [Nguồn thứ cấp] Nguồn: https://petri.com/microsoft-outlook-email-authentication-rules/

**Khuyến nghị cho website nhỏ**: dù không gửi số lượng lớn, vẫn cài đủ cả ba SPF, DKIM, DMARC ngay từ đầu. Nếu website gửi thư tự động (biểu mẫu liên hệ, xác nhận đăng ký) qua dịch vụ như Resend, Brevo, Mailchimp, phải thêm bản ghi của dịch vụ đó vào SPF/DKIM. [Kinh nghiệm thực hành]

---

## Phần 4. Yêu cầu pháp lý tại Việt Nam

### 4.1. Bảo vệ dữ liệu cá nhân

**Văn bản hiện hành**:
- **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15**, hiệu lực **01/01/2026** (khoản 1 Điều 38). [Đã kiểm]
  Nguồn: https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Law-91-2025-QH15-Personal-Data-Protection-665440.aspx
- **Nghị định 356/2025/NĐ-CP** ngày 31/12/2025 quy định chi tiết Luật, hiệu lực 01/01/2026, **thay thế Nghị định 13/2023/NĐ-CP**. [Nguồn thứ cấp, EY và PwC Việt Nam khớp nhau]
  Nguồn: https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan ; https://www.pwc.com/vn/vn/publications/legal-news-brief/20260128-new-rules-personal-data-protection.html

Như vậy, **Nghị định 13/2023 không còn hiệu lực từ 01/01/2026**. Tài liệu nào (kể cả một số trang của nhà cung cấp công cụ cookie) nói "Nghị định 13 và Luật cùng song song hiệu lực" là sai.

**Các điểm then chốt** [Đã kiểm trên văn bản Luật qua thuvienphapluat.vn, trừ chỗ ghi khác]:

- **Sự đồng ý (Điều 9)**: phải tự nguyện, dựa trên thông tin rõ ràng về loại dữ liệu, mục đích xử lý, bên kiểm soát dữ liệu; thể hiện rõ ràng, cụ thể, bằng văn bản hoặc dạng điện tử kiểm chứng được; **"Sự im lặng hoặc không phản hồi không được coi là sự đồng ý"** (điểm d khoản 4 Điều 9); đồng ý theo từng mục đích, không gộp điều kiện.
- **Xử lý không cần đồng ý (Điều 19)**: tình huống khẩn cấp bảo vệ tính mạng, sức khỏe; an ninh quốc gia; hoạt động cơ quan nhà nước; **thực hiện hợp đồng/thỏa thuận** với chủ thể dữ liệu; trường hợp khác theo luật. [Đã kiểm qua bản tiếng Anh; chưa đối chiếu từng chữ bản tiếng Việt]
- **Mức phạt (Điều 8)**: vi phạm chuyển dữ liệu xuyên biên giới tối đa 5% doanh thu năm trước của tổ chức; mua bán dữ liệu tối đa 10 lần khoản thu từ vi phạm; vi phạm khác tối đa 3 tỷ đồng với tổ chức; cá nhân bằng một nửa.
- **Miễn trừ cho doanh nghiệp nhỏ (Điều 38)**:
  - Khoản 2: **doanh nghiệp nhỏ, doanh nghiệp khởi nghiệp sáng tạo** được quyền lựa chọn thực hiện hay không Điều 21, Điều 22 và khoản 2 Điều 33 trong **05 năm** kể từ 01/01/2026.
  - Khoản 3: **hộ kinh doanh, doanh nghiệp siêu nhỏ** không phải thực hiện các quy định đó.
  - Điều 21: "Đánh giá tác động xử lý dữ liệu cá nhân"; Điều 22: "Cập nhật hồ sơ đánh giá tác động xử lý dữ liệu cá nhân và hồ sơ đánh giá tác động chuyển dữ liệu cá nhân xuyên biên giới"; Điều 33 về lực lượng bảo vệ dữ liệu cá nhân (khoản 2 liên quan bộ phận/nhân sự bảo vệ dữ liệu). [Đã kiểm tiêu đề Điều 21, 22 qua hethongphapluat.com; nội dung khoản 2 Điều 33 theo tóm tắt EY]
  - **Ngoại lệ của miễn trừ**: không áp dụng cho đơn vị cung cấp dịch vụ xử lý dữ liệu, xử lý dữ liệu nhạy cảm, hoặc xử lý dữ liệu số lượng lớn. Theo EY, Nghị định 356 đặt ngưỡng **100.000 chủ thể dữ liệu** tích lũy. [Nguồn thứ cấp cho con số 100.000]
  - **Quan trọng**: miễn trừ chỉ là miễn lập hồ sơ đánh giá tác động và bộ phận/nhân sự chuyên trách. **Không miễn** nghĩa vụ xin đồng ý, thông báo mục đích, bảo vệ dữ liệu, đáp ứng quyền của chủ thể.
- **Thời hạn đáp ứng yêu cầu của chủ thể dữ liệu** theo Nghị định 356 (tóm tắt EY): rút lại đồng ý/hạn chế/phản đối xử lý phản hồi trong 2 ngày làm việc, thực hiện trong 15 ngày; truy cập/chỉnh sửa phản hồi 10 ngày, thực hiện 15 ngày; xóa phản hồi 20 ngày, thực hiện 30 ngày. [Nguồn thứ cấp]
  Nguồn: https://www.ey.com/content/dam/ey-unified-site/ey-com/vi-vn/technical/tax/documents/ey-vietnam-legal-alert-march-2026-decree-no356-2025-nd-cp-providing-detailed-guidance-for-implementation-of-personal-data-protection-law-viet.pdf
- **Dữ liệu nhạy cảm** được mở rộng, theo EY gồm cả dữ liệu theo dõi hành vi trên dịch vụ viễn thông, mạng xã hội, truyền thông trực tuyến; tình trạng sức khỏe hiểu rộng; thông tin đăng nhập; ảnh giấy tờ tùy thân; thông tin tài khoản tài chính. [Nguồn thứ cấp; Chưa chắc về phạm vi chính xác của "theo dõi hành vi", điều này quan trọng với công cụ phân tích và quảng cáo]
- **Chuyển dữ liệu ra nước ngoài**: website lưu biểu mẫu trên dịch vụ nước ngoài (Google Sheets, Vercel, Supabase, Mailchimp) về bản chất là chuyển dữ liệu xuyên biên giới. EY cho rằng việc này cần hồ sơ đánh giá tác động chuyển dữ liệu xuyên biên giới nộp Cục An ninh mạng (A05). [Chưa chắc]: chưa rõ hộ kinh doanh/doanh nghiệp siêu nhỏ có được miễn cả hồ sơ chuyển dữ liệu xuyên biên giới không, vì Điều 38 miễn Điều 22 (cập nhật hồ sơ, gồm hồ sơ xuyên biên giới) nhưng tôi chưa thấy điều khoản lập hồ sơ xuyên biên giới gốc có nằm trong danh sách miễn hay không. Cá nhân tự làm website cá nhân (không phải doanh nghiệp) thì vị trí pháp lý càng chưa rõ. **Cần hỏi luật sư** nếu thu thập dữ liệu nhiều.
- **Phạm vi**: Luật áp dụng cho "cơ quan, tổ chức, cá nhân", tôi **không thấy** điều khoản loại trừ việc xử lý dữ liệu cho mục đích cá nhân/gia đình như GDPR. [Chưa chắc]

**Danh sách việc cần làm cho website nhỏ thu tên, email, số điện thoại** (bản dễ hiểu)

Dành cho: blog cá nhân, trang giới thiệu dịch vụ coaching/đào tạo, trang đăng ký sự kiện, quy mô dưới vài nghìn người.

1. **Thu ít nhất có thể**: chỉ hỏi những trường thật sự cần (thường là tên và email). Không hỏi ngày sinh, địa chỉ, số căn cước nếu không cần.
2. **Viết rõ mục đích ngay cạnh biểu mẫu**, ví dụ: "Chúng tôi dùng email của bạn để gửi xác nhận đăng ký và thông tin buổi học. Chúng tôi không bán hay chia sẻ dữ liệu cho bên khác."
3. **Ô đồng ý không đánh dấu sẵn**, mỗi mục đích một ô: một ô "Tôi đồng ý cho [tên đơn vị] xử lý dữ liệu theo Chính sách bảo mật", một ô riêng "Tôi muốn nhận bản tin" (không bắt buộc). Không được coi việc bấm "Gửi" mà không tích là đồng ý cho mọi mục đích.
4. **Lưu bằng chứng đồng ý**: thời điểm, nội dung câu đồng ý, phiên bản chính sách. Hầu hết công cụ biểu mẫu có thể lưu thêm cột thời gian và nội dung ô tích.
5. **Trang "Chính sách bảo mật" [privacy policy]** gồm: ai là bên kiểm soát dữ liệu (tên, địa chỉ liên hệ, email); loại dữ liệu thu; mục đích; căn cứ (đồng ý hoặc thực hiện hợp đồng); dữ liệu lưu ở đâu (nêu rõ dịch vụ nước ngoài nếu có); lưu bao lâu; ai được tiếp cận; quyền của người dùng (xem, sửa, xóa, rút lại đồng ý) và cách liên hệ; cập nhật lần cuối ngày nào.
6. **Cách rút lại đồng ý dễ như khi đồng ý**: liên kết hủy đăng ký trong mỗi email; một địa chỉ email tiếp nhận yêu cầu.
7. **Bảo mật cơ bản**: bật 2FA cho tài khoản chứa dữ liệu (Google Sheets, công cụ email); không chia sẻ bảng tính "ai có liên kết cũng xem được".
8. **Xóa dữ liệu khi hết mục đích** (ví dụ 12 tháng sau sự kiện).
9. **Khi có sự cố lộ dữ liệu**: thông báo theo quy định (Nghị định 356 có mốc 72 giờ cho một số loại vi phạm theo EY) [Nguồn thứ cấp]; ghi nhận sự cố.
10. **Không mua bán, trao đổi danh sách email**: mức phạt tới 10 lần khoản thu.
11. Nếu là doanh nghiệp vừa trở lên, hoặc xử lý dữ liệu sức khỏe/tâm lý (ví dụ phiếu sàng lọc tâm lý, hồ sơ trị liệu): **không được miễn**, cần hồ sơ đánh giá tác động và nên có tư vấn pháp lý.

Lưu ý riêng cho lĩnh vực tâm lý, coaching, giáo dục: câu hỏi về tình trạng cảm xúc, sức khỏe tâm thần trong biểu mẫu đăng ký **có thể là dữ liệu nhạy cảm** (sức khỏe hiểu rộng), khiến miễn trừ doanh nghiệp nhỏ không áp dụng. Nên tách câu hỏi sàng lọc ra khỏi biểu mẫu công khai. [Suy luận từ nguồn EY; Chưa chắc]

### 4.2. Thông báo website thương mại điện tử với Bộ Công Thương

**Bối cảnh văn bản** (có thay đổi lớn năm 2026):
- **Luật Thương mại điện tử số 122/2025/QH15**, thông qua 10/12/2025, **hiệu lực 01/7/2026**. [Đã kiểm qua thuvienphapluat.vn]
  Nguồn: https://thuvienphapluat.vn/phap-luat-nha-dat/toan-van-luat-thuong-mai-dien-tu-2025-luat-so-1222025qh15-moi-nhat-ra-sao-13968.html
- **Nghị định 248/2026/NĐ-CP** ngày 30/6/2026 quy định chi tiết một số điều của Luật Thương mại điện tử, hiệu lực 01/7/2026. [Nguồn thứ cấp, Bộ Công Thương và LuatVietnam đều nhắc tên]
  Nguồn: https://moit.gov.vn/tin-tuc/bo-cong-thuong-pho-bien-luat-thuong-mai-dien-tu-va-nghi-dinh-so-248-2026-nd-cp.html ; https://luatvietnam.vn/bai-viet-lien-quan/luat-122-2025-qh15-423356.html
- Nghị định 52/2013/NĐ-CP (sửa bởi Nghị định 85/2021/NĐ-CP) là khung cũ. [Chưa chắc]: tôi chưa xác nhận Nghị định 248/2026 đã thay thế toàn bộ Nghị định 52/2013 hay chỉ một phần.

**Khi nào phải thông báo**:
- Luật mới khoản 1 Điều 14 (bản tiếng Anh trên thuvienphapluat.vn): đơn vị vận hành "nền tảng thương mại điện tử kinh doanh trực tiếp **có chức năng đặt hàng trực tuyến**" phải thông báo với cơ quan quản lý trước khi hoạt động. [Đã kiểm qua bản dịch tiếng Anh; nên đối chiếu nguyên văn tiếng Việt]
  Nguồn: https://thuvienphapluat.vn/van-ban/EN/Thuong-mai/Law-122-2025-QH15-Electronic-Commerce/703876/tieng-anh.aspx
- Cổng thông báo: **online.gov.vn** (Cổng thông tin quản lý hoạt động thương mại điện tử của Bộ Công Thương), quy trình: tạo tài khoản thương nhân, chờ duyệt khoảng 3 ngày làm việc, khai báo website, chờ xác nhận khoảng 3 ngày làm việc, nhận mã biểu tượng "Đã thông báo Bộ Công Thương" gắn lên trang. [Nguồn thứ cấp]
  Nguồn: https://doanhnghiephoinhap.vn/nhung-dieu-can-biet-ve-viec-thiet-lap-website-thuong-mai-dien-tu-ban-hang-128790.html
- Theo khung cũ, đối tượng thông báo gồm thương nhân, tổ chức, và **cá nhân đã có mã số thuế cá nhân**. [Nguồn thứ cấp] Nguồn: https://luatvietan.vn/thong-bao-website-thuong-mai-dien-tu.html
- **Chuyển tiếp** (khoản 1 Điều 41): website đã được xác nhận thông báo/đăng ký trước 01/7/2026 được tiếp tục hoạt động đến hết **30/6/2027**; sau đó phải làm lại theo quy định mới. [Đã kiểm]

**Áp dụng vào trường hợp điển hình**:

| Loại website | Phải thông báo? |
|---|---|
| Blog cá nhân, trang giới thiệu bản thân | Không |
| Trang giới thiệu dịch vụ, chỉ có nút "liên hệ" hoặc dẫn sang Zalo/Messenger | Nhiều khả năng không, vì không có chức năng đặt hàng trực tuyến [Chưa chắc] |
| Trang bán khóa học/dịch vụ có giỏ hàng, chọn gói, thanh toán trực tuyến | **Có** |
| Trang đăng ký sự kiện miễn phí | Nhiều khả năng không [Chưa chắc] |
| Trang đăng ký sự kiện thu phí, có thanh toán trên trang | Nhiều khả năng **có** [Chưa chắc] |

- Mức phạt khi không thông báo: một trường hợp cá nhân bị phạt 15 triệu đồng được báo chí nêu. [Nguồn thứ cấp] Nguồn bài trên doanhnghiephoinhap.vn ở trên. Mức phạt chính xác theo nghị định xử phạt hiện hành tôi chưa kiểm.
- Việc thông báo **người dùng phải tự làm**: AI không thể đăng nhập cổng nhà nước thay, không thể ký, không thể khai mã số thuế.

### 4.3. Giấy phép trang thông tin điện tử tổng hợp: khi nào không cần

Theo Nghị định 147/2024/NĐ-CP:
- **Khoản 2 Điều 24**: các loại **không phải cấp phép** gồm trang thông tin điện tử cung cấp dịch vụ chuyên ngành, **trang thông tin điện tử cá nhân**, **trang thông tin điện tử nội bộ**, cổng thông tin điện tử của cơ quan nhà nước, diễn đàn nội bộ. [Nguồn thứ cấp, thuvienphapluat.vn]
  Nguồn: https://thuvienphapluat.vn/hoi-dap-phap-luat/tu-25122024-trang-thong-tin-dien-tu-nao-khong-phai-cap-phep-138039788.html
- **Khoản 3 Điều 24**: các trang nội bộ, chuyên ngành **nếu có cung cấp thông tin tổng hợp** thì phải có giấy phép trang thông tin điện tử tổng hợp. [Nguồn thứ cấp]
- Khoản 20 Điều 3 định nghĩa trang thông tin điện tử tổng hợp là trang "của cơ quan, tổ chức, doanh nghiệp cung cấp thông tin tổng hợp". Phân loại các trang nằm ở Điều 20. [Nguồn thứ cấp]
  Nguồn: https://thuvienphapluat.vn/hoi-dap-phap-luat/website-co-phai-la-trang-thong-tin-dien-tu-phan-loai-trang-thong-tin-dien-tu-tu-ngay-25122024-138038200.html

**Nguyên tắc dễ nhớ** [Diễn giải; Chưa chắc ở ranh giới]:
- Website **viết nội dung của chính mình** (bài viết, giới thiệu dịch vụ, sản phẩm của mình): không cần giấy phép.
- Website **đăng lại, tổng hợp tin tức từ báo chí, nguồn khác** theo kiểu trang tin: cần giấy phép (và cá nhân không thuộc đối tượng được cấp loại này theo định nghĩa "của cơ quan, tổ chức, doanh nghiệp").
- Trang có nhiều người dùng đăng bài, bình luận công khai (diễn đàn, mạng xã hội) chịu quy định khác về mạng xã hội.

**Thông tin cần hiển thị trên website**: Nghị định 174/2026/NĐ-CP (ngày 15/5/2026, hiệu lực 01/7/2026, xử phạt vi phạm hành chính) phạt 10 đến 20 triệu đồng nếu cung cấp không đầy đủ hoặc không chính xác thông tin: "tên của cơ quan, tổ chức, doanh nghiệp, cá nhân quản lý trang thông tin điện tử, tên cơ quan chủ quản (nếu có), địa chỉ liên lạc, thư điện tử, số điện thoại liên hệ, tên người chịu trách nhiệm quản lý nội dung". [Nguồn thứ cấp, báo Luật sư Việt Nam; Chưa chắc nghĩa vụ này áp dụng cho mọi loại trang hay chỉ trang phải cấp phép]
Nguồn: https://lsvn.vn/tang-muc-xu-phat-tien-doi-voi-cac-vi-pham-ve-trang-thong-tin-dien-tu-a177134.html

**Khuyến nghị an toàn**: chân trang mọi website nên có tên chủ website, email, số điện thoại hoặc địa chỉ liên hệ, người chịu trách nhiệm nội dung. Chi phí gần như bằng không, giảm rủi ro.

### 4.4. Cookie

- Pháp luật Việt Nam **không có quy định riêng mang tên "cookie"**. Cookie và công cụ theo dõi (Google Analytics, Meta Pixel) thu thập dữ liệu gắn với một người (định danh thiết bị, hành vi duyệt web) nên thuộc phạm vi Luật Bảo vệ dữ liệu cá nhân 2025. [Suy luận từ nguồn thứ cấp]
- Một nhà cung cấp công cụ đồng ý cookie cho rằng Việt Nam theo mô hình **đồng ý trước [opt-in]**, không có cơ chế "thông báo rồi cho từ chối". [Nguồn thứ cấp, có lợi ích thương mại; trang này còn viết sai rằng Nghị định 13 vẫn song song hiệu lực]
  Nguồn: https://flexyconsent.com/blog/vietnam-pdpd-cookie-consent-guide/
- Nguyên tắc "im lặng không phải là đồng ý" (Điều 9 Luật) khiến banner kiểu "Tiếp tục duyệt là bạn đồng ý" khó được coi là hợp lệ. [Suy luận]

**Khuyến nghị thực hành**:
1. Đơn giản nhất: **không dùng cookie theo dõi**. Website tĩnh trên Vercel/Netlify không tự đặt cookie theo dõi.
2. Nếu cần thống kê lượt xem, dùng công cụ không dùng cookie, không định danh người dùng (ví dụ Vercel Web Analytics, Plausible, Cloudflare Web Analytics). [Kinh nghiệm thực hành; nên đọc chính sách từng công cụ]
3. Nếu dùng Google Analytics/Meta Pixel: cần banner có nút "Đồng ý" và "Từ chối" ngang hàng, chỉ tải mã theo dõi sau khi người dùng đồng ý, và ghi trong Chính sách bảo mật.
4. Phông chữ từ Google Fonts tải từ máy chủ Google sẽ gửi địa chỉ IP người xem cho Google; tự lưu phông chữ trên host của mình là lựa chọn an toàn hơn về dữ liệu. Google Fonts FAQ có mục riêng về quyền riêng tư và tự lưu trữ. Nguồn: https://fonts.google.com/faq [Đã kiểm sự tồn tại của mục, chưa đọc chi tiết]

### 4.5. Bản quyền hình ảnh, phông chữ, nội dung

- **Phông chữ Google Fonts**: dùng giấy phép SIL Open Font License, dùng thương mại miễn phí. [Đã kiểm] Nguồn: https://fonts.google.com/faq
  Phông chữ thương mại (mua kèm phần mềm thiết kế, tải từ trang chia sẻ) thường **không** cho phép nhúng web [web embedding] nếu không mua giấy phép web riêng. [Kinh nghiệm thực hành]
- **Ảnh Unsplash**: "irrevocable, nonexclusive, worldwide copyright license ... for free, including for commercial purposes, without permission from or attributing the photographer"; cấm gom ảnh để tạo dịch vụ cạnh tranh. Ghi công tác giả không bắt buộc nhưng được khuyến khích. [Đã kiểm] Nguồn: https://unsplash.com/license
  Lưu ý: giấy phép Unsplash không bao gồm quyền hình ảnh của người xuất hiện trong ảnh hay nhãn hiệu trong ảnh khi dùng để quảng cáo; với ảnh có người rõ mặt dùng cho quảng cáo, cân nhắc kỹ. [Kinh nghiệm thực hành]
- **Ảnh lấy từ Google Hình ảnh, Facebook, báo chí**: mặc định có bản quyền; dùng không xin phép là vi phạm Luật Sở hữu trí tuệ. [Nguyên tắc chung; tôi không trích số điều cụ thể vì chưa kiểm]
- **Ảnh học viên, khách hàng, người tham gia sự kiện**: ngoài bản quyền còn là **dữ liệu cá nhân** và quyền đối với hình ảnh cá nhân (Bộ luật Dân sự); cần sự đồng ý bằng văn bản/điện tử. [Chưa kiểm số điều]
- **Ảnh và văn bản do AI tạo**: điều khoản sử dụng của từng công cụ quy định quyền sử dụng thương mại; tình trạng bảo hộ bản quyền cho sản phẩm do AI tạo tại Việt Nam chưa rõ ràng. [Chưa chắc]
- **Công cụ, khung, bảng kiểm của người khác** đưa lên website: ghi rõ tác giả và nguồn.

---

## Phần 5. Tài khoản cần tạo và bảo mật cơ bản

### 5.1. Danh sách tài khoản điển hình

| Tài khoản | Dùng để | Ai phải đứng tên |
|---|---|---|
| Email chủ (Gmail hoặc email tên miền) | Đăng ký mọi tài khoản khác, nhận mã khôi phục | Chủ website |
| Nhà đăng ký tên miền | Mua, gia hạn, quản lý DNS | Chủ website (bắt buộc theo luật với ".vn") |
| GitHub | Lưu mã nguồn | Chủ website (freelancer được mời làm cộng tác viên) |
| Vercel/Netlify/Cloudflare | Lưu trữ và xuất bản website | Chủ website |
| Google Workspace/Zoho (nếu có) | Email tên miền | Chủ website |
| Công cụ biểu mẫu, gửi email, phân tích | Thu dữ liệu, gửi thư | Chủ website (vì chủ website là bên kiểm soát dữ liệu theo luật) |

### 5.2. GitHub và xác thực hai lớp

- GitHub **bắt buộc 2FA** với tài khoản "có hành động cho thấy là người đóng góp" [contributor]: phát hành ứng dụng/action, tạo bản phát hành [release], đóng góp vào kho quan trọng, giữ vai trò quản trị hoặc chủ tổ chức. Không phải mọi tài khoản đều bị bắt buộc ngay. Thời gian đăng ký 45 ngày, cộng 7 ngày ân hạn; quá hạn thì "you will not be able to access GitHub.com until you enable 2FA". [Đã kiểm]
- Phương thức khuyến nghị: ứng dụng tạo mã một lần theo thời gian [TOTP] (Google Authenticator, Microsoft Authenticator, 2FAS, Authy...) làm chính; passkey, khóa bảo mật, GitHub Mobile làm dự phòng; SMS không khuyến khích.
  Nguồn: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication
- **Khuyến nghị**: bật 2FA cho GitHub ngay khi tạo tài khoản, không chờ bị bắt buộc.

### 5.3. Bảo mật cơ bản cho người không chuyên

[Kinh nghiệm thực hành]

1. **Một email chủ duy nhất** cho mọi tài khoản liên quan website; bật 2FA cho email này đầu tiên vì nó là "chìa khóa của mọi chìa khóa".
2. **Trình quản lý mật khẩu** [password manager] (Bitwarden có gói miễn phí; 1Password, trình quản lý mật khẩu của Google/Apple): mỗi dịch vụ một mật khẩu khác nhau, dài, ngẫu nhiên.
3. **Mã khôi phục [recovery codes]**: mỗi khi bật 2FA, dịch vụ cấp 8 đến 16 mã dùng một lần. Lưu vào trình quản lý mật khẩu **và** một bản in cất nơi an toàn. Mất điện thoại mà không có mã khôi phục thì có thể mất tài khoản vĩnh viễn (đặc biệt GitHub).
4. **Không gửi mật khẩu qua Zalo/Messenger/email**. Khi cần người khác làm hộ, dùng chức năng mời thành viên [invite/collaborator] của từng dịch vụ.
5. **Không đưa khóa bí mật [API key, token] vào mã nguồn** công khai trên GitHub; dùng biến môi trường [environment variables] trên Vercel/Netlify.
6. **Bảng ghi tài khoản**: một tài liệu riêng (trong trình quản lý mật khẩu) liệt kê: dịch vụ, email đăng nhập, ngày gia hạn, phương thức 2FA, nơi cất mã khôi phục.
7. **Lịch gia hạn**: ghi ngày hết hạn tên miền và email vào lịch, nhắc trước 30 ngày.

### 5.4. Ai sở hữu tài khoản khi thuê freelancer làm web

[Kinh nghiệm thực hành; một số điểm có căn cứ pháp lý đã nêu ở trên]

- **Tên miền đứng tên khách hàng**, tài khoản nhà đăng ký do khách hàng tạo bằng email của khách hàng, thanh toán bằng thẻ của khách hàng (hoặc khách hàng hoàn tiền nhưng chuyển quyền ngay). Với ".vn", thông tin chủ thể phải chính xác theo Điều 9 Nghị định 147/2024.
- **Kho mã GitHub thuộc tài khoản hoặc tổ chức [organization] của khách hàng**; freelancer được mời làm cộng tác viên, xong việc thì gỡ quyền.
- **Tài khoản hosting (Vercel/Netlify) do khách hàng tạo**; freelancer được mời vào nhóm [team]. Lưu ý một số gói miễn phí giới hạn số thành viên hoặc không cho dùng thương mại (ví dụ gói Hobby của Vercel dành cho mục đích phi thương mại [Chưa kiểm lại điều khoản năm 2026]).
- **Hợp đồng ghi rõ**: quyền sở hữu mã nguồn, thiết kế, nội dung, hình ảnh chuyển cho khách hàng khi thanh toán xong; danh sách tài khoản và quyền bàn giao.
- **Dữ liệu người dùng** (danh sách đăng ký) thuộc khách hàng với tư cách bên kiểm soát dữ liệu; freelancer là bên xử lý, chỉ được dùng theo thỏa thuận.
- **Buổi bàn giao**: khách hàng tự đăng nhập từng tài khoản, đổi mật khẩu, bật 2FA của chính mình, xác nhận nhận được mã khôi phục.

---

## Phần 6. Danh sách việc người dùng phải tự tay làm (tóm lược theo thứ tự)

1. Tạo (hoặc chọn) **email chủ**, bật 2FA, cất mã khôi phục.
2. Cài **trình quản lý mật khẩu**.
3. Bật thanh toán quốc tế trên thẻ Visa/Mastercard (nếu mua ".com" hoặc dịch vụ nước ngoài).
4. **Mua tên miền**: chọn đuôi, kiểm giá gia hạn, khai thông tin thật (với ".vn": số định danh cá nhân, địa chỉ thường trú), bật tự động gia hạn, bật khóa chuyển.
5. Tạo tài khoản **GitHub** (bật 2FA) và **Vercel/Netlify/Cloudflare** (đăng nhập bằng GitHub hoặc email chủ).
6. Trong bảng điều khiển hosting: thêm tên miền, **chép đúng giá trị DNS hiện ra**.
7. Trong bảng điều khiển nhà đăng ký (hoặc Cloudflare): xóa bản ghi cũ, thêm bản ghi mới, chờ, kiểm tra bằng dnschecker.
8. Xác nhận HTTPS hoạt động.
9. (Nếu cần email tên miền) đăng ký Zoho/Google Workspace/Microsoft 365, thêm MX, SPF, DKIM, DMARC; gửi thử tới Gmail và xem thư có vào hộp thư chính không.
10. Đọc, sửa, tự quyết **Chính sách bảo mật** và câu chữ ô đồng ý (AI soạn nháp được, người dùng chịu trách nhiệm).
11. Tự xác định: website có **chức năng đặt hàng trực tuyến** không; nếu có thì tự làm thủ tục trên online.gov.vn.
12. Đưa thông tin chủ website và liên hệ vào chân trang.
13. Lập lịch gia hạn và bảng ghi tài khoản.

---

## Phụ lục A. Những điểm chưa chắc cần kiểm lại trước khi dùng cho tư vấn chính thức

1. Nguyên văn quy định đối tượng ".edu.vn" và giấy tờ chứng minh trong Thông tư 48/2025/TT-BKHCN.
2. Nguyên văn khoản 8 Điều 9 Nghị định 147/2024 về xác thực thông tin chủ thể tên miền (chữ ký số, định danh điện tử).
3. Phí duy trì ".edu.vn" theo Thông tư 10/2025/TT-BTC (50.000 đ hay 100.000 đ).
4. Viettel IDC có phải nhà đăng ký ".vn" chính thức hay đại lý.
5. Nghị định 248/2026/NĐ-CP: tiêu chí "chức năng đặt hàng trực tuyến", đối tượng cá nhân, có thay thế Nghị định 52/2013 hoàn toàn không; mức phạt hiện hành khi không thông báo.
6. Luật Bảo vệ dữ liệu cá nhân: điều khoản lập hồ sơ chuyển dữ liệu xuyên biên giới có thuộc diện miễn trừ của Điều 38 không; cá nhân (không đăng ký kinh doanh) vận hành website có thuộc diện "bên kiểm soát dữ liệu" với đầy đủ nghĩa vụ không.
7. Phạm vi "dữ liệu theo dõi hành vi" trong danh mục dữ liệu nhạy cảm của Nghị định 356/2025, ảnh hưởng tới Google Analytics/Meta Pixel.
8. Nghĩa vụ hiển thị thông tin chủ quản theo Nghị định 174/2026 áp dụng cho mọi trang hay chỉ trang tổng hợp.
9. Giá Microsoft 365 Business Basic tại Việt Nam (3,50 USD là mức trên trang Microsoft Việt Nam, thấp hơn mức thường gặp ở thị trường khác).
10. Phạm vi chính xác việc Gmail bỏ "Send as" từ 01/2027 đối với địa chỉ tên miền riêng (văn bản chính thức của Google chỉ nêu ví dụ Yahoo, Outlook; báo chí cho rằng gồm cả tên miền riêng).

## Phụ lục B. Danh sách nguồn chính (truy cập 07/10/2026)

Văn bản và cơ quan nhà nước, trang tra cứu luật:
- https://hethongphapluat.com/nghi-dinh-147-2024-nd-cp-quan-ly-cung-cap-su-dung-dich-vu-internet-va-thong-tin-tren-mang/dieu-9
- https://thuvienphapluat.vn/hoi-dap-phap-luat/thong-tin-nao-phai-cung-cap-khi-dang-ky-su-dung-ten-mien-tu-25122024-138038198.html
- https://pbgdpl.cantho.gov.vn/bo-truong-bo-khoa-hoc-va-cong-nghe-ban-hanh-thong-tu-so-482025tt-bkhcn-huong-dan-ve-quan-ly-va-su-dung-tai-nguyen-internet
- https://luatvietan.vn/quy-dinh-ve-phi-le-phi-su-dung-ten-mien-theo-thong-tu-10-2025-tt-btc.html
- https://vnnic.vn/en/domain-name-vn/registras/registras-system
- https://thuvienphapluat.vn/van-ban/Bo-may-hanh-chinh/Law-91-2025-QH15-Personal-Data-Protection-665440.aspx
- https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025.html/dieu-21 và /dieu-22
- https://thuvienphapluat.vn/van-ban/EN/Thuong-mai/Law-122-2025-QH15-Electronic-Commerce/703876/tieng-anh.aspx
- https://moit.gov.vn/tin-tuc/bo-cong-thuong-pho-bien-luat-thuong-mai-dien-tu-va-nghi-dinh-so-248-2026-nd-cp.html
- https://thuvienphapluat.vn/hoi-dap-phap-luat/tu-25122024-trang-thong-tin-dien-tu-nao-khong-phai-cap-phep-138039788.html
- https://lsvn.vn/tang-muc-xu-phat-tien-doi-voi-cac-vi-pham-ve-trang-thong-tin-dien-tu-a177134.html

Phân tích của công ty tư vấn:
- EY Việt Nam về Nghị định 356/2025 (trang và bản PDF tháng 3/2026)
- PwC Việt Nam, bản tin 28/01/2026
- VCCI: https://vcci.com.vn/tin-tuc/luat-bao-ve-du-lieu-ca-nhan-luu-y-ve-hanh-lang-phap-ly-moi-cho-doanh-nghiep

Tài liệu nhà cung cấp:
- Vercel: https://vercel.com/docs/domains/set-up-custom-domain ; https://vercel.com/kb/guide/a-record-and-caa-with-vercel
- Netlify: https://docs.netlify.com/manage/domains/configure-domains/configure-external-dns/
- GitHub Pages và GitHub 2FA: docs.github.com (hai trang đã dẫn)
- Cloudflare: Registrar, Pages, Workers, Email Routing (developers.cloudflare.com)
- Firebase: https://firebase.google.com/docs/hosting/custom-domain
- Gmail: https://support.google.com/mail/answer/81126 ; https://support.google.com/mail/answer/22370
- Zoho: https://www.zoho.com/mail/zohomail-pricing.html
- Unsplash: https://unsplash.com/license ; Google Fonts: https://fonts.google.com/faq

Giá và tin ngành:
- https://www.matbao.net/ten-mien/bang-gia-ten-mien.html ; https://nhanhoa.com/ten-mien/bang-gia-ten-mien.html
- https://tenten.vn/en/email-server/gsuite
- https://domainoffer.net/tld/com/cloudflare ; https://domainoffer.net/tld/com/porkbun
- https://domainnamewire.com/2026/04/23/breaking-verisign-raising-wholesale-com-prices/
- https://androidauthority.com/gmail-killing-third-party-send-as-feature-3694659 ; https://improvmx.com/guides/gmail-send-as-alternatives

# Nghiên cứu G: giao diện và trải nghiệm cho web-app, công cụ học tập và ứng dụng có trí năng nhân tạo

Tổng quan tài liệu ngày 24/11/2026, làm nền cho chuan/11-giao-dien-trai-nghiem.md. Ca tham chiếu: lần thay toàn bộ giao diện của một web-app phản tư nhiều bước có trí năng nhân tạo cùng ngày (mục 4). Mỗi nguồn ghi tác giả, năm, nơi công bố và đường dẫn; nguồn đã mở lại để kiểm trong ngày được đánh dấu ✓ ở mục 6.

## 1. Câu hỏi và phạm vi

Chuẩn thiết kế hiện có (chuan/03) viết cho trang đích, trang hồ sơ, trang báo giá: người xem đọc rồi làm một hành động. Web-app thì khác: người dùng làm việc nhiều bước, quay lại nhiều lần, nhập chữ dài, chờ máy chủ, và (ở bậc 4) đối thoại với một mô hình ngôn ngữ. Với sản phẩm giáo dục và phát triển con người, việc người dùng làm thường là suy nghĩ về chính mình: phản tư, tự đánh giá, ra quyết định. Câu hỏi của báo cáo:

1. Giao diện nhiều bước nên tổ chức thế nào để người dùng luôn biết mình ở đâu, đã làm gì, còn gì?
2. Bố cục nào hợp với điện thoại (nơi phần lớn người dùng đến) mà vẫn tận dụng màn hình rộng?
3. Khi có trí năng nhân tạo, giao diện phải làm gì để người dùng giữ được suy nghĩ của mình, không giao phó nó cho máy?
4. Thiết kế thế nào để công cụ nâng đỡ an lành và tự chủ của người dùng, không giữ chân hay thao túng họ?

Ngoài phạm vi: thiết kế thương hiệu, màu, chữ (chuan/03), kỹ thuật tiếp cận và hiệu năng (chuan/05), chữ trên giao diện (chuan/04).

## 2. Cách làm

Gom 4 lớp nguồn, xếp theo sức nặng chứng cứ: nghiên cứu thực nghiệm có đối chứng; tổng quan tài liệu và mô hình lý thuyết đã được trích dẫn rộng; hướng dẫn hành nghề của các tổ chức lớn (Nielsen Norman Group, Material Design, W3C); kinh nghiệm từ ca thật của xưởng. Chỗ nào chỉ có hướng dẫn hành nghề mà chưa có nghiên cứu, báo cáo nói rõ.

## 3. Bảy cụm tri thức

### 3.1. Nền khả dụng: phản hồi, trạng thái, thời gian chờ

- Mười nguyên tắc đánh giá khả dụng của Jakob Nielsen (1994) vẫn là bộ khung kiểm phổ biến nhất: cho thấy trạng thái hệ thống, nói ngôn ngữ người dùng, cho người dùng quyền kiểm soát và đường lui, nhất quán, phòng lỗi, nhận ra thay vì phải nhớ, linh hoạt, tối giản, giúp nhận biết và gỡ lỗi, có trợ giúp. Don Norman (2013) bổ sung khái niệm phản hồi, ràng buộc và mô hình khái niệm: người dùng phải hình dung được hệ thống vận hành ra sao mới dùng tự tin.
- Ba ngưỡng thời gian đáp ứng (Nielsen, 1993, dựa trên nghiên cứu của Miller, 1968): dưới 0,1 giây người dùng cảm thấy chính mình làm thay đổi trên màn hình; dưới 1 giây dòng suy nghĩ không bị ngắt; quá 10 giây người dùng bắt đầu nghĩ sang việc khác. Chỉ báo tiến độ có phần trăm giúp người dùng chịu được chờ lâu (Myers, 1985).
- Hệ quả cho web-app có trí năng nhân tạo: một lời gọi mô hình thường mất 5 đến 60 giây, vượt ngưỡng 10 giây. Giao diện phải nói đang làm gì và chừng bao lâu, và việc nhiều phút phải chạy nền để người dùng rời trang được (chuan/10 mục 8).

### 3.2. Tải nhận thức và trình bày từng phần

- Lý thuyết tải nhận thức (Sweller, 1988) và các nguyên lý học tập đa phương tiện của Richard Mayer (2021, bản 3) có bằng chứng thực nghiệm nhất quán: chia nội dung thành từng đoạn người học tự điều khiển nhịp [segmenting], làm nổi phần cốt lõi [signaling], bỏ chi tiết thừa [coherence].
- Trình bày từng phần [progressive disclosure] (Nielsen, 2006): chỉ hiện điều cần cho bước hiện tại, phần nâng cao để sau một lần bấm. Lợi cho người mới, không cản người quen.
- Hệ quả: luồng nhiều bước hiện từng ô một, mỗi bước nói mục đích; phần đã xong thu gọn mà vẫn mở lại được để đối chiếu.

### 3.3. Bố cục đáp ứng và điều hướng

- Material Design 3 chia cửa sổ theo bề rộng: hẹp dưới 600, vừa 600 đến 839, rộng 840 đến 1199, lớn 1200 đến 1599, rất lớn từ 1600 (đơn vị dp, gần bằng px CSS). Ba bố cục chuẩn [canonical layouts]: danh sách và chi tiết, khung chính và khung phụ [supporting pane], dòng tin [feed]. Với khung phụ, Android khuyên chia khoảng 70% cho nội dung chính, 30% cho nội dung phụ ở khổ rộng. Đây là hướng dẫn hành nghề, chưa phải nghiên cứu đối chứng, nhưng được kiểm qua hàng triệu ứng dụng.
- Điều hướng ẩn sau nút ba gạch làm giảm việc dùng điều hướng: thử nghiệm định lượng của Kara Pernice và Raluca Budiu (Nielsen Norman Group, 2016, 179 người) thấy trên máy tính người dùng chỉ dùng menu ẩn ở 27% trường hợp, so với 48 đến 50% khi điều hướng hiện sẵn; thời gian làm việc dài hơn, cảm nhận khó hơn. Trên điện thoại ẩn là bất đắc dĩ, nên phải bù bằng đường vào hiện sẵn ở trang chính.
- Vùng chạm: WCAG 2.2 tiêu chí 2.5.8 (mức AA) đặt sàn 24 x 24 px CSS; Apple khuyên 44 x 44 điểm, Material khuyên 48 x 48 dp. Xưởng giữ 44 px cho nút trong web-app.

### 3.4. Tương tác giữa người và trí năng nhân tạo

- Bộ 18 nguyên tắc tương tác người và trí năng nhân tạo của Saleema Amershi và cộng sự (Microsoft, CHI 2019) chia bốn nhóm: lúc bắt đầu (nói rõ hệ thống làm được gì, làm tốt đến đâu), trong lúc dùng (đúng lúc, đúng ngữ cảnh, tránh định kiến), khi hệ thống sai (dễ bỏ qua, dễ sửa, giải thích vì sao), theo thời gian (học từ người dùng một cách thận trọng, báo trước thay đổi).
- Ben Shneiderman (2020) đề xuất trí năng nhân tạo hướng về con người [human-centered artificial intelligence]: không chọn giữa tự động hóa và quyền con người, mà thiết kế để cả hai cùng cao: máy làm nhiều, người vẫn kiểm soát.
- Phụ thuộc quá mức [overreliance]: người dùng chấp nhận cả đầu ra sai của máy. Tổng quan khoảng 60 nghiên cứu của Samir Passi và Mihaela Vorvoreanu (Microsoft, 2022) cho thấy giải thích kèm theo không đủ để giảm phụ thuộc, có khi còn làm tăng.
- Thử nghiệm của Zana Buçinca, Maja Barbara Malaya và Krzysztof Gajos (CSCW 2021, 199 người): các can thiệp buộc người dùng tự nghĩ trước [cognitive forcing], như tự quyết trước rồi mới xem gợi ý của máy, giảm rõ phụ thuộc quá mức so với chỉ đưa giải thích; đổi lại, người dùng đánh giá các thiết kế này kém dễ chịu nhất. Đây là đánh đổi cần nói thẳng khi thiết kế.
- Khảo sát 319 người làm tri thức với 936 ví dụ thật của Hao-Ping Lee, Advait Sarkar và cộng sự (CHI 2025): càng tin vào trí năng nhân tạo, người dùng càng ít tư duy phản biện; càng tự tin vào năng lực của mình, càng tư duy phản biện nhiều. Đây là dữ liệu tự báo cáo, cho thấy liên hệ chứ chưa chứng minh nhân quả.
- Hệ quả cho sản phẩm phản tư: người dùng viết trước, máy soi sau; lời máy luôn kèm căn cứ (trích nguyên văn lời người dùng); giọng máy và lời người dùng phân biệt bằng mắt; máy không quyết định thay.

### 3.5. Phản tư và ma sát có chủ đích

- Rowanne Fleck và Geraldine Fitzpatrick (OZCHI 2010) chia phản tư thành các mức: mô tả lại [R0], mô tả có lý giải [R1], đối thoại giữa các góc nhìn [R2], chuyển hóa (nhìn lại để làm khác) [R3], phản tư phê phán (xét cả bối cảnh xã hội, đạo đức) [R4]. Công nghệ hỗ trợ được từng mức: lưu lại để xem lại, đặt câu hỏi, đưa góc nhìn khác, đối chiếu dự định với kết quả.
- Anna Cox và cộng sự (CHI 2016) lập luận cho ma sát có chủ đích [design frictions]: những ranh giới nhỏ [microboundaries] ngắt thao tác tự động, mời người dùng dừng lại nghĩ. Robert Bjork (1994) gọi đó là khó khăn đáng có [desirable difficulties]: nỗ lực vừa phải giúp học sâu và nhớ lâu.
- Hệ quả: bớt ma sát ở thao tác máy móc (đăng nhập, lưu, điều hướng); giữ ma sát ở chỗ cần suy nghĩ (tự viết trước, dừng lại cảm nhận cơ thể, trả lời từng câu hỏi phản tư mới mở bước sau). Giữ dấu vết tư duy theo thời điểm: lời đã gửi không bị sửa đè, chỉ bổ sung, để sau này người dùng tự đối chiếu được.

### 3.6. Động lực, an lành và an toàn tâm lý

- Dorian Peters, Rafael Calvo và Richard Ryan (Frontiers in Psychology, 2018) đưa thuyết tự quyết [self-determination theory] vào thiết kế qua mô hình METUX: ba nhu cầu tâm lý cơ bản là tự chủ, năng lực, kết nối; cần xét ở năm phạm vi (lúc tiếp cận công nghệ, lúc dùng giao diện, việc làm cùng công nghệ, hành vi được hỗ trợ, đời sống) nằm trong phạm vi thứ sáu là xã hội. Gắn kết nhiều không đồng nghĩa với an lành.
- Janet X. Chen, Allison McDonald, Yixin Zou và cộng sự (CHI 2022) chuyển sáu nguyên tắc tiếp cận thấu hiểu chấn thương tâm lý [trauma-informed] sang điện toán: an toàn, tin cậy, hỗ trợ đồng đẳng, cộng tác, trao quyền, giao thoa (nhạy với văn hóa, lịch sử, giới). Thiết kế theo các nguyên tắc này có lợi cho mọi người dùng, không chỉ người từng trải chấn thương tâm lý.
- Mark Weiser và John Seely Brown (1996) đề xuất công nghệ êm [calm technology]: thông tin nằm ở vùng ngoại vi, chỉ vào trung tâm chú ý khi cần. Chuan/03 đã dùng ý này cho trang đích; web-app càng cần vì người dùng ở lại lâu.

### 3.7. Đạo đức thiết kế

- Colin Gray và cộng sự (CHI 2018) phân 5 chiến lược mẫu lừa [dark patterns]: quấy rầy lặp lại [nagging], cản trở [obstruction], che giấu [sneaking], can thiệp giao diện (đẩy một lựa chọn, giấu lựa chọn khác) [interface interference], ép buộc [forced action].
- Batya Friedman và David Hendry (2019) với thiết kế nhạy giá trị [value sensitive design]: xác định giá trị của mọi bên liên quan (kể cả người không trực tiếp dùng) và giữ chúng xuyên suốt quy trình.
- Hệ quả: không chuỗi ngày, không huy hiệu, không đếm ngược, không nhắc dồn; xóa dữ liệu, rút chia sẻ, dừng giữa chừng phải dễ như bắt đầu; mặc định riêng tư.

## 4. Ca tham chiếu: thay giao diện một web-app phản tư (24/11/2026)

### 4.1. Bối cảnh

Chủ sản phẩm đưa một bản mẫu dựng trong một công cụ thiết kế (4 màn máy tính 1440 px, 7 màn điện thoại 390 px) và yêu cầu thay toàn bộ giao diện của một web-app phản tư nhiều chặng mà giữ nguyên luồng tư duy. Bản mẫu có thêm một số tính năng đổi luồng; chủ sản phẩm quyết không làm: trí năng nhân tạo không nhận xét sau từng ô, câu đã gửi không sửa được (chỉ bổ sung, để giữ dấu vết tư duy tại thời điểm làm), nhãn các ô giữ đúng bản đã chốt, thẻ góp ý giữ bộ câu đã duyệt. Bài học đầu tiên: bản mẫu của công cụ thiết kế thường kèm tính năng mới; tách phần giao diện khỏi phần đổi luồng và để chủ sản phẩm quyết từng phần.

### 4.2. Những gì đã làm, và nguyên lý đằng sau

| Quyết định | Nguyên lý (mục 3) |
|---|---|
| Ba vùng ở màn rộng: thanh bên liệt kê các lượt theo nhóm việc ("Đến lượt bạn", "Chờ hậu kiểm", "Đã xong", "Đã dừng"), cuộc đối luyện ở giữa, cột phải "Phiếu và tiến trình" | danh sách và chi tiết, khung chính và khung phụ (3.3); trạng thái hệ thống luôn hiện (3.1) |
| Ở 1024 đến 1279 px cột phải thành ngăn kéo; dưới 1024 px thanh bên cũng thành ngăn kéo; trang chính điện thoại có thêm lịch sử để bù điều hướng ẩn | điều hướng ẩn giảm khả năng tìm thấy (3.3) |
| Trang chính mở lượt mới ngay từ ô viết quyết định | bớt ma sát ở thao tác máy móc (3.5) |
| Mỗi chặng ghi mục đích; chặng đã xong thu thành một dòng "Xem lại"; cuối thẻ nhập ghi "Câu 3/7 của chặng" | trình bày từng phần, làm nổi cốt lõi (3.2) |
| Lời trí năng nhân tạo in chữ có chân, nghiêng, không khung; lời người dùng nằm trong thẻ | phân biệt giọng máy và giọng người (3.4) |
| Ô dự báo tách cặp "Nếu" và "thì" | cấu trúc gợi cách nghĩ, giảm tải nhớ khuôn câu (3.2) |
| "Đã lưu nháp lúc 15:03" ở cuối thẻ | trạng thái hệ thống, an tâm không mất chữ (3.1, 3.6) |
| Bản ghi quyết định ở cột phải chỉ gom lời người dùng, không có lời máy | người dùng là tác giả của quyết định (3.4, 3.6) |
| Thẻ lời hẹn, tệp lịch .ics không ghi nội dung quyết định, in bản ghi bằng CSS | đối chiếu dự định với kết quả (3.5); riêng tư mặc định (3.7) |
| Hậu kiểm đặt điều đã viết hôm chốt ngay trên ô nhập kết quả | nhận ra thay vì phải nhớ (3.1); phản tư mức chuyển hóa (3.5) |
| Chia sẻ với giảng viên nằm ở đầu lượt, mặc định riêng tư | trao quyền, tin cậy (3.6, 3.7) |

### 4.3. Chỗ vấp khi dựng

| Chỗ vấp | Cách gỡ | Nguyên lý rút ra |
|---|---|---|
| Thẻ câu trả lời chia hai cột (nhãn trái, nội dung phải) như bản mẫu; nhãn đã chốt của dự án dài tới 30 chữ nên cột nhãn vỡ thành 7 dòng | xếp nhãn trên, nội dung dưới | bố cục phải chịu được chữ thật dài nhất, không chỉ chữ mẫu |
| Thanh bên còn ghi "Đang làm" sau khi lượt đã chốt | màn lượt đẩy trạng thái mới nhất lên thanh bên, không chờ trang chính tải lại | mọi vùng hiện cùng một dữ liệu phải cùng một nguồn sự thật |
| Ô đã bỏ qua hiện cả phía dưới ô đang hỏi | chỉ hiện ô bỏ qua đứng trước ô hiện tại | thứ tự trên màn hình phải đúng thứ tự thời gian của luồng |
| "Đã lưu nháp lúc..." của ô trước còn hiện ở ô mới để trống | xóa mốc lưu khi sang ô khác | thông báo trạng thái phải gắn đúng đối tượng |
| Dòng thu gọn liệt kê 5 tên chặng, trên điện thoại vỡ 4 dòng | "Chặng 1-5 · từ Bắt đầu đến Phản tư và Tự quyết" | chữ trên điều khiển phải thử ở 390 px |
| Thanh bên trượt ra rồi đóng khi đổi trang làm ảnh chụp kiểm thử lệch | chụp sau khi hoạt ảnh xong, tải lại trang | kiểm thử giao diện có hoạt ảnh cần chờ hoặc tắt hoạt ảnh |

### 4.4. Kiểm

Playwright trên máy giả lập Firebase đi trọn hai lượt ở 1440 px và 390 px, chụp từng trạng thái (trang chính trống, đang nhập, chờ trí năng nhân tạo, phiếu, khung suy xét, chờ hậu kiểm, hậu kiểm, xong), xem giảng viên đọc lượt được chia sẻ, in bản ghi ra PDF (8 trang); 23 kiểm thử lõi không đổi. Không phải sửa hàm máy chủ nào: giao diện thay được trọn vẹn vì lõi và máy chủ tách khỏi giao diện ngay từ đầu (chuan/10 mục 3).

## 5. Đưa vào chuẩn

Chuan/11 gom các kết luận trên thành 10 mục: tinh thần, hành trình và trạng thái, bố cục theo khổ, luồng nhiều bước, phản hồi và chờ đợi, giao diện có trí năng nhân tạo, ma sát có chủ đích, an lành và an toàn tâm lý, danh sách cấm, chi tiết thực thi và kiểm.

## 6. Nguồn

Kiểm lại ngày 24/11/2026: ✓ là đã mở trang gốc hoặc trang của tác giả, tổ chức.

- ✓ Amershi, S., Weld, D., Vorvoreanu, M., và cộng sự (2019). Guidelines for Human-AI Interaction. CHI 2019. https://doi.org/10.1145/3290605.3300233
- ✓ Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. Proc. ACM HCI 5(CSCW1), 188. https://doi.org/10.1145/3449287
- ✓ Chen, J. X., McDonald, A., Zou, Y., và cộng sự (2022). Trauma-Informed Computing: Towards Safer Technology Experiences for All. CHI 2022. https://doi.org/10.1145/3491102.3517475
- ✓ Cox, A. L., Gould, S. J. J., Cecchinato, M. E., Iacovides, I., & Renfree, I. (2016). Design Frictions for Mindful Interactions: The Case for Microboundaries. CHI EA 2016, 1389-1397. https://doi.org/10.1145/2851581.2892410
- ✓ Fleck, R., & Fitzpatrick, G. (2010). Reflecting on reflection: framing a design landscape. OZCHI 2010, 216-223. https://doi.org/10.1145/1952222.1952269
- ✓ Gray, C. M., Kou, Y., Battles, B., Hoggatt, J., & Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. CHI 2018. https://doi.org/10.1145/3173574.3174108
- ✓ Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI 2025, 1121.
- ✓ Nielsen, J. (1993, cập nhật 2014). Response Times: The 3 Important Limits. Nielsen Norman Group. https://www.nngroup.com/articles/response-times-3-important-limits/
- ✓ Passi, S., & Vorvoreanu, M. (2022). Overreliance on AI: Literature Review. Microsoft, MSR-TR-2022-12.
- ✓ Pernice, K., & Budiu, R. (2016). Hamburger Menus and Hidden Navigation Hurt UX Metrics. Nielsen Norman Group. https://www.nngroup.com/articles/hamburger-menus/
- ✓ Peters, D., Calvo, R. A., & Ryan, R. M. (2018). Designing for Motivation, Engagement and Wellbeing in Digital Experience. Frontiers in Psychology, 9, 797. https://doi.org/10.3389/fpsyg.2018.00797
- ✓ Android Developers (cập nhật 2025). Use window size classes; Canonical layouts. https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. Trong Metcalfe & Shimamura (chủ biên), Metacognition: Knowing about knowing, MIT Press, 185-205.
- Friedman, B., & Hendry, D. G. (2019). Value Sensitive Design: Shaping Technology with Moral Imagination. MIT Press.
- Mayer, R. E. (2021). Multimedia Learning (bản 3). Cambridge University Press.
- Myers, B. A. (1985). The importance of percent-done progress indicators for computer-human interfaces. CHI 1985, 11-17.
- Nielsen, J. (1994). Enhancing the explanatory power of usability heuristics. CHI 1994, 152-158; bản phổ biến: 10 Usability Heuristics for User Interface Design, nngroup.com.
- Nielsen, J. (2006). Progressive Disclosure. Nielsen Norman Group.
- Norman, D. A. (2013). The Design of Everyday Things (bản sửa đổi). Basic Books.
- Shneiderman, B. (2020). Human-Centered Artificial Intelligence: Reliable, Safe & Trustworthy. International Journal of Human-Computer Interaction, 36(6), 495-504.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257-285.
- W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2, tiêu chí 2.5.8 Target Size (Minimum).
- Weiser, M., & Brown, J. S. (1996). Designing Calm Technology. PowerGrid Journal, 1(1).

# 11. Giao diện và trải nghiệm cho web-app

Chuẩn cho web-app, công cụ tra cứu, trắc nghiệm, bài tự đánh giá, ứng dụng có trí năng nhân tạo: nơi người dùng làm việc nhiều bước, quay lại nhiều lần, nhập chữ dài, chờ máy chủ. Trang đích, trang hồ sơ, trang báo giá theo chuan/03; màu, chữ, thành phần chung vẫn theo chuan/03; tiếp cận và hiệu năng theo chuan/05; chữ trên giao diện theo chuan/04. Nguồn, chứng cứ và ca tham chiếu: nghien-cuu/G-giao-dien-trai-nghiem.md.

## 0. Tinh thần

Giao diện phục vụ suy nghĩ của người dùng, không suy nghĩ thay họ, không giữ chân họ. Ba câu hỏi cho mọi màn hình: người dùng có biết mình đang ở đâu, đã làm gì, còn gì không; họ có giữ được quyền quyết định (dừng, rút, xóa, tải về, không làm) không; màn hình có đòi chú ý nhiều hơn mức việc cần không. Gắn kết nhiều không phải mục tiêu; người dùng làm xong việc và sống tốt hơn mới là mục tiêu (Peters, Calvo và Ryan, 2018).

## 1. Hành trình và trạng thái, trước khi vẽ

- Viết hành trình trong đặc tả: người dùng vào từ đâu (thường là đường dẫn Zalo, Facebook trên điện thoại), làm những bước nào, mỗi bước mất bao lâu, khi nào rời đi và quay lại.
- Liệt kê đủ trạng thái của từng màn trước khi dựng, vì lỗi giao diện hay nằm ở trạng thái ít gặp: lần đầu (chưa có dữ liệu), đang nhập, đã lưu nháp, đang gửi, đang chờ trí năng nhân tạo, lỗi mạng, lỗi máy chủ, hết hạn mức, đã khóa hay chỉ đọc, xong, đã dừng, đã xóa, màn của người xem có quyền khác (giảng viên, quản trị).
- Mỗi trạng thái có chữ nói điều đang xảy ra và việc người dùng làm được tiếp theo. Không có trạng thái nào là ngõ cụt.

## 2. Bố cục theo khổ màn hình

| Khổ (px CSS) | Bố cục mặc định |
|---|---|
| Dưới 600 (điện thoại) | Một cột. Thanh trên: nút mở ngăn điều hướng, tên màn, một nút cho khung phụ nếu có. Đường vào quan trọng nhất hiện sẵn ở trang chính, không chỉ nằm trong ngăn ẩn. |
| 600 đến 1023 | Một cột rộng hơn, điều hướng vẫn trong ngăn kéo. |
| Từ 1024 | Thanh bên trái hiện sẵn (danh sách việc, các mục theo vai trò, tài khoản và hạn mức ở cuối) và vùng chính. |
| Từ 1280 | Thêm khung phụ bên phải khi có nội dung phụ trợ đi kèm (tiến trình, bản ghi, chú thích): vùng chính khoảng 70%, khung phụ khoảng 30%; dưới 1280 khung phụ thành ngăn kéo mở bằng nút. |

- Chọn một trong hai mẫu chuẩn của Material Design 3: danh sách và chi tiết (chọn một mục, xem mục đó), khung chính và khung phụ (việc chính cần thông tin hỗ trợ bên cạnh). Đừng chế bố cục mới khi mẫu chuẩn đã đủ.
- Cột đọc và nhập trong vùng chính tối đa khoảng 680 px, kể cả trên màn rất rộng.
- Danh sách trong thanh bên xếp theo việc người dùng cần làm ("Đến lượt bạn", "Đang chờ", "Đã xong"), không chỉ theo ngày.
- Mọi vùng hiện cùng một dữ liệu (thanh bên, đầu màn, khung phụ) lấy từ một nguồn: khi màn đang mở đổi trạng thái, các vùng kia đổi theo ngay.

## 3. Luồng nhiều bước

- Tiến trình luôn hiện: bước nào, bước thứ mấy trên tổng số, câu thứ mấy trong bước. Trên điện thoại dùng thanh vạch mảnh dưới đầu màn; trên máy tính dùng danh sách bước ở khung phụ.
- Mỗi bước có một dòng mục đích nói người dùng sẽ làm gì và vì sao.
- Hiện từng ô một; ô sau mở khi ô trước đủ. Ô được bỏ qua chỉ hiện khi luồng đã đi qua nó, không hiện trước.
- Bước đã xong thu thành một dòng có nút "Xem lại"; không giấu hẳn, vì đối chiếu với điều mình đã viết là một phần của suy nghĩ.
- Lưu nháp tự động sau khi người dùng ngừng gõ, và nói ra ("Đã lưu nháp lúc 15:03", gắn với đúng ô đang viết). Rời trang, mất mạng, đóng máy không làm mất chữ.
- Nút gửi chỉ bật khi đủ điều kiện, và dòng gợi ý nói còn thiếu gì; không để người dùng bấm rồi mới báo lỗi.
- Lời người dùng đã gửi là dấu vết tư duy tại thời điểm đó: chỉ cho bổ sung, không cho sửa đè, khi sản phẩm cần người dùng đối chiếu về sau (phản tư, dự báo, tự đánh giá). Với dữ liệu hành chính (tên, lớp, cài đặt) thì cho sửa.

## 4. Phản hồi và chờ đợi

| Thời gian chờ | Cách làm |
|---|---|
| Dưới 0,1 giây | không cần báo gì, kết quả hiện ngay |
| 0,1 đến 1 giây | khóa nút vừa bấm để không gửi hai lần |
| 1 đến 10 giây | chỉ báo đang làm, nói đang làm gì ("Đang soạn phản hồi...") |
| Trên 10 giây (thường gặp với lời gọi mô hình) | nói thời lượng ước chừng ("thường mất từ nửa phút đến một phút"); giữ nguyên phần đã viết trên màn; việc nhiều phút thì chạy nền, cho rời trang, báo khi xong (chuan/10 mục 8) |

Lỗi nói bằng lời thường: chuyện gì xảy ra, phần đã viết có còn không, làm gì tiếp. Không mã lỗi trần, không "Đã có lỗi xảy ra" đứng một mình.

4 mẫu dùng lại cho mọi web-app:

- **Đang tải**: khung xương (các khối xám đúng chỗ nội dung sẽ hiện) thay cho dòng "Đang tải..." trơn; trình đọc màn hình nhận một câu ẩn nói đang tải gì (`role="status"`). Sau 6 giây chưa xong thì hiện câu báo mạng đang chậm, kèm câu trấn an phần đã gửi vẫn còn nếu màn đó có chữ người dùng.
- **Mất kết nối giữa chừng**: băng báo nằm trong đầu màn (cùng khối dính đầu trang, không chồng lên), nói phần đã gửi vẫn còn, phần đang viết vẫn nằm trong ô, đừng tải lại trang; có nút "Thử lại"; khi có mạng trở lại thì tự tải lại dữ liệu và báo "Đã kết nối lại" vài giây rồi ẩn.
- **3 trang lỗi**: không tìm thấy (đường dẫn sai, mục đã xóa; đường dẫn lạ không lặng lẽ đưa về trang chính), chưa kết nối được máy chủ (tự thử lại khi có mạng), lỗi phía máy chủ (nói rõ không phải lỗi của người dùng, nêu nơi liên hệ). Mỗi trang có nút "Thử lại" khi thử lại có ích và nút về trang chính.
- **Phân biệt lỗi mạng với lỗi máy chủ** ở phía trình duyệt: hàm gọi của Firebase trả mã `internal` cả khi mất mạng, nên nhận diện lỗi mạng bằng cả mã (`unavailable`, `deadline-exceeded`), trạng thái `navigator.onLine` và thông điệp đã đổi sang lời thường.

## 5. Giao diện có trí năng nhân tạo

1. **Người dùng nghĩ trước, máy soi sau.** Ở việc cần suy xét, người dùng viết nhận định của mình trước khi thấy nhận định của máy. Cách này giảm phụ thuộc quá mức vào máy (Buçinca và cộng sự, 2021), đổi lại người dùng thấy tốn sức hơn: giải thích ngắn vì sao, đừng bỏ.
2. **Phân biệt giọng máy và lời người dùng bằng mắt.** Lời máy nói với người dùng (câu mời, câu hỏi) có nhãn tên và kiểu chữ riêng; câu người dùng đã viết nằm trong thẻ. Nội dung có cấu trúc do máy soạn (tóm lược, phiếu, phản chiếu) có khung và nhãn riêng.
3. **Mỗi nhận xét của máy kèm căn cứ** người dùng kiểm được (trích nguyên văn lời họ), và nói rõ đó là giả thuyết để tự kiểm, không phải kết luận.
4. **Nói rõ máy làm được gì, không làm gì** ngay lúc bắt đầu (Amershi và cộng sự, 2019): ví dụ không quyết định thay, không chẩn đoán, không chấm điểm con người.
5. **Bản ghi thuộc về người dùng.** Bản tổng hợp quyết định, kết quả gom đúng lời người dùng; lời máy để riêng.
6. **Không nhân hóa quá mức**: không ảnh đại diện người thật cho máy, không hiệu ứng gõ chữ giả, không lời khen xã giao.
7. **Đường lui khi máy sai**: cho yêu cầu lập lại có giới hạn, cho bỏ qua, cho bổ sung dữ kiện.
8. **Riêng tư hiện ngay đầu**: ai đọc được nội dung này, nội dung gửi đi đâu; công tắc chia sẻ ở đầu màn, mặc định riêng tư.

## 6. Ma sát có chủ đích

- Bớt ma sát ở thao tác máy móc: mở việc mới ngay từ ô nhập ở trang chính, đăng nhập một nút, không hỏi lại điều đã biết.
- Giữ ma sát ở chỗ cần suy nghĩ: tự viết trước, dừng lại cảm nhận, trả lời xong câu này mới mở câu sau, tự đặt mức tin cậy và ngày đối chiếu (Cox và cộng sự, 2016; Bjork, 1994).
- Mỗi chỗ ma sát phải trả lời được câu hỏi "người dùng học hay nghĩ được gì nhờ dừng ở đây". Không trả lời được thì bỏ.

## 7. An lành và an toàn tâm lý

- **Tự chủ**: dừng, rút chia sẻ, tải về, xóa dễ như bắt đầu; không ép làm tiếp; lời mời dùng "bạn có thể", không "bạn phải".
- **Năng lực**: cho thấy tiến bộ bằng chính nội dung của người dùng (điều đã viết, điều đã đối chiếu), không bằng điểm số, huy hiệu, chuỗi ngày.
- **Kết nối**: khi có người thật đứng sau (giảng viên, người hướng dẫn), nói rõ ai và khi nào họ đọc.
- **Thấu hiểu chấn thương tâm lý** (Chen và cộng sự, 2022): an toàn (không bất ngờ, không lộ), tin cậy và minh bạch, trao quyền và lựa chọn, ngôn ngữ không phán xét, có đường tới người thật khi nội dung nặng.
- **Êm** (Weiser và Brown, 1996): thông báo ở vùng ngoại vi; mỗi màn tối đa một lời nhắc nổi bật; không âm thanh, không rung, không chấm đỏ đếm số.

## 8. Danh sách cấm (mẫu lừa và mẫu giữ chân)

Theo 5 chiến lược mẫu lừa của Gray và cộng sự (2018):

1. Quấy rầy lặp lại: hộp thoại mời lặp mỗi lần vào, nhắc đẩy dồn dập, "bạn chắc chưa?" hai lớp.
2. Cản trở: xóa, rút chia sẻ, dừng, hủy gói phải qua nhiều bước hơn bắt đầu; giấu nút tải dữ liệu.
3. Che giấu: chi phí, hạn mức, thời hạn lưu dữ liệu, việc gửi nội dung cho bên thứ ba không nói ra trước.
4. Can thiệp giao diện: nút đồng ý to và sáng, nút từ chối mờ; ô đồng ý đánh dấu sẵn; câu từ chối hạ thấp người dùng.
5. Ép buộc: bắt chia sẻ, bắt đánh giá, bắt mời bạn bè mới cho dùng tiếp.

Cùng họ, cấm trong web-app: chuỗi ngày và "đừng làm đứt chuỗi", huy hiệu thành tích, bảng xếp hạng người dùng, đếm ngược giả, số "người đang xem", thúc nâng gói khi hết hạn mức.

## 9. Chi tiết thực thi

- Vùng chạm 44 x 44 px cho nút trong web-app (sàn WCAG 2.2 là 24 px); khoảng cách giữa hai vùng chạm ít nhất 8 px.
- Nút chỉ có biểu tượng phải có `aria-label`; ngăn kéo, trình đơn đóng bằng Escape và bằng chạm ra ngoài; vùng đang xem trong danh sách có `aria-current`.
- Mỗi màn một tiêu đề cấp 1; bước, chặng là tiêu đề cấp 2.
- Kiểu chữ riêng cho giọng máy phải đủ dấu tiếng Việt (tự lưu trữ đủ ba tệp con vietnamese, latin-ext, latin) và cỡ từ 17 px.
- Bố cục phải chịu được chữ thật dài nhất của dự án (nhãn đã chốt, tên người dùng đặt), không chỉ chữ mẫu ngắn: nhãn dài xếp trên nội dung, không ép thành cột hẹp.
- Ngày hẹn có tệp lịch .ics; tệp không chứa nội dung riêng tư (lịch thường đồng bộ ra nhiều nơi), chỉ đường dẫn về đúng màn.
- Bản in, bản PDF làm bằng CSS `@media print`: ẩn khung, nút, ô nhập; mở mọi phần đang thu gọn; thêm đầu trang có tên và ngày.
- Hoạt ảnh trượt của ngăn kéo 200 ms, tôn trọng `prefers-reduced-motion`.
- Việc tiêu tài nguyên có hạn (lượt, tiền) hoặc có hệ quả về riêng tư (chia sẻ cho người khác đọc) đi qua hộp xác nhận hay nút xác nhận nói rõ hệ quả ngay chỗ bấm, không giấu trong điều khoản. Câu nói hệ quả phải khớp đúng quy tắc trong mã máy chủ (đọc hàm tính hạn mức trước khi viết câu), vì gói khác nhau có thể tính khác nhau.
- Luồng dài có viên chặng nổi dưới đầu màn khi người dùng cuộn lên xem lại: cho biết đang xem bước nào, nút "Về chỗ đang làm"; theo dõi cả lúc trang đổi chiều cao (mở, thu các bước đã xong) bằng `ResizeObserver`, không chỉ sự kiện cuộn.

## 10. Kiểm

Theo chuan/09, thêm cho web-app:

1. Playwright đi trọn luồng ở 390 px và 1280 px (thêm 1440 px nếu có khung phụ), chụp từng trạng thái ở mục 1, cả vai người dùng thường và vai có quyền khác, ở cả theme sáng và tối. Giả lập mất mạng bằng `context.set_offline`, mạng chậm và lỗi mạng khi mở trang bằng `page.route` (trì hoãn hoặc `abort`); in thử từ theme tối.
2. Claude nhìn từng ảnh với 10 câu hỏi: biết đang ở đâu không; biết bước sau không; chữ dài nhất có vỡ khung không; nút chính có rõ không; có ngõ cụt không; lỗi nói cách sửa không; giọng máy và lời người dùng có phân biệt không; riêng tư có rõ không; có gì đòi chú ý thừa không; có mẫu nào trong danh sách cấm không.
3. Chờ hoạt ảnh xong (hoặc tắt hoạt ảnh) trước khi chụp; tải lại trang khi cần dữ liệu mới.
4. Một người thật (chủ sản phẩm hoặc người được mời thử) làm trọn một lượt trên điện thoại của chính họ trước khi mở rộng.

## 11. Hệ thống hình ảnh: token, theme tối, nhận diện

- **Một bộ token** khai báo một lần ở đầu CSS: màu theo vai (nền 4 bậc, chữ 3 bậc, đường kẻ, màu chính và chữ trên màu chính, màu nhấn, màu riêng của giọng máy, trạng thái thành công, cảnh báo, lỗi kèm nền nhạt), bo góc 5 bậc, lưới khoảng cách 4 px, 2 mức bóng, 2 họ chữ. Thành phần chỉ dùng token, không viết mã màu; tên biến cũ của dự án trỏ về token để đổi dần mà không vỡ.
- **Thẻ không viền**, phân lớp bằng nền và bóng; chỉ ô nhập và khung soạn giữ viền đủ tương phản 3:1 để người dùng thấy chỗ nhập được (WCAG 1.4.11). Không thẻ viền màu bên trái, không chuyển màu trang trí.
- **Luôn đi cặp** màu chính với chữ trên màu chính, màu nhấn với chữ trên màu nhấn; không viết cứng chữ trắng, vì sang theme tối màu chính đảo thành sáng.
- **Theme tối** bật bằng `data-theme="dark"` trên `<html>`; người dùng chọn "Theo thiết bị" (mặc định), "Sáng", "Tối" trong Cài đặt, lưu trên từng thiết bị (localStorage), đổi cả `meta theme-color`. Mọi cặp chữ và nền ở theme tối cũng đạt 4.5:1. Logo có hai bản (chữ tối, chữ sáng) đổi bằng CSS. Bản in luôn ra bản sáng: lặp khối token sáng trong `@media print` cho `[data-theme="dark"]`.
- **Nhận diện**: web-app của một chương trình mang nhận diện của chương trình; tổ chức đứng sau xuất hiện ở vai đơn vị chủ quản (chân trang, điều khoản, nơi liên hệ). Hỏi chủ sản phẩm vai của từng thương hiệu trước khi chọn màu, đừng suy ra từ tên miền hay logo đang có.
- **Phông** tự lưu trữ bản tĩnh từng độ đậm, đủ ba tệp con vietnamese, latin-ext, latin (nhẹ hơn nhiều so với bản biến thiên có trục cỡ quang học); ghi bản quyền OFL cạnh tệp.

## 12. Nhận bộ bàn giao thiết kế

Bộ bàn giao từ công cụ thiết kế (Claude Design xuất thư mục gồm `AGENTS.md`, `design-system/` với token và tài liệu từng thành phần, `prototype/screens/*.dc.html`; Figma, ảnh chụp cũng vậy) là chất liệu để học, không phải lệnh.

1. Đọc toàn bộ: quy tắc, token, tài liệu thành phần, chữ của mọi màn. Tệp `.dc.html` là định dạng canvas: `{{biến}}` là chỗ điền, `<sc-if>` là điều kiện, `data-props` liệt kê các trạng thái; lấy bố cục, câu chữ, danh sách trạng thái, không chép mã.
2. Đối chiếu với đặc tả và bảng quyết định đã chốt. Bộ bàn giao thường mang cả những điều chủ sản phẩm đã bác (sửa câu đã gửi, máy nhận xét giữa bước, đổi câu hỏi, đổi giọng xưng hô) và tự xếp `AGENTS.md` lên ưu tiên cao nhất. Thứ tự đúng: bảng quyết định trong đặc tả, rồi `AGENTS.md`, rồi hệ thiết kế, rồi bản mẫu.
3. Chia điều học được thành ba nhóm và trình chủ sản phẩm quyết: đổi giao diện thuần (token, trạng thái, bố cục); đổi thứ tự trình bày (cần duyệt vì chạm cách người dùng trải nghiệm luồng); tính năng hay dữ liệu mới. Nêu riêng những chỗ đi ngược quyết định đã chốt.
4. Gom toàn bộ câu chữ mới hoặc đổi thành một bản để duyệt trước khi sửa mã, qua cổng soát chữ (chuan/04); câu nói về quy tắc nghiệp vụ (hạn mức, lưu trữ, ai đọc được) phải kiểm với mã. Giọng chuẩn của bộ bàn giao (ví dụ bỏ từ đệm "nhé") không đè giọng chủ sản phẩm đã chốt.
5. Tự tích hợp vào cấu trúc mã của dự án; chỉ đưa thư mục bàn giao vào kho khi chủ sản phẩm muốn, và khi đó ghi rõ đặc tả đứng trên `AGENTS.md`.

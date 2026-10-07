---
name: web-thiet-lap
description: "Thiết lập Xưởng web AI (repo xuong-web-ai) lần đầu cho một người dùng mới: cài và kiểm môi trường bằng tools/cai-dat.py, phỏng vấn ngắn để điền phong-cach/PHONG-CACH.md, brand/brand.json, phong-cach/tu-ngu.json theo phong cách của chính họ (tên, chức danh nguyên văn, chủ đề màu web, logo, liên hệ chân trang, giọng chữ), tạo thử một trang mang tên họ để duyệt bằng mắt, rồi giới thiệu xưởng có hệ thống. Kích hoạt khi người dùng nói 'thiết lập xưởng web', 'bắt đầu', 'cài đặt', 'cá nhân hoá', 'đổi phong cách', 'đổi màu, logo, chức danh, liên hệ mặc định', 'kiểm tra xưởng', hoặc khi phong-cach/PHONG-CACH.md còn chỗ trống hay chưa có cau-hinh.json. Cũng kích hoạt để GIỚI THIỆU XƯỞNG khi người dùng nói 'xưởng làm được gì', 'giới thiệu xưởng', 'hướng dẫn tôi cách dùng', 'mới vào chưa biết làm gì', hoặc khi thiết lập vừa xong mà chưa giới thiệu."
---

# Thiết lập xưởng web lần đầu

Mục tiêu: sau khoảng 30-60 phút, người dùng (chuyên gia, giảng viên, diễn giả, tổ chức nhỏ; thường mới dùng AI, chưa từng làm web) có một xưởng chạy được trên máy của họ, mang tên, chức danh, màu, logo, liên hệ và giọng chữ đúng ý họ, đã thấy một trang mang tên mình trên điện thoại và máy tính, hiểu xưởng làm được gì, việc nào họ phải tự tay làm, và biết câu đầu tiên cần nói. Nguyên tắc: hỏi ít, mỗi lượt tối đa 4 câu, luôn có phương án mặc định, giải thích bằng lời thường, không bắt người dùng đọc tài liệu kỹ thuật. Người dùng vắng mặt thì chọn mặc định và ghi rõ giả định vào PHONG-CACH.md.

Phong cách là của NGƯỜI DÙNG. Không đề xuất tên, chức danh, màu, câu chữ của tác giả xưởng hay của bất kỳ ai khác.

## Bước 0 - Định vị

Đọc `CLAUDE.md` (trợ lý khác Claude: `AGENTS.md`) nếu chưa đọc trong phiên. Xác định nơi chạy lệnh (`docs/QUY-TRINH-KY-THUAT.md` mục 2, `skills/_chung/van-hanh.md`): trợ lý chạy thẳng trên máy người dùng, hay Claude Cowork có máy ảo gắn thư mục (và có sandbox đám mây hay không). Chưa có quyền vào thư mục xưởng thì dừng, hướng dẫn người dùng thêm thư mục theo `BAT-DAU.md` bước 3.

Kiểm vị trí: repo nên nằm trong một thư mục cha (gợi ý "Web AI") để `Web/` và `Du an/` ở cạnh repo. Repo đang nằm thẳng trong Documents, Desktop hay Downloads thì đề nghị người dùng tạo thư mục cha và chuyển repo vào trước (một câu lý do: để web và hồ sơ không lẫn với tài liệu khác, và cập nhật xưởng không đụng tới chúng), rồi gắn thư mục cha vào phiên.

Người dùng nói "kiểm tra xưởng" mà xưởng đã thiết lập: chỉ chạy bước 1 (cài phần còn thiếu, tạo thử lại), `python3 tools/kiem-tai-lieu.py`, `python3 tools/kiem-sach.py`, báo kết quả bằng lời thường; không phỏng vấn lại.

## Bước 1 - Cài và kiểm môi trường

Chạy ở gốc repo: `python3 tools/cai-dat.py` (Windows: `py tools\cai-dat.py` hoặc `python tools\cai-dat.py`). Lệnh tự bỏ qua bước đã xong. Mã thoát 2 = đang tải, chạy lại y nguyên tới khi thấy "CÀI XONG". Báo tiến độ bằng lời thường ("đang cài bộ kiểm web").

- Thấy "tạo thử và kiểm thử ĐẠT": sang bước 2.
- Không có trình duyệt kiểm (thường gặp ở máy ảo Claude Cowork): không phải lỗi; bước kiểm bằng trình duyệt chạy ở sandbox đám mây của phiên (`skills/_chung/van-hanh.md`). Báo người dùng một câu: "Máy làm việc của mình không có trình duyệt, nên phần chụp và kiểm web mình chạy ở môi trường đám mây của phiên."
- Tạo thử KHÔNG ĐẠT: đọc chẩn đoán, sửa, chạy lại. Chưa đạt thì chưa làm web thật.
- Node.js chưa có: không cần ngay. Nói với người dùng sẽ cài khi làm web nhiều trang (Astro) hoặc web-app lần đầu.

## Bước 2 - Phỏng vấn phong cách (3 lượt)

Đọc `phong-cach/PHONG-CACH.md` (bước 1 đã chép từ bản khởi đầu `PHONG-CACH.mau.md`, còn chỗ trống trong ngoặc vuông; sửa bản không có `.mau`) và phần `chuDe` của `brand/brand.json` trước. Dùng câu hỏi có lựa chọn sẵn (Claude: AskUserQuestion), mỗi lượt tối đa 4 câu.

**Lượt 1, về người dùng**: tên hiển thị kèm học vị (hỏi đúng cách viết học vị: "TS" hay "TS."); chức danh đúng nguyên văn (nhấn mạnh sẽ hiện y như vậy trên mọi web, hỏi lại chính tả chữ dễ nhầm); có bản chức danh thứ hai không (bản dễ hiểu cho người xem đại chúng, bản tiếng Anh) và khi nào dùng; tên thương hiệu hoặc đơn vị đứng tên web (cá nhân hay tổ chức). Người xem chính và nơi họ đến từ (Zalo, Facebook, email, mã QR) hỏi luôn nếu chưa rõ.

**Lượt 2, về web và cảm giác**: loại web hay cần (đa chọn: trang đích khoá học, sự kiện; hồ sơ cá nhân; trang liên kết; báo giá; thư viện tra cứu; trắc nghiệm; web có blog; web-app có đăng nhập); ba từ tả cảm giác muốn người xem nhận được; chủ đề màu: trình sáu chủ đề khởi đầu bằng một câu cảm giác mỗi chủ đề (giay-muc điềm tĩnh và sâu; than-dong trầm ấm, cả trang tối; dem-vang sang trọng cho sự kiện; dem-xanh rõ ràng, hiện đại, cả trang tối; am-ap gần gũi; trang-xanh hiện đại, tin cậy), kèm lựa chọn "pha từ màu logo của tôi" và "mô tả riêng". Gợi ý một chủ đề chính cho web thường ngày và một chủ đề cho sự kiện. Nói thêm một câu: web đọc dài nên nền sáng là mặc định an toàn.

**Lượt 3, về chữ, liên hệ, logo**: xưng hô với người xem; từ ngữ phải viết đúng (tên chương trình, thuật ngữ nghề) và từ không bao giờ dùng; giữ hay đổi quy ước chữ mặc định của xưởng (PHONG-CACH mục 4); liên hệ công khai ở chân trang (tên chủ quản, email, điện thoại, số Zalo, địa chỉ có thể chỉ ghi thành phố; giải thích một câu: Nghị định 174/2026 xử phạt trang thông tin thiếu tên chủ quản, địa chỉ liên lạc, email, điện thoại (phạm vi áp cho trang cá nhân còn cần đối chiếu, `chuan/08-phap-ly-vn.md`), nên xưởng luôn đặt sẵn; các dòng này hiện công khai); có logo không (có thì nhờ thả vào `brand/logo/` ngay, đọc `brand/logo/README.md`).

Mỗi lượt xong, ghi ngay vào PHONG-CACH.md (thay đúng chỗ trống tương ứng, giữ cấu trúc tệp, đổi cả tiêu đề tệp thành tên người dùng), rồi mới hỏi lượt kế. Ghi máy đọc song song:

- `brand/brand.json`: `nhanVat.chinh` (ten, hocVi, tenDayDu, chucDanh với các bản), `thuongHieu.chinh` (ten, chuDeMacDinh, chuDeHop, logo theo tệp đã thả, khauHieu, website), `lienHe` (chuQuan, email, dienThoai, zalo, diaChi, website), `cap-nhat`. Dòng người dùng chưa muốn công khai: để nguyên dạng `[...]`, web tạo ra sẽ đánh dấu chỗ trống và cổng `kiem-web.py --len` nhắc trước khi lên mạng. Tên thương hiệu khác tên người (một tổ chức): ghi ở `thuongHieu.chinh.ten`.
- Chủ đề màu riêng (pha từ logo hay mô tả): chép một chủ đề gần nhất trong `chuDe` thành khoá mới, đổi mã màu theo vai (`chuan/03-thiet-ke-web.md` mục vai màu); `nhan` là màu duy nhất có cá tính; nền tối thì `toi: true`. Chạy `python3 tools/tuong-phan.py <khoá mới>` tới khi ĐẠT (chữ chính 7:1, chữ phụ, liên kết, chữ trên nút 4.5:1, viền ô nhập 3:1); chưa đạt thì chỉnh độ đậm, không bỏ qua.
- `phong-cach/tu-ngu.json`: mỗi từ không dùng một mục `{"mau": "\\btừ\\b", "lyDo": "dùng ... thay cho ..."}` trong `tuCam`; kiểm tệp đọc được bằng `python3 tools/kiem-tai-lieu.py`.
- Logo: ghi tên tệp vào `thuongHieu.chinh.logo` (`nenSang`, `nenToi`, `bieuTuongSang` nếu có), thay ba tệp logo mẫu. Logo chỉ có một bản: dùng cho loại nền hợp với nó, ghi chú trong PHONG-CACH mục 5. Không có logo: xoá khoá `logo` để web hiện tên bằng chữ.

## Bước 3 - Tạo thử một trang mang tên người dùng

`python3 tools/web-moi.py "Thu phong cach" --khuon ho-so --web thu-phong-cach` (người dùng chủ yếu làm trang đích thì dùng `--khuon landing`). Điền vào trang vài dòng thật của người dùng (tên, chức danh, một đoạn giới thiệu ngắn họ vừa kể; không bịa số liệu, lời cảm nhận); chỗ chưa có để `[[...]]`. Chạy `python3 tools/kiem-web.py thu-phong-cach` (nơi có trình duyệt), NHÌN tờ tổng thể, rồi gửi người dùng kèm câu hỏi đúng ba điều: màu có đúng cảm giác không, tên và chức danh đúng chưa, logo cân đối chưa. Muốn so hai chủ đề: tạo thêm một bản với `--chu-de <chủ đề kia> --web thu-phong-cach-2`. Sửa brand.json, PHONG-CACH theo góp ý, tạo lại tới khi gật. Mỗi góp ý ghi vào sổ tay góp ý (PHONG-CACH mục 6).

Không kiểm được bằng trình duyệt ở đâu cả: gửi người dùng cách mở `Xem web` trên máy họ, nhờ họ nhìn; ghi chú "chưa duyệt thử bằng ảnh chụp" trong PHONG-CACH.

Xong bước này: `python3 tools/cai-dat.py --danh-dau thiet-lap`. Trang thử ở `Web/thu-phong-cach/` và hồ sơ ở `Du an/`: hỏi người dùng giữ làm mẫu hay chuyển vào `Du an/_to_delete/` (không tự xoá).

## Bước 4 - Giới thiệu xưởng và bàn giao

Thiết lập xong mà người dùng chưa biết xưởng làm được gì cho họ thì chưa thật sự bàn giao.

**4a. Tóm tắt thiết lập (5-7 câu).** Đã cài gì, kiểm bằng trình duyệt ở đâu, chủ đề màu nào, logo, liên hệ, cái gì còn treo (Node.js, logo chưa có, dòng liên hệ chưa điền). Nhắc: mọi thứ vừa chọn đều đổi được bằng một câu nói, hoặc sửa tay `phong-cach/PHONG-CACH.md`.

**4b. Giới thiệu có hệ thống (khoảng 10 phút).** Làm theo `references/gioi-thieu-xuong.md`: sáu chặng, mỗi lượt một chặng, kết bằng một câu hỏi; cá nhân hoá bằng những gì người dùng vừa kể. Cuối chặng 6: `python3 tools/cai-dat.py --danh-dau gioi-thieu`.

Người dùng nói "để sau" hay vắng mặt: tóm tắt chặng 1 và 6 trong một tin nhắn, vẫn ghi dấu, nói họ gọi lại bằng câu "giới thiệu lại xưởng". Kết bằng câu đầu tiên họ có thể nói để làm web thật.

Cuối phiên: `python3 tools/kiem-sach.py` ĐẠT.

## Khi người dùng hỏi xưởng làm được gì (bất cứ lúc nào)

Không chạy lại thiết lập. Làm 4b (sáu chặng, hoặc chỉ chặng được hỏi), cập nhật theo PHONG-CACH và các dự án đã có trong `Du an/`. Người dùng cũ hỏi "nên làm gì tiếp" thì gợi ý theo web họ đã có (có trang đích mà chưa có trang hồ sơ, web đã lên mạng mà chưa gắn tên miền, chưa bật đo lượt xem...).

## Khi người dùng muốn đổi phong cách về sau

Đọc PHONG-CACH hiện tại, chỉ hỏi về phần muốn đổi, sửa PHONG-CACH + brand.json (+ tu-ngu.json), tạo thử lại một trang để xác nhận, ghi sổ tay góp ý. Không hỏi lại từ đầu. Web đã lên mạng không tự đổi theo: hỏi người dùng có muốn áp phong cách mới cho web nào (chép lại `tokens.css`, logo, chân trang, rồi kiểm lại từng web).

## Quy tắc cứng

- Chức danh, tên viết đúng nguyên văn người dùng đưa; không tự rút gọn, không tự "sửa cho hay".
- Không đưa tên, chức danh, màu, câu chữ của tác giả xưởng hay của người khác vào phong cách của người dùng.
- Ghi PHONG-CACH sau mỗi lượt hỏi, không gom tới cuối; máy đọc (brand.json, tu-ngu.json) luôn khớp người đọc (PHONG-CACH).
- Không sửa bản khởi đầu `*.mau.*`; không xoá chủ đề màu khởi đầu (khuôn và kiểm tài liệu cần chúng).
- Liên hệ là thông tin công khai: chỉ ghi điều người dùng đồng ý hiện trên web; không bao giờ ghi mật khẩu, mã xác thực, khoá bí mật vào bất kỳ tệp nào.
- Chưa tạo thử ĐẠT thì nói rõ, không nói "xưởng đã sẵn sàng".

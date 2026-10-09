---
name: web-thiet-lap
description: "Thiết lập xưởng web riêng (dựng từ bản vẽ Xưởng web AI, thư mục xuong-web-ai) cho người dùng mới: cài và kiểm môi trường, phỏng vấn ngắn để điền phong cách của chính họ (tên, chức danh nguyên văn, chủ đề màu, logo, liên hệ chân trang, giọng chữ), tạo thử một trang mang tên họ, đóng gói bộ skill riêng và dẫn họ lưu vào tài khoản AI, rồi giới thiệu xưởng có hệ thống. Kích hoạt khi người dùng nói thiết lập xưởng web, bắt đầu, cài đặt, cá nhân hoá, đổi phong cách, đổi màu, logo, chức danh, liên hệ mặc định, kiểm tra xưởng, skill là gì, lưu skill vào tài khoản, đóng gói lại skill, kiểm skill tài khoản, xưởng làm được gì, giới thiệu xưởng, hướng dẫn tôi cách dùng, mới vào chưa biết làm gì, hoặc khi phong cách còn chỗ trống, chưa có cau-hinh.json, chưa có skill riêng."
---

# Thiết lập xưởng web lần đầu

Mục tiêu: sau khoảng 45-75 phút, người dùng (chuyên gia, giảng viên, diễn giả, tổ chức nhỏ; thường mới dùng AI, chưa từng làm web) có một xưởng chạy được trên máy của họ, mang tên, chức danh, màu, logo, liên hệ và giọng chữ đúng ý họ, đã thấy một trang mang tên mình trên điện thoại và máy tính, có bộ skill riêng (đã lưu vào tài khoản AI nếu họ muốn) và hiểu skill là gì, hiểu xưởng làm được gì, việc nào họ phải tự tay làm, và biết câu đầu tiên cần nói. Nguyên tắc: hỏi ít, mỗi lượt tối đa 4 câu, luôn có phương án mặc định, giải thích bằng lời thường, không bắt người dùng đọc tài liệu kỹ thuật. Người dùng vắng mặt thì chọn mặc định và ghi rõ giả định vào PHONG-CACH.md.

Phong cách là của NGƯỜI DÙNG. Không đề xuất tên, chức danh, màu, câu chữ của tác giả xưởng hay của bất kỳ ai khác.

## Bước 0 - Định vị

Đọc `CLAUDE.md` (trợ lý khác Claude: `AGENTS.md`) nếu chưa đọc trong phiên. Xác định nơi chạy lệnh (`docs/QUY-TRINH-KY-THUAT.md` mục 2, `skills/_chung/van-hanh.md`): trợ lý chạy thẳng trên máy người dùng, hay Claude Cowork có máy ảo gắn thư mục (và có sandbox đám mây hay không). Chưa có quyền vào thư mục làm việc thì dừng, hướng dẫn người dùng gắn thư mục làm việc vào phiên (Cowork: nút thêm thư mục; ứng dụng khác: mở thư mục).

Kiểm xưởng đã dựng: gốc xưởng có `XUONG.json`. Chưa có (thư mục đang mở là bản vẽ hay bản tải về của bản vẽ): dừng thiết lập, dựng xưởng theo `DUNG-XUONG.md` của bản vẽ trước (bản vẽ: https://github.com/wincreator3012/xuong-web-ai, bắt đầu từ `AGENTS.md` của bản vẽ). Xưởng nằm trong thư mục làm việc (gợi ý "Web AI") để `Web/`, `Du an/` ở cạnh; phiên phải gắn thư mục làm việc, không phải riêng thư mục xưởng.

Skill này được gọi từ tài khoản (tên `xuong-web-thiet-lap`) mà phiên chưa gắn thư mục làm việc: nhờ người dùng gắn; không gắn được thì chỉ giới thiệu xưởng, trả lời câu hỏi dựa vào `references/` của skill (bản chụp phong cách, hướng dẫn sử dụng, kịch bản giới thiệu), nói rõ đó là bản chụp; không thiết lập, không đóng gói.

Người dùng nói "kiểm tra xưởng" mà xưởng đã thiết lập: chỉ chạy bước 1 (cài phần còn thiếu, tạo thử lại), `python3 tools/ban-dung.py --kiem`, `python3 tools/kiem-tai-lieu.py`, `python3 tools/kiem-sach.py`, báo kết quả bằng lời thường; không phỏng vấn lại.

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

## Bước 4 - Skill riêng cho tài khoản AI

Mục tiêu: người dùng hiểu skill là gì và, nếu muốn, lưu bốn skill của xưởng vào tài khoản AI của họ, để trợ lý nhận ra việc làm web ở mọi cuộc trò chuyện. Toàn bộ chất liệu giải thích và các bước lưu nằm ở `skills/README.md`.

1. **Cấu hình cho gói.** `XUONG.json` cần có `thuMucLamViec` (đường dẫn thư mục làm việc trên máy người dùng như họ thấy, ví dụ `~/Documents/Web AI`, không phải đường dẫn máy ảo) và `xungHoNguoiDung` (trợ lý gọi người dùng là gì); thiếu thì hỏi rồi ghi. Muốn riêng cho skill thì ghi `cau-hinh.json` > `skillTaiKhoan` với cùng hai khoá.
2. **Đóng gói.** `python3 tools/dong-goi-skill.py`. Dấu hiệu xong: "ĐÓNG GÓI: ĐẠT" và bốn tệp `xuong-web-*.zip` trong `Du an/_skill/`. Cảnh báo "cấu hình cá nhân còn thiếu": điền mục được báo (tên hiển thị trong `brand/brand.json`, dòng "Xưng hô với người xem:" trong PHONG-CACH mục 4, giữ đúng nhãn này; `thuMucLamViec` trong `XUONG.json`) rồi đóng gói lại. Mở `Du an/_skill/xuong-web-thiet-ke/SKILL.md`: khối "Cấu hình cá nhân" không còn "(chưa thiết lập)" mới trình người dùng. LỖI khoá bí mật: gỡ khoá khỏi tệp được báo, nói người dùng thu hồi khoá đó.
3. **Giải thích bằng lời thường** (4-6 câu, theo đoạn đầu `skills/README.md`): skill là cuốn sổ tay quy trình trợ lý mở ra đúng lúc; bản gốc nằm trong xưởng; lưu lên tài khoản thì mọi cuộc trò chuyện đều nhận ra việc làm web, kể cả khi đang ở điện thoại, nhờ bản chụp phong cách; vì là bản chụp nên đổi phong cách thì đóng gói lại. Hỏi một câu có lựa chọn: lưu ngay, để sau, hay không cần.
4. **Dẫn lưu từng bước** theo `skills/README.md` mục "Lưu vào tài khoản", đúng nền tảng người dùng dùng hằng ngày (`XUONG.json` > `ungDungHangNgay`; hỏi nếu chưa rõ); kiểm trang trợ giúp hiện hành trước khi dẫn. Một bước mỗi lượt; người dùng tự bấm tải lên, tự chọn tệp. Tệp `.zip` đã nằm sẵn trong `Du an/_skill/` trên máy họ; trong Cowork có thể gửi thêm tệp vào khung chat cho tiện.
5. **Thử** theo mục "Thử xem skill đã chạy chưa" của `skills/README.md` (không tiện mở cuộc trò chuyện mới ngay thì hẹn thử sau buổi giới thiệu).
6. `python3 tools/cai-dat.py --danh-dau skill`. Người dùng chọn để sau hoặc không cần: vẫn ghi dấu, nói họ gọi lại bằng câu "lưu skill vào tài khoản".

Nền tảng người dùng dùng không có tính năng skill: giải thích một câu rằng không cần, trợ lý đọc thẳng `skills/` khi mở thư mục làm việc; vẫn đóng gói để họ dùng khi đổi sang nền tảng có skill.

## Bước 5 - Giới thiệu xưởng và bàn giao

Thiết lập xong mà người dùng chưa biết xưởng làm được gì cho họ thì chưa thật sự bàn giao.

**5a. Tóm tắt thiết lập (5-7 câu).** Đã cài gì, kiểm bằng trình duyệt ở đâu, chủ đề màu nào, logo, liên hệ, skill đã lưu lên tài khoản chưa, cái gì còn treo (Node.js, logo chưa có, dòng liên hệ chưa điền, skill để sau). Nhắc: mọi thứ vừa chọn đều đổi được bằng một câu nói, hoặc sửa tay `phong-cach/PHONG-CACH.md`.

**5b. Giới thiệu có hệ thống (khoảng 10 phút).** Làm theo `references/gioi-thieu-xuong.md`: sáu chặng, mỗi lượt một chặng, kết bằng một câu hỏi; cá nhân hoá bằng những gì người dùng vừa kể. Cuối chặng 6: `python3 tools/cai-dat.py --danh-dau gioi-thieu`.

Người dùng nói "để sau" hay vắng mặt: tóm tắt chặng 1 và 6 trong một tin nhắn, vẫn ghi dấu, nói họ gọi lại bằng câu "giới thiệu lại xưởng". Kết bằng câu đầu tiên họ có thể nói để làm web thật.

Cuối phiên: `python3 tools/kiem-sach.py` ĐẠT.

## Khi người dùng hỏi xưởng làm được gì (bất cứ lúc nào)

Không chạy lại thiết lập. Làm 5b (sáu chặng, hoặc chỉ chặng được hỏi), cập nhật theo PHONG-CACH và các dự án đã có trong `Du an/`. Người dùng cũ hỏi "nên làm gì tiếp" thì gợi ý theo web họ đã có (có trang đích mà chưa có trang hồ sơ, web đã lên mạng mà chưa gắn tên miền, chưa bật đo lượt xem...).

## Khi người dùng nhờ đóng gói lại hay kiểm skill tài khoản

- "Đóng gói lại skill", "lưu skill vào tài khoản": bước 4 từ mục 2; đã có bản cũ trên tài khoản thì dẫn thay bản cũ (`skills/README.md` mục "Khi nào đóng gói lại và thay bản cũ").
- "Kiểm skill tài khoản": đọc được bản đang cài (thư mục skill của ứng dụng; Claude Cowork, Claude Code: bản tài khoản có thể được đồng bộ vào thư mục skill của phiên, thường dưới `~/.claude/skills/`; kiểm thư mục có thật trước khi dùng) thì `python3 tools/dong-goi-skill.py --so <thư mục chứa các skill>`; không đọc được thì nhờ người dùng mở skill trên tài khoản, so khối "Cấu hình cá nhân" và dấu gói trong `references/DONG-GOI.md` với `python3 tools/dong-goi-skill.py --van-tay`. Báo bằng lời thường skill nào lệch, nên đóng gói lại không.

## Khi người dùng muốn đổi phong cách về sau

Đọc PHONG-CACH hiện tại, chỉ hỏi về phần muốn đổi, sửa PHONG-CACH + brand.json (+ tu-ngu.json), tạo thử lại một trang để xác nhận, ghi sổ tay góp ý. Không hỏi lại từ đầu. Người dùng đã lưu skill lên tài khoản thì đóng gói lại và dẫn thay bản cũ, vì bản trên tài khoản mang bản chụp phong cách cũ. Web đã lên mạng không tự đổi theo: hỏi người dùng có muốn áp phong cách mới cho web nào (chép lại `tokens.css`, logo, chân trang, rồi kiểm lại từng web).

## Quy tắc cứng

- Chức danh, tên viết đúng nguyên văn người dùng đưa; không tự rút gọn, không tự "sửa cho hay".
- Không đưa tên, chức danh, màu, câu chữ của tác giả xưởng hay của người khác vào phong cách của người dùng.
- Ghi PHONG-CACH sau mỗi lượt hỏi, không gom tới cuối; máy đọc (brand.json, tu-ngu.json) luôn khớp người đọc (PHONG-CACH).
- Không sửa bản khởi đầu `*.mau.*`; không xoá chủ đề màu khởi đầu (khuôn và kiểm tài liệu cần chúng).
- Liên hệ là thông tin công khai: chỉ ghi điều người dùng đồng ý hiện trên web; không bao giờ ghi mật khẩu, mã xác thực, khoá bí mật vào bất kỳ tệp nào.
- Chưa tạo thử ĐẠT thì nói rõ, không nói "xưởng đã sẵn sàng".

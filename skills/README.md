# SKILL CỦA XƯỞNG: là gì, sống ở đâu, lưu vào tài khoản AI thế nào

Tài liệu này dành cho bạn, chủ xưởng, và cho trợ lý AI đang hướng dẫn bạn. Đọc một lần khoảng 5 phút; phần "Lưu vào tài khoản" làm theo từng bước cùng trợ lý.

## Skill là gì, nói bằng lời thường

Skill là một quy trình làm việc đã được kiểm chứng, viết thành tệp chữ `SKILL.md` để trợ lý AI đọc và làm theo. Hình dung một cuốn sổ tay nghề: khi bạn nói "làm trang đăng ký khoá học", trợ lý mở đúng cuốn sổ về làm web, đi theo các bước đã định (hỏi nhu cầu, lập bản tóm tắt yêu cầu, thiết kế, dựng, tự kiểm, bàn giao) thay vì mỗi lần nghĩ lại từ đầu. Nhờ vậy chất lượng đều tay, và những gì bạn đã dặn "từ nay" được giữ lại.

Skill không phải phần mềm cài vào máy, không chạy ngầm, không đọc dữ liệu của bạn. Nó chỉ là chỉ dẫn; trợ lý đọc nó khi việc bạn nhờ khớp với phần mô tả ở đầu tệp.

## Xưởng của bạn có bốn skill

| Skill nguồn trong xưởng | Tên trên tài khoản AI của bạn | Trợ lý dùng khi bạn |
|---|---|---|
| `skills/web-thiet-lap/` | `xuong-web-thiet-lap` | thiết lập lần đầu, đổi phong cách, hỏi "xưởng làm được gì", nhờ đóng gói lại skill |
| `skills/web-thiet-ke/` | `xuong-web-thiet-ke` | làm hay sửa bất kỳ web nào (lõi: tư vấn, thiết kế, dựng, kiểm, bàn giao) |
| `skills/web-trien-khai/` | `xuong-web-trien-khai` | đưa web lên mạng, tài khoản, tên miền, email theo tên miền, đo lượt xem, bàn giao cho khách |
| `skills/web-ung-dung/` | `xuong-web-ung-dung` | form ghi dữ liệu, thanh toán VietQR, web nhiều trang có blog, web-app có đăng nhập, rà an toàn |

`skills/_chung/` là phần vận hành dùng chung, không phải skill riêng. Tên trên tài khoản có thêm tiền tố `xuong-` để không trùng với skill khác bạn đang có.

## Hai nơi skill sống

- **Trong xưởng** (`skills/` trong thư mục `xuong-web-ai`): bản gốc, luôn mới nhất, đi cùng công cụ, khuôn, chuẩn của xưởng. Khi bạn mở thư mục làm việc trong ứng dụng AI, trợ lý đọc thẳng bản này. Chỉ dùng xưởng trong thư mục đó thì không cần làm gì thêm.
- **Trên tài khoản AI của bạn**: bản đóng gói từ bản gốc, mang khối "Cấu hình cá nhân" (tên bạn, cách trợ lý gọi bạn, thư mục làm việc) và bản chụp phong cách cùng chuẩn nghề. Lợi ích:
  - trợ lý tự nhận ra việc làm web ở **mọi cuộc trò chuyện**, kể cả khi bạn quên mở thư mục, và nhắc bạn gắn thư mục xưởng;
  - đang ở điện thoại, chưa gắn được thư mục, trợ lý vẫn tư vấn, lên kế hoạch, viết chữ đúng phong cách của bạn nhờ bản chụp (chỉ chưa chạy được công cụ kiểm và khuôn);
  - mọi cuộc trò chuyện dùng cùng một quy trình, không lệch nhau.

Điều cần nhớ: bản trên tài khoản là bản chụp tại lúc đóng gói. Bạn đổi phong cách hay xưởng được cập nhật thì đóng gói lại và thay bản cũ (mục "Khi nào đóng gói lại").

## Gói skill của bạn có gì

Trợ lý tạo gói bằng lệnh `python3 tools/dong-goi-skill.py`, ghi vào `Du an/_skill/` (ngoài xưởng): mỗi skill một tệp `.zip` để tải lên, kèm một thư mục cùng tên để bạn mở ra xem.

```
xuong-web-thiet-ke.zip
└── xuong-web-thiet-ke/
    ├── SKILL.md                 quy trình; ngay dưới tiêu đề là khối "Cấu hình cá nhân" của bạn
    └── references/              bản chụp lúc đóng gói, giữ đường dẫn như trong xưởng
        ├── DONG-GOI.md          danh sách tệp chụp, vân tay, dấu gói
        ├── phong-cach/PHONG-CACH.md
        └── chuan/...            chuẩn nghề skill cần khi chưa gắn thư mục
```

Vài chữ trong sơ đồ: `references/` là tài liệu tham khảo đi kèm; vân tay là một chuỗi ký tự máy tính ra từ nội dung tệp, để kiểm hai tệp có giống hệt nhau không; dấu gói là vân tay của cả gói, giúp biết bản trên tài khoản có đúng bản mới nhất không.

Gói không bao giờ chứa mật khẩu hay khoá bí mật: công cụ dừng lại nếu thấy dấu hiệu khoá trong bất kỳ tệp nào. Liên hệ trong phong cách của bạn là thông tin công khai bạn đã đồng ý đặt ở chân trang web.

## Lưu vào tài khoản: từng bước

Giao diện các ứng dụng AI đổi thường xuyên. Các bước dưới đây theo trang trợ giúp chính thức, kiểm ngày 09/10/2026; trợ lý kiểm lại trang trợ giúp hiện hành trước khi dẫn bạn, và dẫn theo đúng chữ trên màn hình bạn đang thấy.

### Claude (ứng dụng trên máy tính, trang web claude.ai, Cowork)

1. **Bật tính năng cần thiết (một lần).** Gói Free, Pro, Max: mở Settings [Cài đặt] > Capabilities (đây là mục cài đặt, khác với mục Customize ở bước 2), bật "Code execution and file creation". Gói Team, Enterprise: người quản trị tổ chức bật ở Organization settings > Plugins & skills; Team thường bật sẵn. Dấu hiệu xong: thấy mục Skills ở bước 2.
2. **Mở trang skill.** Vào Customize > Skills.
3. **Tải gói lên.** Bấm nút "+", chọn "+ Create skill", chọn "Upload a skill", chọn tệp `.zip` trong `Du an/_skill/` (mỗi lần một tệp). Dấu hiệu xong: skill hiện trong danh sách với công tắc đang bật.
4. **Lặp lại** cho ba gói còn lại.

Nếu không thấy mục Skills hay nút tải lên: kiểm lại bước 1, hoặc gói của tổ chức đã tắt tính năng tự tạo skill (hỏi người quản trị). Nguồn: [Use skills in Claude](https://support.claude.com/en/articles/12512180), [How to create custom skills](https://support.claude.com/en/articles/12512198).

### Claude Code

Đăng nhập Claude Code bằng cùng tài khoản: skill đã bật trên claude.ai được đồng bộ sang (gõ `/skills` để xem, theo trang trợ giúp ở trên). Dùng Claude Code bằng khoá API hay qua nhà cung cấp đám mây thì không có đồng bộ: chép thư mục skill trong `Du an/_skill/` vào thư mục skill của Claude Code theo tài liệu hiện hành.

### ChatGPT

ChatGPT có tính năng skill theo chuẩn mở Agent Skills (giai đoạn thử nghiệm, có thể chưa bật cho mọi tài khoản; ở không gian làm việc của tổ chức, người quản trị bật). Có mục skill thì tải gói theo hướng dẫn trong trang trợ giúp của OpenAI; trợ lý tra trang đó trước khi dẫn bạn. Chưa có thì không sao: khi bạn mở thư mục xưởng trong ChatGPT desktop hay Codex, trợ lý đọc thẳng `skills/` trong xưởng.

### Trợ lý khác (Codex, Gemini, Antigravity, Cursor...)

Công cụ theo chuẩn Agent Skills thường đọc skill từ một thư mục cấu hình riêng; trợ lý tra tài liệu chính thức của công cụ trước khi chép gói vào đó. Không có tính năng skill: không cần làm gì, trợ lý đọc `skills/` trong xưởng khi bạn mở thư mục làm việc.

## Thử xem skill đã chạy chưa

Mở một cuộc trò chuyện mới, chưa gắn thư mục, nói: "Tôi muốn làm một trang đăng ký cho khoá học sắp mở." Skill chạy đúng thì trợ lý nhận ra đây là việc của xưởng web, gọi bạn đúng cách bạn đã chọn, nhắc gắn thư mục làm việc để dùng công cụ kiểm, và bắt đầu hỏi về người xem, nơi họ đến từ đâu. Trong Claude, bạn thường thấy dòng cho biết skill `xuong-web-thiet-ke` đang được dùng.

## Khi nào đóng gói lại và thay bản cũ

Nói với trợ lý "đóng gói lại skill" khi: vừa đổi phong cách (chức danh, màu, liên hệ, xưng hô), vừa cập nhật xưởng mà trợ lý báo skill nguồn đã đổi, hoặc chuyển thư mục làm việc sang chỗ khác. Thay bản trên Claude: tắt công tắc skill cũ, bấm "..." cạnh công tắc, chọn "Delete", rồi tải gói mới lên như bước 3. Muốn biết bản trên tài khoản có còn khớp xưởng không: nói "kiểm skill tài khoản".

## An toàn

- Skill là chỉ dẫn cho trợ lý: chỉ cài skill từ nguồn bạn tin. Gói của xưởng do chính trợ lý của bạn tạo trên máy bạn, từ tệp bạn xem được.
- Không đưa mật khẩu, khoá truy cập, thông tin cá nhân của người khác vào phong cách hay skill.
- Skill trên tài khoản đi theo tài khoản của bạn: muốn ngừng dùng thì tắt hoặc xoá trong Customize > Skills.

## Gỡ rối

| Bạn thấy | Thường do | Làm gì |
|---|---|---|
| Tải lên báo lỗi về mô tả [description] | trang trợ giúp Claude ghi giới hạn 200 ký tự cho mô tả skill tải lên; mô tả của xưởng dài hơn để trợ lý nhận ra nhiều cách nói | nhờ trợ lý chạy `python3 tools/dong-goi-skill.py --mo-ta-ngan` rồi tải lại |
| Báo trùng tên skill | bản cũ còn trên tài khoản | xoá bản cũ (mục thay bản cũ) rồi tải lại |
| Không thấy mục Skills, không có nút tải lên | chưa bật "Code execution and file creation", hoặc tổ chức đã tắt | xem bước 1 phần Claude |
| Skill có trên tài khoản nhưng trợ lý không dùng | công tắc đang tắt, hoặc câu nói chưa khớp mô tả | bật công tắc; nói rõ hơn, ví dụ "dùng skill xuong-web-thiet-ke để làm trang hồ sơ" |
| Trợ lý dùng skill nhưng gọi sai tên, sai xưng hô, sai thư mục | gói đóng trước khi đổi phong cách, hoặc thư mục làm việc chưa ghi | đổi phong cách trong xưởng, đóng gói lại, thay bản cũ |
| Hai bản skill cùng việc chạy lẫn nhau | đã tải cả bản cũ lẫn bản mới, hoặc trùng với skill làm web khác | giữ một bản, tắt bản kia |

## Dành cho trợ lý AI khi hướng dẫn phần này

- Giải thích skill bằng lời thường trong bốn đến sáu câu (đoạn đầu tệp này là chất liệu), rồi hỏi người dùng có muốn lưu vào tài khoản không. Không muốn thì tôn trọng: xưởng vẫn chạy đủ khi mở thư mục.
- Dẫn từng bước một, đúng chữ trên màn hình, chờ xác nhận; có trình duyệt dựng sẵn hay công cụ điều khiển trình duyệt thì mở đúng trang và chỉ chỗ bấm, nhưng người dùng tự bấm tải lên và tự chọn tệp.
- Trước khi dẫn, kiểm trang trợ giúp hiện hành của nền tảng khi có công cụ tìm kiếm; khác với tài liệu này thì dẫn theo trang hiện hành và báo để tác giả bản vẽ cập nhật.
- Xong thì cùng người dùng thử một câu (mục "Thử xem skill đã chạy chưa"), rồi ghi dấu: `python3 tools/cai-dat.py --danh-dau skill`.

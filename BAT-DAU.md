# BẮT ĐẦU: để trợ lý AI dựng xưởng web cho bạn, từng bước

Tài liệu này dành cho người chưa từng dùng AI làm việc với tệp trên máy và chưa từng làm web. Đọc hết một lần mất khoảng 10 phút; làm theo mất khoảng 45-75 phút, phần lớn là ngồi chờ máy và trả lời vài câu hỏi. Bạn không cần tải gì từ GitHub và gần như không phải gõ lệnh nào: trợ lý AI đọc bản vẽ rồi dựng xưởng trên máy bạn.

## Trước khi bắt đầu, bạn cần

- **Một máy tính** Mac hoặc Windows 10/11.
- **Một ứng dụng AI làm việc được với thư mục trên máy** (bước 1). Trợ lý AI chỉ chat trên trang web, không ghi được tệp vào máy bạn, thì không dựng được xưởng.
- **Mạng ổn định** trong lúc dựng (trợ lý đọc gần 180 tệp từ bản vẽ và cài bộ kiểm web, tổng cộng khoảng 150-300 MB).
- **Khoảng 1 GB trống** trên ổ đĩa.
- **Tư liệu để thử** (tuỳ chọn nhưng nên có): logo của bạn (PNG nền trong suốt là tốt nhất), một ảnh chân dung gốc, vài dòng giới thiệu bạn là ai, và địa chỉ một hai trang web bạn thấy đẹp.

Chưa cần tài khoản GitHub, Cloudflare hay tên miền: tới lúc đưa web lên mạng, trợ lý dẫn bạn tạo từng thứ một, theo thẻ hướng dẫn trong xưởng.

## Bước 1: cài một ứng dụng AI làm việc được với thư mục

Xưởng được viết và kiểm chứng trên Claude; các ứng dụng khác dùng được vì xưởng là tệp chữ và công cụ Python thông thường, nhưng ít được thử hơn. Chọn MỘT:

| Ứng dụng | Hợp với ai | Tải ở đâu | Ghi chú |
|---|---|---|---|
| **Claude Desktop** (chế độ Cowork) | người mới, muốn ít trục trặc nhất | [claude.ai/download](https://claude.ai/download) | Khuyên dùng. Cowork cần gói trả phí; có cho Mac và Windows. Claude làm việc với thư mục bạn gắn vào và tự lo phần máy móc phía sau |
| **ChatGPT desktop** (có Codex) | người đang dùng ChatGPT | [chatgpt.com/download](https://chatgpt.com/download) | Dùng chế độ Codex (mở một thư mục rồi làm việc trong đó); khung chat thường không dựng được xưởng |
| **Google Antigravity** | người quen sản phẩm Google, không ngại giao diện kiểu phần mềm lập trình | [antigravity.google](https://antigravity.google) | Mở thư mục làm dự án |
| **Claude Code**, **Codex CLI**, Cursor... | người quen dòng lệnh, lập trình | trang của từng công cụ | Chạy thẳng trên máy |

Giá, gói và tên gọi của các ứng dụng AI thay đổi nhanh; xem trang chính thức của từng hãng trước khi đăng ký.

Cài xong, mở ứng dụng và đăng nhập. Với Claude Desktop: chọn chế độ **Cowork** ở thanh bên.

## Bước 2: tạo thư mục làm việc và gắn vào ứng dụng

1. Mở **Documents** (Tài liệu), tạo một thư mục mới, để trống, tên **Web AI**. Đây là nơi chứa xưởng và mọi web bạn làm với nó.
2. Gắn thư mục đó vào ứng dụng:
   - **Claude Desktop, Cowork**: bắt đầu một phiên mới, bấm nút thêm thư mục (biểu tượng thư mục hoặc chữ "Add folder"), chọn `Web AI`. Lần đầu, máy có thể hỏi quyền truy cập thư mục: bấm cho phép.
   - **ChatGPT desktop, Codex**: chọn mở thư mục (Open folder) hoặc tạo dự án từ thư mục `Web AI`.
   - **Antigravity, Cursor**: File, Open Folder, chọn `Web AI`.

Từ lúc này trợ lý đọc và ghi được trong thư mục đó, và chỉ thư mục đó.

## Bước 3: nói câu đầu tiên

Gõ vào khung chat:

> Đọc bản vẽ xưởng web ở https://github.com/wincreator3012/xuong-web-ai (bắt đầu từ AGENTS.md) rồi dựng xưởng web riêng cho tôi trong thư mục Web AI.

Trợ lý sẽ đọc bản vẽ trên GitHub. Bạn không cần mở trang GitHub, không bấm nút tải về nào.

## Bước 4: chuyện gì sẽ xảy ra

**Vài câu hỏi đầu (2 phút).** Trợ lý hỏi một lượt: dùng thư mục nào, gọi bạn là gì, bạn dùng ứng dụng AI nào hằng ngày, bạn có sẵn logo, ảnh, vài dòng giới thiệu không.

**Dựng xưởng (10-20 phút, bạn chỉ chờ).** Trợ lý đọc danh mục của bản vẽ rồi chép phần năng lực (công cụ, khuôn web, chuẩn nghề, phông chữ) vào thư mục `Web AI/xuong-web-ai`, kiểm từng tệp khớp bản vẽ. Sau đó cài thư viện ảnh nhẹ và bộ kiểm web, tạo thử một web mẫu và tự kiểm nó. Bạn sẽ thấy dòng "tạo thử và kiểm thử ĐẠT". Máy thiếu Python thì trợ lý hướng dẫn cài (mục "Nếu máy chưa có Python").

**Vài câu hỏi về bạn (10-15 phút).** Trợ lý hỏi ba lượt ngắn, mỗi lượt vài câu có sẵn lựa chọn:

- Bạn là ai: tên hiển thị kèm học vị, chức danh đúng nguyên văn (trợ lý giữ y như vậy, không tự rút gọn), đơn vị, người xem chính của bạn và họ thường đến từ đâu (Zalo, Facebook, email).
- Bạn cần những web nào, muốn người xem cảm thấy thế nào. Có sáu chủ đề màu để chọn: giấy ngà và mực (điềm tĩnh, sâu), than và đồng ấm (trầm ấm, cả trang tối), đêm xanh thẫm và vàng kim (sang trọng cho sự kiện), đêm xanh và xanh ngọc (rõ ràng, hiện đại), kem ấm và đất nung (gần gũi), trắng và xanh dương (tin cậy). Không ưng cái nào thì pha từ màu logo của bạn.
- Chữ viết thế nào (xưng hô với người xem, từ phải viết đúng, từ không bao giờ dùng), liên hệ công khai đặt ở chân trang (tên chủ quản, email, điện thoại, Zalo: Nghị định 174/2026 xử phạt trang thông tin điện tử thiếu các dòng này; phạm vi áp cho trang cá nhân còn cần đối chiếu, nên xưởng đặt sẵn cho chắc), có logo không.

Trả lời tới đâu trợ lý ghi tới đó vào `phong-cach/PHONG-CACH.md` và `brand/brand.json` trong xưởng. Sau này bạn mở `PHONG-CACH.md` đọc lại, sửa tay được, hoặc chỉ cần nói "từ nay đổi X thành Y".

**Xem thử một trang mang tên bạn (5-10 phút).** Trợ lý tạo một trang mẫu với tên, chức danh, màu, logo, liên hệ của bạn, gửi bạn ảnh chụp trên điện thoại và máy tính. Bạn góp ý về màu, chữ, logo; trợ lý sửa tới khi bạn ưng.

**Bộ skill riêng của bạn (5-10 phút).** Skill là một quy trình đã kiểm chứng viết thành tệp chữ, để trợ lý mở ra đúng lúc và làm theo, như một cuốn sổ tay nghề. Trợ lý giải thích kỹ hơn, đóng gói bốn skill mang cấu hình của bạn vào `Web AI/Du an/_skill/`, rồi dẫn bạn lưu chúng vào tài khoản AI (với Claude: vài cú bấm trong Customize > Skills). Bạn tự bấm tải lên; trợ lý chỉ từng bước. Không muốn lưu lúc này cũng được: xưởng vẫn chạy đủ khi bạn mở thư mục. Chi tiết: `skills/README.md` trong xưởng.

**Buổi giới thiệu xưởng (khoảng 10 phút).** Trợ lý giải thích xưởng làm được gì cho bạn, một web đi qua những bước nào, việc nào bạn phải tự tay làm, những gì xưởng chưa làm, rồi cùng bạn chọn web đầu tiên. Muốn nghe lại lúc nào cũng được: "giới thiệu lại xưởng".

Kết quả trên máy bạn:

```
Documents/
└── Web AI/
    ├── xuong-web-ai/   xưởng của bạn (năng lực + phong cách của bạn)
    ├── Du an/          hồ sơ từng dự án; Du an/_skill/ là gói skill riêng
    └── Web/            mã nguồn từng web
```

## Bước 5: làm web đầu tiên

Nói với trợ lý một câu có đủ ba ý: làm gì, cho ai, họ đến từ đâu và cần làm gì trên trang. Ví dụ:

> Làm trang đăng ký khoá "Lắng nghe trọn vẹn" khai giảng tối thứ Năm 12/11, học trực tuyến 8 buổi, cho phụ huynh có con tuổi teen. Phụ huynh bấm link từ nhóm Zalo, đăng ký và chuyển khoản học phí. Nội dung khoá học ở đây [kèm tệp].

Trợ lý hỏi thêm vài câu, rồi đề xuất giải pháp đơn giản nhất đủ dùng kèm chi phí mỗi năm (nhiều web chỉ tốn tiền tên miền: khoảng 270.000 đ một năm cho .com, 650.000-830.000 đ cho .vn, giá kiểm 10/2026) và những việc bạn phải tự làm. Bạn duyệt **bản tóm tắt yêu cầu** [brief]. Trợ lý trình **kế hoạch thiết kế** 10-15 dòng; bạn duyệt. Trợ lý dựng, tự kiểm, gửi **tờ tổng thể** (trang chụp ở ba khổ cạnh nhau). Bạn góp ý bằng lời. Ưng rồi thì **đưa lên mạng**: trợ lý chuẩn bị mọi thứ và dẫn bạn tạo tài khoản, nối kho, gắn tên miền, từng bước một.

Cách đặt yêu cầu cho từng loại web, ví dụ câu nói, xử lý khi có gì lạ: `HUONG-DAN.md` trong xưởng của bạn.

## Những điều nên biết

- **Xưởng là của bạn, không nối với bản vẽ.** Không có gì tự đổi sau lưng bạn. Muốn nhận bản mới của bản vẽ: nói "cập nhật xưởng"; trợ lý kể bạn nghe điều gì mới rồi mới áp.
- **Tệp bấm đúp trong thư mục xưởng**: `Xem web` mở web bạn đang làm trên trình duyệt của máy bạn. Mac dùng bản `.command`, Windows dùng bản `.bat`. Lần đầu, Mac có thể chặn tệp: bấm **Done** [Xong], mở **System Settings** [Cài đặt hệ thống] > **Privacy & Security** [Quyền riêng tư và bảo mật], kéo xuống cuối, bấm **Open Anyway** [Vẫn mở], nhập mật khẩu máy (chỉ một lần; macOS bản cũ hơn 15 thì bấm chuột phải vào tệp, chọn Open). Windows có thể hiện "Windows protected your PC": bấm "More info" rồi "Run anyway".
- **Mật khẩu là của bạn.** Trợ lý không bao giờ hỏi mật khẩu, mã xác thực hai lớp hay mã khôi phục. Ai hỏi những thứ đó, kể cả một trợ lý AI, thì đừng đưa.
- **Web của bạn ở trên máy bạn** (thư mục `Web/`), và trên GitHub, nơi lưu trữ mà chính bạn đứng tên khi đưa lên mạng. Ứng dụng AI chạy trên đám mây chỉ nhận những tệp cần cho bước đang làm.
- **Dùng trên hai máy**: đặt thư mục `Web AI` vào iCloud Drive, Dropbox hay OneDrive là dùng chung được; chờ tệp tải hết về máy đang ngồi trước khi làm việc lớn. Trên mỗi máy mới, nói với trợ lý "kiểm tra xưởng" để nó cài phần còn thiếu.
- **Muốn đổi phong cách** (màu, chức danh, logo, liên hệ, cách viết): nói "đổi phong cách" và nêu điều muốn đổi. Không cần làm lại từ đầu. Đã lưu skill lên tài khoản thì nhờ "đóng gói lại skill" (cũng vậy sau khi cập nhật xưởng hay chuyển thư mục làm việc).
- **Web nhiều trang, blog, web-app có đăng nhập**: lần đầu làm, trợ lý sẽ nhờ bạn cài Node.js (một lần, có hướng dẫn).

## Nếu máy chưa có Python

- **Mac**: Python 3 thường có sẵn. Chưa có thì trợ lý hướng dẫn cài bằng một lệnh, hoặc tải bản cài từ [python.org](https://www.python.org/downloads/).
- **Windows**: tải bản cài từ [python.org](https://www.python.org/downloads/), lúc cài nhớ đánh dấu ô "Add python.exe to PATH". Trên Windows, lệnh là `py` thay cho `python3`.

## Khi có gì không chạy

Nói với trợ lý điều bạn thấy, bằng lời thường ("nó dừng ở chỗ chép tệp", "web không vào được", "bấm nút gửi không thấy gì"). Trợ lý có mục gỡ rối trong bản vẽ và tài liệu chẩn đoán trong xưởng. Ba việc bạn tự kiểm được: thư mục `Web AI` còn được gắn vào ứng dụng không; máy còn mạng không; ổ đĩa còn chỗ không. Muốn trợ lý tự kiểm toàn bộ, nói: "kiểm tra xưởng".

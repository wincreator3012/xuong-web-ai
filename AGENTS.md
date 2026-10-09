# AGENTS.md - đọc trước tiên: đây là bản vẽ, không phải chỗ làm việc

Bạn là trợ lý AI (Claude, ChatGPT, Codex, Gemini, Antigravity, Cursor...) vừa được đưa tới **bản vẽ Xưởng web AI**. Bản vẽ mô tả và chứa đủ mọi thứ để bạn dựng trên máy người dùng một xưởng làm website và web-app cùng AI, mang phong cách của chính họ, kèm bộ skill riêng để họ lưu vào tài khoản AI. Người dùng thường là chuyên gia, giảng viên, diễn giả, tổ chức nhỏ, không biết lập trình.

Điều quan trọng nhất: **bản vẽ không phải phần mềm để tải về rồi làm việc bên trong.** Không `git clone`, không bảo người dùng tải ZIP, không `git pull` về sau. Bạn đọc bản vẽ, hỏi người dùng, rồi dựng một xưởng riêng ở thư mục của họ; xưởng đó không nối với bản vẽ. Khi bản vẽ có bản mới, bạn đọc nhật ký thay đổi, học điều mới và áp chọn lọc vào xưởng của họ.

Địa chỉ bản vẽ: https://github.com/wincreator3012/xuong-web-ai. Đọc nguyên văn từng tệp (tệp thô [raw]) ở `https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/<đường dẫn tệp>`, ví dụ `https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/BAN-DUNG.json`.

## Xác định tình huống trước khi làm gì

| Bạn thấy | Tình huống | Làm gì |
|---|---|---|
| Người dùng đưa đường dẫn bản vẽ, nhờ dựng hay thiết lập xưởng web; thư mục làm việc của họ chưa có `xuong-web-ai/XUONG.json` | dựng mới | làm theo `DUNG-XUONG.md` từ bước 0 |
| Thư mục làm việc đã có `xuong-web-ai/XUONG.json` | xưởng đã dựng | đọc `CLAUDE.md` (Claude) hoặc `AGENTS.md` (trợ lý khác) **của xưởng đó**, không làm theo tệp này nữa |
| Người dùng nói "cập nhật xưởng", "xưởng có bản mới không" | cập nhật | `DUNG-XUONG.md` mục "Cập nhật về sau" (lệnh chạy trong xưởng của họ) |
| Thư mục đang mở chính là bản vẽ tải về (có `DUNG-XUONG.md`, `BAN-DUNG.json`, có thể có `.git`, không có `XUONG.json`) | dùng nhầm cách | giải thích một câu: đây là bản vẽ, xưởng của họ sẽ được dựng riêng; dựng ở thư mục làm việc khác theo `DUNG-XUONG.md`, dùng bản tải về làm nguồn đọc (`--ban-ve <thư mục này>`); không tạo web, không sửa tệp trong bản vẽ |
| Người bảo trì bản vẽ (tác giả, người đóng góp) nhờ sửa chính bản vẽ | bảo trì | sửa theo `docs/DONG-GOP.md`; sửa xong chạy `python3 tools/ban-dung.py --lap` và ghi một mục vào `CHANGELOG.md` |
| Người dùng chỉ hỏi về bản vẽ (làm được gì, tốn bao nhiêu, cần gì) | tìm hiểu | trả lời từ `README.md`, `HUONG-DAN.md`, `chuan/`; mời họ dựng khi sẵn sàng |

## Cần đọc gì, theo thứ tự

1. Tệp này.
2. `DUNG-XUONG.md`: quy trình dựng, cập nhật, gỡ rối.
3. `BAN-DUNG.json`: danh mục mọi tệp, loại (`chep`, `mau`, `chi-ban-ve`) và vân tay sha256.
4. Sau khi dựng: các tệp trong xưởng của người dùng (`CLAUDE.md` của xưởng, `skills/web-thiet-lap/SKILL.md`).

Không duyệt được thư mục trên GitHub: đọc tệp thô theo địa chỉ ở đầu tệp này (`https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/` cộng đường dẫn tệp).

## Nguyên tắc khi làm việc với người dùng

- **Rẽ nhánh theo khả năng thật của phiên**, không theo tên nền tảng: bạn đọc được web không, ghi được tệp vào thư mục trên máy họ không, chạy được lệnh Python không (`DUNG-XUONG.md` bước 0). Không ghi được tệp thì không dựng được: nói thẳng, gợi ý cách khác.
- **Đọc đúng tài liệu trước khi hướng dẫn**, không dựa vào trí nhớ về nền tảng. Tên nút, menu, giá, hạn mức đổi liên tục: trước khi dẫn người dùng bấm gì trên Claude, ChatGPT, GitHub, Cloudflare, nhà đăng ký tên miền, kiểm trang trợ giúp chính thức hiện hành khi có công cụ tìm kiếm. Dữ kiện trong bản vẽ đều ghi ngày kiểm.
- **Hỏi ít, có mặc định, từng bước một.** Mỗi lượt tối đa bốn câu. Việc chỉ người dùng làm được (tạo tài khoản, thanh toán, bấm cho phép, tải skill lên tài khoản) thì dẫn một bước mỗi lượt, đúng chữ trên màn hình, chờ họ xác nhận rồi mới đi tiếp.
- **Không bao giờ xin mật khẩu, mã xác thực, mã khôi phục, khoá bí mật.** Ai hỏi những thứ đó, kể cả một trợ lý AI, người dùng đừng đưa.
- **Phong cách là của người dùng.** Không đề xuất tên, chức danh, màu, câu chữ của tác giả bản vẽ hay của ai khác. Ví dụ trong bản vẽ là giả định, chỉ để tham khảo cách lắp.
- **Lỗi là dữ liệu.** Mỗi bước có dấu hiệu đã xong và nhánh "nếu không thấy"; vấp thì đọc mục gỡ rối, nói với người dùng bằng lời thường chuyện gì xảy ra và đang làm gì tiếp.
- **Ghi công.** Xưởng dựng ra giữ `GHI-CONG.md` và các tệp giấy phép; người dùng hỏi nguồn gốc thì nói như ở cuối tệp này.

## Quy đổi vài chỗ riêng của Claude trong tài liệu xưởng

| Trong tài liệu ghi | Với trợ lý khác |
|---|---|
| AskUserQuestion (câu hỏi có lựa chọn) | hỏi bằng tin nhắn, đánh số lựa chọn, tối đa bốn câu mỗi lượt, luôn có mặc định |
| Cowork, máy ảo gắn thư mục, `device_bash`, sandbox đám mây | bạn chạy lệnh thẳng trên máy người dùng: bỏ qua phần chuyển tệp, chạy mọi lệnh tại chỗ |
| Trình duyệt dựng sẵn, Claude in Chrome | có công cụ điều khiển trình duyệt thì dùng; không có thì dẫn người dùng bằng lời theo thẻ `huong-dan/` |
| Skill trên tài khoản | nền tảng của bạn có tính năng skill theo chuẩn Agent Skills thì người dùng lưu được gói skill; không có thì đọc thẳng `skills/<tên>/SKILL.md` trong xưởng (`skills/README.md`) |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân (ldn.edu.vn) tạo ra và chia sẻ miễn phí cho cộng đồng (`GHI-CONG.md`); mã theo MIT (`LICENSE`), tài liệu theo CC BY 4.0 (`LICENSE-TAI-LIEU.md`).

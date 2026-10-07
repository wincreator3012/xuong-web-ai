# Vận hành chung cho mọi skill web

## Đọc gì trước

`CLAUDE.md`, `docs/QUY-TRINH-KY-THUAT.md`, `phong-cach/PHONG-CACH.md`. Rồi SKILL.md của việc đang làm và các tệp `chuan/` nó trỏ tới.

## Nơi chạy lệnh

Xác định ngay đầu phiên (`docs/QUY-TRINH-KY-THUAT.md` mục 2):

- **Trợ lý chạy trên máy người dùng** (Claude Code, Codex, Antigravity, ChatGPT desktop): mọi lệnh chạy tại chỗ. Kiểm bằng trình duyệt cần Playwright (`pip install playwright && python3 -m playwright install chromium`).
- **Claude Cowork** có máy ảo gắn thư mục (`device_bash`) và sandbox đám mây (`Bash`):
  - Máy ảo: đọc, sửa tệp web, hồ sơ dự án, chạy `web-moi.py`, kiểm tĩnh `kiem-web.py --khong-trinh-duyet`, `kiem-sach.py`, `tuong-phan.py`. Máy ảo không có trình duyệt.
  - Sandbox: kiểm bằng trình duyệt (chụp ba khổ, axe-core), dựng Astro (`npm`), ảnh chia sẻ (`anh-chia-se.py`). Đưa lên: đóng gói repo và web RA NGOÀI repo (`Du an/_tam/`), stage, giải nén dựng lại đúng cây `<làm việc>/<repo>`, `<làm việc>/Web/<web>`, `<làm việc>/Du an/<dự án>` (để `cau-hinh.json` tương đối còn đúng), chạy, rồi ghi kết quả về đúng chỗ trên máy (`device_commit_files`): báo cáo, ảnh chụp vào `Du an/<dự án>/kiem/`, tệp web đã sửa vào `Web/<web>/` (kèm `expectedMtimeMs` để không ghi đè sửa tay mới của người dùng).
  - Mạng của sandbox có thể chặn vài tên miền (gstatic, img.vietqr.io): kiem-web đánh dấu là CẢNH BÁO "tài nguyên ngoài", không phải lỗi web.

## Hai chốt với người dùng

1. Brief (`BRIEF.md`): nhu cầu, giải pháp, phạm vi, danh sách KHÔNG làm.
2. Kế hoạch thiết kế (`THIET-KE.md`), rồi tờ tổng thể bản đầu.
Người dùng vắng mặt: chọn phương án hợp lý, ghi giả định, nói rõ khi trình.

## Trình người dùng

Tờ tổng thể (`kiem/<trang>-tong-the.jpg`) + 3-6 dòng: lựa chọn chính và lý do, cảnh báo còn lại, điều cần người dùng chốt. Góp ý ghi `SO-GOP-Y.md`; lặp lần hai thì sửa nguồn mặc định và ghi sổ tay PHONG-CACH mục 6.

## Việc người dùng tự tay làm

Theo thẻ trong `huong-dan/`: một bước mỗi lượt, đúng chữ trên màn hình, không bao giờ xin mật khẩu, mã xác thực, khoá bí mật. Có trình duyệt dựng sẵn hoặc Claude in Chrome thì mở đúng trang và chỉ chỗ bấm; người dùng tự đăng nhập, tự xác nhận các bước liên quan tiền, danh tính.

## Repo sạch (mọi phiên)

1. Đầu phiên: `python3 tools/kiem-sach.py`.
2. Trong phiên: web ở `Web/`, hồ sơ ở `Du an/`, việc tạm ở `Du an/_tam/`; công cụ tự dừng nếu bị bắt ghi vào repo.
3. Ứng dụng Claude có thể chép mỗi tệp gửi vào chat thành `Claude outputs/` trong thư mục gắn đầu tiên: rác của phiên.
4. Cuối phiên: chạy lại `kiem-sach.py`; còn nháp lạc thì xin phép xoá một lần rồi `--xoa`; tệp lạ thì hỏi.
5. Câu trả lời cuối nói rõ: repo sạch hay còn gì, đã dọn gì.

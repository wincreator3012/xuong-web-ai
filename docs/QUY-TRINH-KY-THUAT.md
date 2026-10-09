# QUY TRÌNH KỸ THUẬT

Môi trường, lệnh, bản đồ tài nguyên, cấu trúc web và dự án, cổng nghiệm thu, xử lý sự cố. Chỉ giữ điều đang đúng: sự thật đổi thì sửa thẳng vào đúng mục; bài học kèm câu chuyện thì ghi `docs/BAI-HOC.md`.

## 1. Bản đồ tài nguyên

| Thứ | Ở đâu | Ghi chú |
|---|---|---|
| Tên, chức danh, từ ngữ, tông, liên hệ, sổ góp ý | `phong-cach/PHONG-CACH.md` | mục 1, 4 nguyên văn, khớp hai xưởng anh em |
| Luật chữ riêng cho máy kiểm | `phong-cach/tu-ngu.json` | luật chung trong `tools/chung.py` |
| Thương hiệu, chủ đề màu web, nhân vật, liên hệ | `brand/brand.json`, `brand/logo/` | mọi chủ đề qua `tools/tuong-phan.py` |
| Chuẩn nghề (tư vấn, loại web, thiết kế, chữ, kỹ thuật, dữ liệu, triển khai, pháp lý, nghiệm thu) | `chuan/01` tới `chuan/09`, `chuan/kho-dich-vu.json` | nguồn gốc ở `nghien-cuu/` |
| Thẻ hướng dẫn việc người dùng tự làm | `huong-dan/00` tới `huong-dan/12` | cách dẫn: `huong-dan/README.md` |
| Nền chung mọi web | `he-thong/nen.css`, `he-thong/nen.js` | sửa xong: chuan/09 mục 6 |
| Mẫu hồ sơ dự án, tệp kèm web, trang dùng chung | `he-thong/mau-du-an/`, `he-thong/mau-web/`, `he-thong/trang-chung/` | |
| Khuôn web | `khuon/<id>/` (danh mục `khuon/README.md`) | 9 khuôn, 3 tầng kỹ thuật |
| Phông tự lưu trữ | `fonts/` | Lora, Playfair Display, Be Vietnam Pro; SIL OFL |
| Công cụ | `tools/` | mục 3 |
| Dấu xưởng đã dựng, địa chỉ bản vẽ, danh mục tệp của lần dựng | `XUONG.json`, `BAN-DUNG.json` (gốc xưởng) | kiểm, cập nhật: `tools/ban-dung.py`; xưởng không nối git với bản vẽ |
| Skill nguồn | `skills/` | bản ở đây là gốc duy nhất (SKILL.md, `kem.json`); gói cho tài khoản: `tools/dong-goi-skill.py`, ghi ra `Du an/_skill/` |
| Nghiên cứu gốc | `nghien-cuu/` | 5 báo cáo, 07/10/2026 |
| Đường dẫn riêng từng máy | `cau-hinh.json` (`tools/cai-dat.py` tạo từ `cau-hinh.mau.json`, không lên git) | `thuMucDuAn` = `../Du an`, `thuMucWeb` = `../Web` |

### Thư mục làm việc (ngoài repo, trong "Web AI")

```
Web AI/
  xuong-web-ai/              repo xưởng (năng lực)
  Du an/<YYYY-MM tên>/       BRIEF.md, THIET-KE.md, SO-GOP-Y.md, VAN-HANH.md, du-an.json, nguon/, kiem/ (báo cáo, ảnh chụp)
  Du an/_tam/                việc tạm của công cụ và Claude (ghi đè được)
  Web/<tên-web>/             mã nguồn một web: public/ (phần đưa lên mạng), README.md, xuong.json, cấu hình nơi lưu trữ
```

Mỗi web về sau là một kho git riêng nối GitHub và nơi lưu trữ (`huong-dan/01-github.md`). Cấu trúc trong một web: `chuan/05-ky-thuat.md` mục 1.

### Repo sạch (bất biến)

Repo chỉ chứa năng lực. Không có ngoại lệ cho thư mục tạm trong repo.

| Loại tệp | Nơi ghi |
|---|---|
| Brief, kế hoạch, sổ góp ý, hồ sơ vận hành, tư liệu, báo cáo kiểm, ảnh chụp | `Du an/<YYYY-MM tên>/` |
| Mã nguồn web | `Web/<tên-web>/` |
| Web thử, kiểm khuôn, gói repo đưa lên sandbox, tập lệnh dùng một lần | `Du an/_tam/` (ở sandbox: thư mục tạm của phiên) |
| Bản chép tệp gửi vào chat (`Claude outputs/` ứng dụng tự tạo) | rác của phiên, xoá cuối phiên |

`web-moi.py`, `kiem-web.py`, `anh-chia-se.py` từ chối ghi vào repo (báo DỪNG). Cổng: `python3 tools/kiem-sach.py` (đầu và cuối phiên).

## 2. Nơi chạy lệnh

- **Máy người dùng** (Mac hoặc Windows; với Claude Cowork, Claude chạm qua `device_bash` trong máy ảo Linux có gắn thư mục): đọc, sửa web và hồ sơ, `web-moi.py`, `kiem-web.py --khong-trinh-duyet`, `tuong-phan.py`, `kiem-sach.py`, `kiem-tai-lieu.py`. Máy ảo không có trình duyệt; có Node.js nhưng mạng có thể bị giới hạn. Người dùng xem thử web trên máy thật bằng `python3 tools/xem.py <web>` (hoặc bấm đúp `public/index.html` với web tĩnh).
- **Sandbox đám mây** (`Bash`): kiểm bằng trình duyệt (Playwright + Chromium có sẵn, không chạy "playwright install"), dựng Astro (`npm`), ảnh chia sẻ, thử cấu hình (`npx wrangler deploy --dry-run`). Quy trình đưa lên, mang về: `skills/_chung/van-hanh.md` mục "Nơi chạy lệnh".
- **Đưa web lên mạng thật** cần tài khoản của người dùng: cách thường ngày là nối kho GitHub với nơi lưu trữ (người dùng Commit, Push bằng GitHub Desktop); Firebase thì người dùng chạy lệnh `npx firebase-tools deploy` trên máy sau một lần đăng nhập (`huong-dan/05-firebase.md`).

### Khởi động phiên ở sandbox

```bash
# 1. trên máy (device_bash), đóng gói RA NGOÀI repo:
#    cd "<Web AI>" && tar czf "Du an/_tam/xuong.tgz" --exclude=.git --exclude=node_modules --exclude="Claude outputs" xuong-web-ai "Web/<tên-web>" "Du an/<dự án>"
# 2. stage tệp đó, giải nén vào <làm việc>/ ở sandbox (giữ nguyên cây thư mục)
# 3. kiểm
python3 xuong-web-ai/tools/kiem-web.py <tên-web>
# 4. mang BAO-CAO.md, ảnh trong Du an/<dự án>/kiem/ và tệp web đã sửa về đúng chỗ trên máy (device_commit_files)
```

### Trên máy người dùng (một lần)

- `python3 tools/cai-dat.py` (Windows: `py tools\cai-dat.py`): tạo `cau-hinh.json`, hai thư mục làm việc, tệp phong cách của bạn từ bản `*.mau.*`, cài Pillow, Playwright và tạo thử một web; chạy lại bao nhiêu lần cũng an toàn, `--trang-thai` để xem. Python 3.9 trở lên (Mac có sẵn hoặc cài từ python.org; Windows cài từ python.org, đánh dấu "Add python.exe to PATH").
- Kiểm bằng trình duyệt ngay trên máy: `tools/cai-dat.py` đã cài Playwright; cài tay thì `pip3 install playwright pillow && python3 -m playwright install chromium`.
- Web Astro, đưa lên Firebase bằng dòng lệnh: cài Node.js 22 LTS (nodejs.org).
- GitHub Desktop (desktop.github.com) để Commit, Push.

## 3. Lệnh thường dùng

```bash
python3 tools/cai-dat.py [--trang-thai]                         # cài, kiểm môi trường, tạo thử một web (chạy lại an toàn)
python3 tools/web-moi.py --ds                                        # khuôn, chủ đề màu, thương hiệu
python3 tools/web-moi.py "Trang khoá học mùa thu" --khuon landing     # tạo hồ sơ dự án + mã nguồn web
python3 tools/web-moi.py "Hội thảo mùa xuân" --khuon landing --thuong-hieu chinh   # chọn thương hiệu trong brand.json, dùng chủ đề mặc định của nó
python3 tools/kiem-web.py <tên-web>                                  # cổng nghiệm thu (tĩnh + trình duyệt nếu có)
python3 tools/kiem-web.py <tên-web> --len                            # cổng trước khi đưa lên mạng
python3 tools/anh-chia-se.py <tên-web> [--tieu-de ... --dong-phu ... --nhan ...]   # ảnh 1200x630 cho Zalo, Facebook
python3 tools/xem.py <tên-web>                                       # xem thử trên máy (http://localhost:8000)
python3 tools/dua-len.py --so-sanh                                   # bảng chọn nơi lưu trữ
python3 tools/dua-len.py <tên-web> --noi cloudflare                  # tạo cấu hình + kiểm --len + in bước tiếp
python3 tools/dua-len.py <tên-web> --ten-mien https://ten.vn         # gắn tên miền: canonical, OG, sitemap, robots
python3 tools/dua-len.py <tên-web> --noi cloudflare --that           # đưa lên thật (máy đã đăng nhập công cụ)
python3 tools/tuong-phan.py                                          # kiểm tương phản mọi chủ đề màu
python3 tools/kiem-sach.py [--xoa]                                   # cổng repo sạch
python3 tools/kiem-tai-lieu.py                                       # cổng tài liệu, skill, khuôn của xưởng
python3 tools/dong-goi-skill.py [<skill>] [--so <thư mục>]            # gói skill (.zip) để lưu vào tài khoản; --so: so lệch với bản đang cài
python3 tools/ban-dung.py --kiem | --so-ban-ve | --doc-tho             # xưởng còn nguyên không; bản vẽ có gì mới; chép phần năng lực mới
```

## 4. Hồ sơ máy đọc

- `Web/<tên-web>/xuong.json`: khuôn, loại (`tinh` | `astro` | `firebase`), bậc, thư mục công khai, thương hiệu, chủ đề, phông, tên miền, nơi lưu trữ, hồ sơ dự án. Công cụ đọc và ghi; không đưa lên mạng (nằm ngoài `public/`).
- `Du an/<dự án>/du-an.json`: tên, web, khuôn, thương hiệu, chủ đề. `kiem-web.py` dựa vào đây để ghi báo cáo đúng chỗ.
- Thay thế khi tạo web: `{{TEN}}`, `{{TEN_NGUOI}}`, `{{CHUC_DANH}}`, `{{EMAIL}}`, `{{DIEN_THOAI}}`, `{{ZALO_LINK}}`, `{{URL}}`... lấy từ `brand/brand.json` (`tools/web-moi.py` > `bang_thay`). Giá trị chưa có thành chỗ trống `[[...]]`.

## 5. Cổng nghiệm thu

1. `tools/kiem-web.py` không LỖI; cảnh báo còn lại có lý do (chuan/09).
2. Claude NHÌN tờ tổng thể và từng khổ; đọc soát từng âm tiết; tên, chức danh đúng PHONG-CACH mục 1.
3. Trước khi đưa lên mạng: `--len` ĐẠT; bậc 3 làm `KIEM-BAO-MAT.md` cùng người dùng.
4. Sửa `he-thong/` hay khuôn: thử web từ mọi khuôn bị ảnh hưởng (chuan/09 mục 6).
5. Repo sạch: `tools/kiem-sach.py` ĐẠT cuối mọi phiên có chạm vào repo; sửa tài liệu, skill thì thêm `tools/kiem-tai-lieu.py` ĐẠT.

## 6. Khi một khâu hỏng

| Triệu chứng | Nguyên nhân thường gặp | Cách xử lý |
|---|---|---|
| Bấm đúp index.html mà trang tra cứu, trắc nghiệm báo "chưa đọc được dữ liệu" | trình duyệt chặn đọc tệp JSON khi mở trực tiếp từ ổ đĩa | xem qua máy chủ thử: `tools/xem.py` |
| kiem-web báo "không tải được tài nguyên ngoài" (gstatic, vietqr) | mạng nơi kiểm chặn tên miền đó | CẢNH BÁO, không phải lỗi web; kiểm lại trên máy có mạng |
| Dấu tiếng Việt rơi sang phông khác | thiếu tệp `vietnamese` của phông, hoặc đổi phông không có tiếng Việt | chỉ dùng phông trong `fonts/`; kiem-web kiểm `dauViet` |
| Chữ trong bài Astro thành nháy cong, ba chấm Unicode | Astro bật smartypants mặc định | giữ `markdown: { smartypants: false }` trong astro.config.mjs |
| Astro báo "Invalid URL" | `site` chưa phải URL hợp lệ | khuôn để `https://chua-dat-ten-mien.invalid` tới khi có tên miền (`dua-len.py --ten-mien`) |
| Web trên Vercel, Firebase lộ tệp ngoài trang | đưa cả thư mục gốc lên | chỉ `public/`, `dist/` (vercel.json `outputDirectory`, firebase.json `public`); kiem-web chặn |
| Cloudflare báo lỗi tên Worker khi dựng từ kho | tên Worker khác `name` trong wrangler.jsonc | đổi cho khớp |
| Đăng nhập Google không chạy khi mở link trong Zalo, Facebook | trình duyệt nhúng bị Google chặn | lá chắn trong khuôn app hướng dẫn mở bằng Chrome, Safari |
| Firestore `permission-denied` | luật chặn đúng thiết kế, hoặc dữ liệu ghi thiếu, thừa trường | đối chiếu `keys().hasOnly`; gửi dòng lỗi cho Claude |
| Zalo vẫn hiện ảnh chia sẻ cũ | bộ đệm của Zalo | developers.zalo.me/tools/debug-sharing |
| Công cụ báo DỪNG vì ghi vào repo | đường dẫn đầu ra trỏ vào repo | tạo web bằng `web-moi.py` (vào `Web/`), hoặc `--ra "Du an/_tam/..."` |

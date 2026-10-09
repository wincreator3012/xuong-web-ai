# Nhật ký thay đổi của bản vẽ

Trợ lý AI đọc tệp này khi người dùng nói "cập nhật xưởng": từ phiên bản ghi trong `XUONG.json` của xưởng tới bản mới nhất, để kể bằng lời thường điều gì mới và điều gì sẽ đổi. Mỗi mục ghi: phiên bản (năm.tháng.ngày), thay đổi, việc trợ lý cần làm trong xưởng đã dựng, dữ kiện đã kiểm chứng lại.

## 2026.10.09

Chuyển sang mô hình bản vẽ.

- Repo trở thành **bản vẽ**: người dùng không tải về hay `git clone`; trợ lý AI đọc bản vẽ rồi dựng xưởng riêng ở thư mục làm việc của người dùng. Cửa vào cho trợ lý: `AGENTS.md`; quy trình: `DUNG-XUONG.md`; danh mục tệp và vân tay: `BAN-DUNG.json`.
- Công cụ mới `tools/ban-dung.py`: lập danh mục (ở bản vẽ), đọc thô và kiểm vân tay khi dựng, kiểm xưởng còn nguyên, so xưởng với bản vẽ mới khi cập nhật; giữ nguyên tệp người dùng đã chủ ý sửa.
- Mẫu điểm vào của xưởng chuyển sang `mau-xuong/` (CLAUDE.md, AGENTS.md, XUONG.json); `CLAUDE.md`, `GEMINI.md` ở bản vẽ chỉ trỏ về `AGENTS.md`.
- **Skill riêng cho tài khoản AI**: công cụ mới `tools/dong-goi-skill.py` đóng gói bốn skill thành `xuong-web-*.zip` (khối cấu hình cá nhân, bản chụp phong cách và chuẩn nghề trong `references/`, kiểm tên, mô tả, khoá bí mật); mỗi skill nguồn có `kem.json`. Hướng dẫn skill đầy đủ: `skills/README.md`. Skill `web-thiet-lap` thêm bước 4 (skill riêng), giới thiệu xưởng thành bước 5; `tools/cai-dat.py` thêm dấu `--danh-dau skill`.
- `HUONG-DAN.md` thêm mục 13 (cập nhật xưởng theo mô hình mới), mục 14 (skill trên tài khoản). `BAT-DAU.md` viết lại theo cách đưa đường dẫn cho trợ lý.

Việc trong xưởng đã dựng trước ngày này (xưởng tải về theo cách cũ, có `.git` hoặc là bản ZIP): trợ lý giải thích mô hình mới; dựng xưởng mới cạnh đó theo `DUNG-XUONG.md`, dùng bản cũ làm nguồn đọc và chép sang phần của người dùng (`brand/brand.json`, logo trong `brand/logo/`, `phong-cach/PHONG-CACH.md`, `phong-cach/tu-ngu.json`, `cau-hinh.json`); kiểm `python3 tools/ban-dung.py --kiem`; rồi để người dùng quyết giữ hay bỏ bản cũ.

Dữ kiện kiểm chứng lại: các bước lưu skill vào tài khoản Claude theo trang trợ giúp "Use skills in Claude" và "How to create custom skills" (kiểm 09/10/2026).

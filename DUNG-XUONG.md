# DỰNG XƯỞNG: quy trình cho trợ lý AI dựng xưởng web riêng từ bản vẽ

Tài liệu này viết cho trợ lý AI. Người dùng đưa bạn đường dẫn bản vẽ Xưởng web AI và nhờ "dựng xưởng web cho tôi". Bạn đọc bản vẽ rồi dựng trên máy họ một xưởng riêng: phần năng lực giống hệt bản vẽ, phần phong cách và bộ skill mang dấu ấn của chính họ. Người dùng chỉ trả lời vài lượt câu hỏi, duyệt bằng mắt, và tự tay lưu skill vào tài khoản AI của họ. Toàn bộ mất khoảng 45-75 phút, phần lớn là máy chạy.

Đọc `AGENTS.md` trước nếu chưa đọc. Mỗi bước dưới đây có ba phần: làm gì, dấu hiệu đã xong, nếu không thấy dấu hiệu đó thì làm gì.

## Ba điều không làm

1. **Không biến bản vẽ thành chỗ làm việc.** Không `git clone`, không bảo người dùng tải ZIP về rồi mở, không làm việc bên trong bản vẽ. Người dùng đã lỡ tải về: dùng bản đó như nguồn đọc (`--ban-ve <thư mục bản tải về>`), dựng xưởng ở chỗ khác, cuối cùng hỏi họ có muốn bỏ bản tải về không (chuyển vào thùng rác là việc của họ).
2. **Không viết lại "theo ý hiểu" các tệp năng lực.** Công cụ, khuôn, nền chung, phông, chuẩn, skill nguồn (loại `chep` trong `BAN-DUNG.json`) phải trùng khớp từng byte với bản vẽ, kiểm bằng vân tay sha256. Gõ lại bằng tay gần như luôn lệch một vài ký tự và làm hỏng công cụ. Cá nhân hoá nằm ở phần riêng và ở bộ skill, không nằm ở công cụ.
3. **Không chép phần riêng của bất kỳ ai.** Bản vẽ chỉ có bản khởi đầu `*.mau.*` và ví dụ giả định; tên, màu, liên hệ, giọng chữ của xưởng mới đều hỏi từ người dùng.

## Kết quả cần có

```
<thư mục làm việc, mặc định Documents/Web AI>/
  xuong-web-ai/   xưởng riêng: năng lực (chép đúng bản vẽ) + phần riêng (phong cách, cấu hình,
                  XUONG.json, CLAUDE.md, AGENTS.md); không có .git, không nối với bản vẽ
  Du an/          hồ sơ từng dự án; Du an/_skill/ chứa gói skill riêng; Du an/_tam/ việc tạm
  Web/            mã nguồn từng web
```

Giữ đúng tên `xuong-web-ai` cho thư mục xưởng: tài liệu kỹ thuật, skill và công cụ gọi thư mục xưởng là "repo `xuong-web-ai`".

## Bước 0: kiểm năng lực của phiên

| Cần | Để làm gì | Không có thì |
|---|---|---|
| Đọc được bản vẽ trực tuyến (công cụ đọc web, hoặc lệnh có mạng tới `github.com` và `raw.githubusercontent.com`) | đọc `BAN-DUNG.json`, tài liệu, tệp thô | nhờ người dùng kiểm mạng; tối thiểu phải đọc được `BAN-DUNG.json` và `tools/ban-dung.py` |
| Ghi tệp vào một thư mục trên máy người dùng | dựng xưởng | không dựng được: nói thẳng, gợi ý ứng dụng làm việc được với thư mục (`BAT-DAU.md` bước 1) |
| Chạy lệnh Python 3.9 trở lên | đọc thô, kiểm, cài, đóng gói skill | hướng dẫn cài Python (`BAT-DAU.md`, mục "Nếu máy chưa có Python") rồi mới đi tiếp |

Rẽ nhánh theo nơi bạn chạy lệnh:

| Phiên | Cách làm |
|---|---|
| Claude Cowork (máy ảo gắn thư mục người dùng, cộng sandbox đám mây của phiên) | Thử `ban-dung.py --doc-tho` trong máy ảo trước. Máy ảo báo lỗi mạng: dựng phần năng lực trong sandbox đám mây (một thư mục tạm có cùng cây `xuong-web-ai/`), `--kiem --chi-nang-luc` ĐẠT ở đó, rồi chuyển cả cây, kể cả `BAN-DUNG.json`, vào thư mục người dùng bằng công cụ chuyển tệp (gần 180 tệp, tối đa 50 tệp mỗi lần, giữ đúng đường dẫn), chạy lại `--kiem --chi-nang-luc` trong máy ảo |
| Claude Code, Codex (kể cả chế độ Codex trong ChatGPT desktop), Antigravity, Cursor (chạy lệnh thẳng trên máy người dùng) | chạy mọi lệnh tại chỗ |
| Chỉ có khung chat, không ghi được tệp (kể cả khung chat thường của ChatGPT, Claude trên web) | không dựng được xưởng; giải thích một câu vì sao, gợi ý ứng dụng phù hợp, vẫn trả lời được câu hỏi về làm web từ tài liệu bản vẽ |

Dấu hiệu xong: bạn biết mình đi nhánh nào, và `python3 --version` (Windows: `py --version`) chạy được ở nơi sẽ dựng, báo 3.9 trở lên.

## Bước 1: hỏi người dùng một lượt

Nói trước một câu: bạn sẽ dựng xưởng trên máy họ, máy chạy khoảng 10-20 phút, rồi mới hỏi về phong cách. Hỏi tối đa bốn câu, câu nào cũng có mặc định:

1. **Thư mục làm việc**: mặc định tạo `Web AI` trong Documents (Tài liệu). Thư mục phải được gắn vào phiên (Cowork: nút thêm thư mục; ứng dụng khác: mở thư mục).
2. **Trợ lý gọi bạn là gì**: "bạn", "anh", "chị", "thầy", "cô", hay tên riêng.
3. **Ứng dụng AI bạn dùng hằng ngày**: Claude (ứng dụng, Cowork, Claude Code), ChatGPT, hay khác. Câu trả lời quyết định bước lưu skill; ghi vào `XUONG.json` > `ungDungHangNgay` ở bước 4.
4. **Tư liệu có sẵn** (không bắt buộc): logo, ảnh chân dung gốc, vài dòng giới thiệu, một hai web bạn thấy đẹp.

Dấu hiệu xong: thư mục làm việc đã gắn vào phiên và bạn đọc, ghi được trong đó. Không thấy: dừng, hướng dẫn người dùng gắn thư mục theo `BAT-DAU.md` bước 2.

## Bước 2: đọc danh mục, viết công cụ dựng

1. Đọc `BAN-DUNG.json` của bản vẽ ở `https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/BAN-DUNG.json`: phiên bản, danh sách tệp, loại từng tệp (`chep`, `mau`, `chi-ban-ve`). Địa chỉ đọc thô của mọi tệp: `https://raw.githubusercontent.com/wincreator3012/xuong-web-ai/main/` cộng đường dẫn tệp (khoá `nguonTho` trong tệp).
2. Tạo `<thư mục làm việc>/xuong-web-ai/tools/`, rồi ghi `tools/ban-dung.py` đúng nguyên văn tệp thô `<nguonTho>tools/ban-dung.py`: có lệnh và mạng thì dùng lệnh đọc tệp thô (ví dụ `curl -fsSL <nguonTho>tools/ban-dung.py -o tools/ban-dung.py`); không có thì đọc bằng công cụ đọc web và ghi bằng công cụ ghi tệp, không sửa một ký tự. Người dùng đã có bản tải về của bản vẽ và gắn nó vào phiên cùng thư mục làm việc: chép `tools/ban-dung.py` từ bản đó.
3. So vân tay, chạy ở gốc xưởng (`xuong-web-ai/`): `python3 -c "import hashlib;print(hashlib.sha256(open('tools/ban-dung.py','rb').read()).hexdigest())"` phải bằng giá trị `sha256` của dòng `tools/ban-dung.py` trong `BAN-DUNG.json`.

Dấu hiệu xong: hai chuỗi vân tay khớp. Không khớp: ghi lại bằng đường đọc thô; công cụ đọc web tóm tắt hay định dạng lại nội dung thì không dùng được cho bước này.

## Bước 3: ghi phần năng lực

Ở gốc xưởng: `python3 tools/ban-dung.py --doc-tho`. Công cụ đọc thô từng tệp loại `chep` từ bản vẽ trực tuyến, kiểm vân tay rồi mới ghi, in một dòng cho mỗi tệp, và lưu `BAN-DUNG.json` của lần dựng vào xưởng (dùng để kiểm và cập nhật về sau). Báo tiến độ cho người dùng bằng lời thường ("đang chép công cụ và khuôn vào xưởng của bạn").

Dấu hiệu xong: dòng cuối "ĐỌC THÔ: ghi ... tệp, ... 0 lỗi", và `python3 tools/ban-dung.py --kiem --chi-nang-luc` ĐẠT. Lệnh `--kiem` đầy đủ lúc này còn KHÔNG ĐẠT vì thiếu ba tệp điểm vào: bình thường, bước 4 lo.

Nếu không thấy: lỗi mạng thì theo nhánh Cowork ở bước 0, hoặc người dùng đã có bản tải về thì `--ban-ve <thư mục bản tải về>`; lỗi vân tay thì xem mục gỡ rối.

## Bước 4: viết phần riêng của xưởng

Ba tệp loại `mau` (đọc từ `mau-xuong/` của bản vẽ, ghi vào gốc xưởng):

- `XUONG.json` từ `mau-xuong/XUONG.mau.json`: điền `phienBan` (của `BAN-DUNG.json`), `ngayDung`, `ngayCapNhat`, `troLyDung`, `thuMucLamViec` (đường dẫn trên máy người dùng như họ thấy trong Finder hay File Explorer, ví dụ `~/Documents/Web AI`, không phải đường dẫn máy ảo), `xungHoNguoiDung` (câu 2 bước 1), `ungDungHangNgay` (câu 3 bước 1); bỏ khoá `_huong-dan`. Tệp này đánh dấu thư mục là xưởng đã dựng, không phải bản vẽ.
- `CLAUDE.md` và `AGENTS.md` từ `mau-xuong/`: chép nguyên nội dung mẫu. Sau bước thiết lập có thể thêm một dòng đầu nói đây là xưởng của ai; không đổi quy tắc cứng.

Dấu hiệu xong: `python3 tools/ban-dung.py --kiem` ĐẠT và `python3 tools/kiem-tai-lieu.py` ĐẠT. Không thấy: đọc dòng báo lỗi, viết bù tệp còn thiếu.

## Bước 5: thiết lập theo phong cách người dùng

Từ đây làm việc trong xưởng vừa dựng, đường dẫn tính từ gốc xưởng. Làm bước 0 tới 3 của `skills/web-thiet-lap/SKILL.md`: cài môi trường (`tools/cai-dat.py`), phỏng vấn ba lượt về tên, chức danh, màu, giọng chữ, liên hệ, logo, rồi tạo một trang thử mang tên họ để duyệt bằng mắt.

Dấu hiệu xong: `python3 tools/cai-dat.py --trang-thai` báo "Tạo thử web: ĐẠT" và "Phong cách: đã thiết lập".

## Bước 6: bộ skill riêng cho tài khoản AI

Là bước 4 của `skills/web-thiet-lap/SKILL.md`: `python3 tools/dong-goi-skill.py` tạo bốn gói `xuong-web-*.zip` trong `Du an/_skill/`, mỗi gói mang khối cấu hình cá nhân và bản chụp phong cách của người dùng. Giải thích skill bằng lời thường, dẫn họ lưu vào tài khoản từng bước theo `skills/README.md`, rồi thử một câu để cùng thấy skill chạy.

Dấu hiệu xong: "ĐÓNG GÓI: ĐẠT", bốn tệp `.zip` trong `Du an/_skill/`, khối "Cấu hình cá nhân" trong các gói không còn "(chưa thiết lập)", và `--trang-thai` báo bước skill riêng đã xong (người dùng lưu ngay hay hẹn sau đều được).

## Bước 7: giới thiệu xưởng và bàn giao

Là bước 5 của `skills/web-thiet-lap/SKILL.md` (giới thiệu sáu chặng). Kết bằng: xưởng nằm ở đâu, các gói skill đã lưu chưa, câu đầu tiên để làm web thật, và câu "cập nhật xưởng" cho về sau.

Dấu hiệu xong: `--trang-thai` báo "Giới thiệu xưởng: đã", `python3 tools/ban-dung.py --kiem` ĐẠT, `python3 tools/kiem-sach.py` ĐẠT.

## Cập nhật về sau

Người dùng nói "cập nhật xưởng", "có bản mới không", hoặc bạn thấy `phienBan` trong `XUONG.json` cũ hơn bản vẽ:

1. `python3 tools/ban-dung.py --so-ban-ve`: liệt kê tệp mới, tệp bản vẽ đã đổi, tệp người dùng cũng đã sửa trong xưởng, tệp bản vẽ đã bỏ.
2. Đọc `CHANGELOG.md` của bản vẽ từ phiên bản trong `XUONG.json` tới bản mới. Kể cho người dùng bằng lời thường: điều gì mới, điều gì sẽ đổi trong xưởng, web đã làm có bị ảnh hưởng không (không: mỗi web giữ bản nền chung riêng).
3. Người dùng đồng ý: `python3 tools/ban-dung.py --doc-tho`. Tệp người dùng đã chủ ý sửa được giữ nguyên và báo ra; cùng họ quyết giữ bản của họ, lấy bản mới (`--ghi-de --chi <đường dẫn>`), hay trộn tay.
4. Tệp bản vẽ đã bỏ: hỏi người dùng; cần bỏ thì chuyển vào `Du an/_to_delete/`, không tự xoá.
5. Mẫu điểm vào đổi (`mau-xuong/`): đọc bản mới, trộn phần mới vào `CLAUDE.md`, `AGENTS.md` của xưởng, giữ phần riêng.
6. Bản khởi đầu `*.mau.*` đổi (ví dụ thêm chủ đề màu): so với bản của người dùng, thêm khoá mới mà không đổi giá trị họ đã đặt; `python3 tools/tuong-phan.py` ĐẠT.
7. Skill nguồn đổi: `python3 tools/dong-goi-skill.py`, hướng dẫn người dùng thay bản trên tài khoản (`skills/README.md`, mục thay bản cũ).
8. Kiểm: `python3 tools/ban-dung.py --kiem`, `python3 tools/kiem-tai-lieu.py`, `python3 tools/kiem-sach.py`, tạo thử một web và `tools/kiem-web.py`; ghi `phienBan`, `ngayCapNhat` mới vào `XUONG.json`.

Muốn một web cũ nhận bản nền chung mới: người dùng nói "cập nhật nền chung cho web <tên>"; bạn chép `he-thong/nen.css`, `he-thong/nen.js` vào web đó, kiểm lại bằng `tools/kiem-web.py` rồi mới để họ đưa lên.

## Gỡ rối

| Thấy | Thường do | Làm gì |
|---|---|---|
| `--doc-tho` báo lỗi mạng, 403, hết thời gian | nơi chạy lệnh bị chặn mạng tới `raw.githubusercontent.com` | chạy ở nơi có mạng (Cowork: sandbox đám mây) rồi chuyển tệp; hoặc nhờ người dùng mở quyền mạng cho ứng dụng |
| "vân tay không khớp bản vẽ" | bản vẽ vừa cập nhật giữa lúc đọc danh mục và lúc đọc tệp, hoặc mạng trung gian sửa nội dung | chờ vài phút, chạy lại `--doc-tho` (chỉ đọc tệp còn thiếu); vẫn lệch thì mở issue trên GitHub của bản vẽ |
| `--kiem` báo THIẾU sau khi chuyển tệp từ sandbox | chuyển thiếu một đợt, hoặc sai đường dẫn | chuyển nốt đúng đường dẫn, chạy lại `--kiem` |
| `kiem-tai-lieu.py` báo bảng skill thiếu trong CLAUDE.md | chưa viết `CLAUDE.md` từ `mau-xuong/` | làm bước 4 |
| Công cụ báo "DỪNG: thư mục này là bản vẽ" | đang chạy lệnh trong bản vẽ tải về | dựng xưởng ở thư mục khác |
| Người dùng gắn nhầm thư mục `xuong-web-ai` thay vì thư mục làm việc | `Web/`, `Du an/` phải nằm cạnh xưởng | nhờ gắn thư mục làm việc (thư mục cha) |
| Windows báo không có `python3` | Windows dùng lệnh `py` | thay `python3` bằng `py` |
| Tải gói skill lên tài khoản bị từ chối | mô tả dài, trùng tên, hoặc tài khoản chưa bật tính năng | `skills/README.md` mục gỡ rối |

---

Bản vẽ do nhà giáo dục Lương Dũng Nhân (ldn.edu.vn) tạo ra và chia sẻ miễn phí (`GHI-CONG.md`); mã theo MIT, tài liệu theo CC BY 4.0.

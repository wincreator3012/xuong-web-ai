# 05. Kỹ thuật: cấu trúc, hiệu năng, khả năng tiếp cận, tìm kiếm

Chuẩn kỹ thuật cho mọi web. Phần lớn đã có sẵn trong khuôn và `he-thong/`; cổng `tools/kiem-web.py` kiểm tự động phần kiểm được. Nguồn: nghien-cuu/D-loai-web-quy-trinh-chuan.md mục 3, 5.

## 1. Cấu trúc một web

```
Web/<ten-web>/            mã nguồn một web (về sau là một kho git riêng)
  public/                 PHẦN ĐƯA LÊN MẠNG, và chỉ phần này
    index.html, ...       trang
    assets/css/           tokens.css (màu, phông của web), nen.css (nền chung, không sửa), trang.css (chỉnh riêng)
    assets/js/            nen.js (nền chung), tệp riêng của web
    assets/fonts/         phông tự lưu trữ, chỉ họ đang dùng
    assets/img/           ảnh, logo, chia-se.jpg
    du-lieu/              dữ liệu công khai (JSON) cho trang tra cứu, trắc nghiệm
    _headers, robots.txt, sitemap.xml, 404.html, chinh-sach-bao-mat.html
  README.md               cách sửa web này, viết cho chủ web
  xuong.json              hồ sơ máy đọc (khuôn, chủ đề, nơi lưu trữ, tên miền)
  wrangler.jsonc | vercel.json | netlify.toml | firebase.json   cấu hình nơi lưu trữ (tools/dua-len.py tạo)
```

Web Astro: mã ở `src/`, tài sản ở `public/`, bản dựng ở `dist/` (đưa `dist/` lên). Web Firebase: thêm `firestore.rules`, `firestore.indexes.json`, `.firebaserc`, `KIEM-BAO-MAT.md` ở gốc (không trong `public/`).

Quy tắc: tên tệp chữ thường, không dấu, gạch nối (`bao-gia.html`); không gì riêng tư trong `public/` (ghi chú, dữ liệu gốc, tập lệnh, khoá). Bài học: nghien-cuu/E-bai-hoc-web-app.md.

## 2. HTML

- `<html lang="vi">`, `meta viewport` (không chặn phóng to), `<title>`, `meta description`, Open Graph (`og:title`, `og:description`, `og:image` tuyệt đối 1200x630, `og:url`, `og:locale` = `vi_VN`).
- Một `h1` mỗi trang; tiêu đề không nhảy bậc; vùng `header`, `main`, `footer`, `nav` đúng nghĩa; liên kết "Bỏ qua, tới nội dung".
- Mỗi ô nhập có `<label>`; nút là `<button>`, liên kết là `<a>`; không `div` bấm được.
- Dữ liệu có cấu trúc (JSON-LD) theo loại: Person/ProfilePage (hồ sơ), Event (sự kiện), Organization, Article (bài viết), Course khi phù hợp. Google không cần tệp hay schema riêng cho tìm kiếm AI; `llms.txt` không bắt buộc.
- JavaScript là lớp nâng cấp: trang vẫn đọc đủ khi JS không chạy (trừ công cụ tương tác, khi đó có `<noscript>` giải thích). Không gắn mã vào thuộc tính `onclick`, `onsubmit` (chính sách bảo mật nội dung chặn).

## 3. Hiệu năng (Core Web Vitals, phân vị 75)

| Chỉ số | Tốt | Thường hỏng vì |
|---|---|---|
| LCP (nội dung chính hiện) | dưới 2,5 giây | ảnh mở đầu nặng, phông chặn hiển thị |
| INP (độ nhạy khi tương tác) | dưới 200 ms | thư viện JS nặng (trang tĩnh gần như luôn đạt) |
| CLS (bố cục giật) | dưới 0,1 | ảnh thiếu `width` `height`, phông thay thế lệch cỡ |

Ngân sách: trang dưới 1,5 MB lần tải đầu, ảnh đơn dưới 350 KB, không thư viện JS khi JS thuần đủ. Phông `font-display: swap`, tách tệp con theo `unicode-range` (đã sẵn trong `fonts/`). Thư viện được phép qua CDN khi thật cần: Chart.js (biểu đồ), Fuse.js (tìm mờ), Firebase SDK (bậc 3).

## 4. Khả năng tiếp cận: WCAG 2.2 AA (ISO/IEC 40500:2025)

Sàn bắt buộc: tương phản chữ 4.5:1 (xưởng nâng chữ chính lên 7:1), thành phần giao diện 3:1; vùng bấm từ 24x24 px (xưởng dùng 44-48 px); phần tử đang chọn bằng bàn phím luôn nhìn thấy, không bị đầu trang dính hay nút nổi che; mọi thao tác kéo có cách làm bằng một lần chạm; kênh trợ giúp (Zalo, điện thoại) cùng vị trí ở mọi trang; không bắt nhập lại thông tin đã nhập; đăng nhập không bắt giải đố, cho dán mật khẩu.

Sáu lỗi phổ biến nhất trên web thế giới năm 2026 (WebAIM Million: tương phản thấp, ảnh thiếu alt, ô nhập thiếu nhãn, liên kết rỗng, nút rỗng, thiếu `lang`) đều do kiem-web bắt bằng axe-core. Máy chỉ bắt được một phần: Claude và người dùng thử thêm bằng phím Tab và trên điện thoại thật.

## 5. Tìm kiếm và chia sẻ

- `sitemap.xml` và `robots.txt` (`tools/dua-len.py --ten-mien` sinh và cập nhật; Astro tự sinh sitemap). Gửi sitemap trong Google Search Console sau khi lên mạng (huong-dan/11-do-luong-search-console.md).
- Trang gửi riêng (báo giá): `meta robots noindex`.
- Một địa chỉ chính thức mỗi trang (`canonical`); chọn một dạng tên miền (có hay không `www`), dạng kia chuyển hướng về.
- Zalo, Facebook đọc OG khi chia sẻ; sửa ảnh chia sẻ xong thì làm mới bộ đệm: developers.zalo.me/tools/debug-sharing, developers.facebook.com/tools/debug.

## 6. Bảo mật trang tĩnh

- Tệp `_headers` (Cloudflare, Netlify; Vercel và Firebase do `dua-len.py` chuyển thành cấu hình) đặt: HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, chống nhúng khung [frame-ancestors], và chính sách bảo mật nội dung [Content-Security-Policy] chỉ mở cho dịch vụ đang dùng (Web3Forms, Apps Script, VietQR, Cloudflare Analytics, Tally, YouTube, Cal.com). Thêm dịch vụ nhúng mới thì mở thêm đúng tên miền của nó.
- Liên kết mở tab mới có `rel="noopener"`. Dữ liệu người dùng hiện lại trên trang luôn qua `textContent`, không `innerHTML`.
- Không có gì cần giấu trong `public/`. Khoá bí mật chỉ ở biến môi trường phía máy chủ (chuan/06).

## 7. Môi trường chạy

- Web tĩnh: không cần cài gì; xem thử bằng `python3 tools/xem.py <web>`.
- Astro 7: Node.js 22.12 trở lên. Dặn trợ lý AI viết theo Astro 7 (docs.astro.build), vì dữ liệu huấn luyện của nhiều mô hình dừng ở Astro 4-5. Tắt đổi dấu tự động trong Markdown (`markdown.smartypants: false`, khuôn đã đặt) để giữ nháy thẳng và ba chấm gõ tay.
- Firebase: SDK bản module 12.x qua CDN gstatic, không cần bước dựng; công cụ dòng lệnh `firebase-tools` qua `npx`.

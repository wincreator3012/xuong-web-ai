# 03. Vercel: cho web cá nhân phi thương mại

Vercel dễ dùng nhất cho người mới, nhưng gói miễn phí Hobby **chỉ cho dùng phi thương mại**: web nhận thanh toán, quảng bá bán khoá học, dịch vụ, gắn quảng cáo đều bị coi là thương mại (vercel.com/docs/limits/fair-use-guidelines). Web như vậy đặt ở Cloudflare (thẻ 02), hoặc trả Vercel Pro (20 USD/tháng). Hobby không nối được kho thuộc tổ chức [organization] GitHub.

Cần: kho GitHub của web (thẻ 01), khoảng 15 phút.

## Bạn làm

1. Vào vercel.com/signup, chọn **Hobby**, đăng ký bằng **Continue with GitHub** (tiện nhất).
2. Claude đã tạo `vercel.json` (`python3 tools/dua-len.py <web> --noi vercel`: chỉ đưa `public/` hoặc `dist/` lên, kèm lớp bảo vệ HTTP), bạn đã Commit và Push.
3. **Add New...** > **Project** > **Import** cạnh kho của web (lần đầu cho phép Vercel đọc kho). **Framework Preset**: để **Other** (web tĩnh) hoặc **Astro** (Vercel tự nhận). Không sửa Build, Output (đã có trong vercel.json).
4. **Deploy**. Khoảng 30 giây sau có địa chỉ `<tên>.vercel.app`; gửi cho Claude.
5. Tên miền riêng: dự án > **Settings** > **Domains** > **Add**, nhập tên miền; Vercel hiện bản ghi cần thêm. Chép ĐÚNG giá trị trên màn hình (dự án mới có thể nhận IP khác `76.76.21.21`, CNAME dạng `cname.vercel-dns-0.com` hoặc giá trị riêng), làm theo thẻ 07.
6. Bật xác thực hai lớp: **Account Settings** > **Authentication**.

## Xong khi

- [ ] Web chạy ở vercel.app hoặc tên miền riêng, có HTTPS; Push thay đổi nhỏ thì tự cập nhật.

## Lỗi hay gặp

- Web hiện danh sách tệp hoặc lộ tệp ngoài `public/`: thiếu `vercel.json` (`outputDirectory`). Bài học từ web lập lịch cũ: nghien-cuu/E-bai-hoc-web-app.md.
- Vượt hạn mức Hobby: web tạm dừng (lỗi 503), không bị tính tiền.

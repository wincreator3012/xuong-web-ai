# 12. Làm web cho người khác: quyền sở hữu và bàn giao

Khi bạn (hoặc Claude cùng bạn) làm web cho một người, một tổ chức khác, mọi thứ thuộc về họ ngay từ đầu. Bạn là người được mời vào làm, không phải chủ. Cách này bảo vệ cả hai phía: họ không bị "giữ" tài khoản, bạn không phải chịu trách nhiệm dữ liệu của họ.

## Ngay từ đầu

1. Khách tự tạo email chủ, bật xác thực hai lớp (thẻ 00).
2. Khách tự mua tên miền, đứng tên họ, thanh toán bằng thẻ của họ (thẻ 06). Với .vn, thông tin chủ thể phải đúng người thật.
3. Khách tạo tài khoản GitHub (hoặc tổ chức GitHub), nơi lưu trữ, dịch vụ form, rồi mời bạn làm cộng tác viên [collaborator, member]. Lưu ý: Vercel Hobby không nối kho của tổ chức GitHub và cấm thương mại.
4. Dữ liệu người dùng (danh sách đăng ký) thuộc khách với tư cách bên kiểm soát dữ liệu; bạn là bên xử lý, chỉ dùng theo thoả thuận.
5. Hợp đồng ghi rõ: quyền sở hữu mã nguồn, thiết kế, nội dung, hình ảnh chuyển cho khách khi thanh toán xong; danh sách tài khoản và quyền bàn giao; ai cập nhật web về sau.

## Buổi bàn giao (30 phút, cùng khách)

1. Khách tự đăng nhập từng tài khoản trong VAN-HANH.md, xác nhận mình là chủ, xác thực hai lớp bật, mã khôi phục đã cất.
2. Khách xem web trên điện thoại của họ, gửi thử form, quét thử mã QR.
3. Trao `README.md` của web (cách sửa) và danh sách chỗ `SỬA Ở ĐÂY` (`tools/kiem-web.py` liệt kê trong báo cáo).
4. Hướng dẫn khách cách nhờ trợ lý AI sửa web (mở thư mục web, nói điều cần đổi), hoặc cách sửa bằng Pages CMS nếu có.
5. Gỡ quyền của bạn ở những dịch vụ không còn cần (hoặc giữ quyền theo hợp đồng bảo trì).
6. Ghi biên bản bàn giao vào VAN-HANH.md: ngày, những gì đã bàn giao, ai giữ gì.

## Xong khi

- [ ] Khách đăng nhập được mọi tài khoản bằng email của họ; không tài khoản nào đứng tên bạn.
- [ ] Khách tự sửa được một dòng chữ và thấy web cập nhật.

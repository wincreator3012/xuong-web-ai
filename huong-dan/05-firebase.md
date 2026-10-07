# 05. Firebase: đăng nhập Google, dữ liệu, đưa web-app lên

Cho web-app bậc 3 (khuôn `app-firebase`): người dùng đăng nhập bằng Google, mỗi người có dữ liệu riêng, quản trị xem tổng hợp. Gói Spark miễn phí, không cần thẻ. Đọc trước chuan/06-du-lieu-bao-mat.md mục 3.

Cần: tài khoản Google (email chủ), máy Mac hoặc Windows có Node.js 22 (để chạy lệnh đưa lên; Claude hướng dẫn cài nếu thiếu), khoảng 45 phút.

## Bạn làm: tạo dự án

1. Vào console.firebase.google.com > **Create a project** [Tạo dự án] > đặt tên (ví dụ `so-ghi-chep-lop-a`). Google Analytics: tắt nếu không cần (bớt cookie, bớt nghĩa vụ đồng ý). Chờ tạo xong.
2. **Build** > **Authentication** > **Get started** > tab **Sign-in method** > **Google** > bật **Enable**, chọn email hỗ trợ > **Save**.
3. **Build** > **Firestore Database** > **Create database** > vị trí `asia-southeast1 (Singapore)` (gần Việt Nam nhất; không đổi được về sau) > chọn **production mode** [chế độ chính thức: cấm hết, luật của xưởng mở đúng phần cần] > **Create**.
4. Biểu tượng bánh răng > **Project settings** > **General** > phần **Your apps** > biểu tượng web `</>` > đặt tên ứng dụng > **Register app**. Màn hình hiện một khối `firebaseConfig`: chép gửi Claude (các giá trị này công khai theo thiết kế của Firebase, dán vào chat được). Claude điền vào `public/assets/js/firebase-cau-hinh.js`.
5. Không tải, không gửi ai tệp **service account key** (Project settings > Service accounts > Generate new private key): web-app của xưởng không cần nó. Đã lỡ tải: cất ngoài thư mục web, xoá khoá đó trong Google Cloud Console nếu từng gửi đi.

## Bạn làm: đưa lên (một lần đăng nhập, sau đó một lệnh)

Mở Terminal (Mac: Spotlight gõ Terminal; Windows: PowerShell) tại thư mục web (Claude đưa sẵn lệnh `cd` đúng đường dẫn), chạy lần lượt:

```bash
npx firebase-tools login                 # mở trình duyệt, đăng nhập email chủ, cho phép
npx firebase-tools use --add             # chọn dự án vừa tạo, đặt bí danh: default
npx firebase-tools deploy                # đưa luật Firestore, chỉ mục và thư mục public/ lên
```

Xong, web chạy ở `https://<mã-dự-án>.web.app`. Các lần sau chỉ cần lệnh cuối (hoặc nhờ Claude nhắc).

## Bạn làm: quản trị và tên miền

1. Quản trị: **Firestore Database** > **Start collection** > Collection ID `quanTri` > Document ID là email Google của người quản trị (chính xác từng chữ) > thêm trường `vaiTro` = `quanTri` > **Save**. Người đó đăng nhập lại sẽ thấy khối Quản trị. Bỏ quyền: xoá tài liệu đó.
2. **Authentication** > **Settings** > **Authorized domains**: chỉ giữ `localhost`, `<mã>.web.app`, `<mã>.firebaseapp.com` và tên miền thật của bạn.
3. Tên miền riêng: **Hosting** > **Add custom domain** > làm theo màn hình (bản ghi TXT xác minh `hosting-site=...` phải giữ vĩnh viễn, bản ghi A riêng của dự án); SSL có thể mất tới 24 giờ.

## Claude làm

- Viết và giải thích luật `firestore.rules` trước giao diện; chạy `tools/kiem-web.py <web> --len`.
- Hướng dẫn bạn làm `KIEM-BAO-MAT.md` (thử bằng hai tài khoản) trước khi mời người dùng thật.

## Khi cần gói Blaze (có thẻ)

Lưu ảnh người dùng tải lên (Cloud Storage), gửi thư tự động, chấm điểm ở máy chủ (Cloud Functions) cần Blaze. Khi nâng: **Usage and billing** > đặt **budget alert** [cảnh báo ngân sách] và giới hạn chi; cảnh báo không tự dừng dịch vụ.

## Lỗi hay gặp

- Bấm đăng nhập không có gì xảy ra trong Zalo, Facebook: trình duyệt nhúng bị Google chặn; khuôn đã hiện hướng dẫn mở bằng Chrome, Safari.
- `permission-denied` khi dùng: luật chặn đúng như thiết kế hoặc dữ liệu ghi thiếu trường; gửi Claude dòng lỗi.
- `The query requires an index`: chạy lại `npx firebase-tools deploy` (tệp `firestore.indexes.json` có sẵn chỉ mục cần), chờ vài phút.

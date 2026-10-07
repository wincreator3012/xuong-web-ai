// Cấu hình Firebase của web: dán từ Firebase Console > Project settings > Your apps > Web app (huong-dan/05-firebase.md).
// Các giá trị này CÔNG KHAI theo thiết kế của Firebase (ai mở trang cũng thấy); dữ liệu được bảo vệ bằng firestore.rules,
// không phải bằng việc giấu cấu hình. KHÔNG BAO GIỜ dán vào đây khoá tài khoản dịch vụ (tệp .json có "private_key").
export const cauHinhFirebase = {
  apiKey: '[[apiKey]]',
  authDomain: '[[ma-du-an]].firebaseapp.com',
  projectId: '[[ma-du-an]]',
  appId: '[[appId]]',
};

#!/bin/bash
# XEM WEB: mở web bạn đang làm trên trình duyệt của máy này, đúng như khi lên mạng.
# Cách dùng: mở thư mục repo trong Finder, bấm đúp tệp này. Giữ cửa sổ mở trong lúc xem; đóng cửa sổ là dừng.
# Lần đầu Mac chặn: bấm Done [Xong], mở System Settings > Privacy & Security, kéo xuống bấm Open Anyway, nhập mật khẩu máy (một lần).
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1
if ! command -v python3 >/dev/null 2>&1; then
  echo "Chưa có Python 3. Mở Terminal, gõ: xcode-select --install (hoặc cài từ https://www.python.org/downloads/), rồi bấm đúp lại tệp này."
  read -r -p "Bấm Enter để đóng."
  exit 1
fi
python3 tools/xem.py "$@"
read -r -p "Đã dừng. Bấm Enter để đóng."

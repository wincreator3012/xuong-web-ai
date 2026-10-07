@echo off
chcp 65001 >nul
rem XEM WEB: mở web bạn đang làm trên trình duyệt của máy này, đúng như khi lên mạng.
rem Cách dùng: mở thư mục repo trong File Explorer, bấm đúp tệp này. Giữ cửa sổ mở trong lúc xem; đóng cửa sổ là dừng.
rem Windows hỏi "Windows protected your PC": bấm "More info" rồi "Run anyway" (một lần).
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
set PYTHONUTF8=1
set PY=
where py >nul 2>nul && set PY=py -3
if not defined PY where python >nul 2>nul && set PY=python
if not defined PY (
  echo Chua co Python 3. Cai tu https://www.python.org/downloads/ , nho danh dau "Add python.exe to PATH", roi bam dup lai tep nay.
  pause
  exit /b 1
)
%PY% tools\xem.py %*
pause

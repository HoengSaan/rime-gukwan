@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:: 設定 OpenCC 相對路徑
set OPENCC_DIR=%~dp0OpenCC
set OPENCC_BIN=%OPENCC_DIR%\bin\opencc.exe
set CONFIG_PATH=%OPENCC_DIR%\share\opencc\

:: 設定文件夾
set INPUT_FOLDER=%~dp0Dict_Removed
set OUTPUT_FOLDER=%~dp0Dict_Converted

:: 創建輸出文件夾
if not exist "%OUTPUT_FOLDER%" mkdir "%OUTPUT_FOLDER%"

:: 檢查removed中是否有文件
echo.
echo 檢查 'Dict_Removed' 文件夾...
set FILE_FOUND=
for %%F in ("%INPUT_FOLDER%\*.yaml") do (
    echo - %%~nxF
    set FILE_FOUND=1
)

if not defined FILE_FOUND (
    echo 未在 'Dict_Removed' 找到可處理詞庫！
    echo 請將詞庫文件放於 'Dict_Removed' 文件夾。
    pause
    exit /b
)

echo.
set /p choice=是否進行繁簡轉換？(y/n): 
if /I "%choice%" NEQ "y" (
    echo 已取消，腳本退出。
    pause
    exit /b
)

echo.
echo 可用配置文件（簡轉繁建議使用t2s.json）：
echo s2t.json - 簡體到繁體
echo t2s.json - 繁體到簡體
echo s2tw.json - 簡體到臺灣正體
echo tw2s.json - 臺灣正體到簡體
echo s2hk.json - 簡體到香港繁體
echo hk2s.json - 香港繁體到簡體
echo s2twp.json - 簡體到繁體（臺灣正體）並轉換爲臺灣常用詞彙
echo tw2sp.json - 繁體（臺灣正體）到簡體並轉換爲中國大陸常用詞彙
echo t2tw.json - 繁體（OpenCC 標準）到臺灣正體
echo hk2t.json - 香港繁體到繁體（OpenCC 標準）
echo t2hk.json - 繁體（OpenCC 標準）到香港繁體
echo t2jp.json - 繁體（OpenCC 標準）到日問新字體
echo jp2t.json - 日文新字體到繁體（OpenCC 標準）
echo tw2t.json - 臺灣正體到繁體（OpenCC 標準）
echo.

set /p CONFIG_FILE=請輸入轉換標準（如: s2t.json）: 

if not exist "%CONFIG_PATH%%CONFIG_FILE%" (
    echo 無法找到配置文件 '%CONFIG_FILE%'，請檢查輸入是否正確！
    pause
    exit /b
)

if not exist "%OPENCC_BIN%" (
    echo 無法找到 OpenCC！請確保其位於 '%OPENCC_DIR%'.
    pause
    exit /b
)

:: 執行 OpenCC 轉換所有文件
echo.
echo 開始轉換...
for %%F in ("%INPUT_FOLDER%\*.yaml") do (
    "%OPENCC_BIN%" -i "%%F" -o "%OUTPUT_FOLDER%\%%~nxF" -c "%CONFIG_PATH%%CONFIG_FILE%"
    echo 已轉換: %%~nxF
)

echo.
echo ✅ 所有詞庫已轉換完成！請查看 'Dict_Converted' 文件夾。
pause

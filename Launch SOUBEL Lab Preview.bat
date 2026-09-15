@echo off
setlocal
cd /d "%~dp0"
echo Starting SOUBEL local preview...
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -NoExit -File "%~dp0tools\preview-soubel-lab.ps1"
echo.
echo The preview process ended.
pause

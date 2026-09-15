@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\preview-soubel-lab.ps1"
if errorlevel 1 (
  echo.
  echo SOUBEL Lab preview could not start.
  pause
)

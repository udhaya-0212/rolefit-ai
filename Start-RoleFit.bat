@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 rolefit_server.py
) else (
  python rolefit_server.py
)
if errorlevel 1 pause

@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 goto use_python
py -3 stash_batch.py stats %*
exit /b %errorlevel%
:use_python
where python >nul 2>nul
if errorlevel 1 goto missing
python stash_batch.py stats %*
exit /b %errorlevel%
:missing
echo Python 3.10 or newer is required. Install Python and reopen CMD.
exit /b 1

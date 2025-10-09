@echo off
title HTML Project Offline Server
color 0A

echo.
echo ========================================
echo    HTML Project Offline Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH!
    echo.
    echo 💡 To install Python:
    echo    1. Go to https://www.python.org/downloads/
    echo    2. Download and install Python
    echo    3. Make sure to check "Add Python to PATH" during installation
    echo.
    echo 🔄 After installing Python, run this file again.
    echo.
    pause
    exit /b 1
)

echo ✅ Python found! Starting server...
echo.

REM Start the Python server
python start_server.py

echo.
echo 🛑 Server stopped.
pause

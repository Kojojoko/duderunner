@echo off
echo Starting local game server...
echo Please ensure Python is installed and in your PATH.
echo Opening browser...
start http://localhost:8000
python -m http.server 8000
pause

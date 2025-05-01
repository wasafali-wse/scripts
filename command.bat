@echo off
cd C:\database\script
echo It's time to back up the data!
python back_script.py

if %ERRORLEVEL% neq 0 (
    echo Backup failed with error code %ERRORLEVEL%!
    pause
    exit /b %ERRORLEVEL%
)

echo Wow done, wohoo!
pause
@echo off
echo Installing requirements for InoKit Tray Application...
pip install -r tray_requirements.txt

echo Creating desktop shortcut...
set SCRIPT="%TEMP%\create_shortcut.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") > %SCRIPT%
echo sLinkFile = oWS.ExpandEnvironmentStrings("%USERPROFILE%\Desktop\InoKit Server.lnk") >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%~dp0start_tray.bat" >> %SCRIPT%
echo oLink.IconLocation = "%~dp0static\images\logos\logo.jpg" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%

echo Setup complete! You can now use the desktop shortcut to start the InoKit server. 
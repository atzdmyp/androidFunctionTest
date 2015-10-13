::get current path
@echo off  
setlocal EnableDelayedExpansion 
set currentPath = !cd! 

::To determine whether to exist *.apk
if exist *.apk goto A
echo not exist
goto end

:A
echo exist
::To determine whether to port in use
set b = str
set b = %b:str=&tasklist|findstr "5073"&
set count = 0
:getCount
if not defined b
goto unUse
echo %b%

set a = deviceName
set a = %a:deviceName=&adb devices&
echo %a%
::To determine whether to connect mobile 
goto end

:unUse
echo not in use
goto end

:end
echo the end
pause 
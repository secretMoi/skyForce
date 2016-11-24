@echo off

set currentpath=%~dp0

cd A:\Programme\Python\

:flag

python %currentpath%\skyForce.py

pause

goto flag
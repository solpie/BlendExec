@echo off
pyinstaller .\BlendExec.py -F
cd .\web_gui\eleme\
npm run build
cd ..\..


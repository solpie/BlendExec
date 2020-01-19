echo "copy eleme dist"
xcopy .\web_gui\eleme\dist\*.* .\dist\assets\ /s /e /c /y /h /r
xcopy .\assets\*.* .\dist\assets\ /s /e /c /y /h /r
echo "copy bpy_scripts"
xcopy .\bpy_scripts\*.* .\dist\bpy_scripts\ /s /e /c /y /h /r

@ECHO OFF
ECHO Start building...
ECHO Building English version......
pyinstaller main.spec
ECHO Building Chinese (Simp) version......
pyinstaller main-zhs.spec
CD dist
xcopy /s .\main-zhs\main-zhs.exe .\main
xcopy /s .\main-zhs\main-zhs.exe.manifest .\main
RMDIR /S /Q .\main-zhs
REN "main" "CJK-character-count-v0.10"
ECHO Build done!
EXIT
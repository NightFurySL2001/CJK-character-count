@ECHO OFF
ECHO Start building...
ECHO Building English version......
pyinstaller main.spec
ECHO Building Chinese (Simp) version......
pyinstaller main-zhs.spec
ECHO Building Chinese (Trad) version......
pyinstaller main-zht.spec
CD dist
ECHO Combining files......
:: copy everything into zht folder as zht need extra GUI font
xcopy /s .\main\main.exe .\main-zht
xcopy /s .\main\main.exe.manifest .\main-zht
xcopy /s .\main-zhs\main-zhs.exe .\main-zht
xcopy /s .\main-zhs\main-zhs.exe.manifest .\main-zht
ECHO Deleting redundant file......
RMDIR /S /Q .\main
RMDIR /S /Q .\main-zhs
REN "main-zht" "CJK-character-count-vX.XX"
ECHO Build done!
ECHO Press Enter to exit.
PAUSE >nul
EXIT
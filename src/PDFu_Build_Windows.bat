@echo off
cd /d "%~dp0"

uv run pyinstaller ^
    --windowed ^
    --onedir ^
    --name="PDFu" ^
    --clean ^
    --icon=icon.ico ^
    --add-data "assets;assets" ^
    --add-data "icon.png;." ^
    --add-data "proxy.json;." ^
    --hidden-import PySide6.QtSvg ^
    --collect-all pdf2docx ^
    --collect-all fitz ^
    --noconfirm ^
    main.py

echo.
echo Build concluido. Saida em: dist\PDFu\
pause

pyinstaller --onefile --console --clean --name "Image_PDF_converter" main.py
rmdir /S /Q build
move dist\Image_PDF_converter.exe Image_PDF_converter.exe
rmdir /S /Q dist
del /S /Q Image_PDF_converter.spec
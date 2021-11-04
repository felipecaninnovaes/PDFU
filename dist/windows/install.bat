md "C:\Program Files\pdfuni"
cd "C:\Program Files\pdfuni"

curl -L https://github.com/felipecaninnovaes/pdfuni/blob/main/pdfuni.exe?raw=true -o pdfuni.exe
curl -L https://raw.githubusercontent.com/felipecaninnovaes/pdfuni/main/pdfuni.reg -o pdfuni.reg
curl -L https://raw.githubusercontent.com/felipecaninnovaes/pdfuni/main/pdfuni.ico -o pdfuni.ico

pdfuni.reg

del pdfuni.reg
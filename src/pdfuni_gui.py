import sys
import os
from glob import glob
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout, QFileDialog, QMessageBox


class PDFUni(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        self.setWindowTitle('Clique no Salvar')

        layout = QVBoxLayout()

        n = 1

        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(n)
        layout.addWidget(self.progressBar)

        self.button = QPushButton('Salvar')
        self.button.setStyleSheet('font-size: 30px; height: 30px;')
        self.button.clicked.connect(lambda status, n_size=n: self.run(n_size))

        layout.addWidget(self.button)
        self.setLayout(layout)

    def run(self, n):
        for i in range(n):
            pdf_merge()
            self.progressBar.setValue(i+1)
            QMessageBox.about(display, "Completo", "Aquivo Gerado com Sucesso")    
        sys.exit(app.exec_())


def pdf_merge():
    file_name = QFileDialog.getSaveFileName()[0]
    file_name = file_name.replace(".pdf", "")
    file_name = file_name.replace(".PDF", "")
    if os.path.exists(file_name + ".pdf"):
        os.remove(file_name + ".pdf")
    else:
        print("Gen New File")
    ##Merge pdf  
    merger = PdfFileMerger()
    allpdfs = [a for a in glob("*.pdf")]
    [merger.append(pdf) for pdf in allpdfs]
    with open(file_name + ".pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    display = PDFUni()
    display.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

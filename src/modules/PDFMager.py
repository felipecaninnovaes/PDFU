#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.1
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import platform, os
from glob import glob
from PyPDF2 import PdfFileMerger

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PDFMarge(object):
    def pdf_merge(self, file_save_name, folder):
        if os.path.exists(file_save_name + ".pdf"):
            os.remove(file_save_name + ".pdf")
        else:
            print("Gen New File")
        if platform.system() == "Windows":
            folder_location = (folder + "\*.pdf")
        else:
            folder_location = (folder + "/*.pdf")
        # Merge pdf
        merger = PdfFileMerger()
        allpdfs = [a for a in glob(folder_location)]
        [merger.append(pdf) for pdf in allpdfs]
        with open(file_save_name + ".pdf", "wb") as new_file:
            
            merger.write(new_file)
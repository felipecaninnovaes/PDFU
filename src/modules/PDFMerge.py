#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.5
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
from pikepdf import Pdf
from glob import glob

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PDFMerge(object):
    def pdf_merge(self, file_save_name, folder):
        if os.path.exists(file_save_name + ".pdf"):
            os.remove(file_save_name + ".pdf")
        elif os.path.exists(file_save_name + ".PDF"):
            os.remove(file_save_name + ".PDF")
        else:
            print("Genereted a New File")
        if platform.system() == "Windows":
            folder_location = (folder + "\*.pdf")
        else:
            folder_location = (folder + "/*.pdf")
        pdf = Pdf.new()

        version = pdf.pdf_version

        for file in glob(folder_location):
            src = Pdf.open(file)
            version = max(version, src.pdf_version)
            pdf.pages.extend(src.pages)


        pdf.remove_unreferenced_resources()
        pdf.save(file_save_name + ".pdf", min_version=version)
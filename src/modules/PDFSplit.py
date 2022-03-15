#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.4
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

class PDFSplit(object):
    def pdf_split(self, file_save_name, file_name):
        pdf = Pdf.open(file_name)

        for n, page in enumerate(pdf.pages):
            dst = Pdf.new()
            dst.pages.append(page)
            dst.save(file_save_name +' '+ f'{n:02d}.pdf')
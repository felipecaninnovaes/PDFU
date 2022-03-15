#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.3
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

from pdf2docx import Converter

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PDFDocx(object):
    def pdf_docx(self, file_save_name, file_name):
        cv = Converter(file_name)
        cv.convert(file_save_name)      
        cv.close()
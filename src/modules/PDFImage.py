#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.9
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

import img2pdf, os
from PIL import Image

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class PDFImage(object):
    def pdf_image(self, file_save_name, file_name):
        if os.path.exists(file_save_name + ".pdf"):
            os.remove(file_save_name + ".pdf")
        elif os.path.exists(file_save_name + ".PDF"):
            os.remove(file_save_name + ".PDF")
        else:
            print("Genereted a New File")
        image_file = Image.open(file_name)
        pdf_bytes = img2pdf.convert(image_file.filename)
        file_save_name = file_save_name + ".pdf"
        file = open(file_save_name, "wb")
        file.write(pdf_bytes)
        image_file.close()
        file.close()
        # output
        print("Successfully made pdf file")
        print(file_save_name)

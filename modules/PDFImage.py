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

# THIS FUNCTION NOT IMPLEMENTED IN CODE

import img2pdf
from PIL import Image
import os
from qt_core import *


class PDFImage(object):
    def pdf_image(self, file_name, folder):
    
		# # storing image path
		# file_name = "C:/Users/Admin/Desktop/GfG_images/do_nawab.png"
		
		# # storing pdf path
		# folder = "C:/Users/Admin/Desktop/GfG_images/file.pdf"
  
  
		image_file = Image.open(file_name)
		pdf_bytes = img2pdf.convert(image_file.filename)
		file = open(folder, "wb")
		file.write(pdf_bytes)
		image_file.close()
		file.close()
		
		# output
		print("Successfully made pdf file")
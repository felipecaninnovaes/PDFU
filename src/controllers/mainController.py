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

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
msg = ""

class mainController():
    def fileNameSave(lineEdit, extension):
        global file_save_name 
        extension = str((extension))
        lower = extension.lower()
        upper = extension.upper()
        file_save_name = ""
        file_save_name = QFileDialog.getSaveFileName()[0]
        file_save_name = file_save_name.replace(upper, "")
        file_save_name = file_save_name.replace(lower, "")
        lineEdit.setText(QApplication.translate(
            "Ui_application_pages", file_save_name + extension))
        return(file_save_name)
       
    def folderLocation(lineEdit):
        global folder
        folder = ""
        folder = QFileDialog.getExistingDirectory()
        lineEdit.setText(QApplication.translate("Ui_application_pages", folder))
        return(folder)
    
    def itemFileLocation(lineEdit):
        global file_name
        file_name = ""
        file_name = QFileDialog.getOpenFileName()[0]
        lineEdit.setText(QApplication.translate("Ui_application_pages", file_name))
        return(file_name)
    
    def menssagen(extension, title, text):
            global msg
            msg = QMessageBox()
            extension = str((extension))
            title = str((title))
            text = str((text))
            if extension == "":
                msg.setWindowTitle(title)
                msg.setText(text)
                msg.show()
            else:
                msg.setWindowTitle(title)
                msg.setText(text + file_save_name + extension)
                msg.show()
            
    def cleanV(lineEdit1, lineEdit2):
        global file_name, file_save_name, folder
        lineEdit1.setText(QApplication.translate("Ui_application_pages", ""))
        lineEdit2.setText(QApplication.translate("Ui_application_pages", ""))
        file_save_name = ""
        file_name = ""
        folder = ""
    
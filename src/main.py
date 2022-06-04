#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.7
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


# IMPORT MODULES    
import sys

# IMPORT QT CORE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#Updater software
from modules.Updater import PDFUpdater
# IMPORT MAIN WINDOW
from windows.main_window.ui_main_windown import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        PDFUpdater.pdf_updater(self, '1.0.7')
        
        self.setWindowTitle("PDFU")
        
        # SETUP
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
           
        #TOGGLE BUTTOn
        self.ui.toggle_button.clicked.connect(self.toggle_button)
           
        
        # Button home
        self.ui.home_button.clicked.connect(self.show_page_1) 
        # Btn widgets
        self.ui.imageconv_button.clicked.connect(self.show_page_2)
        
        self.ui.div_button.clicked.connect(self.show_page_3)
        
        self.ui.docx_button.clicked.connect(self.show_page_4)
        # SHOW APPLICATION
        self.show()

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    # Btn home function
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.home_button.set_active(True)    
    
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.imageconv_button.set_active(True)  

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.div_button.set_active(True)    

    def show_page_4(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.docx_button.set_active(True)  
        
    def toggle_button(self):
        menu_width = self.ui.left_menu.width()
        
        # check width
        width = 50
        if menu_width == 50:
            width = 240 
            
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setWindowIcon(QIcon('icon.png'))
    sys.exit(app.exec())
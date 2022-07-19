#///////////////////////////////////////////////////////////////
#
# BY: FELIPE CANIN NOVAES
# PROJECT MADE WITH: PDFU
# V: 1.0.8
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
import multiprocessing
from multiprocessing.dummy import freeze_support
import sys, json

# IMPORT QT CORE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#Updater software
from modules.Updater import PDFUpdater
# IMPORT MAIN WINDOW
from windows.main_window.ui_main_windown import *

version = '1.0.8'


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            proxy = open('proxy.json', 'r+')
        except FileNotFoundError:
            proxy = open('proxy.json', 'w+')
            proxy.writelines(u'{' +"\n")
            proxy.writelines(u'"enable": "1",' +"\n")
            proxy.writelines(u'"proxy_ip": "0",' +"\n")
            proxy.writelines(u'"proxy_port": "0",' +"\n")
            proxy.writelines(u'"proxy_user": "",' +"\n")
            proxy.writelines(u'"proxy_password": ""' +"\n")
            proxy.writelines(u'}' +"\n")
            proxy = open('proxy.json')
        
        data = json.load(proxy)
        enable = data['enable']
        if enable == '1':
            PDFUpdater.pdf_updater(self, version)
        elif enable == '0':
            print('Disable updater')
        
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
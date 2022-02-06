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


# IMPORT QT CORE
from shiboken6.Shiboken import Object
from qt_core import *

import os

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages
from modules.pdfunify import PDFUni


# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

# MAIN WINDOW
class UI_MainWindow(QWidget):
    
    
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        # INITIAL PARAMETERS

        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)
        parent.setMaximumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #E74856")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # LEFT MENU LAYOUT 
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        
        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
                
        # TOP BTNS
        self.toggle_button = PyPushButton(
            text = "Ocultar menu",
            icon_path = "toggle.svg"
        )      
        
        
        self.home_button = PyPushButton(
            text = "Juntar PDF",
            is_active = True,
            icon_path = "icon_home.svg"
        )
        
        self.imageconv_button = PyPushButton(
            text = "Converter para PDF",
            is_active = False,
            icon_path = "icon_imageconv.svg"
        )
        
        # ADD BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.home_button)
        self.left_menu_top_layout.addWidget(self.imageconv_button)
        
        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # BOTTOm FRAME MENU 
        
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        #BOTTOm BUTTONS
        self.setting_button = QPushButton("Settings")
        
        self.left_menu_bottom_layout.addWidget(self.setting_button)
        
        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.1")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #DED5DE")
        
        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #f5f5f5")
        
        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #DED5DE; color: #000000")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        # TOP LEFT LABEL
        self.top_label_left = QLabel("PDFUtily")
        
        # TOP SPACER
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # TOP RIGHT LABEL
        self.top_label_right = QLabel("| PAGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt")
        
        # ADD TO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        # APPLICATION PAGES
             
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color:#f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        global ui_pages
        self.ui_pages.pushButton.clicked.connect(file_save) 
        self.ui_pages.pushButton_2.clicked.connect(folder_location) 
        self.ui_pages.pushButton_3.clicked.connect(clicked) 
        
        global line_edit, line_edit_2
        line_edit = self.ui_pages.lineEdit
        line_edit_2 = self.ui_pages.lineEdit_2
        global msg
        msg = QMessageBox()
        # self.ui_pages.lineEdit.setText(QApplication.translate("Ui_application_pages", ""))
        
        # BOTTOm BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #DED5DE; color: #000000")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)
        
        # BOTTOm LEFT LABEL
        self.bottom_label_left = QLabel("Criado por: Felipe C. Novaes")
        
        # BOTTOm SPACER
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # BOTTOm RIGHT LABEL
        self.bottom_label_right = QLabel("© 2022")
        self.bottom_label_right.setStyleSheet("font: 700 9pt")
        
        # ADD TO LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        
        # ADD CONETENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        # ADD WIDGETS TO APP 
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)

def clicked(self):
    global file_name, folder, msg
    PDFUni.pdf_merge(self, file_name, folder)
    msg.setWindowTitle("Secesso") 
    msg.setText("Arquivo Gerado com sucesso em: " + file_name)
    msg.show()
    line_edit.setText(QApplication.translate("Ui_application_pages", ""))
    line_edit_2.setText(QApplication.translate("Ui_application_pages", ""))
    file_name = ""
    folder = ""
    

def file_save(self):   
    global file_name
    file_name = ""
    file_name = QFileDialog.getSaveFileName()[0]
    file_name = file_name.replace(".pdf", "")
    file_name = file_name.replace(".PDF", "")     
    line_edit.setText(QApplication.translate("Ui_application_pages", file_name + ".pdf"))
    
def folder_location(self):
    global folder
    folder = ""
    folder = QFileDialog.getExistingDirectory()
    line_edit_2.setText(QApplication.translate("Ui_application_pages", folder))

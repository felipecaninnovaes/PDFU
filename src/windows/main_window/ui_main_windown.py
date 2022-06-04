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

# IMPORT QT CORE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


#Updater software
from modules.Updater import PDFUpdater

# IMPORT PAGES
from pages.ui_pages import Ui_application_pages
from modules.PDFMerge import PDFMerge
from modules.PDFImage import PDFImage
from modules.PDFSplit import PDFSplit
from modules.PDFDocx import PDFDocx
from controllers.mainController import *

file_save_name = ""
file_name = ""
# IMPORT CUSTOM WIDGETS
from widgets.py_push_button import PyPushButton

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
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #FF4742")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BTNS
        self.toggle_button = PyPushButton(
            text="Ocultar menu",
            icon_path="toggle.svg"
        )
    
        self.home_button = PyPushButton(
            text="Juntar PDF",
            is_active=True,
            icon_path="icon_home.svg"
        )

        self.imageconv_button = PyPushButton(
            text="Converter para PDF",
            is_active=False,
            icon_path="icon_imageconv.svg"
        )
        self.div_button = PyPushButton(
            text="Dividir PDF",
            is_active=False,
            icon_path="icon_split.svg"
        )
        self.docx_button = PyPushButton(
            text="PDF para Word (Beta)",
            is_active=False,
            icon_path="icon_docx.svg"
        )

        # ADD BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.home_button)
        self.left_menu_top_layout.addWidget(self.imageconv_button)
        self.left_menu_top_layout.addWidget(self.div_button)
        self.left_menu_top_layout.addWidget(self.docx_button)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOm FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.7")
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
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #DED5DE; color: #000000")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # TOP LEFT LABEL
        self.top_label_left = QLabel("PDFUtily")

        # TOP SPACER
        self.top_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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


        # BOTTOm BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet(
            "background-color: #DED5DE; color: #000000")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # BOTTOm LEFT LABEL
        self.bottom_label_left = QLabel("Criado por: Felipe C. Novaes")

        # BOTTOm SPACER
        self.bottom_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

#==============================================VARIABLES AND FUNCTIONS==============================================================#
        
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        global ui_pages

        global line_edit, line_edit_2, line_edit_3, line_edit_4, line_edit_5, line_edit_6, line_edit_7, line_edit_8
        global push_button3, push_button6, push_button9, push_button12
        
        line_edit = self.ui_pages.lineEdit
        line_edit_2 = self.ui_pages.lineEdit_2
        line_edit_3 = self.ui_pages.lineEdit_3
        line_edit_4 = self.ui_pages.lineEdit_4
        line_edit_5 = self.ui_pages.lineEdit_5
        line_edit_6 = self.ui_pages.lineEdit_6
        line_edit_7 = self.ui_pages.lineEdit_7
        line_edit_8 = self.ui_pages.lineEdit_8
        
        push_button3 = self.ui_pages.pushButton_3
        push_button6 = self.ui_pages.pushButton_6
        push_button9 = self.ui_pages.pushButton_9
        push_button12 = self.ui_pages.pushButton_12
      
        
        self.ui_pages.pushButton.clicked.connect(file_save)
        self.ui_pages.pushButton_2.clicked.connect(folder_location)
        self.ui_pages.pushButton_3.clicked.connect(clicked)
        
        self.ui_pages.pushButton_4.clicked.connect(file_location_img)
        self.ui_pages.pushButton_5.clicked.connect(file_save_img)
        self.ui_pages.pushButton_6.clicked.connect(clicked_img)
        
        self.ui_pages.pushButton_7.clicked.connect(file_location_split)
        self.ui_pages.pushButton_8.clicked.connect(file_save_split)
        self.ui_pages.pushButton_9.clicked.connect(clicked_split)
        
        self.ui_pages.pushButton_10.clicked.connect(file_location_docx)
        self.ui_pages.pushButton_11.clicked.connect(file_save_docx)
        self.ui_pages.pushButton_12.clicked.connect(clicked_docx)

#==============================================FUNCTIONS PDFMerger==============================================================#

def clicked(self):
    global file_save_name, folder, msg
    if file_save_name == "" or folder == "":
        mainController.menssagen("", "Erro", "Selecione os arquivos para continuar")
    else:
        PDFMerge.pdf_merge(self, file_save_name, folder)
        mainController.menssagen(".pdf", "Secesso", "Arquivo Gerado com sucesso em: ")
        mainController.cleanV(line_edit, line_edit_2)

def file_save(self):
    global file_save_name
    file_save_name = mainController.fileNameSave(line_edit, '.pdf')

def folder_location(self):
    global folder
    folder = mainController.folderLocation(line_edit_2)
    
#==============================================FUNCTIONS PDFImage==============================================================#
    
def clicked_img(self):
    global file_save_name, file_name, msg
    if file_save_name == "" or file_name == "":
        mainController.menssagen("", "Erro", "Selecione os arquivos para continuar")
    else:
        PDFImage.pdf_image(self, file_save_name, file_name)
        mainController.menssagen(".pdf", "Secesso", "Arquivo Gerado com sucesso em: ")
        mainController.cleanV(line_edit_3, line_edit_4)


def file_location_img(self):
    global file_name
    file_name = mainController.itemFileLocation(line_edit_3)
    
def file_save_img():
    global file_save_name
    file_save_name = mainController.fileNameSave(line_edit_4, '.pdf')



#==============================================FUNCTIONS PDFSplit==============================================================#
    
def clicked_split(self):
    global file_save_name, file_name, msg
    if file_save_name == "" or file_name == "":
        mainController.menssagen("", "Erro", "Selecione os arquivos para continuar")
    else:
        PDFSplit.pdf_split(self, file_save_name, file_name)
        mainController.menssagen(".pdf", "Secesso", "Arquivo Gerado com sucesso em: ")
        mainController.cleanV(line_edit_5, line_edit_6)


def file_location_split(self):
    global file_name
    file_name = mainController.itemFileLocation(line_edit_5)
    
def file_save_split(self):
    global file_save_name
    file_save_name = mainController.fileNameSave(line_edit_6, '.pdf')

    
#==============================================FUNCTIONS PDFDocx==============================================================#
    
def clicked_docx(self):
    global file_save_name, file_name, msg
    if file_save_name == "" or file_name == "":
        mainController.menssagen("", "Erro", "Selecione os arquivos para continuar")
    else:
        PDFDocx.pdf_docx(self, file_save_name, file_name)
        mainController.menssagen(".docx", "Secesso", "Arquivo Gerado com sucesso em: ")
        mainController.cleanV(line_edit_7, line_edit_8)

def file_save_docx(self):
    global file_save_name
    file_save_name = mainController.fileNameSave(line_edit_8, '.docx')

def file_location_docx(self):
    global file_name
    file_name = mainController.itemFileLocation(line_edit_7)
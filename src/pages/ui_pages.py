# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(960, 540)
        application_pages.setMinimumSize(QSize(720, 240))
        application_pages.setMaximumSize(QSize(960, 540))
        application_pages.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: black;\n"
"font-size: 60px;\n"
"margin-left: 300px;\n"
"")

        self.verticalLayout.addWidget(self.label_6)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(960, 60))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(960, 24))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(80, 24))
        self.pushButton_2.setBaseSize(QSize(0, 0))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(960, 60))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(960, 24))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(80, 24))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 0))
        self.pushButton_3.setMaximumSize(QSize(100, 25))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_3)

        application_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: black;\n"
"font-size: 60px;\n"
"margin-left: 200px;\n"
"font-family: sans-serif;\n"
"\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.label_5)

        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(960, 60))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(960, 24))
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(80, 24))
        self.pushButton_4.setBaseSize(QSize(0, 0))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.page_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(960, 60))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(960, 24))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(80, 24))
        self.pushButton_5.setBaseSize(QSize(0, 0))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(60, 25))
        self.pushButton_6.setMaximumSize(QSize(100, 25))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.frame_7)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;\n"
"font-size: 60px;\n"
"margin-left: 300px;\n"
"font-family: sans-serif;\n"
"\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.label_9)

        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(960, 60))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_5 = QLineEdit(self.frame_10)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(960, 24))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEdit_5)

        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(80, 24))
        self.pushButton_7.setBaseSize(QSize(0, 0))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_7)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(960, 60))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(960, 24))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_6.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QSize(80, 24))
        self.pushButton_8.setBaseSize(QSize(0, 0))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_8)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(60, 25))
        self.pushButton_9.setMaximumSize(QSize(100, 25))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_9.addWidget(self.pushButton_9)


        self.verticalLayout_3.addWidget(self.frame_11)

        application_pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: black;\n"
"font-size: 60px;\n"
"margin-left: 200px;\n"
"font-family: sans-serif;\n"
"\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.label_11)

        self.frame_14 = QFrame(self.page_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(960, 60))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit_7 = QLineEdit(self.frame_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(960, 24))
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.lineEdit_7)

        self.pushButton_10 = QPushButton(self.frame_14)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMaximumSize(QSize(80, 24))
        self.pushButton_10.setBaseSize(QSize(0, 0))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_10)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.page_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(960, 60))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: black;\n"
"font-size: 14px;")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.frame_13)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMaximumSize(QSize(960, 24))
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"    padding-top: 16px;\n"
"    width: 100%;\n"
"    height: 30px;\n"
"    color: #333;\n"
"    font-style: normal;\n"
"    font-size: 14px;\n"
"    border: 2px solid #dcdce6;\n"
"    border-radius: 3px;\n"
"    padding: 0 24px;\n"
"}\n"
"")
        self.lineEdit_8.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_8)

        self.pushButton_11 = QPushButton(self.frame_13)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QSize(80, 24))
        self.pushButton_11.setBaseSize(QSize(0, 0))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_11)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.page_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_12 = QPushButton(self.frame_12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(60, 25))
        self.pushButton_12.setMaximumSize(QSize(100, 25))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    background: #FF4742;\n"
"    border: 1px solid #FF4742;\n"
"    border-radius: 6px;\n"
"    color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    font-weight: 800;\n"
"    outline: 0;\n"
"    text-align: center;\n"
"    text-transform: none;\n"
"    vertical-align: middle;\n"
"    padding-right: 15px;\n"
"    padding-left: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #DE403A;\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_12)


        self.verticalLayout_4.addWidget(self.frame_12)

        application_pages.addWidget(self.page_4)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_6.setText(QCoreApplication.translate("application_pages", u"Juntar PDFS", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Abrir em:    ", None))
        self.lineEdit_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Salvar em: ", None))
        self.pushButton.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("application_pages", u"SALVAR", None))
        self.label_5.setText(QCoreApplication.translate("application_pages", u"Converter para PDF", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Abrir em:    ", None))
        self.lineEdit_3.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Salvar em: ", None))
        self.pushButton_5.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.pushButton_6.setText(QCoreApplication.translate("application_pages", u"SALVAR", None))
        self.label_9.setText(QCoreApplication.translate("application_pages", u"Dividir PDFS", None))
        self.label_8.setText(QCoreApplication.translate("application_pages", u"Abrir em:    ", None))
        self.lineEdit_5.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.label_7.setText(QCoreApplication.translate("application_pages", u"Salvar em: ", None))
        self.pushButton_8.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.pushButton_9.setText(QCoreApplication.translate("application_pages", u"SALVAR", None))
        self.label_11.setText(QCoreApplication.translate("application_pages", u"Converter para Word", None))
        self.label_12.setText(QCoreApplication.translate("application_pages", u"Abrir em:    ", None))
        self.lineEdit_7.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.label_10.setText(QCoreApplication.translate("application_pages", u"Salvar em: ", None))
        self.pushButton_11.setText(QCoreApplication.translate("application_pages", u"...", None))
        self.pushButton_12.setText(QCoreApplication.translate("application_pages", u"SALVAR", None))
    # retranslateUi


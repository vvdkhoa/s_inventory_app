# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(50, 30))
        font = QFont()
        font.setFamily(u"Comic Sans MS")
        font.setPointSize(11)
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.note = QLineEdit(self.frame_6)
        self.note.setObjectName(u"note")
        self.note.setMinimumSize(QSize(150, 25))
        self.note.setMaximumSize(QSize(1000, 50))
        self.note.setFont(font)

        self.gridLayout_2.addWidget(self.note, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 2, 0, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Comic Sans MS")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.product_name = QLineEdit(self.frame_2)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setMinimumSize(QSize(0, 25))
        self.product_name.setFont(font)

        self.gridLayout_4.addWidget(self.product_name, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.product_name_en = QLineEdit(self.frame_2)
        self.product_name_en.setObjectName(u"product_name_en")
        self.product_name_en.setMinimumSize(QSize(0, 25))
        self.product_name_en.setFont(font)

        self.gridLayout_4.addWidget(self.product_name_en, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(265, 300))
        self.frame.setMaximumSize(QSize(200, 600))
        font2 = QFont()
        font2.setPointSize(10)
        self.frame.setFont(font2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.jan = QLineEdit(self.frame)
        self.jan.setObjectName(u"jan")
        self.jan.setMinimumSize(QSize(150, 25))
        self.jan.setMaximumSize(QSize(200, 50))
        self.jan.setFont(font)

        self.gridLayout.addWidget(self.jan, 3, 1, 1, 1)

        self.quantity = QLineEdit(self.frame)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setMinimumSize(QSize(100, 25))
        self.quantity.setMaximumSize(QSize(200, 50))
        self.quantity.setFont(font)

        self.gridLayout.addWidget(self.quantity, 1, 1, 1, 1)

        self.asin = QLineEdit(self.frame)
        self.asin.setObjectName(u"asin")
        self.asin.setMinimumSize(QSize(150, 25))
        self.asin.setMaximumSize(QSize(200, 50))
        self.asin.setFont(font)

        self.gridLayout.addWidget(self.asin, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.mpn = QLineEdit(self.frame)
        self.mpn.setObjectName(u"mpn")
        self.mpn.setMinimumSize(QSize(150, 25))
        self.mpn.setMaximumSize(QSize(200, 50))
        self.mpn.setFont(font)

        self.gridLayout.addWidget(self.mpn, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.location = QLineEdit(self.frame)
        self.location.setObjectName(u"location")
        self.location.setMinimumSize(QSize(150, 25))
        self.location.setMaximumSize(QSize(200, 50))
        self.location.setFont(font)

        self.gridLayout.addWidget(self.location, 5, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.unit_price = QLineEdit(self.frame)
        self.unit_price.setObjectName(u"unit_price")
        self.unit_price.setMinimumSize(QSize(150, 25))
        self.unit_price.setMaximumSize(QSize(200, 50))
        self.unit_price.setFont(font)

        self.gridLayout.addWidget(self.unit_price, 2, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)

        self.condition = QLineEdit(self.frame)
        self.condition.setObjectName(u"condition")
        self.condition.setMinimumSize(QSize(150, 25))
        self.condition.setMaximumSize(QSize(200, 50))
        self.condition.setFont(font)

        self.gridLayout.addWidget(self.condition, 6, 1, 1, 1)

        self.update_date = QLineEdit(self.frame)
        self.update_date.setObjectName(u"update_date")
        self.update_date.setMinimumSize(QSize(150, 25))
        self.update_date.setMaximumSize(QSize(200, 50))
        self.update_date.setFont(font)

        self.gridLayout.addWidget(self.update_date, 7, 1, 1, 1)

        self.created_date = QLineEdit(self.frame)
        self.created_date.setObjectName(u"created_date")
        self.created_date.setMinimumSize(QSize(150, 25))
        self.created_date.setMaximumSize(QSize(200, 50))
        self.created_date.setFont(font)

        self.gridLayout.addWidget(self.created_date, 8, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.downloadImageButton = QPushButton(self.frame_7)
        self.downloadImageButton.setObjectName(u"downloadImageButton")

        self.gridLayout_6.addWidget(self.downloadImageButton, 2, 0, 1, 1)

        self.deleteImageButton = QPushButton(self.frame_7)
        self.deleteImageButton.setObjectName(u"deleteImageButton")

        self.gridLayout_6.addWidget(self.deleteImageButton, 2, 1, 1, 1)

        self.image = QLabel(self.frame_7)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QSize(500, 500))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.image.setFont(font3)
        self.image.setLayoutDirection(Qt.LeftToRight)
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.image, 1, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_7, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.importButton = QPushButton(self.frame_4)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.importButton.setFont(font4)

        self.gridLayout_3.addWidget(self.importButton, 0, 3, 1, 1)

        self.exportButton = QPushButton(self.frame_4)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setMinimumSize(QSize(0, 40))
        self.exportButton.setFont(font4)

        self.gridLayout_3.addWidget(self.exportButton, 0, 4, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_5, 0, 6, 1, 1)

        self.clearButton = QPushButton(self.frame_4)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 40))
        self.clearButton.setFont(font4)

        self.gridLayout_3.addWidget(self.clearButton, 0, 5, 1, 1)

        self.deleteButton = QPushButton(self.frame_4)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(0, 40))
        self.deleteButton.setFont(font4)

        self.gridLayout_3.addWidget(self.deleteButton, 0, 7, 1, 1)

        self.searchButton = QPushButton(self.frame_4)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(0, 40))
        self.searchButton.setFont(font4)

        self.gridLayout_3.addWidget(self.searchButton, 0, 0, 1, 1)

        self.updateButton = QPushButton(self.frame_4)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setMinimumSize(QSize(0, 40))
        self.updateButton.setFont(font4)

        self.gridLayout_3.addWidget(self.updateButton, 0, 1, 1, 1)

        self.insertButton = QPushButton(self.frame_4)
        self.insertButton.setObjectName(u"insertButton")
        self.insertButton.setMinimumSize(QSize(0, 40))
        self.insertButton.setFont(font4)

        self.gridLayout_3.addWidget(self.insertButton, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout_5.addLayout(self.verticalLayout, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 645, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Note", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"JAN", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MPN", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ASIN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Create Date", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Update Date", None))
        self.downloadImageButton.setText(QCoreApplication.translate("MainWindow", u"Download Image", None))
        self.deleteImageButton.setText(QCoreApplication.translate("MainWindow", u"Delete Image", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"EXPORT", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.insertButton.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
    # retranslateUi


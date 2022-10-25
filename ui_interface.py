# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1162, 620)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 561, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_10.setTabletTracking(False)
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_10.setMaxLength(32774)
        self.lineEdit_10.setFrame(True)
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)
        self.lineEdit_10.setAlignment(Qt.AlignCenter)
        self.lineEdit_10.setPlaceholderText(u"Nome")

        self.verticalLayout.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_12)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(590, 10, 561, 270))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit_13 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_13.setTabletTracking(False)
        self.lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_13.setMaxLength(32774)
        self.lineEdit_13.setFrame(True)
        self.lineEdit_13.setEchoMode(QLineEdit.Normal)
        self.lineEdit_13.setAlignment(Qt.AlignCenter)
        self.lineEdit_13.setPlaceholderText(u"Nome Do Cliente")

        self.verticalLayout_3.addWidget(self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_14.setTabletTracking(False)
        self.lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_14.setMaxLength(32774)
        self.lineEdit_14.setFrame(True)
        self.lineEdit_14.setEchoMode(QLineEdit.Normal)
        self.lineEdit_14.setAlignment(Qt.AlignCenter)
        self.lineEdit_14.setPlaceholderText(u"Servi\u00e7o")

        self.verticalLayout_3.addWidget(self.lineEdit_14)

        self.lineEdit_16 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_16.setTabletTracking(False)
        self.lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_16.setMaxLength(32774)
        self.lineEdit_16.setFrame(True)
        self.lineEdit_16.setEchoMode(QLineEdit.Normal)
        self.lineEdit_16.setAlignment(Qt.AlignCenter)
        self.lineEdit_16.setPlaceholderText(u"Valor")

        self.verticalLayout_3.addWidget(self.lineEdit_16)

        self.lineEdit_15 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_15.setTabletTracking(False)
        self.lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:25px;\n"
"")
        self.lineEdit_15.setMaxLength(32774)
        self.lineEdit_15.setFrame(True)
        self.lineEdit_15.setEchoMode(QLineEdit.Normal)
        self.lineEdit_15.setAlignment(Qt.AlignCenter)
        self.lineEdit_15.setPlaceholderText(u"Data")

        self.verticalLayout_3.addWidget(self.lineEdit_15)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(580, 440, 561, 41))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 220, 561, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(580, 500, 561, 41))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 550, 101, 41))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(580, 560, 561, 41))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 290, 559, 261))
        self.tableWidget.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(590, 290, 561, 121))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_2.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 1, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_2.addWidget(self.radioButton_4, 2, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_2.addWidget(self.radioButton_5, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Cadastro De Clientes</span></p></body></html>", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data De Nascimento", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Servi\u00e7os Feitos</span></p></body></html>", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Imprimir em Pdf", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Financeiro Duff Haus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento", None));
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Sabrina", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Jefferson", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Marllon", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Walterlenia", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Outro Funcionario_1", None))
    # retranslateUi


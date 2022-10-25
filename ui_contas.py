# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contas.ui'
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
        MainWindow.resize(1284, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 50, 511, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size: 20px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);font-size: 20px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);font-size: 20px;\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 270, 121, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 350, 121, 171))
        self.tableWidget.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.tableWidget.setRowCount(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(101)
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(570, 50, 731, 330))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_10)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_11)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_14)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_18)

        self.label_19 = QLabel(self.formLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_19)

        self.label_20 = QLabel(self.formLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_20)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 520, 121, 41))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(340, 270, 121, 41))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 250, 181, 65))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.formLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.radioButton_2)

        self.radioButton_4 = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.formLayoutWidget_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.radioButton_3)

        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(150, 350, 121, 171))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(101)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 520, 121, 41))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.tableWidget_3 = QTableWidget(self.centralwidget)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        if (self.tableWidget_3.rowCount() < 1):
            self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(280, 350, 121, 171))
        self.tableWidget_3.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(101)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(280, 520, 121, 41))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.tableWidget_4 = QTableWidget(self.centralwidget)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        if (self.tableWidget_4.rowCount() < 1):
            self.tableWidget_4.setRowCount(1)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(410, 350, 121, 171))
        self.tableWidget_4.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.tableWidget_4.setRowCount(1)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(101)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(410, 520, 121, 41))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 330, 47, 13))
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(150, 330, 47, 13))
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(280, 330, 47, 13))
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(410, 330, 47, 13))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 390, 241, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 60, 60);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Adicionar Contas</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produlto", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Produlto", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Jefferson: R$</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Wallterlenia: R$</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Marllon: R$</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Sabrina: R$</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Outro Func: R$</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Salao: R$</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Comida: R$</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Uber: R$</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Gastos Pes.: R$</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TextLabel</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Comida", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Gastos pessoais", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Salao", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Uber", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Produlto", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Produlto", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Produlto", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Empresa", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Salao", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Uber", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Comida", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Pessoais", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Excluir Todos os Valores", None))
    # retranslateUi


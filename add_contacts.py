# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Contacts(object):
    def setupUi(self, Contacts):
        Contacts.setObjectName("Contacts")
        Contacts.resize(554, 354)
        self.centralwidget = QtWidgets.QWidget(Contacts)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 100, 221, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 130, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 221, 21))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(170, 150, 221, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 111, 16))
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 200, 101, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 200, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        Contacts.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Contacts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Contacts.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Contacts)
        self.statusbar.setObjectName("statusbar")
        Contacts.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Contacts)
        QtCore.QMetaObject.connectSlotsByName(Contacts)

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Contacts", "Contacts"))
        self.label_4.setText(_translate("Contacts", "Дата рождения"))
        self.label_3.setText(_translate("Contacts", "Телефон"))
        self.label.setText(_translate("Contacts", "Имя контакта"))
        self.pushButton_4.setText(_translate("Contacts", "Отмена"))
        self.pushButton_3.setText(_translate("Contacts", "ОК"))
        self.menu.setTitle(_translate("Contacts", "Окно работы с контактами"))
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contacts = QtWidgets.QMainWindow()
    ui = Ui_Contacts()
    ui.setupUi(Contacts)
    Contacts.show()
    sys.exit(app.exec_())'''

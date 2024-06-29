# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordRecovery(object):
    def setupUi(self, PasswordRecovery):
        PasswordRecovery.setObjectName("PasswordRecovery")
        PasswordRecovery.resize(454, 354)
        self.centralwidget = QtWidgets.QWidget(PasswordRecovery)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(PasswordRecovery)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(130, 110, 200, 20))

        self.pushButton_2 = QtWidgets.QPushButton(PasswordRecovery)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(130, 160, 200, 20))

        self.pushButton = QtWidgets.QPushButton(PasswordRecovery)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 200, 20))

        self.retranslateUi(PasswordRecovery)
        QtCore.QMetaObject.connectSlotsByName(PasswordRecovery)

    def retranslateUi(self, PasswordRecovery):
        _translate = QtCore.QCoreApplication.translate
        PasswordRecovery.setWindowTitle(_translate("PasswordRecovery", "Password recovery"))
        self.lineEdit.setPlaceholderText(_translate("PasswordRecovery", "Введите email для восстановления пароля"))
        self.pushButton_2.setText(_translate("PasswordRecovery", "Recover"))
        self.pushButton.setText(_translate("PasswordRecovery", "Back"))

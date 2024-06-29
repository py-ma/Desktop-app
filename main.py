import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from check_db import *
from auth import *
from reg import *
from recover_password import *
from add_contacts import *

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.authorization)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.ui.pushButton_3.clicked.connect(self.open_pass_reg)

        self.check_db = CheckThread()
        self.check_db.signal.connect(self.signal_handler)

    # Проверка правильности ввода
    def check_input(function):
        def correct(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            function(self)
        return correct

    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    @check_input
    def authorization(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_login(email, password)

    def open_pass_reg(self):
        global PasswordRecovery
        PasswordRecovery = QtWidgets.QMainWindow()
        op_ui = Ui_PasswordRecovery()
        op_ui.setupUi(PasswordRecovery)
        self.close()
        PasswordRecovery.show()

        def returnFromOPR():
            PasswordRecovery.close()
            self.show()
        op_ui.pushButton.clicked.connect(returnFromOPR)
        op_ui.pushButton_2.clicked.connect(recover)

    def work(self):
        global Contacts
        Contacts = QtWidgets.QMainWindow()
        w = Ui_Contacts()
        w.setupUi(Contacts)
        self.close()
        Contacts.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())
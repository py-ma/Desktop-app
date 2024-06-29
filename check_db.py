# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import handler

class CheckThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def thr_login(self, email, password):
        handler.login(email, password, self.signal)

    def thr_registration(self, email, password):
        handler.registration(email, password, self.signal)
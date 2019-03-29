#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from familyspace.ui.ui_mainwindow import Ui_MainWindow
from familyspace.login import Login

NEED_LOGIN = True


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def run():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if not NEED_LOGIN or (NEED_LOGIN and login.exec_() == QtWidgets.QDialog.Accepted):
        window = Window()
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    run()

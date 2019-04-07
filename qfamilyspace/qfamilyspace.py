#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from ui.ui_mainwindow import Ui_MainWindow
from login import Login
from profile import Profile

NEED_LOGIN = True


class Window(QtWidgets.QMainWindow):
    def __init__(self, iniFile, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.iniFile = iniFile
        self.settings = QtCore.QSettings(iniFile, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.user = {"token": ""}

        # Чтение настроек
        self.read_settings()

        profile = Profile(self.user["token"])
        profile.handle_get()
        profile.handle_put_profile()
        profile.handle_patch_profile()

    def read_settings(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")
        self.user["token"] = self.settings.value("token")
        self.settings.endGroup()


def run():
    app = QtWidgets.QApplication(sys.argv)
    login = Login("settings.ini")

    if not NEED_LOGIN or (NEED_LOGIN and login.exec_() == QtWidgets.QDialog.Accepted):
        window = Window("settings.ini")
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    run()

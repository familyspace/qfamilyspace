#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import qdarkstyle
from PyQt5 import QtWidgets

from qfamilyspace.ui.controllers.main_controller import MainController
from qfamilyspace.ui.views.main_view import MainView
from qfamilyspace.ui.dialogs.auth_dialog import Auth

# from PyQt5.QtCore import QFile, QTextStream
# import qfamilyspace.ui.resources.breeze_resources


def _create_controller():
    window = MainView()
    # dialogs = Dialogs(window, 'QFamilySpace')
    # return MainController(window, dialogs)
    return MainController(window)


def run():
    app = QtWidgets.QApplication(sys.argv)

    auth = Auth("settings.ini")

    controller = _create_controller()

    # # set stylesheet
    # file = QFile(":/dark.qss")
    # # file = QFile(":/light.qss")
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # style = stream.readAll()
    #
    # auth.setStyleSheet(style)
    # app.setStyleSheet(style)

    # setup stylesheet
    auth.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    if auth.exec_() == QtWidgets.QDialog.Accepted:
        controller.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    run()

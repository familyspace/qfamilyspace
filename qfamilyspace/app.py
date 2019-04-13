#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from qfamilyspace.ui.views.main_view import MainView
from qfamilyspace.ui.dialogs.auth import Auth


def run():
    app = QtWidgets.QApplication(sys.argv)

    auth = Auth("settings.ini")

    if auth.exec_() == QtWidgets.QDialog.Accepted:
        window = MainView()
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    run()

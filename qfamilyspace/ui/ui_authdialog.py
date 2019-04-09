# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName("AuthDialog")
        AuthDialog.setWindowModality(QtCore.Qt.WindowModal)
        AuthDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(AuthDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(AuthDialog)
        self.buttonBox.accepted.connect(AuthDialog.accept)
        self.buttonBox.rejected.connect(AuthDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)

    def retranslateUi(self, AuthDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthDialog.setWindowTitle(_translate("AuthDialog", "Dialog"))



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):

    def setupUi(self):
        # Login.setObjectName("Login")
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton("Login", self)
        self.buttonLogin.clicked.connect(self.handle_login)
        self.buttonSignup = QtWidgets.QPushButton("Signup", self)
        self.buttonSignup.clicked.connect(self.handle_signup)
        self.checkboxShowPassword = QtWidgets.QCheckBox('Show password', self)
        self.checkboxSavePassword = QtWidgets.QCheckBox('Save password', self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.checkboxShowPassword)
        layout.addWidget(self.checkboxSavePassword)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonSignup)

        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

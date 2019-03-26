from PyQt5 import QtWidgets
# from ui.ui_loginwindow import Ui_LoginWindow


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if self.textName.text() == 'foo' and self.textPass.text() == 'bar':
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

import hashlib
import requests
# import urllib2

from PyQt5 import QtWidgets
# from ui.ui_loginwindow import Ui_LoginWindow


def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton("Login", self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonSignup = QtWidgets.QPushButton("Signup", self)
        self.buttonSignup.clicked.connect(self.handleSignup)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonSignup)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

    def handleLogin(self):

        user = self.textName.text()
        password = self.textPass.text()

        password_sha256 = hash_string(password)

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            "password": password_sha256,
        }

        response = requests.post("http://localhost:8000/apiauth/signin/", headers=headers, json=payload)

        if response.status_code == 200:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", str(response.json()["error"]["message"]))

    def handleSignup(self):

        user = self.textName.text()
        password = self.textPass.text()

        password_sha256 = hash_string(password)

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            "password": password_sha256,
        }

        response = requests.post("http://localhost:8000/apiauth/signup/", headers=headers, json=payload)

        if response.status_code == 200:
            QtWidgets.QMessageBox.warning(self, "Registration", "Registration is complete")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", str(response.json()["error"]["message"]))

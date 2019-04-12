import hashlib
import requests
# import urllib2

from PyQt5 import QtWidgets, QtCore

# from ui.ui_loginwindow import Ui_LoginWindow


def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class Login(QtWidgets.QDialog):
    def __init__(self, iniFile, parent=None):
        super(Login, self).__init__(parent)

        self.iniFile = iniFile
        self.settings = QtCore.QSettings(iniFile, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

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

        self.user = {"pass_is_sha256": False}

        self.textPass.textEdited.connect(self.change_pass_status)
        self.checkboxShowPassword.stateChanged.connect(self.change_pass_visibility)

        # Чтение настроек
        self.read_settings()

    def change_pass_status(self):
        self.user["pass_is_sha256"] = False

    def change_pass_visibility(self):
        """"Изменение режима отображения пароля"""
        if self.checkboxShowPassword.checkState():
            self.textPass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

    def read_settings(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")

        self.textName.setText(self.settings.value("login"))
        self.textPass.setText(self.settings.value("password"))
        self.checkboxSavePassword.setChecked(self.settings.value("save_password", False, type=bool))
        self.user["pass_is_sha256"] = True

        self.settings.endGroup()

    def save_settings(self, token=""):
        """Сохранение настроек"""
        # Read data from config file
        self.settings.beginGroup("User")

        self.settings.setValue("save_password", self.checkboxSavePassword.isChecked())
        self.settings.setValue('token', token)
        if self.checkboxSavePassword.checkState():
            self.settings.setValue('login', self.textName.text())
            if self.user["pass_is_sha256"]:
                self.settings.setValue('password', self.textPass.text())
            else:
                self.settings.setValue('password', hash_string(self.textPass.text()))
        else:
            self.settings.setValue('login', "")
            self.settings.setValue('password', "")

        self.settings.endGroup()

    def handle_login(self):

        user = self.textName.text()

        if self.user["pass_is_sha256"]:
            password_sha256 = self.textPass.text()
        else:
            password_sha256 = hash_string(self.textPass.text())

        token = ""

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            "password": password_sha256,
        }

        try:
            response = requests.post("http://localhost:8000/api/auth/signin/", headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if 'response' in response.json():
                token = response.json()['response']['token']

            # Сохранение настроек
            self.settings = QtCore.QSettings(self.iniFile, QtCore.QSettings.IniFormat)
            self.settings.setIniCodec("utf-8")
            self.save_settings(token=token)

            if response.status_code == 200:
                self.accept()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", str(response.json()["error"]["message"]))

    def handle_signup(self):

        user = self.textName.text()
        password = self.textPass.text()

        password_sha256 = hash_string(password)

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            "password": password_sha256,
        }

        try:
            response = requests.post("http://localhost:8000/api/auth/signup/", headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if response.status_code == 200:
                QtWidgets.QMessageBox.warning(self, "Registration", "Registration is complete")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", str(response.json()["error"]["message"]))
                # print(response.content)
                # print(response.json())

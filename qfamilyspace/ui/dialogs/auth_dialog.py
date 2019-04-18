# import hashlib
import requests

from PyQt5 import QtWidgets, QtCore

from qfamilyspace.ui.dialogs.ui_auth_dialog import Ui_AuthDialog


# def hash_string(string):
#     """
#     Return a SHA-256 hash of the given string
#     """
#     return hashlib.sha256(string.encode('utf-8')).hexdigest()


class Auth(QtWidgets.QDialog):
    def __init__(self, iniFile, parent=None):
        super(Auth, self).__init__(parent)

        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)

        self.iniFile = iniFile
        self.settings = QtCore.QSettings(iniFile, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditPasswordSignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditPasswordSignupRepeat.setEchoMode(QtWidgets.QLineEdit.Password)

        # self.user = {"pass_is_sha256": False}

        # self.ui.lineEditPassword.textEdited.connect(self.change_pass_status)
        self.ui.checkBoxShowPassword.stateChanged.connect(self.change_pass_visibility)
        self.ui.checkBoxShowPassworsSignup.stateChanged.connect(self.change_pass_signup_visibility)

        self.ui.pushButtonLogin.clicked.connect(self.handle_login)
        self.ui.pushButtonSignup.clicked.connect(self.handle_signup)

        # Чтение настроек
        self.read_settings()

    # def change_pass_status(self):
    #     self.user["pass_is_sha256"] = False

    def change_pass_visibility(self):
        """"Изменение режима отображения пароля в закладке Войти"""
        if self.ui.checkBoxShowPassword.checkState():
            self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def change_pass_signup_visibility(self):
        """"Изменение режима отображения пароля в закладке Зарегистрироваться"""
        if self.ui.checkBoxShowPassworsSignup.checkState():
            self.ui.lineEditPasswordSignup.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.lineEditPasswordSignupRepeat.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.lineEditPasswordSignup.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.lineEditPasswordSignupRepeat.setEchoMode(QtWidgets.QLineEdit.Password)

    def read_settings(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")

        self.ui.lineEditLogin.setText(self.settings.value("login"))
        self.ui.lineEditPassword.setText(self.settings.value("password"))
        self.ui.checkBoxSavePassword.setChecked(self.settings.value("save_password", False, type=bool))
        # self.user["pass_is_sha256"] = True

        self.settings.endGroup()

    def save_settings(self, token=""):
        """Сохранение настроек"""
        # Read data from config file
        self.settings.beginGroup("User")

        self.settings.setValue("save_password", self.ui.checkBoxSavePassword.isChecked())
        self.settings.setValue('token', token)
        if self.ui.checkBoxSavePassword.checkState():
            self.settings.setValue('login', self.ui.lineEditLogin.text())
            # if self.user["pass_is_sha256"]:
            #     self.settings.setValue('password', self.ui.lineEditPassword.text())
            # else:
            #     self.settings.setValue('password', hash_string(self.ui.lineEditPassword.text()))
            self.settings.setValue('password', self.ui.lineEditPassword.text())
        else:
            self.settings.setValue('login', "")
            self.settings.setValue('password', "")

        self.settings.endGroup()

    def handle_login(self):

        user = self.ui.lineEditLogin.text()

        # if self.user["pass_is_sha256"]:
        #     password_sha256 = self.ui.lineEditPassword.text()
        # else:
        #     password_sha256 = hash_string(self.ui.lineEditPassword.text())
        password = self.ui.lineEditPassword.text()

        token = ""

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            # "password": password_sha256,
            "password": password,
        }

        try:
            response = requests.post("http://localhost:8000/auth_api/signin/", headers=headers, json=payload)
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

        user = self.ui.lineEditLoginSignup.text()
        password = self.ui.lineEditPasswordSignup.text()

        # password_sha256 = hash_string(password)

        headers = {"Accept": "application/json"}
        payload = {
            "login": user,
            # "password": password_sha256,
            "password": password,
        }

        try:
            response = requests.post("http://localhost:8000/auth_api/signup/", headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if response.status_code == 200:
                QtWidgets.QMessageBox.warning(self, "Registration", "Registration is complete")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", str(response.json()["error"]["message"]))
                # print(response.content)
                # print(response.json())

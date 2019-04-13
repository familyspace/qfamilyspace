import hashlib
import requests
# import urllib2

from PyQt5 import QtWidgets, QtCore

# from ui.ui_loginwindow import Ui_LoginWindow
from qfamilyspace.ui.dialogs.ui_auth import Ui_AuthDialog


def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class Auth(QtWidgets.QDialog):
    def __init__(self, iniFile, parent=None):
        super(Auth, self).__init__(parent)

        self.iniFile = iniFile
        self.settings = QtCore.QSettings(iniFile, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)
        # self._initUI()

        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditPasswordSignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEditPasswordSignupRepeat.setEchoMode(QtWidgets.QLineEdit.Password)

        self.user = {"pass_is_sha256": False}

        self.ui.lineEditPassword.textEdited.connect(self.change_pass_status)
        self.ui.checkBoxShowPassword.stateChanged.connect(self.change_pass_visibility)
        self.ui.checkBoxShowPassworsSignup.stateChanged.connect(self.change_pass_signup_visibility)

        self.ui.pushButtonLogin.clicked.connect(self.handle_login)
        self.ui.pushButtonSignup.clicked.connect(self.handle_signup)

        # Чтение настроек
        self.read_settings()

    # def _initUI(self):
    #     # self.textName = QtWidgets.QLineEdit(self)
    #     # self.textPass = QtWidgets.QLineEdit(self)
    #     # self.buttonLogin = QtWidgets.QPushButton("Login", self)
    #     # self.buttonLogin.clicked.connect(self.handle_login)
    #     # self.buttonSignup = QtWidgets.QPushButton("Signup", self)
    #     # self.buttonSignup.clicked.connect(self.handle_signup)
    #     # self.checkboxShowPassword = QtWidgets.QCheckBox('Show password', self)
    #     # self.checkboxSavePassword = QtWidgets.QCheckBox('Save password', self)
    #     # layout = QtWidgets.QVBoxLayout(self)
    #     # layout.addWidget(self.textName)
    #     # layout.addWidget(self.textPass)
    #     # layout.addWidget(self.checkboxShowPassword)
    #     # layout.addWidget(self.checkboxSavePassword)
    #     # layout.addWidget(self.buttonLogin)
    #     # layout.addWidget(self.buttonSignup)
    #
    #     self.layout = QtWidgets.QVBoxLayout(self)
    #     # Создаем лого
    #     self.logoLabel = QtWidgets.QLabel('<i><b><h1>Family Space</h1></b></i>')
    #     self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
    #     # Создаем лейблы для логина и пароля
    #     self.loginLabel = QtWidgets.QLabel('<b><h2>Логин</h2></b>')
    #     self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
    #     self.passLabel = QtWidgets.QLabel('<b><h2>Пароль</h2></b>')
    #     self.passLabel.setAlignment(QtCore.Qt.AlignCenter)
    #     # Создаем поля ввода для логина и пароля
    #     self.loginLine = QtWidgets.QLineEdit()
    #     self.passLine = QtWidgets.QLineEdit()
    #     # Добавляем кнопки входа и регистрации
    #     self.btnLog = QtWidgets.QPushButton('&Войти')
    #     self.btnLog.setStyleSheet('QPushButton {font-weight: bold; font-size: 11pt;}')
    #     self.btnReg = QtWidgets.QPushButton('&Зарегистрироваться')
    #     # Создаем виджет вкладок и сами вкладки
    #     self.tabs = QtWidgets.QTabWidget()
    #     self.tabLog = QtWidgets.QWidget()
    #     self.tabReg = QtWidgets.QWidget()
    #     # Добавляем вкладки вкладки к виджету
    #     self.tabs.addTab(self.tabLog, 'Войти')
    #     self.tabs.addTab(self.tabReg, 'Зарегистрироваться')
    #     # Генерируем создержимое первой вкладки
    #     self.tabLog.layout = QtWidgets.QVBoxLayout(self)
    #     self.tabLog.layout.addWidget(self.logoLabel)
    #     self.tabLog.layout.addWidget(self.loginLabel)
    #     self.tabLog.layout.addWidget(self.loginLine)
    #     self.tabLog.layout.addWidget(self.passLabel)
    #     self.tabLog.layout.addWidget(self.passLine)
    #     self.tabLog.layout.addWidget(self.btnLog)
    #     self.tabLog.setLayout(self.tabLog.layout)
    #     # Создаем лейблы и поля ввода вкладки регистрации
    #     self.regLogoLabel = QtWidgets.QLabel('<i><b><h1>Family Space</h1></b></i>')
    #     self.regLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
    #     # Добавляем кнопку регистрации
    #     self.btnReg = QtWidgets.QPushButton('&Зарегистрироваться')
    #     self.btnReg.setStyleSheet('QPushButton {font-weight: bold; font-size: 11pt;}')
    #
    #     # Генерируем содержимое второй вкладки
    #     self.tabReg.layout = QtWidgets.QVBoxLayout(self)
    #     self.formBoxLayout = QtWidgets.QFormLayout()
    #     self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Логин:</h2></b>'), QtWidgets.QLineEdit())
    #     self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Пароль:</h2></b>'), QtWidgets.QLineEdit())
    #     self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Повторите пароль:</h2></b>'), QtWidgets.QLineEdit())
    #     self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Email:</h2></b>'), QtWidgets.QLineEdit())
    #     self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Телефон:</h2></b>'), QtWidgets.QLineEdit())
    #     self.tabReg.layout.addWidget(self.regLogoLabel)
    #     self.tabReg.layout.addLayout(self.formBoxLayout)
    #     self.tabReg.layout.addWidget(self.btnReg)
    #     self.tabReg.setLayout(self.tabReg.layout)
    #
    #     # Добавляем виджет вкладок к нашему окну
    #
    #     self.layout.addWidget(self.tabs)
    #     self.setLayout(self.layout)
    #
    #     self.setWindowModality(QtCore.Qt.ApplicationModal)

    def change_pass_status(self):
        self.user["pass_is_sha256"] = False

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
        self.user["pass_is_sha256"] = True

        self.settings.endGroup()

    def save_settings(self, token=""):
        """Сохранение настроек"""
        # Read data from config file
        self.settings.beginGroup("User")

        self.settings.setValue("save_password", self.ui.checkBoxSavePassword.isChecked())
        self.settings.setValue('token', token)
        if self.ui.checkBoxSavePassword.checkState():
            self.settings.setValue('login', self.ui.lineEditLogin.text())
            if self.user["pass_is_sha256"]:
                self.settings.setValue('password', self.ui.lineEditPassword.text())
            else:
                self.settings.setValue('password', hash_string(self.ui.lineEditPassword.text()))
        else:
            self.settings.setValue('login', "")
            self.settings.setValue('password', "")

        self.settings.endGroup()

    def handle_login(self):

        # user = self.textName.text()
        user = self.ui.lineEditLogin.text()

        if self.user["pass_is_sha256"]:
            password_sha256 = self.ui.lineEditPassword.text()
        else:
            # password_sha256 = hash_string(self.textPass.text())
            password_sha256 = hash_string(self.ui.lineEditPassword.text())

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

        user = self.ui.lineEditLoginSignup.text()
        password = self.ui.lineEditPasswordSignup.text()

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

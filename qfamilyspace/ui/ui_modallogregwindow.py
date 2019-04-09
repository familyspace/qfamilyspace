import sys

from PyQt5 import QtCore, QtWidgets


class UiLogRegModalWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        # Создаем лого
        self.logoLabel = QtWidgets.QLabel('<i><b><h1>Family Space</h1></b></i>')
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        # Создаем лейблы для логина и пароля
        self.loginLabel = QtWidgets.QLabel('<b><h2>Логин</h2></b>')
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passLabel = QtWidgets.QLabel('<b><h2>Пароль</h2></b>')
        self.passLabel.setAlignment(QtCore.Qt.AlignCenter)
        # Создаем поля ввода для логина и пароля
        self.loginLine = QtWidgets.QLineEdit()
        self.passLine = QtWidgets.QLineEdit()
        # Добавляем кнопки входа и регистрации
        self.btnLog = QtWidgets.QPushButton('&Войти')
        self.btnLog.setStyleSheet('QPushButton {font-weight: bold; font-size: 11pt;}')
        self.btnReg = QtWidgets.QPushButton('&Зарегистрироваться')
        # Создаем виджет вкладок и сами вкладки
        self.tabs = QtWidgets.QTabWidget()
        self.tabLog = QtWidgets.QWidget()
        self.tabReg = QtWidgets.QWidget()
        # Добавляем вкладки вкладки к виджету
        self.tabs.addTab(self.tabLog, 'Войти')
        self.tabs.addTab(self.tabReg, 'Зарегистрироваться')
        # Генерируем создержимое первой вкладки
        self.tabLog.layout = QtWidgets.QVBoxLayout(self)
        self.tabLog.layout.addWidget(self.logoLabel)
        self.tabLog.layout.addWidget(self.loginLabel)
        self.tabLog.layout.addWidget(self.loginLine)
        self.tabLog.layout.addWidget(self.passLabel)
        self.tabLog.layout.addWidget(self.passLine)
        self.tabLog.layout.addWidget(self.btnLog)
        self.tabLog.setLayout(self.tabLog.layout)
        # Создаем лейблы и поля ввода вкладки регистрации
        self.regLogoLabel = QtWidgets.QLabel('<i><b><h1>Family Space</h1></b></i>')
        self.regLogoLabel.setAlignment(QtCore.Qt.AlignCenter)
        # Добавляем кнопку регистрации
        self.btnReg = QtWidgets.QPushButton('&Зарегистрироваться')
        self.btnReg.setStyleSheet('QPushButton {font-weight: bold; font-size: 11pt;}')

        # Генерируем содержимое второй вкладки
        self.tabReg.layout = QtWidgets.QVBoxLayout(self)
        self.formBoxLayout = QtWidgets.QFormLayout()
        self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Логин:</h2></b>'), QtWidgets.QLineEdit())
        self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Пароль:</h2></b>'), QtWidgets.QLineEdit())
        self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Повторите пароль:</h2></b>'), QtWidgets.QLineEdit())
        self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Email:</h2></b>'), QtWidgets.QLineEdit())
        self.formBoxLayout.addRow(QtWidgets.QLabel('<b><h2>Телефон:</h2></b>'), QtWidgets.QLineEdit())
        self.tabReg.layout.addWidget(self.regLogoLabel)
        self.tabReg.layout.addLayout(self.formBoxLayout)
        self.tabReg.layout.addWidget(self.btnReg)
        self.tabReg.setLayout(self.tabReg.layout)

        # Добавляем виджет вкладок к нашему окну

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

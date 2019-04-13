from PyQt5 import QtWidgets


class LeftView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('<center><b><h2>Здравствуйте, User</h2></b></center>')
        self.profileButton = QtWidgets.QPushButton('Профиль')
        self.logOffButton = QtWidgets.QPushButton('Выйти')
        self.logOffButton.setStyleSheet('QPushButton {background-color: red; font-weight: bold; font-size: 11pt}')
        self.contactSearchButton = QtWidgets.QPushButton('Поиск контактов')
        self.groupSearchButton = QtWidgets.QPushButton('Поиск группы')
        self.groupCreateButton = QtWidgets.QPushButton('Создать группу')
        self.yourGroupsButton = QtWidgets.QPushButton('Ваши группы')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.profileButton)
        self.vbox.addWidget(self.contactSearchButton)
        self.vbox.addWidget(self.groupSearchButton)
        self.vbox.addWidget(self.groupCreateButton)
        self.vbox.addWidget(self.yourGroupsButton)
        self.vbox.addWidget(self.logOffButton)
        self.setLayout(self.vbox)

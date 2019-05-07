from PyQt5 import QtCore

from qfamilyspace.libs.group import Group
from qfamilyspace.libs.profile import Profile


class GroupController(QtCore.QObject):

    def __init__(self, view, ini_file):
        QtCore.QObject.__init__(self)

        self.ini_file = ini_file
        self.settings = QtCore.QSettings(self.ini_file, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.view = view
        self.token = ""
        self.get_token()  # Получаем токен из файла настроек
        self.groups = None
        self.make_groups()
        self.view.create_group_signal.connect(self.post_new_group)

    def get_token(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")
        self.token = self.settings.value("token")
        self.settings.endGroup()

    def post_new_group(self, group_data):
        response = self.groups.handle_create_group(group_data)
        if response.status_code == 201:
            msg = "Группа создана"
            # msg = "The profile is saved successfully"
            print(f'{msg} \n {response.content}')

    def make_groups(self):
        self.groups = Group(self.token)

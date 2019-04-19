from PyQt5 import QtCore

from qfamilyspace.libs.profile import Profile


class ProfileController(QtCore.QObject):

    def __init__(self, view, ini_file):
        QtCore.QObject.__init__(self)

        self.ini_file = ini_file
        self.settings = QtCore.QSettings(self.ini_file, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.view = view
        self.profile = None
        self.token = ""
        self.get_token()  # Получаем токен из файла настроек
        self.make_profile()
        self.show_profile()
        self.view.save_profile_signal.connect(self.put_profile_data)
        # self.view.save_profile_signal.connect(self.patch_profile_data)

    def get_token(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")
        self.token = self.settings.value("token")
        self.settings.endGroup()

    def make_profile(self):
        self.profile = Profile(self.token)

    def show_profile(self):
        self.view.fill_profile(self.get_profile_data())

    def get_profile_data(self):
        return self.profile.handle_get_profile()

    def put_profile_data(self, profile_data):
        response = self.profile.handle_put_profile(profile_data)
        if response.status_code == 200:
            msg = "Профиль сохранён успешно"
            # msg = "The profile is saved successfully"
            print(msg)

    # def patch_profile_data(self, profile_data):
    #     response = self.profile.handle_patch_profile(profile_data)
    #     if response.status_code == 200:
    #         print("Профиль обновлён успешно")
    # TODO do we need patch or no

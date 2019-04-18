from PyQt5 import QtCore

from qfamilyspace.libs.profile import Profile


class ProfileController(QtCore.QObject):

    def __init__(self, view):
        QtCore.QObject.__init__(self)

        self.view = view
        self.profile = None
        self.get_profile()
        self.show_profile()
        self.view.save_profile_signal.connect(self.set_profile_data)

    def get_profile(self):
        token = self.get_token()
        profile = Profile(token)
        self.profile = profile

    def show_profile(self):
        profile_data = self.get_profile_data()
        self.view.fill_profile(profile_data)

    def get_profile_data(self):
        profile_data = self.profile.handle_get_profile()
        return profile_data

    def set_profile_data(self, profile_data):
        response = self.profile.handle_put_profile(profile_data)
        if response.status_code == 200:
            print("Профиль сохранён успешно")

    def get_token(self):
        return self.view.token

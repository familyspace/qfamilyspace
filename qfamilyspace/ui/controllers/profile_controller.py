from PyQt5 import QtCore

from qfamilyspace.libs.profile import Profile


class ProfileController(QtCore.QObject):

    def __init__(self, view):
        QtCore.QObject.__init__(self)

        self.view = view

        # self.profile_data = {}

        self.show_profile()

    def show_profile(self):
        # self.get_profile_data()
        self.view.fill_profile(self.get_profile_data())

    @staticmethod
    def get_profile_data():
        profile = Profile("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNiwiZXhwIjoxNTg3MDIzNTE3fQ.f5DvF7WOp6p56xfK-gaeaTX748D5PYmDLuy_jvClejw")
        # profile_data = profile.handle_get_profile()
        return profile.handle_get_profile()

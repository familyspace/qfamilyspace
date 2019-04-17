import sys

from PyQt5 import QtCore

from qfamilyspace.ui.controllers.profile_controller import ProfileController


class MainController(QtCore.QObject):

    def __init__(self, view):
        super(MainController, self).__init__()

        self.view = view

        self._init_controllers()

        # self.view.closeEventSignal.connect(self.view_onCloseEvent)

    def _init_controllers(self):
        self._init_profile()

    # def exit(self):
    #     self.view.close()
    #     sys.exit()

    def show(self):
        self.view.show()

    def _init_profile(self):
        self._profile_controller = ProfileController(self.view.tasks_view.profile_view)

from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.ui_left_panel import Ui_LeftPanel
from qfamilyspace.ui.views.ui_profile_view import Ui_ProfileView


class LeftPanelWidget(QtWidgets.QWidget):

    # save_profile_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(LeftPanelWidget, self).__init__(parent)
        uic.loadUi('ui/views/ui_left_panel.ui', self)
        #
        # self.ui = Ui_LeftPanel()
        # self.ui.setupUi(self)


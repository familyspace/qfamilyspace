from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.ui_rigth_panel import Ui_RigthPanel


class RigthPanelWidget(QtWidgets.QWidget):

    # save_profile_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(RigthPanelWidget, self).__init__(parent)

        self.ui = Ui_RigthPanel()
        self.ui.setupUi(self)


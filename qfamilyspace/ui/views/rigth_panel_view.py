from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.ui_rigth_panel import Ui_RigthPanel


class Tasks(QtWidgets.QWidget):

    # save_profile_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Tasks, self).__init__(parent)
        uic.loadUi('ui/views/ui_rigth_panel.ui', self)
        # self.ui = Ui_RigthPanel()
        # self.ui.setupUi(self)


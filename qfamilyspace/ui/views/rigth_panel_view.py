from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal


class Tasks(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Tasks, self).__init__(parent)
        uic.loadUi('ui/views/ui_rigth_panel.ui', self)
        # self.ui = Ui_RigthPanel()
        # self.ui.setupUi(self)

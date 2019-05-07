from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal


class LeftPanelWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(LeftPanelWidget, self).__init__(parent)
        uic.loadUi('ui/views/ui_left_panel.ui', self)
        #
        # self.ui = Ui_LeftPanel()
        # self.ui.setupUi(self)

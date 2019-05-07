from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.left_panel_view import LeftPanel


class LeftPanelView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.user_base_actions = LeftPanel()

        # offset = QtCore.QSettings().value("ui_margin_offset", -4)
        # self.setContentsMargins(2 * offset, offset, offset, offset)

        layout.addWidget(self.user_base_actions)

        self.setLayout(layout)

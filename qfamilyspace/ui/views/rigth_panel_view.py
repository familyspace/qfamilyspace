from PyQt5 import QtWidgets

from qfamilyspace.ui.views.left_panel_widget import LeftPanelWidget
from qfamilyspace.ui.views.profile_view import ProfileView
from qfamilyspace.ui.views.rigth_panel_widget import RigthPanelWidget


class RigthPanelView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.rigth_panel_widget = RigthPanelWidget()

        # offset = QtCore.QSettings().value("ui_margin_offset", -4)
        # self.setContentsMargins(2 * offset, offset, offset, offset)

        layout.addWidget(self.rigth_panel_widget)

        self.setLayout(layout)

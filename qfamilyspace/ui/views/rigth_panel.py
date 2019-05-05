from PyQt5 import QtWidgets

from qfamilyspace.ui.views.rigth_panel_view import Tasks


class RigthPanelView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.tasks = Tasks()

        # offset = QtCore.QSettings().value("ui_margin_offset", -4)
        # self.setContentsMargins(2 * offset, offset, offset, offset)

        layout.addWidget(self.tasks)

        self.setLayout(layout)

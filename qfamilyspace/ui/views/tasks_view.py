from PyQt5 import QtWidgets

from qfamilyspace.ui.views.profile_view import ProfileView


class TasksView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        self.profile_view = ProfileView(self)

        # offset = QtCore.QSettings().value("ui_margin_offset", -4)
        # self.setContentsMargins(2 * offset, offset, offset, offset)

        layout.addWidget(self.profile_view)

        self.setLayout(layout)

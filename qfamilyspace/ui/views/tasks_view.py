from PyQt5 import QtWidgets


class TasksView(QtWidgets.QWidget):

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self._initUI()

    def _initUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

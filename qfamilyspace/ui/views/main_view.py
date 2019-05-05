from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from qfamilyspace.ui.views.left_panel import LeftPanelView
from qfamilyspace.ui.views.left_view import LeftView
from qfamilyspace.ui.views.rigth_panel import RigthPanelView
from qfamilyspace.ui.views.tasks_view import TasksView


class MainView(QtWidgets.QMainWindow):
    closeEventSignal = QtCore.pyqtSignal(QtGui.QCloseEvent)

    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self._initUI()

    def show(self):
        super(MainView, self).show()

    def hide(self):
        super(MainView, self).hide()

    def _initUI(self):
        self.setWindowTitle("QFamilySpace")

        self.splitter = QtWidgets.QSplitter()
        self.splitter.setHandleWidth(1)

        self.left_panel = LeftPanelView(self.splitter)
        self.rigth_panel = RigthPanelView(self.splitter)

        # self.left_view = LeftView(self.splitter)
        # self.tasks_view = TasksView(self.splitter)

        self.setCentralWidget(self.splitter)

        self.resize(870, 650)
        self.splitter.setSizes([300, 550])

    def closeEvent(self, closeEvent):
        super(MainView, self).closeEvent(closeEvent)
        self.closeEventSignal.emit(closeEvent)

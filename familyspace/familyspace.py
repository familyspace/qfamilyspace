import sys
from PyQt5 import QtWidgets
from ui.ui_mainwindow import Ui_MainWindow
from login import Login

NEED_LOGIN = True


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if not NEED_LOGIN or (NEED_LOGIN and login.exec_() == QtWidgets.QDialog.Accepted):
        window = Window()
        window.show()
        sys.exit(app.exec_())

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.ui_profile_view import Ui_ProfileView


class ProfileView(QtWidgets.QWidget):

    save_profile_signal = pyqtSignal(dict)

    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        super(ProfileView, self).__init__(parent)
        self.ui = Ui_ProfileView()
        self.ui.setupUi(self)

        # self.ui.pushButton_save_profile.clicked.connect(self.save_profile)

    def fill_profile(self, profile_data):
        # self.ui.lineEdit_user = kwargs["user"]
        self.ui.lineEdit_user.setText(str(profile_data["id"]))
        self.ui.lineEdit_first_name.setText(profile_data["first_name"])
        self.ui.lineEdit_last_name.setText(profile_data["last_name"])
        self.ui.lineEdit_middle_name.setText(profile_data["patronymic"])
        self.ui.lineEdit_phone.setText(profile_data["phone"])
        if profile_data["gender"] == "M":
            self.ui.radioButton_man.setChecked(True)
        elif profile_data["gender"] == "W":
            self.ui.radioButton_woman.setChecked(True)
        if profile_data["birth_date"]:
            self.ui.dateEdit_birth_date.setDate(profile_data["birth_date"])  # TODO проверить работоспособность

    # def save_profile(self):
    #     profile_data = {
    #         # "user": self.ui.lineEdit_user.text(),
    #         "user": int(self.ui.lineEdit_user.text()),
    #         "first_name": self.ui.lineEdit_first_name.text(),
    #         "last_name": self.ui.lineEdit_first_name.text(),
    #         "patronymic": self.ui.lineEdit_first_name.text(),
    #         "phone": self.ui.lineEdit_first_name.text(),
    #         "gender": "M" if self.ui.radioButton_man.isChecked() else "W",
    #         "birth_date": self.ui.dateEdit_birth_date.text(),
    #     }
    #     self.save_profile_signal.emit(profile_data)

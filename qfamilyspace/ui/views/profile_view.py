from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

from qfamilyspace.ui.views.ui_profile_view import Ui_ProfileView


class ProfileView(QtWidgets.QWidget):

    save_profile_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(ProfileView, self).__init__(parent)

        self.ui = Ui_ProfileView()
        self.ui.setupUi(self)

        self.ui.pushButton_save_profile.clicked.connect(self.save_profile)

    def fill_profile(self, profile_data):
        self.ui.lineEdit_first_name.setText(profile_data["first_name"])
        self.ui.lineEdit_last_name.setText(profile_data["last_name"])
        self.ui.lineEdit_middle_name.setText(profile_data["patronymic"])
        self.ui.lineEdit_phone.setText(profile_data["phone"])
        if profile_data["gender"] == "M":
            self.ui.radioButton_man.setChecked(True)
        elif profile_data["gender"] == "W":
            self.ui.radioButton_woman.setChecked(True)
        if profile_data["birth_date"]:
            self.ui.dateEdit_birth_date.setDate(QtCore.QDate.fromString(profile_data["birth_date"], "yyyy-MM-dd"))

    def save_profile(self):
        # gender = ""
        # if self.ui.radioButton_man.isChecked():
        #     gender = "M"
        # elif self.ui.radioButton_woman.isChecked():
        #     gender = "W"
        # TODO надо ли оставлять пол невыбранным
        profile_data = {
            "first_name": self.ui.lineEdit_first_name.text(),
            "last_name": self.ui.lineEdit_last_name.text(),
            "patronymic": self.ui.lineEdit_middle_name.text(),
            "phone": self.ui.lineEdit_phone.text(),
            "gender": "W" if self.ui.radioButton_woman.isChecked() else "M",
            "birth_date": self.ui.dateEdit_birth_date.date().toString("yyyy-MM-dd"),
            "email": self.ui.lineEdit_email.text(),
            "password": self.ui.lineEdit_password.text(),
        }
        # password = self.ui.lineEdit_password.text()
        # if password:
        #     profile_data["password"] = password
        self.save_profile_signal.emit(profile_data)

    # TODO сделать частичное сохранение профиля

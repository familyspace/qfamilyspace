from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal


class LeftPanel(QtWidgets.QWidget):
    save_profile_signal = pyqtSignal(dict)
    create_group_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(LeftPanel, self).__init__(parent)
        uic.loadUi('ui/views/ui_left_panel.ui', self)
        # Список категорий
        self.categories_list = None
        #
        # self.ui = Ui_LeftPanel()
        # self.ui.setupUi(self)
        self.Create_Group_pushButton.clicked.connect(self.create_new_group)
        self.pushButton_save_profile.clicked.connect(self.save_profile)

    def fill_profile(self, profile_data):
        self.lineEdit_first_name.setText(profile_data["first_name"])
        self.lineEdit_last_name.setText(profile_data["last_name"])
        self.lineEdit_middle_name.setText(profile_data["patronymic"])
        self.lineEdit_phone.setText(profile_data["phone"])
        self.lineEdit_password.setText('')
        if profile_data["gender"] == "M":
            self.radioButton_man.setChecked(True)
        elif profile_data["gender"] == "W":
            self.radioButton_woman.setChecked(True)
        if profile_data["email"]:
            self.lineEdit_email.setText(profile_data["email"])
        if profile_data["birth_date"]:
            self.dateEdit_birth_date.setDate(QtCore.QDate.fromString(profile_data["birth_date"], "yyyy-MM-dd"))

    def save_profile(self):
        gender = ""
        if self.radioButton_man.isChecked():
            gender = "M"
        elif self.radioButton_woman.isChecked():
            gender = "W"
        profile_data = {
            "first_name": self.lineEdit_first_name.text(),
            "last_name": self.lineEdit_last_name.text(),
            "patronymic": self.lineEdit_middle_name.text(),
            "phone": self.lineEdit_phone.text(),
            "gender": gender,
            "birth_date": self.dateEdit_birth_date.date().toString("yyyy-MM-dd"),
            "email": self.lineEdit_email.text(),
        }
        password = self.lineEdit_password.text()
        if password:
            profile_data["password"] = password
        self.save_profile_signal.emit(profile_data)

    def create_new_group(self):
        def get_id_for_category_name(categories_list, category_name):
            for category in categories_list:
                if category['name'] == category_name:
                    return category['id']
            return None

        group_data = {
            "title": self.New_Group_Title_lineEdit.text(),
            "description": self.New_Group_Description_textEdit.toPlainText(),
            "category": get_id_for_category_name(self.categories_list, self.New_Group_Category_comboBox.currentText()),
            "is_public": bool(self.New_Group_Is_Public_checkBox.checkState()),
        }

        self.create_group_signal.emit(group_data)

    def fill_categories(self, categories):
        self.categories_list = categories
        self.New_Group_Category_comboBox.clear()
        for category in categories:
            self.New_Group_Category_comboBox.addItem(category['name'])

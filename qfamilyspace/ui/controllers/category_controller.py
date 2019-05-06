from PyQt5 import QtCore

from qfamilyspace.libs.category import Category
from qfamilyspace.libs.group import Group
from qfamilyspace.libs.profile import Profile


class CategoryController(QtCore.QObject):

    def __init__(self, view, ini_file):
        QtCore.QObject.__init__(self)

        self.ini_file = ini_file
        self.settings = QtCore.QSettings(self.ini_file, QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("utf-8")

        self.view = view
        self.token = ""
        self.get_token()  # Получаем токен из файла настроек
        self.categories = None
        self.make_categories()
        self.show_categories()
        self.categories_list = self.get_categories()
        # self.view.save_profile_signal.connect(self.put_profile_data)

        # self.view.save_profile_signal.connect(self.patch_profile_data)

    def get_token(self):
        """Чтение настроек"""
        self.settings.beginGroup("User")
        self.token = self.settings.value("token")
        self.settings.endGroup()

    def get_categories(self):
        response, status_code = self.categories.handle_get_categories()
        if status_code == 200:
            msg = "Категории получены"
            # msg = "The categories is received"
            #print(f'{msg} \n {response}')

            return response

    def get_id_for_category_name(self, catogory_name):
        for category in self.categories_list:
            if category['name'] == catogory_name:
                return category['id']
        return None


    def make_categories(self):
        self.categories = Category(self.token)

    def show_categories(self):
        self.view.fill_categories(self.get_categories())

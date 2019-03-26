import requests
# import urllib2
# from requests.auth import HTTPBasicAuth

from PyQt5 import QtWidgets
# from ui.ui_loginwindow import Ui_LoginWindow


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        user = self.textName.text()
        password = self.textPass.text()

        # client_id = 'your_client_id'
        # client_secret = 'your_client_secret'
        #
        # from oauthlib.oauth2 import BackendApplicationClient
        # client = BackendApplicationClient(client_id=client_id)
        # oauth = OAuth2Session(client=client)
        # token = oauth.fetch_token(token_url='https://provider.com/oauth2/token', client_id=client_id,
        #                           client_secret=client_secret)


        # response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(user, password))
        response = requests.get('https://api.github.com/user', auth=(user, password))
        # response = urllib2.urlopen(urllib2.Request('https://api.github.com/user',
        #                                            headers={'Authorization': 'access_token myToken'}))
        # if self.textName.text() == 'foo' and self.textPass.text() == 'bar':
        if response.status_code == 200:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

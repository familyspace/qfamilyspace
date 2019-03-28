import hashlib
import json

import requests
# import urllib2
# from requests.auth import HTTPBasicAuth
from hash import hash_string

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
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

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
        # response = requests.get('https://api.github.com/user', auth=(user, password))

        password_sha256 = hash_string(password)
        print(password_sha256)
        # password_sha256 = '8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92'

        headers = {'Accept': 'application/json'}
        payload = {
            "login": 'user3',
            # "password": password_sha256,
            "password": password,
        }
        # response = requests.post('http://localhost:8000/apiauth/signin/', headers=headers, data=json.dumps(payload))
        response = requests.post('http://localhost:8000/apiauth/signin/', headers=headers, json=payload)
        # print(response.content.decode('utf8'))
        print(response.json())
        # response = urllib2.urlopen(urllib2.Request('https://api.github.com/user',
        #                                            headers={'Authorization': 'access_token myToken'}))
        # if self.textName.text() == 'foo' and self.textPass.text() == 'bar':
        if response.status_code == 200:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Category:
    """
    Class for working with group categories
    """

    def __init__(self, token):
        self.token = token
        self.domain = 'http://localhost:8000/'

    def handle_get_categories(self):

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }

        payload = {}

        try:
            response = requests.get(f'{self.domain}category_api/list/',
                                    headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            return (response.json()["response"], response.status_code)
        return {}

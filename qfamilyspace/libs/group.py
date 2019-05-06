#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Group:
    """
    Class for working with group
    """

    def __init__(self, token):
        self.token = token
        self.domain = 'http://localhost:8000/'

    #     self.user_id = None
    #
    #     self.read_user_id()
    #
    # def read_user_id(self):
    #     self.user_id = self.handle_get_profile()["id"]

    def handle_create_group(self, payload: dict) -> dict:

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }
        try:
            response = requests.post(f"{self.domain}group_api/edit/",
                                     headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if "response" in response.json():
                return response.json()["response"][0]
        return {}

    def handle_put_group(self, payload: dict) -> dict:

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }

        try:
            response = requests.put(f"{self.domain}group_api/edit/{payload['id']}/",
                                    headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            return response.json()["response"][0]
        return {}

    def handle_get_group(self, user_id) -> dict:

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }

        payload = {}

        try:
            response = requests.get(f"{self.domain}group_api/edit/{user_id}/",
                                    headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            return response.json()["response"][0]
        return {}

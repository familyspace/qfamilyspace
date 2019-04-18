#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Profile:
    def __init__(self, token):
        self.token = token
        self.user_id = None

        self.read_user_id()

    def read_user_id(self):
        self.user_id = self.handle_get_profile()["id"]

    def handle_get_profile(self) -> dict:

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }
        payload = {}

        try:
            response = requests.get("http://localhost:8000/user_api/profile/",
                                    headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if "response" in response.json():
                return response.json()["response"][0]
        return {}

    def handle_put_profile(self, payload: dict):

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }

        try:
            response = requests.put(f"http://localhost:8000/user_api/profile/{self.user_id}/",
                                    headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            return response
        return None

    def handle_patch_profile(self):

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }
        payload = {}

        try:
            response = requests.patch(f"http://localhost:8000/user_api/profile/{self.user_id}/",
                                      headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            # print(response.status_code)
            # print(response.json())
            # if "response" in response.json():
            #     return response.json()["response"][0]
            return response
        return None

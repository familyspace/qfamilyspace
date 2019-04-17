#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Profile:
    def __init__(self, token):
        self.token = token
        self.user_id = None

    def handle_get_profile(self):

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }
        payload = {}

        try:
            response = requests.get("http://localhost:8000/user_api/profile/", headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            if "response" in response.json():
                # print(response.json()["response"])
                self.user_id = response.json()["response"][0]["id"]
                # print(self.user_id)
        return response.json()["response"][0]

    def handle_put_profile(self):

        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self.token}",
        }
        payload = {
            "gender": "M",
            "birth_date": "1979-07-20",
        }

        try:
            response = requests.put(f"http://localhost:8000/user_api/profile/{self.user_id}/", headers=headers, json=payload)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: {e}")
        else:
            print(response)
            print(response.json())

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
            print(response)
            print(response.json())

from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_login(self):
        response = requests.post('http://0.0.0.0:5556/api/login')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = requests.post('http://0.0.0.0:5556/api/user/logout')
        self.assertEqual(response.status_code, 200)
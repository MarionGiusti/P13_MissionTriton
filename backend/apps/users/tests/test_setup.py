"""Unit test for the user application"""
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

import datetime

class TestUserSetUp(APITestCase):
    def setUp(self):
        self.login_url = '/api/api-token-auth/'
        self.register_url = '/api/dj-rest-auth/registration/'
        self.api_users = '/api/users/'

        self.user_register_data = {
            'username': 'Edmond',
            'password1': '.R0sTanD!7',
            'password2': '.R0sTanD!7',
            'email': 'edmond@test.com'
        }

        self.user_login_data = {
            'username': 'Edmond',
            'password': '.R0sTanD!7',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class TestMissionUserSetUp(APITestCase):
    def setUp(self):
        self.register_url = '/api/dj-rest-auth/registration/'
        self.api_missions = '/api/missions/'

        self.user_register_data = {
            'username': 'Edmond',
            'password1': '.R0sTanD!7',
            'password2': '.R0sTanD!7',
            'email': 'edmond@test.com'
        }

        self.mission_data = {
            'name': 'NEMO',
            'ship_name': 'Nautilus',
            'start_date': datetime.date(2021,6,12),
            'end_date': datetime.date(2021,8,16)
        }

        self.client.post(self.register_url, self.user_register_data, format='json')
        self.token = Token.objects.get(user__username=self.user_register_data['username'])
        self.client.post(self.api_missions, self.mission_data, hearders=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key), format='json')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

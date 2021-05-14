"""Unit test for the user application"""
# from django.urls import reverse
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        self.login_url = '/api-token-auth/'
        self.register_url = '/dj-rest-auth/registration/'
        
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

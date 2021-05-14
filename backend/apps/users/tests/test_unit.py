"""Unit test for the user application"""
# from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from apps.users.models import CustomUser, MissionUser

class RegisterTests(APITestCase):
    def setUp(self):
        self.data = {
            'username': 'Edmond',
            'password1': '.R0sTanD!7',
            'password2': '.R0sTanD!7',
            'email': 'edmond@test.com'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_register_user(self):
        """
        Ensure we can create a new account object and 
        token is created automatically.
        """
        url = '/dj-rest-auth/registration/'
        response = self.client.post(url, self.data, format='json')
        token = Token.objects.filter(user__username='Edmond').exists()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'Edmond')
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(token, True)

class LoginTests(APITestCase):
    def setUp(self):
        data = {
            'username': 'Edmond',
            'password1': '.R0sTanD!7',
            'password2': '.R0sTanD!7',
            'email': 'edmond@test.com'
        }
        url = '/dj-rest-auth/registration/'
        response = self.client.post(url, data, format='json')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_login_user(self):
        """
        Ensure user can login.
        """
        url = '/api-token-auth/'
        data = {
            'username': 'Edmond',
            'password': '.R0sTanD!7',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

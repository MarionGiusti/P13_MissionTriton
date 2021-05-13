"""Unit test for the user application"""
# from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models import CustomUser, MissionUser
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory

class CustomUserTests(APITestCase):
    def test_register_user(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        url = '/dj-rest-auth/registration/'
        data = {
            'username': 'Edmond',
            'password1': '.R0sTanD!7',
            'password2': '.R0sTanD!7',
            'email': 'edmond@test.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'Edmond')
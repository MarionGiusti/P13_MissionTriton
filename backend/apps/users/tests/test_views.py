"""Unit test for the user application"""
# from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from apps.users.models import CustomUser, MissionUser
from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register_correctly(self):
        """
        """
        response = self.client.post(self.register_url, self.user_register_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, self.user_register_data['username'])

    def test_token_is_created_automatically_when_user_registered(self):
        response = self.client.post(self.register_url, self.user_register_data, format='json')
        token_bool = Token.objects.filter(user__username=self.user_register_data['username']).exists()
        token = Token.objects.filter(user__username=self.user_register_data['username']).values_list('key', flat=True)
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(token_bool, True)
        self.assertEqual(response.data, {'key': token.get()})

    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_register_data, format='json')
        response = self.client.post(self.login_url, self.user_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_data_available_readonly(self):
        self.client.post(self.register_url, self.user_register_data, format='json')
        user_id = CustomUser.objects.get().id
        url = '/api/users/' + str(user_id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.data, {
            'id': user_id,
            'username': self.user_register_data['username'],
            'first_name': '',
            'last_name': '',
            'email': self.user_register_data['email'],
            'profile_image': 'http://testserver/media/profile.png',
            'profile_background_image': 'http://testserver/media/jakob-owens-turtle-unsplash.jpg',
            'linkedin_link': None,
            'researchgate_link': None,
            'missions': []
            }
        )

    def test_user_data_edit_from_owner(self):
        self.client.post(self.register_url, self.user_register_data, format='json')
        user_id = CustomUser.objects.get().id
        url = '/api/users/' + str(user_id) + '/'
        response = self.client.patch(url, {
            username: self.user_register_data['username'],
            first_name: self.user_register_data['username'],
            last_name: 'Rostand',
            email: self.user_register_data['email'],
            linkedin_link: 'http://www.linkedin.com/in/edmond-rostand',
            researchgate_link: None,
            }, self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        )
        import pdb
        pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

"""Unit test for the user application"""
import datetime

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from missions.models import Mission

class TestMissionSetUp(APITestCase):
    def setUp(self):
        self.register_url = '/api/dj-rest-auth/registration/'

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
        self.client.post(reverse('mission-list'), self.mission_data, hearders=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key), format='json')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class TestTimeLineSetUp(APITestCase):
    def setUp(self):
        self.register_url = '/api/dj-rest-auth/registration/'

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
        self.client.post(reverse('mission-list'), self.mission_data, hearders=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key), format='json')
        
        mission =  Mission.objects.get()

        self.timeline_data = {
            'missionId': mission.id,
            'form': {
                'name': 'Départ',
                'start_date': datetime.date(2021,6,12),
                'end_date': None,
                'description': '',
                'color': '#B6885D'
            }
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

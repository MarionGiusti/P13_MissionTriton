"""Unit test for the user application"""
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.users.models import CustomUser
from apps.missions.models import Mission
from apps.schedules.models import Schedule
from apps.schedules.serializers import ScheduleSerializer

from .test_setup import TestScheduleSetUp

class TestSchedule(TestScheduleSetUp):
    def test_user_can_add_schedule_event(self):
        response = self.client.post(self.api_schedule_url, self.schedule_data,
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),  format="json")

        schedule = Schedule.objects.get()
        serializer = ScheduleSerializer(schedule)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_cannot_read_schedule_event_of_other_user(self):
        res = self.client.post(self.api_schedule_url, self.schedule_data,
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),  format="json")

        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }

        # self.client.post(self.register_url, second_user_register_data, format='json')
        # self.client.post('/api/api-token-auth/', {'username': 'Cyrano', 'password': '2BerGe!RAC.',}, format='json')
        # token = Token.objects.get(user__username=second_user_register_data['username'])
        
        url = self.api_schedule_url + str(res.data['id']) + '/'
        response = self.client.get(url, headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_missionusers_from_same_mission_share_schedule_event_if_mission_defined(self):
        mission = Mission.objects.get()
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        second_missionuser_data = {
            'missionId': mission.id,
            'email': second_user_register_data['email']
        }

        schedule_data = {
            'mission': '',
            'name': 'Réunion',
            'start': datetime.date(2021,5,21),
            'end': datetime.date(2021,5,21),
            'details': '',
            'color': '#B6895D'
        }

        self.client.post(self.register_url, second_user_register_data, format='json')
        self.client.post(reverse('missionuser-list'), second_missionuser_data, format='json')
        token = Token.objects.get(user__username=second_user_register_data['username'])

        user = CustomUser.objects.get(username=self.user_register_data['username']).id
        user_second = CustomUser.objects.get(username=second_user_register_data['username'])

        self.client.post(self.api_schedule_url, self.schedule_data,
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),  format="json")
        self.client.post(self.api_schedule_url, schedule_data,
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),  format="json")

        response = self.client.get(self.api_schedule_url, headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key))
        schedule = Schedule.objects.filter(user__id=user)
        serializer = ScheduleSerializer(schedule, many=True)
        # self.client.logout()
        # self.client.post('/api/api-token-auth/', {'username': 'Cyrano', 'password': '2BerGe!RAC.',}, format='json')
        response_second_user = self.client.get(self.api_schedule_url, headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key))
        schedule_second = Schedule.objects.filter(user__id=user, mission__id=user_second.missions.all()[0].id)
        serializer_second = ScheduleSerializer(schedule_second, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response_second_user.data, serializer_second.data)
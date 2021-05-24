"""Unit test for the user application"""
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from users.models import CustomUser, MissionUser
from missions.models import Mission, TimeLine
from missions.serializers import MissionSerializer, TimeLineSerializer

from .test_setup import TestMissionSetUp, TestTimeLineSetUp

class TestMission(TestMissionSetUp):
    def test_user_not_authenticated_can_read_mission(self):
        self.client.logout()
        response = self.client.get(reverse('mission-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_can_edit_mission_if_mission_member(self):
        mission_id =  Mission.objects.get().id
        url = reverse('mission-detail', kwargs={"pk": str(mission_id)})
        response = self.client.patch(url, {
            'end_date': datetime.date(2021,8,22),
            'description': 'La mission porte sur ...',
            },
            hearders=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),
            format='json'
        )
        mission = Mission.objects.filter(id=mission_id).values()
        serializer = MissionSerializer(mission[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_cannot_edit_mission_if_not_mission_member(self):
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, second_user_register_data, format='json')
        token = Token.objects.get(user__username=second_user_register_data['username'])
        mission_id =  Mission.objects.get().id
        url = reverse('mission-detail', kwargs={"pk": str(mission_id)})
        response = self.client.patch(url, {
            'end_date': datetime.date(2021,8,22),
            'description': 'La mission porte sur ...',
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class TestTimeLine(TestTimeLineSetUp):
    def test_user_can_add_event_timeline_if_missionuser_of_the_mission(self):
        response = self.client.post(reverse('timeline-list'), self.timeline_data, format="json")
        timeline = TimeLine.objects.get()
        serializer = TimeLineSerializer(timeline)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_cannot_add_event_timeline_if_not_missionuser_of_the_mission(self):
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, second_user_register_data, format='json')
        token = Token.objects.get(user__username=second_user_register_data['username'])
        response = self.client.post(
            reverse('timeline-list'), self.timeline_data, 
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key), 
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_edit_event_timeline_if_missionuser_of_the_mission(self):
        self.client.post(reverse('timeline-list'), self.timeline_data, format="json")
        timeline = TimeLine.objects.get()
        url = reverse('timeline-detail', kwargs={"pk": timeline.id})
        response = self.client.patch(url, {
            'description': 'Vol direction Ponta Delgada',
            'color': '#1BDBDE'
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),
            format="json")
        timeline = TimeLine.objects.get()
        serializer = TimeLineSerializer(timeline)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_cannot_edit_event_timeline_if_not_missionuser_of_the_mission(self):
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, second_user_register_data, format='json')
        token = Token.objects.get(user__username=second_user_register_data['username'])
        self.client.post(reverse('timeline-list'), self.timeline_data, format="json")
        timeline = TimeLine.objects.get()
        url = reverse('timeline-detail', kwargs={"pk": timeline.id})
        response = self.client.patch(url, {
            'description': 'Vol direction Ponta Delgada',
            'color': '#1BDBDE'
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
            format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

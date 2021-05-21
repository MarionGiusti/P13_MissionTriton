"""Unit test for the user application"""
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth import get_user_model
from apps.users.models import CustomUser, MissionUser
from apps.users.serializers import UserSerializer, MissionUserSerializer

from apps.missions.models import Mission
from .test_setup import TestUserSetUp, TestMissionUserSetUp

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import io


class TestUser(TestUserSetUp):
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_register_correctly(self):
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

    def test_user_cannot_login_with_unregistered_user_data(self):
        user_unregistered_login_data = {
            'username': 'Cyrano',
            'password': '2BerGe!RAC.',
        } 
        response = self.client.post(self.login_url, user_unregistered_login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_users_data_available_readonly(self):
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, self.user_register_data, format='json')
        self.client.post(self.register_url, second_user_register_data, format='json')
        user_id = CustomUser.objects.get(username=self.user_register_data['username']).id
        second_user_id = CustomUser.objects.get(username=second_user_register_data['username']).id
        self.client.logout()
        response = self.client.get(self.api_users)
        # users = CustomUser.objects.all()
        # serializer = UserSerializer(users, many=True)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.data[0], {
        #     'id': user_id,
        #     'username': self.user_register_data['username'],
        #     'first_name': '',
        #     'last_name': '',
        #     'email': self.user_register_data['email'],
        #     'profile_image': 'http://testserver/media/profile.png',
        #     'profile_background_image': 'http://testserver/media/jakob-owens-turtle-unsplash.jpg',
        #     'linkedin_link': None,
        #     'researchgate_link': None,
        #     'missions': []
        #     }
        # )
        # self.assertEqual(response.data[1], {
        #     'id': second_user_id,
        #     'username': second_user_register_data['username'],
        #     'first_name': '',
        #     'last_name': '',
        #     'email': second_user_register_data['email'],
        #     'profile_image': 'http://testserver/media/profile.png',
        #     'profile_background_image': 'http://testserver/media/jakob-owens-turtle-unsplash.jpg',
        #     'linkedin_link': None,
        #     'researchgate_link': None,
        #     'missions': []
        #     }
        # )

    def test_user_detail_data_available_readonly(self):
        self.client.post(self.register_url, self.user_register_data, format='json')
        user_id = CustomUser.objects.get().id
        url = self.api_users + str(user_id) + '/'
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

    def test_user_data_edit_with_owner_authenticated(self):
        self.client.post(self.register_url, self.user_register_data, format='json')
        user_id = CustomUser.objects.get().id
        token = Token.objects.get(user__username=self.user_register_data['username'])
        url = self.api_users + str(user_id) + '/'
        response = self.client.patch(url, {
            'username': self.user_register_data['username'],
            'first_name': self.user_register_data['username'],
            'last_name': 'Rostand',
            'linkedin_link': 'http://www.linkedin.com/in/edmond-rostand',
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
            format='json'
        )
        user = CustomUser.objects.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual({
            response.data['username'],
            response.data['first_name'],
            response.data['last_name'],
            response.data['email'],
            response.data['linkedin_link'],
            response.data['researchgate_link']
            }, {
            user.username,
            user.first_name,
            user.last_name,
            user.email,
            user.linkedin_link,
            user.researchgate_link
            })

    def test_user_data_cannot_edit_with_no_owner_authentication(self):
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, self.user_register_data, format='json')
        self.client.post(self.register_url, second_user_register_data, format='json')

        user_id = CustomUser.objects.get(username=self.user_register_data['username']).id
        token = Token.objects.get(user__username=second_user_register_data['username'])
        url = '/api/users/' + str(user_id) + '/'
        response = self.client.patch(url, {
            'first_name': self.user_register_data['username'],
            'last_name': 'Rostand',
            'linkedin_link': 'http://www.linkedin.com/in/edmond-rostand',
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_user_picture_edit_with_owner_authenticated(self):
    #     # tmp_file = SimpleUploadedFile("file.jpg", "file_content", content_type="image/jpg")
    #     self.client.post(self.register_url, self.user_register_data, format='json')

    #     file = io.BytesIO()
    #     image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    #     image.save(file, 'png')
    #     file.name = 'test.png'
    #     file.seek(0)

    #     profile_image = file

    #     import pdb
    #     pdb.set_trace()
        
    #     token = Token.objects.get(user__username=self.user_register_data['username'])

    #     response = self.client.post('/api/users/profile_picture/', {"profile_image": profile_image},  
    #         headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key), 
    #         content_type = 'multipart/form-data')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestMissionUser(TestMissionUserSetUp):
    def test_missionuser_created_automatically(self):
        """
        User which create the mission has its missionuser 
        automatically created
        """
        missionuser = MissionUser.objects.get()
        response = self.client.get(reverse('missionuser-list'))
        serializer = MissionUserSerializer(missionuser)
        self.assertEqual(response.data[0], serializer.data)

    def test_add_missionuser_if_already_missionuser_of_the_mission(self):
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

        self.client.post(self.register_url, second_user_register_data, format='json')
        response = self.client.post(reverse('missionuser-list'), second_missionuser_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missionuser_data_available_readonly(self):
        missionuser = MissionUser.objects.get()
        response = self.client.get(reverse('missionuser-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missionuser_edit_with_owner_authenticated(self):
        missionuser = MissionUser.objects.get()
        url = reverse('missionuser-detail', kwargs={'pk': str(missionuser.id)})
        response = self.client.patch(url, {
            'job': 'chercheur en acoustique sous-marine',
            'team_lab': 'LGO',
            'description': "déploiement d'un réseau d'hydrophones...",
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),
            format='json'
        )

        edit_missionuser = MissionUser.objects.get()
        serializer = MissionUserSerializer(edit_missionuser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_missionuser_edit_with_no_owner_authentication(self):
        """
        User authenticated but not owner of missionuser can not
        edit missionuser of other user
        """
        second_user_register_data = {
            'username': 'Cyrano',
            'password1': '2BerGe!RAC.',
            'password2': '2BerGe!RAC.',
            'email': 'cyrano@test.com'
        }
        self.client.post(self.register_url, second_user_register_data, format='json')
        token = Token.objects.get(user__username=second_user_register_data['username'])

        missionuser = MissionUser.objects.get()
        url = reverse('missionuser-detail', kwargs={'pk': str(missionuser.id)})
        response = self.client.patch(url, {
            'job': 'chercheur en acoustique sous-marine',
            'team_lab': 'LGO',
            'description': "déploiement d'un réseau d'hydrophones...",
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

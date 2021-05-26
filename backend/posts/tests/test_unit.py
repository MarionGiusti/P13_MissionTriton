"""Unit test for the user application"""
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from missions.models import Mission
from posts.models import Post
from posts.serializers import PostSerializer

from .test_setup import TestPostSetUp

class TestPost(TestPostSetUp):
    def test_user_not_authenticated_can_read_post(self):
        self.client.logout()
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_add_post_event(self):
        response = self.client.post(reverse('post-list'), self.post_data,
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),  format="json")

        post = Post.objects.get()
        serializer = PostSerializer(post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_user_can_edit_post_if_missionuser_of_the_mission(self):
        self.client.post(reverse('post-list'), self.post_data, format="json")
        post = Post.objects.get()
        url = reverse('post-detail', kwargs={"pk": post.id})
        response = self.client.patch(url, {
            'video_url': 'https://www.youtube.com/embed/EmvnIq7ZtVM',
            },
            headers=self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key),
            format="json")
        post = Post.objects.get()
        serializer = PostSerializer(post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q

from users.permissions import IsMissionMemberOrReadOnly
from users.models import MissionUser
from missions.models import Mission
from .serializers import PostSerializer, PictureSerializer
from .models import Post, Picture

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsMissionMemberOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        category = request.GET.get('category')
        mission_id = request.GET.get('missionId')
        queryset = queryset.filter(
            Q(category = category) &
            Q(mission = mission_id)
        ).order_by('-created_at')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        mission_user=MissionUser.objects.get(
            user=request.user.id , mission=data["missionId"])
        mission = Mission.objects.get(id = data["missionId"])
        new_post = Post.objects.create(
            mission_user=mission_user, mission=mission,
            title=data["form"]["title"], content=data["form"]["content"],
            video_url=data["form"]["video_url"], category=data["category"])
        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def post_picture(self, request):
        post = Post.objects.last()
        post.post_image = request.FILES["file"]
        post.save()
        return Response(status=status.HTTP_200_OK,)

    @action(methods=["POST"], detail=False,
        url_path=r'update_post_picture/(?P<post_id>\d+)')
    def update_post_picture(self, request, post_id):
        post = Post.objects.get(id = post_id)
        self.check_object_permissions(request, post)
        post.post_image = request.FILES["file"]
        post.save()
        return Response(status=status.HTTP_200_OK,)

class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pictures to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsMissionMemberOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        mission_id = request.GET.get('missionId')
        queryset = queryset.filter(
            Q(mission = mission_id)
        ).order_by('-created_at')
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False,
        url_path=r'post_picture/(?P<mission_id>\d+)')
    def post_picture(self, request, mission_id):
        images = request.FILES.getlist('file')
        for image in images:
            mission=Mission.objects.get(id=mission_id)
            new_pic = Picture(mission=mission, picture=image)
            self.check_object_permissions(request, new_pic)
            new_pic.save()
            serializer = PictureSerializer(new_pic)
        return Response(status=status.HTTP_200_OK,)

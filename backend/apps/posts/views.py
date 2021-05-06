from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from django.db.models import Q

from .serializers import PostSerializer, PictureSerializer
from .models import Post, Picture
from apps.users.models import MissionUser
from apps.missions.models import Mission


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request):
        queryset= self.get_queryset()
        category = request.GET.get('category')
        mission_id = request.GET.get('missionId') 
        print('BOUH', category, mission_id)       

        queryset = queryset.filter(
            Q(category = category) &
            Q(mission = mission_id)
        ).order_by('-created_at')

        serializer = PostSerializer(queryset, many=True)
        print("serializer.data:", serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        data = request.data

        mission_user=MissionUser.objects.get(user=request.user.id , mission=data["missionId"])
        mission = Mission.objects.get(id = data["missionId"])

        new_post = Post.objects.create(mission_user=mission_user, mission=mission, title=data["form"]["title"], content=data["form"]["content"], video_url=data["form"]["video_url"], category=data["category"])
        
        print("new post:", new_post)
        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data)

    @action(methods=["POST"], detail=False)
    def post_picture(self, request):     
        post = Post.objects.last()
        post.post_image = request.FILES["file"]
        post.save()

        return Response(
           status=status.HTTP_200_OK,
        )

    @action(methods=["POST"], detail=False, url_path=r'update_post_picture/(?P<post_id>\d+)')
    def update_post_picture(self, request, post_id):
        print('FILE', request.FILES["file"])
        print('POSTID', post_id)
        # print("PK", post_id)
        post = Post.objects.get(id = post_id)
        post.post_image = request.FILES["file"]
        post.save()

        return Response(
           status=status.HTTP_200_OK,
        )

class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (AllowAny,)


    def list(self, request):
        queryset= self.get_queryset()
        mission_id = request.GET.get('missionId') 

        queryset = queryset.filter(
            Q(mission = mission_id)
        ).order_by('-created_at')

        serializer = PictureSerializer(queryset, many=True)
        print("serializer.data:", serializer.data)
        return Response(serializer.data)

    
    # def create(self, request, *args, **kwargs):
    #     print("REQUEST DATA", request.data)
    #     data = request.data

    #     mission=MissionUser.objects.get(id=data["form"]["missionId"])
    #     new_pic = Picture.objects.create(mission=mission, title=data["form"]["title"])

    #     new_pic.save()
    #     serializer = PictureSerializer(new_pic)
    #     return Response(serializer.data)


    @action(methods=["POST"], detail=False, url_path=r'post_picture/(?P<mission_id>\d+)')
    def post_picture(self, request, mission_id):
        print('LAALALALA', request.FILES)

        print('MISSION_ID', mission_id)

        images = request.FILES.getlist('file')

        for image in images:
            mission=Mission.objects.get(id=mission_id)
            new_pic = Picture.objects.create(mission=mission, picture=image)
            new_pic.save()
            serializer = PictureSerializer(new_pic)

        return Response(status=status.HTTP_200_OK,)

    @action(methods=["POST"], detail=False, url_path=r'update_post_picture/(?P<post_id>\d+)')
    def update_post_picture(self, request, post_id):
        print('FILE', request.FILES["file"])
        print('POSTID', post_id)
        # print("PK", post_id)
        post = Picture.objects.get(id = post_id)
        post.picture = request.FILES["file"]
        post.save()

        return Response(
           status=status.HTTP_200_OK,
        )
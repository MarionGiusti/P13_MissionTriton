# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, MissionUserSerializer
from .models import CustomUser, MissionUser
from apps.missions.models import Mission

###########
# test customauthtoken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
###########
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    # @action(methods=["POST"], detail=False)
    # def profile_picture(self, request):
    #     print("HEEEEELLLLLLLLOOOOOOO", request.FILES, request.FILES["file"])

    #     return Response(
    #         {"test": "hello"},
    #         status=status.HTTP_200_OK,
    #     )

    @action(methods=["POST"], detail=False)
    def profile_picture(self, request):     
        user = CustomUser.objects.get(id = request.user.id)
        user.profile_image = request.FILES["file"]
        user.save()

        return Response(
            {"test": user.profile_image.name},
            status=status.HTTP_200_OK,
        )

    @action(methods=["POST"], detail=False)
    def background_picture(self, request):
        print("HEEEEELLLLLLLLOOOOOOO", request.FILES, request.FILES["file"])
      
        user = CustomUser.objects.get(id = request.user.id)
        user.profile_background_image = request.FILES["file"]
        user.save()

        return Response(
            {"test": user.profile_background_image.name},
            status=status.HTTP_200_OK,
        )


class MissionUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MissionUser.objects.all()
    serializer_class = MissionUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        print("TRALALA", request.data)
        data = request.data

        mission = Mission.objects.get(name = data["mission"])
        mission_id = mission.id

        # for mail in data["email"]:
            # print("MMMMMM",mail)
            # user = CustomUser.objects.get(email = mail)
            # user_id = user.id
            # new_missionuser = MissionUser(user=user_id, mission=mission_id)
            # new_missionuser.save()
        user = CustomUser.objects.get(email = data["email"])
        user_id = user.id

        new_missionuser = MissionUser.objects.create(user=user, mission=mission)
        print("new missionuser:", new_missionuser)
        new_missionuser.save()

        return Response(
            {"test": new_missionuser},
            status=status.HTTP_200_OK,
        )

    def list(self, request):
        print("HULLOOOOOOO", request.user.id)
        queryset= self.get_queryset()
        # queryset = queryset.filter(user = request.user)
        queryset = queryset.filter(user = request.user.id)
        mission_id = request.GET.get('missionid')
        print("mission_id type", type(mission_id))
        
        if mission_id:
            queryset = queryset.filter(mission__id = mission_id)
        serializer = MissionUserSerializer(queryset, many=True)
        print("serializer.data:", serializer.data)
        return Response(serializer.data)

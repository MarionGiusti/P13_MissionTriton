from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from missions.models import Mission
from .permissions import IsMissionUserOwnerOrReadOnly, IsUserOwnerOrReadOnly
from .serializers import UserSerializer, MissionUserSerializer
from .models import CustomUser, MissionUser

class CustomAuthToken(ObtainAuthToken):
    """
    API endpoint that allows users
    to have a token and be authenticated.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

    def create(self, request):
        data = request.data
        new_user = MissionUser.objects.create(
            email = data["email"], username = data["username"],
            password = data["password1"])
        new_user.save()
        serializer = UserSerializer(new_user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsUserOwnerOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     queryset = CustomUser.objects.all()
    #     serializer = UserSerializer(queryset, many=True, context={"request":request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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
    permission_classes = (IsMissionUserOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        mission = Mission.objects.get(id = data["missionId"])
        user = CustomUser.objects.get(email = data["email"])
        new_missionuser = MissionUser.objects.create(user=user, mission=mission)
        new_missionuser.save()
        serializer = MissionUserSerializer(new_missionuser)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset= self.get_queryset()
        queryset = queryset.filter(user = request.user.id)
        mission_id = request.GET.get('missionid')
        if mission_id:
            queryset = queryset.filter(mission__id = mission_id)
        serializer = MissionUserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=["GET"], detail=False)
    def get_team(self, request):
        mission_id = request.GET.get('missionId')
        team = MissionUser.objects.filter(mission__id = mission_id).values()
        team_mission = []
        for member in team:
            user = CustomUser.objects.filter(id= member["user_id"]).values()
            team_user = {
            'first_name': user[0]["first_name"],
            'last_name': user[0]["last_name"],
            'email': user[0]["email"],
            'picture': user[0]["profile_image"],
            'linkedin': user[0]["linkedin_link"],
            'researchgate': user[0]["researchgate_link"],
            'job': member["job"],
            'team_lab':member["team_lab"],
            'description':member["description"],
            'missionuser_id': member["id"]
            }
            team_mission.append(team_user)
        return Response(data=team_mission)

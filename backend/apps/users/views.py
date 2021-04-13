# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, MissionUserSerializer
from .models import CustomUser, MissionUser


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
        print("HEEEEELLLLLLLLOOOOOOO", request.FILES, request.FILES["file"])
      
        user = CustomUser.objects.get(id = request.user.id)
        user.profile_image = request.FILES["file"]
        user.save()

        print("huuuuuuuuuu", user)
        print("iiiiiiii", user.profile_image.name)
        print("poooooo", user.profile_image.url)

        return Response(
            {"test": user.profile_image.name},
            status=status.HTTP_200_OK,
        )

        # if userserializer.is_valid():
        #     userserializer.save()
        #     return Response(userserializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(userserializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)



class MissionUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MissionUser.objects.all()
    serializer_class = MissionUserSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (AllowAny,)

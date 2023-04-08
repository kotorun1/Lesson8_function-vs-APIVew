from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer, AuthTokenSerializer
from .authentication import BearerAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Регистрации пользователя
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Авторизации пользователя
class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class LogoutView(APIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"message":"Logout sucess"}, status=204)

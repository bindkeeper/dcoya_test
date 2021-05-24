from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializer, UserListSerializer
from rest_framework import status
from .services import create_jwt_and_save_jwt

import logging

logger = logging.getLogger(__name__)


class RegisterNewUser(CreateAPIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = create_jwt_and_save_jwt(user)
            logger.info(f"registered new user name:{user.username}")
            return Response(token, status=status.HTTP_201_CREATED)
        else:
            logger.warning(f"failed to register user")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowClientList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer


class AuthorizeClient(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        logger.info(f"{request.user} passed authentication")
        return Response("Authenticated")

from django.shortcuts import render

from jwt_project import settings
from . import models
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

# FOR USER AUTHENTICATION


# to get refresh token and access token for user
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_token_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data['access'],
                    expires=settings.SIMLE_JWT['ACCCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                )
                response.data = {'Success': "Login successfully", "data": data}
                return response
            else:
                return Response({"No active": "This account is not active!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": "Invalid username or password"}, status=status.HTTP_404_NOT_FOUND)


# FOR BOOKS APIS


class ListBook(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = models.BookModel.objects.all()
    serializer_class = serializers.BookSerializer


class AddBook(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.BookSerializer

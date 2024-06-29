from django.shortcuts import render
from . import models
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import serializers
from rest_framework.permissions import IsAuthenticated


class ListBook(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = models.BookModel.objects.all()
    serializer_class = serializers.BookSerializer


class AddBook(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.BookSerializer

from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookModel
        fields = '__all__'

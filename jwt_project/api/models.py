from django.contrib.auth.models import AbstractUser
from django.db import models


# for custom user authentication
class CustomUserAuthentication(AbstractUser):
    email = models.EmailField(unique=True)


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(unique=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title

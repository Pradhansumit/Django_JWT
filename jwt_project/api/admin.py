from django.contrib import admin
from .models import BookModel, CustomUserAuthentication

admin.site.register(BookModel)
admin.site.register(CustomUserAuthentication)

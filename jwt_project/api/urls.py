from django.urls import path
from . import views
urlpatterns = [
    path('ListBook/', views.ListBook.as_view(), name="ListBook"),
    path('AddBook/', views.AddBook.as_view(), name="AddBook"),
]

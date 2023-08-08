from django.urls import path

from authors.views import register

urlpatterns = [
    path("register/", register, name='register'),
]

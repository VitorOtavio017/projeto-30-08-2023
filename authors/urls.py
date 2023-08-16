from django.urls import path

from authors.views import register_create, register_register, login_create, login_view, logout_view

urlpatterns = [
    path("register/create/", register_create, name='authors-create'),
    path("register/", register_register, name='authors-register'),
    path("login/create/", login_view, name='authors-login'),
    path("login/", login_create, name='authors-login-create'),
    path("logout/", logout_view, name='authors-logout'),
]

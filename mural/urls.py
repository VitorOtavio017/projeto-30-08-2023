from django.urls import path
from mural.views import index, login, register, menu, sobre, mycards, create_card

urlpatterns = [
    path('', index, name="projeto-index"),
    path('login/', login, name="projeto-login"),
    path('menu/', menu, name="projeto-menu"),
    path('sobre/', sobre, name="projeto-sobre"),
    path('mycards/', mycards, name="projeto-mycards"),
    path('create-cards/', create_card, name="create-cards"),

]

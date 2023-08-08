from django.urls import path
from mural.views import index, login, register, menu, sobre, mycards

urlpatterns = [
    path('', index, name="projeto-index"),
    path('login/', login, name="projeto-login"),
    path('register/', register, name="projeto-register"),
    path('menu/', menu, name="projeto-menu"),
    path('sobre/', sobre, name="projeto-sobre"),
    path('mycards/', mycards, name="projeto-mycards"),
    # path('cards/<int:id>/', cards, name="projeto-cards")
]

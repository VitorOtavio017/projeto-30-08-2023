from django.urls import path

from authors.views import register_create, register_register, login_create, login_view, logout_view, projetos, projetos_card_edit, projetos_card_new, projetos_card_delete

urlpatterns = [
    path("register/create/", register_create, name='authors-create'),
    path("register/", register_register, name='authors-register'),
    path("login/create/", login_view, name='authors-login'),
    path("login/", login_create, name='authors-login-create'),
    path("logout/", logout_view, name='authors-logout'),
    path("projetos/", projetos, name='authors-projetos'),
    path("projetos/card/new", projetos_card_new, name='authors-projetos-card-new'),
    path("projetos/card/<int:id>/edit", projetos_card_edit, name='authors-projetos-card-edit'),
    path("projetos/card/delete", projetos_card_delete, name='authors-projetos-card-delete'),

]

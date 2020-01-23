from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resultado/", views.resultado, name="resultado"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("teste/<str:doenca>", views.teste, name="TESTE"),

]

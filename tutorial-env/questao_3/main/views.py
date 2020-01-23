from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GetDiseases, Login
from .models import Doencas


def index(request) -> render:
    doencas_a_pesquisar = GetDiseases()
    return render(request, "main/inicio.html", {"form": doencas_a_pesquisar})


def resultado(response) -> render:
    pass


def login(response) -> render:
    usuario = Login()
    return render(response, "main/login.html", {"form": usuario})


def signup(response) -> render:
    pass


def teste(request, doenca):
    return HttpResponse(Doencas.objects.filter(doenca__iexact=doenca).values()[0]['doenca'])

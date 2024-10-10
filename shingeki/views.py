from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html") #pagina home do projeto

def root_view(request):
    return render(request, "root.html") #pagina inicial do runserver

def dev(request):
    return render(request, "dev.html") #Pagina sobre a desenvolvedora

def tropas(request):
    return render(request, "tropas.html") #Pagina sobre as tropas

def titans(request):
    return render(request, "titans.html") #Pagina sobre os titans

def muralhas(request):
    return render(request, "muralhas.html") #Pagina das muralhas Maria, Rose, Sina

def personagens(request):
    return render(request, "personagens.html") #Pagina de personagens
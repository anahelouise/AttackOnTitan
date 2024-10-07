from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html") #pagina home do projeto

def root_view(request):
    return render(request, "home.html") #pagina inicial do runserver

def dev(request):
    return render(request, "dev.html") #Pagina sobre a desenvolvedora

def tropas(request):
    return render(request, "tropas.html") #Pagina sobre as tropas
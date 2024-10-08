from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "inicio.html") #pagina home do projeto

def root_view(request):
    return render(request, "root.html") #pagina inicial do runserver

def dev(request):
    return render(request, "dev.html") #Pagina sobre a desenvolvedora

def tropas(request):
    return render(request, "tropas.html") #Pagina sobre as tropas
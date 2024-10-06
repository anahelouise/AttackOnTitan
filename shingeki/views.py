from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_view(request):
    return HttpResponse("Uma teste string de resposta")

def home(request):
    return render(request, "homepage.html")

def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")

def root_view(request):
    return render(request, "homepage.html")

def contexto(request):
    context = {
        'nome': 'Ana Helouise',
        'idade': 20,
        'hobbies': ['Ouvir musicas', 'Assistir Shingeki no Kyojin', 'Programar']
    }
    return render(request, 'contexto.html', context)

def anahelouise(request):
    return render(request, "anahelouise.html")
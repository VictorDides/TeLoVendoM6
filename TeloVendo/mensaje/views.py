from django.shortcuts import render
from django.http import HttpResponse

publicaciones = [
    {
        'autor': "autor1",
        'titulo': "titulo1",
        'fecha':"13 de julio 2023"
    },
    {
        'autor': "autor2",
        'titulo': "titulo2",
        'fecha':"12 de julio 2023"
    }

]
def mensaje_bienvenida(request):
    return HttpResponse("<h1> Bienvenidos a TeLoVendo </h1>")

def home(request):
    contexto ={
        'publicaciones': publicaciones
    }
    return render(request,'mensaje/index.html', contexto)
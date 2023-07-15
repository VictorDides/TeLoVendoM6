from django.shortcuts import render
from django.http import HttpResponse

clientes = [
    {
        'nombre': 'Cliente 1',
        'edad': 30,
        'correo': 'cliente1@example.com',
        'telefono': '1234567890',
        'direccion': 'Calle 1, Ciudad 1'
    },
    {
        'nombre': 'Cliente 2',
        'edad': 25,
        'correo': 'cliente2@example.com',
        'telefono': '9876543210',
        'direccion': 'Calle 2, Ciudad 2'
    },
    {
        'nombre': 'Cliente 3',
        'edad': 35,
        'correo': 'cliente3@example.com',
        'telefono': '5678901234',
        'direccion': 'Calle 3, Ciudad 3'
    },
    {
        'nombre': 'Cliente 4',
        'edad': 40,
        'correo': 'cliente4@example.com',
        'telefono': '4321098765',
        'direccion': 'Calle 4, Ciudad 4'
    },
    {
        'nombre': 'Cliente 5',
        'edad': 28,
        'correo': 'cliente5@example.com',
        'telefono': '9012345678',
        'direccion': 'Calle 5, Ciudad 5'
    }
]

def funcion_preliminar(request):
    return HttpResponse("<h1> Bienvenidos a TeLoVendo </h1>")

def landing(request):
    contenido = {
        'clientes': clientes
    }
    return render(request,'Pagina/landing.html', contenido)


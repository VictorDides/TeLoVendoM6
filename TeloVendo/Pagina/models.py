from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicacion(models.Model):
    nombre = models.CharField(max_length=254)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=254)
    telefono = models.TextField()
    direccion = models.CharField(max_length=254)

# Create your models here.

from django.db import models
from pais.models import Pais

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    nit = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    creacion_fecha = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return str (self.nombre) 


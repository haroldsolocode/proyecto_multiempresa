from django.db import models

class Empresa(models.Model):
    PAISES_LATAM = [
        ('AR', 'Argentina'), ('BO', 'Bolivia'), ('BR', 'Brasil'), ('CL', 'Chile'),
        ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('DO', 'República Dominicana'),
        ('EC', 'Ecuador'), ('SV', 'El Salvador'), ('GT', 'Guatemala'), ('HN', 'Honduras'),
        ('MX', 'México'), ('NI', 'Nicaragua'), ('PA', 'Panamá'), ('PY', 'Paraguay'),
        ('PE', 'Perú'), ('PR', 'Puerto Rico'), ('UY', 'Uruguay'), ('VE', 'Venezuela'),
        ('US', 'Estados Unidos'), ('ES', 'España')
    ]

    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=50, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    pais = models.CharField(max_length=2, choices=PAISES_LATAM)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


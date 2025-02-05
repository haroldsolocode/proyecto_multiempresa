from django.db import models
from django.contrib.auth.models import AbstractUser
from empresas.models import Empresa
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your models here.
class Usuario(AbstractUser):
    ADMIN = 'admin'
    CLIENTE = 'cliente'
    ROLES = [(ADMIN, 'Admin'), (CLIENTE, 'Cliente')]
    
    rol = models.CharField(max_length=10, choices=ROLES)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    activation_token = models.CharField(max_length=50, blank=True, null=True)
    
    def generate_activation_token(self):
        self.activation_token = get_random_string(50)
        self.save()
    
    def send_activation_email(self):
        activation_link = f"http://localhost:8000/api/activate/{self.activation_token}/"
        send_mail(
            'Activa tu cuenta',
            f'Haz clic en el siguiente enlace para activar tu cuenta: {activation_link}',
            'noreply@multiempresa.com',
            [self.email],
            fail_silently=False,
        )

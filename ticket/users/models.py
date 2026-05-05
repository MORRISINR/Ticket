from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Tipos de usuario (roles)
    ROLE_CHOICES = (
        ('ADMINISTRADOR', 'ADMINISTRADOR'),
        ('TRABAJADOR', 'TRABAJADOR'),
        ('USUARIO', 'USUARIO'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USUARIO')

    # Campos extra opcionales
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'ticket_usuarios'
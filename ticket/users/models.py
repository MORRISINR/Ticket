from django.contrib.auth.models import AbstractUser
from django.db import models
from constants import DEPARTAMENTOS


class Usuario(AbstractUser):
    # Tipos de usuario (roles)
    email = models.EmailField(
        unique=True, error_messages={"unique": "Ya existe un usuario con ese correo."}
    )
    
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "Ya existe un usuario con ese nombre."
        }
    )

    class Roles(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRATOR", "ADMINISTRADOR"
        TRABAJADOR = "TRABAJADOR", "TRABAJADOR"
        USUARIO = "USUARIO", "USUARIO"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USUARIO)
    # Campos extra opcionales
    phone = models.CharField(max_length=10)
    department = models.CharField(
        max_length=100,
        choices=DEPARTAMENTOS,
        blank=True,
    )
    is_verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Convertir a mayúsculas antes de guardar
        if self.username:
            self.username = self.username.upper()
        if self.phone:
            self.phone = self.phone.upper()
        if self.department:
            self.department = self.department.upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "ticket_usuarios"
        managed = True

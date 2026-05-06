from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'phone',
            #'role',
            'department',
            'password1',
            'password2',
        )
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'phone': 'Teléfono o Anexo',
            'department': 'Departamento',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():

            if name == "email":
                field.widget.attrs.update({
                    "class": "form-control",
                    "style": "text-transform: none;"
                })
            else:
                field.widget.attrs.update({
                    "class": "form-control",
                    "style": "text-transform: uppercase;"
                })
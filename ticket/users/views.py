from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # luego creamos esta ruta
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})
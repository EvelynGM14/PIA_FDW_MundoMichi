from django.shortcuts import render, redirect
from .forms import FormularioAdopcion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Asegúrate de que 'index' esté en urls.py
        else:
            print("Error en formulario de login:", form.errors)  # Ver errores en la consola
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')  # Redirige a la página principal
        else:
            print("Error en formulario de registro:", form.errors)  # Ver errores en la consola
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login o a donde prefieras


@login_required
def index(request):
    return render(request, 'index.html')

def tipos_de_gatos(request):
    return render(request, 'TiposDeGatos.html')

def alimentacion(request):
    return render(request, 'Alimentacion.html')

def cuidado(request):
    return render(request, 'Cuidado.html')

def adopcion(request):
    return render(request, 'Adopcion.html')

def formulario_adopcion(request):
    if request.method == 'POST':
        form = FormularioAdopcion(request.POST)
        if form.is_valid():
            return render(request, 'gracias.html') 
    else:
        form = FormularioAdopcion()

    return render(request, 'adopcion_form.html', {'form': form})


from django.shortcuts import render
from .forms import FormularioAdopcion

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
            # Aquí puedes guardar los datos en la base de datos o realizar otras acciones
            # form.save()  # Si estuviera conectado a un modelo, por ejemplo.
            return render(request, 'gracias.html')  # Página de gracias después de enviar el formulario
    else:
        form = FormularioAdopcion()

    return render(request, 'adopcion_form.html', {'form': form})


from django import forms

class FormularioAdopcion(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=15)
    email = forms.EmailField(label='Correo Electrónico')
    direccion = forms.CharField(label='Dirección', max_length=255)
    tipo_vivienda = forms.ChoiceField(label='Tipo de Vivienda', choices=[('Casa', 'Casa'), ('Departamento', 'Departamento')])
    mascotas_actuales = forms.BooleanField(label='¿Tienes mascotas actualmente?', required=False)
    experiencia = forms.CharField(label='Experiencia con Mascotas', widget=forms.Textarea)
    razon_adopcion = forms.CharField(label='Razón para la Adopción', widget=forms.Textarea)


from django.db import models

class SolicitudAdopcion(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    tipo_vivienda = models.CharField(max_length=50)
    mascotas_actuales = models.BooleanField()
    experiencia = models.TextField()
    razon_adopcion = models.TextField()

    def __str__(self):
        return self.nombre


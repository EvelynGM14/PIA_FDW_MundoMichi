
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('TiposDeGatos/', views.tipos_de_gatos, name='TiposDeGatos'),
    path('Alimentacion/', views.alimentacion, name='Alimentacion'),
    path('Cuidado/', views.cuidado, name='Cuidado'),
    path('Adopcion/', views.adopcion, name='Adopcion'),
]

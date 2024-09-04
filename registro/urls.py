from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('registrar_propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('registrar_vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('registrar_registro/', views.registrar_registro, name='registrar_registro'),
    path('ver_propietarios/', views.ver_propietarios, name='ver_propietarios'),
    path('ver_vehiculos/', views.ver_vehiculos, name='ver_vehiculos'),
    path('ver_registros/', views.ver_registros, name='ver_registros'),
]

from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Vehiculo, Registro
from .forms import PropietarioForm, VehiculoForm, RegistroForm

def registrar_propietario(request):
    if request.method == "POST":
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro:ver_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'registro/registrar_propietario.html', {'form': form})

def registrar_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro:ver_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'registro/registrar_vehiculo.html', {'form': form})

def registrar_registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro:ver_registros')
    else:
        form = RegistroForm()
    return render(request, 'registro/registrar_registro.html', {'form': form})

def ver_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'registro/ver_propietarios.html', {'propietarios': propietarios})

def ver_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'registro/ver_vehiculos.html', {'vehiculos': vehiculos})

def ver_registros(request):
    registros = Registro.objects.all()
    return render(request, 'registro/ver_registros.html', {'registros': registros})

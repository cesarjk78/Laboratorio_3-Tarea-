from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=200)
    numero_apartamento = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.modelo}"

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehiculo.matricula} - {self.fecha_hora_entrada}"

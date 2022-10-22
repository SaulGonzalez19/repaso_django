from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()

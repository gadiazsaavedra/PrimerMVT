from django.db import models

# import datetime

# Create your models here.
class Familia(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    rol = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    fecha_de_nacimiento = models.DateField()

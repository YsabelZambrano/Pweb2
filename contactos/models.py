from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.IntegerField()

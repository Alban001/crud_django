from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    ciudad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
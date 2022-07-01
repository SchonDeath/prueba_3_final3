from django.db import models

# Create your models here.
class personas(models.Model):
    rut=models.CharField(max_length=12)
    nombre=models.CharField(max_length=30)
    apellido_parterno=models.CharField(max_length=30)
    apellido_materno=models.CharField(max_length=30)
    edad=models.CharField(max_length=30)
    nombreVacuna=models.CharField(max_length=3)
    fecha=models.CharField(max_length=30)


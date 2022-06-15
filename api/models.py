from django.db import models

# Create your models here.

class Contador(models.Model):
    numero = models.IntegerField()
    mensaje = models.CharField(max_length=100)


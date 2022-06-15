from django.db import models

# Create your models here.

class Contador(models.Model):
    mensaje = models.CharField(max_length=100)


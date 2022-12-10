from django.conf import settings
from django.db import models

# Create your models here.
class portafolio(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    foto = models.URLField(max_length=200)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    etiqueta = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.titulo

class ips(models.Model):
    ip = models.CharField(max_length=50)
    enrutable = models.CharField(max_length=50)

    def __str__(self):
        return self.ip
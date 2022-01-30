from django.db import models

# Create your models here.

class Autoridade(models.Model):
    nome = models.CharField(
         verbose_name= "Nome",
         max_length= 60
    )
    email = models.EmailField(
         verbose_name= "E-mail",
         max_length= 60
    )
    contato = models.CharField(
         verbose_name= "Número para contato",
         max_length= 25
    )
    latitude = models.CharField(
        verbose_name= "Latitude",
        max_length= 60
    )
    longitude = models.CharField(
        verbose_name= "Longitude",
        max_length= 60
    )
    uf = models.CharField(
        verbose_name= "UF",
        max_length= 2
    )
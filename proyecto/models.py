from django.db import models
from django.contrib.auth.models import *


# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(
        null=False,
        max_length=100,
        verbose_name='Titulo'
    )

    texto = models.CharField(
        null=False,
        max_length=1000,
        verbose_name='Texto'
    )

    post_status_choices = [
        ("DRAFT","Borrador"),
        ("Publish","Publicado")
    ]
    estado = models.CharField(
        default="DRAFT",
        choices=post_status_choices,
        null=False,
        max_length=200,
        verbose_name="Estado"
    )

    user = models.ForeignKey(
        User,null=True,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        auto_now=True,null=True
    )

class Comentario(models.Model):

    texto = models.CharField(
        null=False,
        max_length=1000,
        verbose_name='Texto'
    )

    user = models.ForeignKey(
        User,null=True,
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        auto_now=True,null=True
    )

    publicacion = models.ForeignKey(
        Publicacion,
        null=True,
        on_delete=models.CASCADE
    )
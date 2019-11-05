from django.contrib import admin
from . import models
# Register your models here.
admin .site.register(models.Publicacion)
admin .site.register(models.Comentario)
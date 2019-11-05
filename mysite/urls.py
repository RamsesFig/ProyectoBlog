from django.contrib import admin
from django.urls import path
from django.conf import settings
from proyecto import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',v.home,name="Home"),
    path('Salir/',v.salir_view,name="Salir"),
    path('Registro/',v.registro_view,name="Registro"),
    path('Ingresar/',v.ingresar_view,name="Ingresar"),

    path('Publicar/', v.publicar_view, name='Publicar'),
    path('VerPublicaciones/',v.verpublicaciones_view, name='VerPublicaciones'),
    path('LeerPublicacion/<int:publicacion_pk>/', v.leerpublicaciones_view, name='LeerPublicacion'),
    path('Modificar/<int:publicacion_pk>/', v.modificar_view, name='Modificar'),
]

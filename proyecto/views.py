from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from . import forms as r
from . import  models as m
from django.http import HttpResponseRedirect

def redirect_root(request):
      return HttpResponseRedirect('/usuarios/Home/')

def home(request):
    return render(request,'usuarios/home.html',{})

def leerpublicacion(request):
    return render(request,'publicaciones/LeerPublicacion.html',{})

def registro_view(request):
    if request.method == 'POST':
        registro_form = r.RegistroForm(request.POST)
        if registro_form.is_valid():
            username = registro_form.cleaned_data['username']
            first_name = registro_form.cleaned_data['first_name']
            last_name = registro_form.cleaned_data['last_name']
            email = registro_form.cleaned_data['email']
            password = registro_form.cleaned_data['password']

            usuarioNuevo = User(username=username, first_name=first_name, last_name= last_name, email=email)
            usuarioNuevo.set_password(password)
            usuarioNuevo.save()
            login(request,usuarioNuevo)
            return redirect(home)

    else:
         registro_form = r.RegistroForm()
    return render(request,'usuarios/Registro.html',{'RegistroForm': registro_form})

def salir_view(request):
    logout(request)
    return redirect(home)

def ingresar_view(request):
    if request.method == 'POST':
        ingresar_form = r.IngresarForm(request.POST)
        if ingresar_form.is_valid():
            username = ingresar_form.cleaned_data['username']
            print(username)
            password = ingresar_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request,'usuarios/Ingresar.html',{'form': ingresar_form})
            login(request,user)
            return redirect(home)
    else:
        ingresar_form = r.IngresarForm()
    return render(request,'usuarios/Ingresar.html',{'IngresarForm': ingresar_form})

def publicar_view(request):
    usuario = request.user
    form = r.PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']
            estado = form.cleaned_data['estado']

            publicacionNueva = m.Publicacion()
            publicacionNueva.titulo = titulo
            publicacionNueva.texto = texto
            publicacionNueva.estado = estado
            publicacionNueva.user = usuario
            publicacionNueva.save()

            return redirect(home)
    form=r.PostForm()
    return render(request,'publicaciones/Publicar.html',{'form': form})

def verpublicaciones_view(request):
    publicaciones = m.Publicacion.objects.all().order_by('-date')
    return render(request, 'publicaciones/VerPublicaciones.html', {'publicaciones': publicaciones})

def leerpublicaciones_view(request,publicacion_pk):
    publicacion = m.Publicacion.objects.get(id=publicacion_pk)
    comentarios = m.Comentario.objects.all().order_by('-date')
    formulario = r.Comentario()
    if request.method == 'POST':
        # Get: Form from the request #
        post_comment_form = r.Comentario(request.POST)
        if post_comment_form.is_valid():
            # Create: new post comment #
            comentario = m.Comentario()
            comentario.publicacion = m.Publicacion.objects.get(id=publicacion_pk)
            comentario.user = request.user
            comentario.texto = post_comment_form.cleaned_data['texto']

            # Save: new post comment #
            comentario.save()
    return render(request, 'publicaciones/LeerPublicacion.html', {
        'publicacion': publicacion,
        'formulario' : formulario,
        'comentarios' : comentarios
    })

def modificar_view(request, publicacion_pk):
    publicacion = get_object_or_404(m.Publicacion, id=publicacion_pk)
    usuario = request.user
    if request.method == "POST":
        form = r.PostForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            texto = form.cleaned_data['texto']
            estado = form.cleaned_data['estado']

            publicacion.titulo = titulo
            publicacion.texto = texto
            publicacion.estado = estado
            publicacion.user = usuario
            publicacion.save()
            return redirect(verpublicaciones_view)
    else:
        form = r.PostForm()
    return render(request, 'publicaciones/Modificar.html', {'form': form})

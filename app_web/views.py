from django.shortcuts import render, redirect, get_object_or_404
from .models import  Perfil, Publicacion
from .form import EditarPerfil, PerfilForm, PublicacionForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def inicio (request):
    return render (request, "app_web/inicio.html")


@login_required
def publicaciones_generales(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion') 
    contexto = {'publicaciones': publicaciones} 
    return render(request, 'app_web/publicaciones_generales.html', contexto)


@login_required
def mis_publicaciones(request):
    if request.user.is_authenticated: 
        publicaciones = Publicacion.objects.filter(autor=request.user)
        return render(request, 'app_web/mis_publicaciones.html', {'publicaciones': publicaciones})
    else:
        return render(request, 'app_web/mis_publicaciones.html', {'mensaje': 'Debes iniciar sesión para ver tus publicaciones.'})
    
@login_required
def publicaciones_formulario(request):
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST, request.FILES)
        if publicacion_form.is_valid():
            publicacion = publicacion_form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('publicaciones-generales')
        else:
            return render(request, 'app_web/form/publicaciones-formulario.html', {'publicacion_form': publicacion_form})
    else:
        publicacion_form = PublicacionForm()
    return render(request, 'app_web/form/publicaciones-formulario.html', {'publicacion_form': publicacion_form})


def acerca_de_mi (request):
    return render (request, "app_web/acerca_de_mi.html")


@login_required
def eliminar_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id) 
    publicacion.delete()
    return redirect('publicaciones-generales') 


@login_required
def editar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST, request.FILES, instance=publicacion) #instancia el formulario con los datos y la instancia
        if publicacion_form.is_valid():
            publicacion_form.save()
            return redirect('mis-publicaciones')
    else:
        publicacion_form = PublicacionForm(instance=publicacion) #instancia el formulario con la instancia para mostrar los datos actuales
    return render(request, 'app_web/editar_publicacion.html', {'publicacion_form': publicacion_form})


@login_required
def detalle_publicacion (request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'app_web/detalle_publicacion.html', {'publicacion': publicacion})


def inicio_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {"success_message": "Inicio de sesión exitoso"}
            return render(request, "app_web/form/inicio-sesion.html", context)  # Renderiza con mensaje
        else:
            context = {"error": "Usuario o contraseña incorrectos"}
            return render(request, "app_web/form/inicio-sesion.html", context)
    else:
        return render(request, "app_web/form/inicio-sesion.html")
    
@login_required
def cerrar_sesión(request):
        logout(request)
        return redirect ("inicio-sesion")
    
    
def registro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = UserCreationForm()
    return render(request, "app_web/form/registro-usuario.html", {"form": form})


@login_required
def mostrar_perfil(request):
    return render(request, "app_web/mostrar_perfil.html")


@login_required
def editar_perfil(request):
    usuario = request.user
    perfil, _ = Perfil.objects.get_or_create(user=usuario)
    if request.method == "POST":
        user_form = EditarPerfil(request.POST, instance=usuario)
        profile_form = PerfilForm(request.POST, request.FILES, instance=perfil) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("mostrar-perfil")
        else:
            return redirect("inicio")
    else:
        user_form = EditarPerfil(instance=usuario)
        profile_form = PerfilForm(instance=perfil) 
    return render(request, "app_web/form/editar-perfil.html", {"user_form": user_form,"profile_form": profile_form})


@login_required
def cambiar_contraseña(request):
    usuario = request.user
    if request.method == "POST":
        form_password = PasswordChangeForm(usuario, request.POST)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, usuario)
            return redirect("inicio")
        else:
            return redirect("inicio")
    else:
        form_password = PasswordChangeForm(usuario)
    return render(request, "app_web/form/cambiar-contraseña.html", {"form_password":form_password})
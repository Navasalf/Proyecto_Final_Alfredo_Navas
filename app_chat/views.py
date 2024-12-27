from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.models import User
from .models import Mensaje
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def enviar_mensaje(request, usuario_id):
    destinatario = get_object_or_404(User, pk=usuario_id)
    
    if request.method == "POST":
        destinatario_username = request.POST.get("destinatario")
        contenido = request.POST.get("contenido")

        if contenido and destinatario_username:
            destinatario = User.objects.get(username=destinatario_username)
            Mensaje.objects.create(remitente=request.user, destinatario=destinatario, contenido=contenido)
            return redirect("ver-mensaje")

    usuarios = User.objects.exclude(username=request.user.username)
    return render(request, "app_chat/enviar_mensajes.html", {"usuarios": usuarios})


@login_required
def ver_mensaje(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user) 
    return render(request, "app_chat/ver_mensajes.html", {"mensajes": mensajes})
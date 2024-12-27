from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')  # Add related_name
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')  # Add related_name
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario}"
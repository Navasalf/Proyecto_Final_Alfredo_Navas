from django.db import models
from django.contrib.auth.models import User  

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True, null=True) #opcional
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # Relación con el autor (usuario)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_portada = models.ImageField(upload_to='blog/portadas/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_publicacion']


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="perfil_imagen/", null=True, blank=True)
from django.urls import path
from .views import enviar_mensaje, ver_mensaje


urlpatterns = [
    path('enviar-mensaje/', enviar_mensaje, name="enviar-mensaje"),
    path('enviar-mensaje/<int:usuario_id>', enviar_mensaje, name="enviar-mensaje"),
    path('ver-mensaje/', ver_mensaje, name="ver-mensaje"),
]
from django.urls import path
from .views import enviar_mensaje, ver_mensaje, seleccionar_destinatario


urlpatterns = [
    path('seleccionar-destinatario/', seleccionar_destinatario, name="seleccionar-destinatario"),
    path('enviar-mensaje/<int:usuario_id>', enviar_mensaje, name="enviar-mensaje"),
    path('ver-mensaje/', ver_mensaje, name="ver-mensaje"),
]
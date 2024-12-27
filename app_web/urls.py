from django.urls import path
from app_web.views import inicio, mis_publicaciones, acerca_de_mi, inicio_sesion, cerrar_sesión, registro_usuario, mostrar_perfil, editar_perfil, cambiar_contraseña, publicaciones_generales, publicaciones_formulario, detalle_publicacion, eliminar_publicacion, editar_publicacion

urlpatterns = [
    
    path('', inicio, name="inicio"),
    path('acerca_de_mi/', acerca_de_mi, name="acerca_de_mi"),
    
    path('publicaciones-generales/', publicaciones_generales, name="publicaciones-generales"),
    path('mis-publicaciones/', mis_publicaciones, name="mis-publicaciones"),
    path("detalle-publicacion/<int:pk>/", detalle_publicacion, name="detalle-publicacion"),
    path("eliminar-publicacion/<int:id>", eliminar_publicacion, name="eliminar-publicacion"),
    path("publicaciones-formularios/", publicaciones_formulario, name="publicaciones-formulario"),
    path("editar-publicacion/<int:publicacion_id>", editar_publicacion, name="editar-publicacion"),
    
    path("inicio-sesion/", inicio_sesion, name="inicio-sesion"),
    path("cerrar-sesión/",cerrar_sesión, name="cerrar-sesión"),
    path("registro-usuario/",registro_usuario, name="registro-usuario"),
    path("mostrar-perfil/", mostrar_perfil, name="mostrar-perfil"),
    path("editar-perfil/", editar_perfil, name="editar-perfil"),
    path("cambiar-contraseña/", cambiar_contraseña, name="cambiar-contraseña"),
    
]
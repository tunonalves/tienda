from django.urls import path 
from . import views
from .views import VRegistro, cerrar_seccion, loguear, user_edit


urlpatterns = [
    path('',VRegistro.as_view(), name="autenticacion"),
    path('cerrar_seccion',cerrar_seccion, name="cerrar_seccion"),
    path('loguear',loguear, name="loguear"),
    path('edit',user_edit, name="edit"),

    path('user/list/', views.UserList.as_view(), name='user_list'),
    path('user/<pk>', views.UserDetalle.as_view(), name='user_detalle'),
    path('user/nuevo/', views.UserCreacion.as_view(), name='user_crear'),
    path('user/editar/<pk>', views.UserEdicion.as_view(), name='user_editar'),
    path('user/borrar/<pk>', views.UserEliminacion.as_view(), name='user_borrar'),
]

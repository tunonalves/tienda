from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('',views.blog, name="Blog"),
    path('post/',views.formpost,name="post"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
   
    path('post/list/', views.PostList.as_view(), name='post_list'),
    path('post/<pk>', views.PostDetalle.as_view(), name='post_detalle'),
    path('post/nuevo/', views.PostCreacion.as_view(), name='post_crear'),
    path('post/editar/<pk>', views.PostEdicion.as_view(), name='post_editar'),
    path('post/borrar/<pk>', views.PostEliminacion.as_view(), name='post_borrar'),
]
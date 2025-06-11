from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# DjangoCMS URL Configuration for the CMS application
# This file defines the URL patterns for the DjangoCMS application.
urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('articulo/<int:id>/', views.detalle_articulo, name='detalle_articulo'),
    path('categoria/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),

    # Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='cms/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='lista_articulos'), name='logout'),

    # Registro de usuarios
    path('registro/', views.registro, name='registro'),

    path('articulo/<int:id>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:id>/eliminar/', views.eliminar_articulo, name='eliminar_articulo'),
]

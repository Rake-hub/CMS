from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Articulo, Categoria, Usuario

# Register your models here.

"""  First draft of admin.py for DjangoCMS project
admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Usuario)  # Register the custom user model if needed
"""


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    pass

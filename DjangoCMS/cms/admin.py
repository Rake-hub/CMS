from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Articulo, Categoria, Usuario

# Register your models here.


admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Usuario)  # Register the custom user model if needed

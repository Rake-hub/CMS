from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Models for a simple blog application
# with categories and articles, including a custom user model.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
### ---

class Articulo(models.Model):
    ESTADOS = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='borrador')

    def __str__(self):
        return self.titulo

### ---


class Usuario(AbstractUser):
    # Custom user model extending AbstractUser
    # You can add additional fields if needed
    #pass
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


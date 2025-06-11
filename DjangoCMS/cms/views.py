from django.shortcuts import render

# Create your views here.

from .models import Articulo

def lista_articulos(request):
    articulos = Articulo.objects.filter(estado='publicado').order_by('-fecha_creacion')
    return render(request, 'cms/lista_articulos.html', {'articulos': articulos})

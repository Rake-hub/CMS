from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.

#Lista de artículos publicados
from .models import Articulo

def lista_articulos(request):
    articulos = Articulo.objects.filter(estado='publicado').order_by('-fecha_creacion')
    return render(request, 'cms/lista_articulos.html', {'articulos': articulos})


#Detalle de un artículo
from django.shortcuts import get_object_or_404

def detalle_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    return render(request, 'cms/detalle_articulo.html', {'articulo': articulo})


#Artículos por categoría
from .models import Categoria

def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulo.objects.filter(categoria=categoria, estado='publicado')
    return render(request, 'cms/articulos_por_categoria.html', {
        'categoria': categoria,
        'articulos': articulos
    })


#Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cms/registro.html', {'form': form})



# Edición y eliminación de artículos (solo para autores o superusers)
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)

    # Permitir solo al autor o superuser
    if request.user != articulo.autor and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        articulo.titulo = request.POST['titulo']
        articulo.contenido = request.POST['contenido']
        articulo.save()
        return redirect('detalle_articulo', id=articulo.id)
    
    return render(request, 'cms/editar_articulo.html', {'articulo': articulo})

@login_required
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)

    if request.user != articulo.autor and not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        articulo.delete()
        return redirect('lista_articulos')

    return render(request, 'cms/eliminar_articulo.html', {'articulo': articulo})

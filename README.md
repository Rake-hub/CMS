# CMS
Desarrollar un sistema de gestión de contenidos (CMS) desde cero utilizando el framework Django (Python)

---
---

# Pasos:

## Requisitos previos 

Instalar Visual Studio Code con la extensión de Python 

Instalar Python

Instalar Django

---

## Parte 1

### 1 Crear un nuevo proyecto Django

Terminal:

    django-admin startproject DjangoCMS
        
    cd DjangoCMM

### 2 Crear una aplicación Django llamada cms

Terminal:

    python manage.py startapp cms

Esto crea una carpeta cms/ con esta estructura:
cms/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── __init__.py


### 3 Configurar la base de datos

edita el archivo:

DjangoCMS/settings.py, sección DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Por defecto Django usa SQLite

### 4 Habilitar la app en settings.py 

Abre el archivo DjangoCMS/settings.py.

Busca la lista INSTALLED_APPS.

Agrega 'cms', a esa lista.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'cms', 
]

---

## Parte 2: Modelado de Datos

### 1 Crear el modelo Articulo

Modificar archivo cms/models.py

### 2 Crear el modelo Categoria

Modificar archivo cms/models.py

### 3 Extender el modelo Usuario

En cms/models.py

### 4 Registrar modelos en el admin

En cms/admin.py

### 5 Realizar migraciones y probar el servidor

Ver png servidor

---

## Parte 3: Panel de Administración

### 1 Registrar modelos en admin.py

Ya hecho en Parte 2

### 2 Personalizar la vista del administrador para que sea más intuitiva

En admin.py modificar los modelos

### 3 Probar creación, edición y eliminación de artículos desde admin

Ver png Articulo

---

## Parte 4: Interfaz Web Pública

### 1 Crear vistas para:
####    Listado de artículos
####    Detalle de cada artículo
####    Artículos por categoría

cms/views.py → Aquí crearemos las vistas

### 2 Crear templates HTML base.

Plantillas (templates): las crearemos para mostrar los datos
cms/templates/cms/nombre.html

### 3 Configurar URLs públicas.

cms/urls.py → Aquí registraremos las rutas

---

## Parte 5: Autenticación de Usuarios

### 1 Crear rutas para login, logout y registro de usuarios

Django ya viene con LoginView y LogoutView incorporados.

cms/urls.py

### 2 Restringir edición y eliminación de artículos solo al autor o al admin

cms/views.py

### 3 Añadir navegación condicional según estado de autenticación

templates/cms/base.html
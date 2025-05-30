# CMS
Desarrollar un sistema de gestión de contenidos (CMS) desde cero utilizando el framework Django (Python)

---

# Pasos:

## Necesario 

Instalar Visual Studio Code con la extensión de Python 

Instalar Python

Instalar Django


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


## Parte 2: Modelado de Datos


# CMS en Django

Este proyecto es un CMS (Sistema de Gestión de Contenidos) básico construido con Django, que permite a los usuarios crear, editar, visualizar y eliminar artículos clasificados por categorías.

---

## ¿Qué es un CMS?

Un **CMS** (Content Management System) es una aplicación que permite a los usuarios crear, modificar, organizar y publicar contenido digital fácilmente, sin necesidad de conocimientos técnicos avanzados. Suelen incluir un panel de administración, control de usuarios, permisos y edición en línea.


### Ejemplos populares de CMS

**Open Source:**
- WordPress
- Joomla
- Drupal
- Ghost
- Strapi

**Privados / Comerciales:**
- Webflow
- Wix
- Squarespace
- Contentful
- Shopify (para e-commerce)

---

## Modelo de datos

### `Articulo`
| Campo               | Tipo            | Descripción                         |
|--------------------|-----------------|-------------------------------------|
| `titulo`           | CharField       | Título del artículo                 |
| `contenido`        | TextField       | Cuerpo del contenido                |
| `fecha_creacion`   | DateTimeField   | Fecha en que se creó                |
| `fecha_actualizacion` | DateTimeField | Última edición                      |
| `autor`            | ForeignKey      | Usuario que creó el artículo        |
| `categoria`        | ForeignKey      | Categoría asociada                  |
| `estado`           | CharField       | Publicado / Borrador                |
| `imagen`           | ImageField      | (opcional) Imagen destacada         |

### `Categoria`
| Campo      | Tipo        | Descripción               |
|------------|-------------|---------------------------|
| `nombre`   | CharField   | Nombre de la categoría    |
| `slug`     | SlugField   | URL amigable              |

### `UsuarioPersonalizado` (opcional)
Extiende el modelo base de Django para personalización futura.

---

## ¿Cómo ejecutar el proyecto en local?

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio

2. Crea y activa un entorno virtual:
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate

3. Instala dependencias:
    pip install -r requirements.txt    

4. Crea la base de datos y aplica migraciones:
    python manage.py makemigrations
    python manage.py migrate

5. Crea un superusuario:
    python manage.py createsuperuser

6. Ejecuta el servidor:
    python manage.py runserver

7. Accede en tu navegador a: 
    http://127.0.0.1:8000    


## ¿Cómo desplegar en Railway?

1. Sube tu proyecto a GitHub.

2. Entra a https://railway.app y crea un nuevo proyecto.

3. Elige Deploy from GitHub Repo y selecciona el tuyo.

4. Railway detectará automáticamente el Procfile y comenzará el deploy.

5. Añade las variables de entorno necesarias:

VARIABLE	    VALOR
SECRET_KEY	    Una clave segura
DEBUG	        False
DATABASE_URL	Railway la genera

6. Añade PostgreSQL como plugin si no lo hace automáticamente.

7. Accede al dominio que te asigna Railway para probar tu CMS en producción.



## Usuario Demo

Si quieres probar la versión desplegada, usa el siguiente acceso (si está habilitado):

URL: https://tu-app.railway.app/admin/
Usuario: demo_user
Contraseña: demo1234


---
---


# Proyecto explicado paso a paso:

## Requisitos previos 

Instalar Visual Studio
https://code.visualstudio.com/

Instalar Python
En VS Code, abre la pestaña de extensiones (icono de cuadrados o Ctrl+Shift+X)
Busca e instala "Python" (de Microsoft)

Instalar Django
pip install django
django-admin --version


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

---

## Parte 6: Despliegue del CMS

### 1 Crear repositorio en GitHub

Hecho
https://github.com/Rake-hub/CMS

### 2 Añadir requirements.txt y Procfile 

Desde la raiz DjangoCMS

pip freeze > requirements.txt

touch Procfile

web: gunicorn DjangoCMS.wsgi


DjangoCMS/
├── cms/                # app
├── DjangoCMS/        # configuración Django
├── manage.py
├── requirements.txt    <-- lo acabamos de crear
├── Procfile            <-- lo acabamos de crear


### 3 Configurar variables de entorno (SECRET_KEY, DB, etc.)

Dentro de Railway

Entra a tu proyecto
Ve a la pestaña "Variables" o "Environment"
Ahí verás un botón “New Variable” o directamente una tabla editable

Nombre	Valor	Obligatoria	Descripción
DEBUG	False	✅	Activa modo producción
SECRET_KEY	⚠️ Genera uno seguro (ver abajo)	✅	Protege tu app
DATABASE_URL	✅ Railway la genera automáticamente si usas PostgreSQL	✅	Conexión DB
ALLOWED_HOSTS	* o tu dominio personalizado	✅	Permite conexiones externas
CLOUDINARY_CLOUD_NAME	tu_cloud_name (si usas imágenes en Cloudinary)	❌	Para subir imágenes
CLOUDINARY_API_KEY	1234567890	❌	API key Cloudinary
CLOUDINARY_API_SECRET	a1b2c3d4e5f6	❌	API secret


python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


### 4 Desplegar el proyecto en Railway

Asegúrate de tener listo:

    Tu proyecto Django funcionando localmente.

    Un repositorio en GitHub con el código subido.

    Un archivo requirements.txt generado

Imagenes guardadas en png

pip install gunicorn
pip install dj-database-url
pip install whitenoise

pip freeze > requirements.txt
Configurar settings.py



### 5 Verificar funcionamiento en línea
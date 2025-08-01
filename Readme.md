# Proyecto de Reseñas de Películas

## Descripción
Este proyecto es una aplicación web desarrollada en Django que permite a los usuarios visualizar y buscar películas. Fue desarrollado como parte del Taller 1 de la materia "Proyecto 1" de la Universidad EAFIT, en la carrera de Ingeniería de Sistemas.

**Autor:** Samuel Henao Castrillón  
**Institución:** Universidad EAFIT  
**Materia:** Proyecto 1  
**Taller:** Taller 1

## Características Principales

### Funcionalidades Implementadas
- **Visualización de Películas:** Lista todas las películas disponibles en el sistema
- **Búsqueda por Título:** Permite buscar películas por su título (búsqueda insensible a mayúsculas/minúsculas)
- **Detalles de Película:** Muestra título, descripción, imagen y enlaces externos
- **Panel de Administración:** Interfaz para gestionar películas (crear, editar, eliminar)
- **Diseño Responsivo:** Utiliza Bootstrap 5.3.7 para una interfaz moderna y adaptable

### Tecnologías Utilizadas
- **Backend:** Django (Python)
- **Base de Datos:** SQLite
- **Frontend:** HTML, CSS (Bootstrap 5.3.7)
- **Lenguaje:** Python

## Estructura del Proyecto

```
moviereviewsproject/
├── movie/                    # Aplicación principal
│   ├── models.py            # Modelo de datos (Movie)
│   ├── views.py             # Lógica de negocio
│   ├── admin.py             # Configuración del panel de administración
│   └── Templates/           # Plantillas HTML
│       ├── home.html        # Página principal con búsqueda
│       └── about.html       # Página de información
├── moviereviews/            # Configuración del proyecto
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # Configuración de URLs
│   └── wsgi.py              # Configuración WSGI
└── manage.py                # Script de gestión de Django
```

## Modelo de Datos

### Movie
- **title:** Título de la película (CharField, máximo 100 caracteres)
- **description:** Descripción de la película (CharField, máximo 250 caracteres)
- **image:** Imagen de la película (ImageField, se guarda en 'movie/images/')
- **url:** Enlace externo opcional (URLField, opcional)

## Vistas Implementadas

### Home (Página Principal)
- **URL:** `/`
- **Funcionalidad:** 
  - Muestra todas las películas
  - Permite búsqueda por título
  - Filtra resultados en tiempo real

### About
- **URL:** `/about/`
- **Funcionalidad:** Página de información del proyecto

### Admin
- **URL:** `/admin/`
- **Funcionalidad:** Panel de administración para gestionar películas

## Instalación y Configuración



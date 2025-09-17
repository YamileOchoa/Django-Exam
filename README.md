# Proyecto Django: [Biblioteca virtual]

## Autor
Yamile Ochoa Marin

## Video Funcional
https://youtu.be/FvSxkzeCJ-M

## Descripción
Este proyecto es una aplicación web desarrollada en Django que permite administrar [Entidad 1] y [Entidad 2].  
La aplicación implementa un CRUD completo para ambas entidades y establece la relación necesaria entre ellas.  
Se hizo uso de **templates de Django** para estructurar las páginas y **Bootstrap 5** para mejorar la interfaz y la experiencia del usuario.

## Funcionalidades
- Listado de [Entidad 1] y [Entidad 2]  
- Creación, edición y eliminación de registros  
- Relación entre [Entidad 1] y [Entidad 2] mediante ForeignKey  
- Plantillas base reutilizables para consistencia en todas las vistas  
- Navegación sencilla con navbar y enlaces entre las entidades  
- Interfaz estilizada con Bootstrap

## Estructura de carpetas
src/
├─ [app1]/
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ [app1]_list.html
│  │  └─ [app1]_form.html
│  └─ views.py
├─ [app2]/
│  └─ templates/
│     ├─ [app2]_list.html
│     └─ [app2]_form.html
└─ manage.py

## Tecnologías usadas
- Python 3.x  
- Django 5.x  
- Bootstrap 5  
- HTML5 / CSS3  
- SQLite (por defecto) o cualquier otra base de datos soportada por Django

## Notas
- Todo el CRUD y las vistas fueron programadas manualmente, sin usar Django Admin.  
- Las plantillas permiten reutilizar componentes y mantener un diseño consistente.  



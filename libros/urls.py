from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path("", views.libro_list, name="libro_list"),
    path("libro/create/", views.libro_create, name="libro_create"),
    path("libro/<int:pk>/edit/", views.libro_edit, name="libro_edit"),
    path("libro/<int:pk>/delete/", views.libro_delete, name="libro_delete"),
]

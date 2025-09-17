from django.urls import path
from . import views

app_name = 'autores'

urlpatterns = [
    path("", views.autor_list, name="autor_list"),
    path("autor/create/", views.autor_create, name="autor_create"),
    path("autor/<int:pk>/edit/", views.autor_edit, name="autor_edit"),
    path("autor/<int:pk>/delete/", views.autor_delete, name="autor_delete"),
]
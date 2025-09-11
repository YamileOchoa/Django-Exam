from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_organizadores, name='listar_organizadores'),
    path('nuevo/', views.crear_organizador, name='crear_organizador'),
    path('editar/<int:id>/', views.editar_organizador, name='editar_organizador'),
]
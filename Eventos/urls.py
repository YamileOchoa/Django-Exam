from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_eventos, name='listar_eventos'),
    path('nuevo/', views.crear_evento, name='crear_evento'),
    path('editar/<int:id>/', views.editar_eventos, name='editar_eventos'),
]

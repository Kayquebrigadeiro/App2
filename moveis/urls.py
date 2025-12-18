from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('novo/', views.novo, name='novo'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
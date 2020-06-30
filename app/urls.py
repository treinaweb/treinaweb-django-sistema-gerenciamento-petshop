from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cadastrar_cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_clientes', cliente_views.listar_clientes, name='listar_clientes'),
    path('lista_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
]
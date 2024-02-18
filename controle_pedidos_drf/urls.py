"""
URL configuration for controle_pedidos_drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import generics
from back import serializers, models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', generics.ListCreateAPIView.as_view(queryset=models.Cliente.objects.all(), serializer_class=serializers.ClienteSerializer), name='clientes-list'),
    path('pedidos/', generics.ListCreateAPIView.as_view(queryset=models.Pedido.objects.all(), serializer_class=serializers.PedidoSerializer), name='pedidos-list'),
    path('contato_telefone_cliente/', generics.ListCreateAPIView.as_view(queryset=models.ContatoTelefoneCliente.objects.all(), serializer_class=serializers.ContatoTelefoneClienteSerializer), name='ContatoTelefoneClientes-list'),
    path('contato_email_cliente/', generics.ListCreateAPIView.as_view(queryset=models.ContatoEmailCliente.objects.all(), serializer_class=serializers.ContatoEmailClienteSerializer), name='ContatoEmailClientes-list'),

    path('cliente/<int:pk>/', generics.RetrieveUpdateDestroyAPIView.as_view(queryset=models.Cliente.objects.all(), serializer_class=serializers.ClienteSerializer), name='cliente'),
    path('pedido/<int:pk>/', generics.RetrieveUpdateDestroyAPIView.as_view(queryset=models.Pedido.objects.all(), serializer_class=serializers.PedidoSerializer), name='pedido'),
    path('contato_telefone_cliente/<int:pk>/', generics.RetrieveUpdateDestroyAPIView.as_view(queryset=models.ContatoTelefoneCliente.objects.all(), serializer_class=serializers.ContatoTelefoneClienteSerializer), name='ContatoTelefoneCliente'),
    path('contato_email_cliente/<int:pk>/', generics.RetrieveUpdateDestroyAPIView.as_view(queryset=models.ContatoEmailCliente.objects.all(), serializer_class=serializers.ContatoEmailClienteSerializer), name='ContatoEmailCliente'),
]

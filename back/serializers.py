from rest_framework import serializers
from back import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/40541822/how-to-show-depth-of-a-single-field-in-django-rest-framework
    #cliente = ClienteSerializer(many=False, read_only=True)
    class Meta:
        model = models.Pedido
        fields = '__all__'
        exclude=[]

class ContatoTelefoneClienteSerializer(serializers.ModelSerializer):
    #cliente = ClienteSerializer(many=False, read_only=True)
    class Meta:
        model = models.ContatoTelefoneCliente
        fields = '__all__'

class ContatoEmailClienteSerializer(serializers.ModelSerializer):
    #cliente = ClienteSerializer(many=False, read_only=True)
    class Meta:
        model = models.ContatoEmailCliente
        fields = '__all__'

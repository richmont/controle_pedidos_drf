from django.db import models

# Create your models here.
class Cliente(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)

class Pedido(models.Model):
    valor_total = models.IntegerField()
    data_criacao = models.DateField(blank=False)
    prazo_final = models.DateField(blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ContatoTelefoneCliente(models.Model):
    telefone = models.CharField(max_length=14, blank=False)
    whatsapp = models.BooleanField()
    fixo = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class ContatoEmailCliente(models.Model):
    email = models.CharField(blank=False, max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


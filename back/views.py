from rest_framework import generics
from back import serializers, models

class ClienteView(generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
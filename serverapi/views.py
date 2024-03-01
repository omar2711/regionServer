# serverapi/views.py
from rest_framework import viewsets
from .models import Computer
from serverapi.serializers import ComputerSerializer  # Asegúrate de importar ComputerSerializer

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

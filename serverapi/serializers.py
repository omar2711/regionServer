# serverapi/serializers.py
from rest_framework import serializers
from .models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'  # Esto incluye todos los campos del modelo en el serializador

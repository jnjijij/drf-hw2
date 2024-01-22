from rest_framework import serializers
from .models import CarModel

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year', 'color']  # Example fields from the Car model
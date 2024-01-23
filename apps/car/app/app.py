from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year']

    def validate_year(self, value):
        if value < 1886:  
            raise serializers.ValidationError("Invalid year")
        return value


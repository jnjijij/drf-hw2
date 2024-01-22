from rest_framework import serializers
from .models import CarModel

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year']

    def validate_year(self, value):
        if value < 1886:  # First car was invented in 1886
            raise serializers.ValidationError("Invalid year")
        return value


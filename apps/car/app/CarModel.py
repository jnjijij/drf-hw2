from rest_framework import serializers

class CarModelSerializer(serializers.ModelSerializer):
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    year = serializers.IntegerField()

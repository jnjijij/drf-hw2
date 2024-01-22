from django.db import models
from rest_framework import generics
from rest_framework import filters
import django_filters
from .models import CarModel
from .serializers import CarSerializer
class CarModel(models.Model):
 class Meta:
     model = CarModel

db_table = 'cars'


brand = models.CharField(max_length=20)
price = models.IntegerField()
year = models.IntegerField()

queryset = CarModel.objects.all()
serializer_class = CarSerializer
filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
filterset_fields = {
        'brand': ['exact', 'icontains', 'istartswith', 'iendswith'],
        'year': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'seats': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'body_type': ['exact', 'icontains', 'istartswith', 'iendswith'],
        'engine_volume': ['exact', 'gt', 'lt', 'gte', 'lte'],
    }
ordering_fields = '__all__'
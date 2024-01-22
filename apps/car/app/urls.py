from django.urls import path
from .views import CarList

urlpatterns = [
    path('cars/', CarList.as_view(), name='car_list'),
    # Add other URL patterns here
]
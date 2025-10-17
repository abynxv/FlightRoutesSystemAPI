# serializers.py
from rest_framework import serializers
from .models import Airport, Route

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    airport = AirportSerializer()
    
    class Meta:
        model = Route
        fields = ['airport', 'position', 'duration']

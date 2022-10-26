from rest_framework import serializers
from .models import Sensordata

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensordata
        fields = ('id', 'humidity', 'temperature', 'time')

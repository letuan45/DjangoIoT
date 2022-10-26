from django.shortcuts import render
from rest_framework.response import Response
from .models import Sensordata
from .serializers import DataSerializer
from rest_framework.decorators import api_view
from rest_framework import generics

import serial
import time
import datetime

# Create your views here.

def get_t_h():
    ser = serial.Serial('COM4', 115200, timeout=1)
    time.sleep(2)
    while 1:
        line = str(ser.readline().decode('utf-8'))
        if len(line.strip()) > 0:
            my_list = line.split(',')
            my_list.append(str(datetime.datetime.now()))
            return my_list
        time.sleep(1)

def index(request):
    return render(request, 'polls/index.html')

@api_view(['GET'])
def get_all_sensor_data(request):
    sensor_data = Sensordata.objects.all()
    serializers = DataSerializer(sensor_data, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_latest_data(request):
    sensor_data = Sensordata.objects.all()
    if(len(sensor_data) == 0):
        return Response(None)

    latest_data = sensor_data[len(sensor_data)-1]

    serializer = DataSerializer(latest_data, many=False)
    return Response(serializer.data)

class DeleteAll(generics.CreateAPIView):
    queryset = Sensordata.objects.all().delete()
    serializer_class = DataSerializer

@api_view(['GET'])
def create_sensor_data(request):
    sensor_data = get_t_h()

    if(len(sensor_data) > 0):
        temperature = float(sensor_data[0])
        humidity = float(sensor_data[1])
        time = sensor_data[2]

        serializer = DataSerializer(data={"temperature": temperature, "humidity": humidity, "time": time})
        if(serializer.is_valid()):
             serializer.save()

    sensor_datas = Sensordata.objects.all() #get all data
    if(len(sensor_datas) > 10):
        oldest_data = sensor_datas[0]
        oldest_data.delete()

    return Response("Successfully")
    
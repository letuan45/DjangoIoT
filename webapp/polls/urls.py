from django.urls import path
from .views import get_all_sensor_data
from .views import index
from .views import get_latest_data
from .views import DeleteAll
from .views import create_sensor_data

urlpatterns = [
    path('', index),
    path('get-all-data', get_all_sensor_data),
    path('get-latest', get_latest_data),
    path('delete-all', DeleteAll.as_view()),
    path('create-sensor-data', create_sensor_data),
]
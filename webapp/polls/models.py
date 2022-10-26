from django.db import models

# Create your models here.
class Sensordata(models.Model):
	id = models.AutoField(primary_key=True)
	humidity = models.FloatField()
	temperature = models.FloatField()
	time = models.DateTimeField()

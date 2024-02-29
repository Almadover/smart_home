from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
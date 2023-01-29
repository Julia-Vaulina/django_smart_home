from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, )
    description = models.CharField(max_length=50, )


    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', related_name='measurements', on_delete=models.PROTECT, null=True)
    temperature = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.title



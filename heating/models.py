from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200, null=False)
    temp_actual = models.FloatField()
    temp_default = models.FloatField()
    # temp_plan = 
    
    def __str__(self) -> str:
        return self.name

class Temp_Segment(models.Model):
    time_start = models.TimeField(blank=False)
    time_end = models.TimeField(blank=False)
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    
    def __str__(self) -> str:
        return f'{self.time_start} - {self.time_end} : {self.temp_min} - {self.temp_max}'



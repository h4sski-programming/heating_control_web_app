from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200, null=False)
    _temp_actual = models.FloatField()
    _temp_default = models.FloatField()
    # temp_plan = 
    
    def get_temp_actual(self) -> float:
        # Debug purpouse calculation, comment out while in production
        def get_debug_value(self) -> float:
            from datetime import datetime
            t = datetime.now().second
            return self._temp_actual - t * 5/60
    
        
        return get_debug_value(self)
        # return self._temp_actual
    
    def set_temp_default(self, temp: float) -> None:
        self._temp_default = temp
    
    def get_temp_default(self) -> float:
        return self._temp_default
    
    def __str__(self) -> str:
        return self.name

class Temp_Segment(models.Model):
    _time_start = models.TimeField(blank=False)
    _time_end = models.TimeField(blank=False)
    _temp_min = models.FloatField()
    _temp_max = models.FloatField()
    
    def __str__(self) -> str:
        return f'{self.time_start} - {self.time_end} : {self.temp_min} - {self.temp_max}'



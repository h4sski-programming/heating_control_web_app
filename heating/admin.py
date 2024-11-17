from django.contrib import admin

# Register your models here.
from .models import Room, Temp_Segment

admin.site.register(Room)
admin.site.register(Temp_Segment)
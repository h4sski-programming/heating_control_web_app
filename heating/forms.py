from django import forms

from .models import Room, Temp_Segment


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', '_temp_actual', '_temp_default']


class RoomForm2(forms.Form):
    name = forms.CharField(max_length=100, label="Room name")
    temp_default = forms.FloatField(label="Default temp", initial=20.5)
    
    # Debug only ??
    temp_actual = forms.FloatField(label="Actual temp", initial=20.5)
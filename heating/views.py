from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import Room, Temp_Segment


class IndexView(TemplateView):
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        # Start with the default context from the superclass
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        ccc = {
            "hello": "Hello World!",
            'rooms': Room.objects.all(),
            'temp_segments': Temp_Segment.objects.all()
        }
        
        return {**context, **ccc}
        # return context.update(ccc)
        

class RoomsView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'
    

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room'

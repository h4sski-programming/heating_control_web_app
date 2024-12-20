# from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .models import Room, Temp_Segment
from .forms import RoomForm


class IndexView(TemplateView):
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        # Start with the default context from the superclass
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        ccc = {
            "hello": "Hello World!",
            'rooms': Room.objects.all(),
            'temp_segments': Temp_Segment.objects.all(),
        }
        
        return {**context, **ccc}
        # return context.update(ccc)
        

class RoomsView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'
    
    def get_context_data(self, **kwargs):
        # Start with the default context from the superclass
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        ccc = {
            'room_form': RoomForm(),
        }
        
        return {**context, **ccc}
    

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'
    context_object_name = 'room'
    

class RoomFormView(FormView):
    form_class = RoomForm
    template_name = 'room_form.html'
    success_url = reverse_lazy('rooms')
    
    def form_valid(self, form):
        form.save()  # Save the form data
        return super().form_valid(form)
    

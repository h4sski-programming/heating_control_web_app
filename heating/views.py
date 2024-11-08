from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    
    
    def get_context_data(self, **kwargs):
        # Start with the default context from the superclass
        context = super().get_context_data(**kwargs)
        
        # Add additional context data
        ccc = {
            "hello": "Hello World!",
        }
        
        return {**context, **ccc}
        # return context.update(ccc)
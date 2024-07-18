from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from typing import Any
from nomencladores.models import departamentos

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    #@method_decorator(login_required)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    
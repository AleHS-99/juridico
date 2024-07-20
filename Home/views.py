from django.shortcuts import render
from django.views.generic import TemplateView
from typing import Any
from contratos.models import contrato
from django.utils import timezone
from django.db.models import Q

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    #@method_decorator(login_required)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["c_contratos"] = len(contrato.objects.all())
        context["ca_contratos"] = len(contrato.objects.all())
        now = timezone.now()
        first_day_of_month = now.replace(day=1)
        last_day_of_month = (first_day_of_month+timezone.timedelta(days=32)).replace(day=1)-timezone.timedelta(days=1)
        context["cvm_contratos"] = contrato.objects.filter(fecha_fin__gte=first_day_of_month, fecha_fin__lte=last_day_of_month)
        context["cv_contratos"] = contrato.objects.filter(fecha_fin__lt=timezone.now())
        return context
    
    
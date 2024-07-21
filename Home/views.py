from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from typing import Any
from contratos.models import contrato
from django.utils import timezone
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from nomencladores.models import departamentos
from django.contrib.auth import update_session_auth_hash
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    @method_decorator(login_required)
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

class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class UserChangePassword(FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'user/change.html'
    success_url = reverse_lazy('Home')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args: Any, **kwargs: Any):
        return super().dispatch(request, *args, **kwargs)
    
    def get_form(self,form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form
    
    def post(self, request, *args,**kwargs):
        data = {}
        try:
            action=request.POST['action']
            if action=='edit':
                form = PasswordChangeForm(user=request.user,data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request,form.user)
                else:
                    data['error']=form.errors
            else:
                data['error']='No ha ingresado a ninguna opción'
        except Exception as e:
            data['error']=str(e)
        
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar Contraseña'
        context['list_url']=reverse_lazy('Home')
        context['form_url']=reverse_lazy('user_pass_change')
        context['action']='edit'
        return context

def datos_barra(request):
    data = {}
    departament = departamentos.objects.all()
    now = timezone.now()
    first_day_of_month = now.replace(day=1)
    last_day_of_month = (first_day_of_month+timezone.timedelta(days=32)).replace(day=1)-timezone.timedelta(days=1)   
    for d in departament:
        activos = contrato.objects.filter(departamento=d).count()
        por_vencer = contrato.objects.filter(fecha_fin__gte=first_day_of_month, fecha_fin__lte=last_day_of_month, departamento=d).count()
        vencido = contrato.objects.filter(fecha_fin__lt=timezone.now(), departamento=d).count()
        data[d.departamento] = [activos,por_vencer,vencido]
    return JsonResponse(data)


from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from typing import Any
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *
# Create your views here.

class listContrato(ListView):
    model = contrato
    template_name = 'contrato/list.html'
    
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        #esta funcion maneja como llegan los metodos de las peticiones
        self.departamento_id = self.kwargs.get('pk')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return contrato.objects.filter(departamento=self.departamento_id)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['depa_id'] = self.departamento_id
        context['title'] = f"Listado de Contratos del departamento: {departamentos.objects.get(id=self.departamento_id)}" 
        return context

class addContrato(CreateView):
    model = contrato
    form_class = contratoForm
    template_name = 'globals/form.html'
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.departamento_id = self.kwargs.get('pk')
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        initial['departamento'] = self.departamento_id
        return initial
    
    def get_success_url(self):
        # Concatena el ID del departamento a la URL deseada
        return reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Contrato'
        context['list_url']=reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
        context['form_url']=reverse_lazy('add_contrato', kwargs={'pk': self.departamento_id})
        context['action']='add'
        return context

    def form_valid(self, form):
        # Guarda el objeto
        form.save()
        # Redirige a la página deseada
        return redirect(self.success_url)
    
    def post(self, request, *args,**kwargs):
        data = {}
        try:
            action=request.POST['action']
            if action=='add':
                # form=CategoryForm(request.POST)
                #asi es lo mismo que arriba, pero es mejor, en tal caso que se envien archivos, eso va en el request.FILES pero con el self.get_form() obtengo todo el formulario
                form=self.get_form()
                #ahi ya sobreescribi el metodo save
                data = form.save()
            else:
                data['error']='No ha ingresado a ninguna opción'
        except Exception as e:
            data['error']=str(e)
        
        return JsonResponse(data)

class updateContrato(UpdateView):
    model = contrato
    form_class = contratoForm
    template_name = 'globals/form.html'
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.departamento_id = self.kwargs.get('dp')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        # Concatena el ID del departamento a la URL deseada
        return reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Contrato'
        context['list_url']=reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
        context['action']='edit'
        return context
    
    def post(self, request, *args,**kwargs):
        data = {}
        try:
            action=request.POST['action']
            if action=='edit':
                # form=CategoryForm(request.POST)
                #asi es lo mismo que arriba, pero es mejor, en tal caso que se envien archivos, eso va en el request.FILES pero con el self.get_form() obtengo todo el formulario
                form=self.get_form()
                #ahi ya sobreescribi el metodo save
                data = form.save()
            else:
                data['error']='No ha ingresado a ninguna opción'
        except Exception as e:
            data['error']=str(e)
        
        return JsonResponse(data)

class deleteContrato(DeleteView):
    model = contrato
    template_name = 'globals/delete.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.departamento_id = self.kwargs.get('dp')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        # Concatena el ID del departamento a la URL deseada
        return reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje'] = "¿Estas seguro de querer eliminarl este contrato?"
        context['title'] = "Eliminar Contrato"
        context['list_url']=reverse_lazy("listContratoU", kwargs={'pk': self.departamento_id})
        return context




from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *
# Create your views here.

class tContratoView(ListView):
    model = tipo_contrato
    template_name = 'nomencladores/tpc/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        #esta funcion maneja como llegan los metodos de las peticiones
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return tipo_contrato.objects.all()
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado Tipos de Contratos"
        return context

class addTcontrato(CreateView):
    model = tipo_contrato
    form_class = tContratoForm
    template_name = 'nomencladores/tpc/form.html'
    success_url =reverse_lazy("t_contrato")
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir tipo de Contrato'
        context['list_url']=reverse_lazy('t_contrato')
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

class updateTcontrato(UpdateView):
    model = tipo_contrato
    form_class = tContratoForm
    template_name = 'nomencladores/tpc/form.html'
    success_url =reverse_lazy("t_contrato")
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar tipo de Contrato'
        context['list_url']=reverse_lazy('t_contrato')
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

class deleteTcontrato(DeleteView):
    model = tipo_contrato
    template_name = 'nomencladores/tpc/delete.html'
    success_url = reverse_lazy("t_contrato")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje'] = "Al borrar este tipo de contrato, tambien se borraran los contratos que lo utilicen.\n¿Estas seguro de querer eliminarlo?"
        context['title'] = "Eliminación de un Tipo de Contrato"
        context['list_url']=reverse_lazy('t_contrato')
        return context

class fPagoView(ListView):
    model = forma_pago
    template_name = 'nomencladores/fpago/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        #esta funcion maneja como llegan los metodos de las peticiones
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return forma_pago.objects.all()
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado Forma de Pagos"
        return context

class addfPago(CreateView):
    model = forma_pago
    form_class = fPagoForm
    template_name = 'nomencladores/tpc/form.html'
    success_url =reverse_lazy("t_contrato")
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Forma de Pago'
        context['list_url']=reverse_lazy('f_pago')
        context['form_url']=reverse_lazy('add_f_pago')
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

class updatefPago(UpdateView):
    model = forma_pago
    form_class = fPagoForm
    template_name = 'nomencladores/tpc/form.html'
    success_url =reverse_lazy("f_pago")
    
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Forma de Pago'
        context['list_url']=reverse_lazy('f_pago')
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

class deletefPago(DeleteView):
    model = forma_pago
    template_name = 'nomencladores/tpc/delete.html'
    success_url = reverse_lazy("f_pago")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje'] = "Al borrar esta forma de pago, tambien se borraran los contratos que lo utilicen.\n¿Estas seguro de querer eliminarlo?"
        context['title'] = "Eliminación de una forma de pago"
        context['list_url']=reverse_lazy('f_pago')
        return context


class listDepart(ListView):
    model = departamentos
    template_name = 'nomencladores/depart/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        #esta funcion maneja como llegan los metodos de las peticiones
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return departamentos.objects.all()
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado Departamentos"
        return context



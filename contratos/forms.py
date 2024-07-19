from django.forms import *
from .models import *

class contratoForm(ModelForm):
    class Meta:
        model = contrato
        fields ='no_contrato', 'proveedor', 't_contrato', 'obj_contrato', 'dictamen', 'f_pago', 'departamento', 'fecha_ini', 'fecha_fin', 'observaciones'
        widgets={
            'no_contrato':TextInput(attrs={'placeholder':"Ingrese No. Contrato"}),
            'proveedor':TextInput(attrs={'placeholder':"Ingrese Proveedor"}),
            't_contrato':Select(),
            'obj_contrato':TextInput(attrs={'placeholder':"Ingrese Objeto del Contrato"}),
            'dictamen':TextInput(attrs={'placeholder':"Ingrese Dictamen"}),
            'f_pago':Select(),
            'departamento':Select(),
            'fecha_ini':DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin':DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'observaciones':Textarea(attrs={'placeholder':"Observaciones"}),
        }
        
    def save(self,commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

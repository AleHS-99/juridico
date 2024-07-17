from django.forms import *
from .models import *

class tContratoForm(ModelForm):
    class Meta:
        model = tipo_contrato
        fields ='__all__'
        widgets={
            't_contrato':TextInput(attrs={'placeholder':"Ingrese Tipo de Contrato"})
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
from django.db import models
from nomencladores.models import *

# Create your models here.
class contratos(models.Model):
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contrators'
    id = models.AutoField(primary_key=True)
    no_contrato = models.CharField(max_length=200,blank=False,null=False, verbose_name="No. Contrato")
    proveedor = models.CharField(max_length=200,blank=False,null=False, verbose_name="Proveedor")
    t_contrato = models.ForeignKey(tipo_contrato,on_delete=models.CASCADE, verbose_name="Tipo de Contrato")
    obj_contrato = models.CharField(max_length=500,blank=False,null=False, verbose_name="Objeto del Contrato")
    dictamen = models.CharField(max_length=200,verbose_name="Dictamen")
    f_pago = models.ForeignKey(forma_pago,on_delete=models.CASCADE,verbose_name="Forma de Pago")
    fecha_ini = models.DateField(verbose_name="Fecha de Firma del Contrato")
    fecha_fin = models.DateField(verbose_name="Fecha de Vencimiento del Contrato")
    observaciones = models.TextField(verbose_name="Observaciones", blank=True, null=True)
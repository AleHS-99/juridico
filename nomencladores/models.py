from django.db import models

# Create your models here.
class tipo_contrato(models.Model):
    class Meta:
        verbose_name = 'Tipo Contrato'
        verbose_name_plural = 'Tipos de Contratos'
    id = models.AutoField(primary_key=True)
    t_contrato = models.CharField(max_length=1000,blank=False,null=False, verbose_name="Tipo de Contrato", unique=True)
    def __str__(self):
        return self.t_contrato
class forma_pago(models.Model):
    class Meta:
        verbose_name = 'Forma de pago'
        verbose_name_plural = 'Formas de pago'
    id = models.AutoField(primary_key=True)
    f_pago = models.CharField(max_length=1000,blank=False,null=False, verbose_name="Forma de Pago")
    def __str__(self):
        return self.f_pago

class departamentos(models.Model):
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    id = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=1000,blank=False,null=False)
    def __str__(self):
        return self.departamento
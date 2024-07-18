# Generated by Django 5.0.7 on 2024-07-18 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomencladores', '0002_alter_tipo_contrato_t_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='contratos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_contrato', models.CharField(max_length=200, verbose_name='No. Contrato')),
                ('proveedor', models.CharField(max_length=200, verbose_name='Proveedor')),
                ('obj_contrato', models.CharField(max_length=500, verbose_name='Objeto del Contrato')),
                ('dictamen', models.CharField(max_length=200, verbose_name='Dictamen')),
                ('fecha_ini', models.DateField(verbose_name='Fecha de Firma del Contrato')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de Vencimiento del Contrato')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.departamentos', verbose_name='Departamento')),
                ('f_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.forma_pago', verbose_name='Forma de Pago')),
                ('t_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.tipo_contrato', verbose_name='Tipo de Contrato')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contrators',
            },
        ),
    ]
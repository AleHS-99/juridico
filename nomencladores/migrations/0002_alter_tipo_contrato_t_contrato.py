# Generated by Django 5.0.7 on 2024-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_contrato',
            name='t_contrato',
            field=models.CharField(max_length=1000, unique=True, verbose_name='Tipo de Contrato'),
        ),
    ]
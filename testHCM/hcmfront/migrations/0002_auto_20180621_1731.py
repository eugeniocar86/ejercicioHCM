# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcmfront', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='empleado',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleado_reserva', to='hcmfront.Empleado'),
        ),
    ]


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Sala, Insumo, Solicitud, Reserva, Empleado, Status

admin.site.register(Sala)
admin.site.register(Insumo)
admin.site.register(Solicitud)
admin.site.register(Reserva)
admin.site.register(Empleado)
admin.site.register(Status)

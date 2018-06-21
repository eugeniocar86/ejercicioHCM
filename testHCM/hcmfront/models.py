
# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Insumo(models.Model):
	nombre = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.nombre

class Status(models.Model):
	nombre = models.CharField(max_length=100) #solo este campo a efectos del ejemplo

	def __unicode__(self):
		return u"%s status (%s)" % (self.id, self.nombre)

# Create your models here.
class Sala(models.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = models.CharField(max_length=100)
	capacidad = models.IntegerField(default=0, null=True)
	horario_desde = models.TimeField(blank=True)
	horario_hasta = models.TimeField(blank=True)
	insumos = models.ManyToManyField(Insumo)
	status = models.ForeignKey(Status, related_name='sala_status')

	def __unicode__(self):
		return u"%s status (%s)" % (self.nombre, self.status.nombre)

class Empleado(models.Model):
	nombre = models.CharField(max_length=100) #solo este campo a efectos del ejemplo

	def __unicode__(self):
		return self.nombre

class Reserva(models.Model):
	sala = models.ForeignKey(Sala, related_name='sala_reserva')
	#empleado = models.ForeignKey(Empleado, related_name='empleado_reserva', null=True, default=None)
	horario_inicio = models.TimeField(blank=True)
	horario_termino = models.TimeField(blank=True)
	date = models.DateTimeField(blank=True, null=True)
	insumos = models.ManyToManyField(Insumo)
	cantidad_personas = models.IntegerField(default=0, null=True)

	def __unicode__(self):
		return u"Sala (%s)" % (self.sala.nombre)

class Solicitud(models.Model):
	empleado = models.ForeignKey(Empleado, related_name='empleado_solicitud')
	sala = models.ForeignKey(Sala, related_name='sala_solicitud')

	def __unicode__(self):
		return u"%s (%s)" % (self.empleado.nombre, self.sala.nombre)

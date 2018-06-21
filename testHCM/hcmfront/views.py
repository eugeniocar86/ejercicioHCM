# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Insumo
from .models import Sala
from .models import Reserva

from django.http import Http404  

from django.db.models import Q
# Create your views here.

def HomeView(request):
	#validar q el codigo exista si no eviar a 404
	insumos = Insumo.objects.all()
	return render(request, 'home.html', {"insumo": insumos})

def SearchView(request):
	#validar q el codigo exista si no eviar a 404
	cantidad = request.GET.get('cantidad', 0)
	insumos = request.GET.get('arr_ids', "")

	if insumos != "":
		insumos = insumos[:-1]

	arr_insumos = insumos.split(",")

	arr = []

	for a in arr_insumos:
		arr.append(int(a))

	if cantidad == "":
		cantidad = 0

	cantidad = int(cantidad)

	salas = Sala.objects.filter(Q(capacidad__gte=cantidad, insumos__in=arr)).distinct()

	return render(request, 'search.html', {"sala": salas, "insumos": arr})

def ReservarView(request, pk):
	#validar q el codigo exista si no eviar a 404	
	try:
		sala = Sala.objects.get(id=pk)
		insumos = sala.insumos.all()
	except Sala.DoesNotExist:
		raise Http404

	return render(request, 'reserva.html', {"sala": sala, "insumos": insumos})

def GuardarView(request, pk):
	#validar q el codigo exista si no eviar a 404	
	try:
		sala = Sala.objects.get(id=pk)
	except Sala.DoesNotExist:
		raise Http404

	insumos = request.POST.get('arr_ids', "")

	if insumos != "":
		insumos = insumos[:-1]

	arr_insumos = insumos.split(",")

	arr = []

	for a in arr_insumos:
		arr.append(a)

	cantidad = request.POST.get('capacidad')

	if cantidad == "":
		cantidad = 0

	cantidad = int(cantidad)

	r = Reserva.objects.create(sala_id=pk, 
							   horario_inicio=request.POST.get('hora_inicio', ""), 
							   horario_termino=request.POST.get('hora_fin', ""), 
							   date=request.POST.get('date', ""),
							   cantidad_personas=cantidad
							   )
	
	r.save()

	for i in arr:
		insumo = Insumo.objects.get(id=i)
		r.insumos.add(insumo)

	r.save()

	mensaje = "Reserva Guardada"

	return render(request, 'save.html', {"mensaje": mensaje, "insumos": arr})

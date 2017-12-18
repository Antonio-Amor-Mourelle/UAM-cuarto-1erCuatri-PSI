# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from aplicacion.models import Reserva, Destino

# Create your views here.
def reserva(request):
    error = None
    reservas = None
    try:
        destino = Destino.objects.filter(nombreD='destino-4')[0]
        reservas = Reserva.objects.filter(destino=destino)
    except:
        error = "No hay reservas"

    return render(request,'aplicacion/reserva.html',
    {'error': error,
    'reservas': reservas,})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aplicacion.models import Cliente, Destino, Reserva

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombreC")

class DestinoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombreD")

class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "destino", "fechaDeReserva")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Destino, DestinoAdmin)
admin.site.register(Reserva, ReservaAdmin)

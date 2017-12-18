# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

# Create your models here.
class  Cliente(models.Model):
    nombreC = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombreC
    def __unicode__(self):
        return self.nombreC

class Destino(models.Model):
    nombreD = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombreD
    def __unicode__(self):
        return self.nombreD

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    destino = models.ForeignKey(Destino)
    fechaDeReserva = models.DateTimeField(default=now)

    def __str__(self):
        return "%d" % self.id
    def __unicode__(self):
        return "%d" % self.id

from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombreP = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombreP
    def __unicode__(self):
        return self.nombreP

class Medico(models.Model):
    nombreM = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nombreM
    def __unicode__(self):
        return self.nombreM

class Receta(models.Model):
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)

    def __str__(self):
        return "%d" % self.id
    def __unicode__(self):
        return "%d" % self.id

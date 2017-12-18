from django.contrib import admin
from aplicacion.models import Medico, Paciente, Receta
# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
	list_display = ("id", "nombreP")

class MedicoAdmin(admin.ModelAdmin):
	list_display = ("id", "nombreM")

class RecetaAdmin(admin.ModelAdmin):
	list_display = ("id", "medico", "paciente")

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Receta, RecetaAdmin)


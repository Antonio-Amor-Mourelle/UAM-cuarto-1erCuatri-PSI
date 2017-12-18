from django.shortcuts import render
from aplicacion.models import Receta

# Create your views here.
def receta(request):
    error = None
    try:
        recetas = Receta.objects.all().order_by('-id')[:3]
    except:
        error = "No hay recetas"

    return render(request,'aplicacion/receta.html',
    {'error': error,
    'recetas': recetas,})

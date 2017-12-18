import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')

import django
django.setup()


from aplicacion.models import Medico, Paciente, Receta

def add_Medico(nombre):
    m = Medico.objects.get_or_create(nombreM=nombre)[0]
    return m

def add_Paciente(nombre):
    p = Paciente.objects.get_or_create(nombreP=nombre)[0]
    return p

def add_Receta(id_m, id_p):
    m = Medico.objects.get(id=id_m)
    p = Paciente.objects.get(id=id_p)
    r = Receta.objects.get_or_create(medico=m, paciente=p)
    return r

def populate():
    medicos = ['medico1', 'medico2', 'medico3', 'medico4']
    pacientes = ['paciente1', 'paciente2']

    for name in medicos:
        add_Medico(name)

    for name in pacientes:
        add_Paciente(name)

    add_Receta(1,1)
    add_Receta(2,1)
    add_Receta(1,2)
    add_Receta(2,2)
    add_Receta(3,2)


if __name__ == '__main__':
    print("Starting shop population script...")
    populate()


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'proyecto.settings')
import django
django.setup()

from aplicacion.models  import Cliente, Destino, Reserva

def add_cliente(id,nombre):
    c = Cliente.objects.get_or_create(id=id,nombreC=nombre)
    return c

def add_destino(id,nombre):
    d = Destino.objects.get_or_create(id=id,nombreD=nombre)
    return d

def add_reserva(id, id_destino, id_cliente=-1):
    d = Destino.objects.get(id=id_destino)
    if id_cliente != -1:
        c = Cliente.objects.get(id=id_cliente)
        r = Reserva.objects.get_or_create(id=id, cliente=c, destino=d)
    else:
        r = Reserva.objects.get_or_create(id=id, destino=d)
    return r

def populate():
    clientes = ['cliente-%d'%i for i in range(1,4)]
    destinos = ['destino-%d'%i for i in range(1,5)]

    for i in range(1001,1004):
        add_cliente(i, clientes[i-1001])

    for i in range(1001,1005):
        add_destino(i, destinos[i-1001])

    add_reserva(id=1001,id_cliente=1001,id_destino=1001)
    add_reserva(id=1002,id_cliente=1001,id_destino=1002)
    add_reserva(id=1003,id_destino=1001)
    add_reserva(id=1004,id_destino=1004)
    add_reserva(id=1005,id_cliente=1002,id_destino=1002)

if __name__ == '__main__':
    print("Starting population script...")
    populate()

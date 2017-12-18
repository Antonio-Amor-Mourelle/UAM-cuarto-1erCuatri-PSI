from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from aplicacion.models import Reserva, Destino, Cliente

# Create your tests here.
class examenTests(TestCase):
    def setUp(self):
        self._client   = Client()
        self.clean_database()
        self.populate()

    def clean_database(self):
        Reserva.objects.all().delete()
        Cliente.objects.all().delete()
        Destino.objects.all().delete()

    def populate(self):
        c1 = Cliente.objects.get_or_create(nombreC='cliente1')[0]
        c2 = Cliente.objects.get_or_create(nombreC='cliente2')[0]
        d1 = Destino.objects.get_or_create(nombreD='destino1')[0]
        d2 = Destino.objects.get_or_create(nombreD='destino2')[0]
        d3 = Destino.objects.get_or_create(nombreD='destino3')[0]
        Reserva.objects.get_or_create(destino=d1, cliente=c1)[0]
        Reserva.objects.get_or_create(destino=d2, cliente=c1)[0]
        Reserva.objects.get_or_create(destino=d1)[0]
        Reserva.objects.get_or_create(destino=d2, cliente=c2)[0]

    def test_reservas(self):
        response = self._client.get(reverse('reserva'), follow=True)
        #Comprobamos que aparece el nombre medico1
        self.assertIn('No hay reservas', response.content)

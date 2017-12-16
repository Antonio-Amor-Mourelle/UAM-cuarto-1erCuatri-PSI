from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from aplicacion.models import Medico, Paciente, Receta

# Create your tests here.
class examenTests(TestCase):
    def setUp(self):
        self._client   = Client()
        self.clean_database()
        self.populate()

    def clean_database(self):
        Receta.objects.all().delete()
        Paciente.objects.all().delete()
        Medico.objects.all().delete()

    def populate(self):
        m = Medico.objects.get_or_create(nombreM='medico1')[0]
        p = Paciente.objects.get_or_create(nombreP='paciente1')[0]
        Receta.objects.get_or_create(id=1,medico=m, paciente=p)[0]
        Receta.objects.get_or_create(id=2,medico=m, paciente=p)[0]
        Receta.objects.get_or_create(id=3,medico=m, paciente=p)[0]
        Receta.objects.get_or_create(id=4,medico=m, paciente=p)[0]

    def test_recetas(self):
        response = self._client.get(reverse('receta'), follow=True)
        #Comprobamos que aparece el nombre medico1
        self.assertIn('medico1', response.content)
        #Comprobamos que aparece el nombre paciente1
        self.assertIn('paciente1', response.content)
        
        #Comprobamos que existen los id de las recetas
        for i in range(2,5):
            self.assertIn("%d"%i, response.content)

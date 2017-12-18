# Uncomment if you want to run tests in transaction mode with a final rollback
#from django.test import TestCase
#uncomment this if you want to keep data after running tests
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from shop.models import Product, Category

import os
base_path   = os.getcwd()
static_path = os.path.join(base_path,"static")


#python ./manage.py test shop.tests.viewsTests --keepdb

DEBUG = False
from PIL import Image
from StringIO import StringIO
from django.core.files.base import File
from populate_onlineshop import populate #import de la funcion que puebla la base de datos


"""
Funciones de prueba de la base de datos
Cambios menores realizados con los nombres de los datos de nuestra aplicacion
"""
class viewsTests(TestCase):
    def setUp(self):
        self._client   = Client()
        self.clean_database()
        populate()

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def clean_database(self):
        Product.objects.all().delete()
        Category.objects.all().delete()


    def test_produnct_list(self):
        response = self._client.get(reverse('product_list'), follow=True)
        for cat in ["Refrigerators", "Washing machines", "Dishwashers"]:
            self.assertIn(cat, response.content)
        for cat in ["Refrigerator", "Washing-machine", "Dishwasher"]:
            for counterProd in range(1, 7):
                self.assertIn(b"%s-%d"%(cat,counterProd), response.content)

    def test_produnct_list_cat_0(self):
        response = self._client.get(reverse('product_list_by_category',
                                            kwargs={'catSlug':'refrigerators'}), follow=True)
        for cat in ["Refrigerators", "Washing machines", "Dishwashers"]:
            self.assertIn(cat, response.content)
        for cat in ["Refrigerator"]:
            for counterProd in range(1, 7):
                self.assertIn(b"%s-%d"%(cat,counterProd), response.content)
        for cat in ["Washing-machine", "Dishwasher"]:
            for counterProd in range(0, 5):
                self.assertNotIn(b"%s-%d" % (cat, counterProd), response.content)

    def test_product_detail_fileName_0_0(self):
        prodName='Refrigerator-1'
        p = Product.objects.get(prodName = prodName)
        response = self._client.get(reverse('product_detail',
                                            kwargs={'id':p.id,
                                                    'prodSlug':p.prodSlug}), follow=True)
        self.assertIn   (b'Refrigerators', response.content)
        self.assertNotIn(b'Washing machines', response.content)

        self.assertIn(p.description, response.content)
        self.assertNotIn(b'description_0_1', response.content)

from unittest import TestCase
from django.test import Client
from shoppingcart import ShoppingCart
from django.core.urlresolvers import reverse
from shop.models import Product, Category

class myShoppingCartTest(TestCase):
    def setUp(self):
        self._client   = Client()
        
    def add_cat(self, name):
        c = Category.objects.get_or_create(catName=name)[0]
        return c

    def add_product(self,cat, name, description, price, stock):
        from django.core.files import File
        products = Product.objects.filter(prodName=name)
        if products.exists():
            p = products[0]
            p.delete()
        p = Product.objects.get_or_create(category=cat,
                                          prodName=name,
                                          description=description,
                                          price=price,
                                          stock=stock)[0]

        return p
        
    def test_cart(self):
        response = self._client.get(reverse('product_list'))
        request = response.wsgi_request
        cat = self.add_cat("Prueba_categ")
        product = self.add_product(cat, "Prueba_prod", "Desc", 6.5, 10)
        
        shoppingcart = ShoppingCart(request)
        
        shoppingcart.addProduct(product, units=5, update_units=False)
        
        self.assertIsNotNone(request.session[shoppingcart.cartKey])
        
        shoppingcart.clear()  
        
        self.assertFalse(request.session.get(shoppingcart.cartKey))
        
        
        
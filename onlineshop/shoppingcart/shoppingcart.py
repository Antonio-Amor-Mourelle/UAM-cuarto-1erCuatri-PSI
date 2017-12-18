from decimal import Decimal
from shop.models import Product
from django.template.context_processors import request
from numpy.distutils.from_template import item_re

class ShoppingCart(object):
    cartKey = "shoppingCart"

    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(self.cartKey)
        if not cart:
            cart=self.session[self.cartKey]={}
        self.cart=cart
        
    #Test: python manage.py test shoppingcart_tests.shoppingCartTest.test_shoppingCartAdd --keepdb  
    def addProduct(self, product, units=1,update_units=False):
        """
        Autor: Antonio Amor Mourelle
        Annade varias unidades de un articulo al carro
        """
        
        val = self.cart.get(str(product.id))
        if val and update_units:
            val["units"]=units
        elif val:
            val["units"]+=units
        else:
            self.cart[str(product.id)]={"units":units, "price": str(product.price)}
        self.saveCart()

    def saveCart(self):
        self.session[self.cartKey]=self.cart
        self.session.modified=True

    #Test python manage.py test shoppingcart_tests.shoppingCartTest.test_shoppingCartRemoveProduct --keepdb 
    def removeProduct(self, product):
        """
        Autor: Esther Lopez Ramos
        Elimina un producto del carrito
        """
        del self.cart[str(product.id)]
        self.saveCart()
        
    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        for product in products :
            self.cart[str(product.id)]["product"]=product

        for item in self.cart.values():
            item["price"]=Decimal(item["price"])
            item["total_price"]=item["price"]*item["units"]
            yield item

    #Test python manage.py test shoppingcart_tests.shoppingCartTest.test_shoppingCartLen --keepdb 
    def __len__(self):
        """
        Autor: Esther Lopez Ramos
        Devuelve la longitud del carro entendiendo como la suma 
        de todas las cantidades de sus productos
        """
        length = 0
        for prod in self.cart.values():
            length += prod["units"]
        return length
    
    def get_total_price(self):
        """
        Autor: Antonio Amor
        Devuelve el precio total a pagar
        """

        pf=0
        for item in self.cart.values():
            pf+=Decimal(item["price"])*item["units"]
        return pf

    def clear(self):
        del self.session[self.cartKey]
        self.session.modified=True

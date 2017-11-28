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

    def addProduct(self, product, units=1,update_units=False):

        #TODO: casos 1 nuevo prod
        #            2 mopdificar unidades
        #CASE 1
        val=self.session.get(str(product.id))
        if  val and update_units:
            val["units"]+=units
        else:
            self.session[str(product.id)]={"units":units, "price":product.price}

        self.saveCart()

    def saveCart(self):
        self.session[self.cartKey]=self.cart
        self.session.modified=True

    def removeProduct(self, product):
        #TODO

    def __iter__(self):
        product_ids=self.cart.keys()
        products=Products.objects.filter(id__in=product_ids)
        for product in products :
            self.cart[str(product.id)]["product"]=product

        for item in self.cart.values():
            item["price"]=Decimal(item["price"])
            item["total_price"]=item["price"]*item["units"]
            yield item

    def __len__(self):
        #TODO count items carro (sumando unidades)
        return

    def get_total_price(self):
        '''
        Autor: Antonio Amor
        Devuelve el precio total a pagar
        '''

        pf=0
        for item in self.cart.values():
            pf+=Decimal(item["price"])*Decimal(item["units"])
        return pf

    def clear(self):
        del self.session[self.cartKey]
        self.session.modified=True

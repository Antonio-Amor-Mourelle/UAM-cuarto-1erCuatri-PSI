from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.shoppingcart_list,  name='shoppingcart_list'),
    url(r'^list/$', views.shoppingcart_list,  name='shoppingcart_list'),
]

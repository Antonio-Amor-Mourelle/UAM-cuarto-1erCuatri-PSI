from django.conf.urls import url
from placeorder import views

urlpatterns = [
    url(r'^create/$', views.createOrder, name='createOrder'),
    url(r'^confirm_order/$', views.confirmOrder, name='confirmOrder'),
]

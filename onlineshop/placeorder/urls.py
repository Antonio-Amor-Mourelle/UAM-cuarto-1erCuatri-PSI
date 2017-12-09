from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^create_order/$', views.createOrder, name='createOrder'),
]

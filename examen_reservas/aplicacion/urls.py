from django.conf.urls import url
from aplicacion import views
urlpatterns = [
    url(r'^reserva/$', views.reserva, name='reserva'),
]

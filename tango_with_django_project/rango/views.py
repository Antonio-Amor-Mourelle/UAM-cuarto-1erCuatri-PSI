# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index (request):
    return HttpResponse("Rango says hey there partner!")

def about(request):
    response = HttpResponse("Rango says here is the about page.")
    response.write("<a href=/rango/>Main page</a>")
    return response

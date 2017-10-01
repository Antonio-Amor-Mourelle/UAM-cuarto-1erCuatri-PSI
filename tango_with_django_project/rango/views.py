# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index (request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy cupcake!"}
    # response = HttpResponse("Rango says hey there partner!<br />")
    # response.write("<a href=/rango/about>About page</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Antonio Amor and Esther López"}
    # response = HttpResponse("Rango says here is the about page <br />")
    # response.write("<a href=/rango/>Main page</a>")
    return render(request, 'rango/about.html', context=context_dict)

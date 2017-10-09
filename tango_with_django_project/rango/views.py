# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rango.models import Category, Page
from django.http import HttpResponse

def index (request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': pages_list,
    'boldmessage': "Crunchy, creamy, cookie, candy cupcake!"}
    # response = HttpResponse("Rango says hey there partner!<br />")
    # response.write("<a href=/rango/about>About page</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Antonio Amor and Esther López"}
    # response = HttpResponse("Rango says here is the about page <br />")
    # response.write("<a href=/rango/>Main page</a>")
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
# Can we find a category name slug with the given name?
# If we can't, the .get() method raises a DoesNotExist exception.
# So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
# Retrieve all of the associated pages.
# Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
# Adds our results list to the template context under name pages.
        context_dict['pages']=pages
# We also add the category object from
# the database to the context dictionary.
# We'll use this in the template to verify that the category exist
        context_dict['category'] = category
    except Category.DoesNotExist:
# We get here if we didn't find the specified category.
# Don't do anything -
# the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
# Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)


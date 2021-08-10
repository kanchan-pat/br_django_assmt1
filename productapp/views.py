from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    prod_lst = Product.objects.order_by('-price')
    template = loader.get_template('productapp/index.html')
    context = {
        'prod_lst': prod_lst,
    }

    return HttpResponse( template.render(context, request))

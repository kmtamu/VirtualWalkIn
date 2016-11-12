from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *



def index(request):
    template = loader.get_template('index.html')
    context ={ #Has all the data for index.html view to render to the user
        'var': "Hello"
    }
    return HttpResponse(template.render(context, request))

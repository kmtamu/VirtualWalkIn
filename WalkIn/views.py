from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from opentok import OpenTok
from .models import *

api_key = 45717642
api_secret = "df1752d514a1e6d89f98a66bb661a08c2db8ee73"
opentok = OpenTok(api_key, api_secret) // \\

def index(request):
    template = loader.get_template('index.html')
    context ={ #Has all the data for index.html view to render to the user
        'var': "Hello"
    }
    return HttpResponse(template.render(context, request))

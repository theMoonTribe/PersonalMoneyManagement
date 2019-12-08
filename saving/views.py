'''
Created on 8 Dec 2019

@author: raywong
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")

def home(request):
    return HttpResponse("Home!")
'''
Created on 8 Dec 2019

@author: raywong
'''
from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/saving/
    path('', views.index, name='index'),
    
    #http://127.0.0.1:8000/saving/home
    path('home', views.home, name='home'),
]

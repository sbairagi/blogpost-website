from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.bloghome, name='blogHome'),
    path('<str:slug>', views.blogpost, name='blogPost'),
]

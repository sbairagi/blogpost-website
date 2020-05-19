from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [

    # API to post comment
    path('postComment', views.postComment, name="postComments"),

    path('', views.bloghome, name='blogHome'),
    path('<str:slug>', views.blogpost, name='blogPost')



]

from django.contrib import admin
from django.urls import path
from . import views


app_name='homepage'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('inquiry/', views.inquiry, name='inquiry'),    
 
]
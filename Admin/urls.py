from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns = [
    path('HomePage', views.HomePage,name='Homepage'),
    path("Contact",views.Contact,name='Contact'),
    path("About",views.About,name='About'),


]
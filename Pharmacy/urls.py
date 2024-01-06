from django.urls import path,include
from .import views
from .views import about,cart,home

urlpatterns = [
    path('',about,name="dashboard"),
    path('about',about,name="about"),
    path('cart',cart,name="cart"),
    path('home',home,name="home"),
]


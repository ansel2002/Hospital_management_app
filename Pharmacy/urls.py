from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.about,name="dashboard"),
    path('about',views.about,name="about"),
    path('cart',views.cart,name="cart"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
]


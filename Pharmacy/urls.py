from django.urls import path,include
from .import views
from .views import about,cart

urlpatterns = [
    path('',about,name="dashboard"),
    path('about',about,name="about"),
    path('cart',cart,name="cart"),
]


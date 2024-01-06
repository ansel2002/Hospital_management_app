from django.urls import path,include
from .import views
from .views import about

urlpatterns = [
    path('',about,name="dashboard"),
    path('about',about,name="about"),
]


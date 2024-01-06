from django.urls import path,include
from .import views
from .views import about

urlpatterns = [
    path('',about,name="about"),
]


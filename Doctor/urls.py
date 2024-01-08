from django.urls import path, include
from . import views


urlpatterns = [
    path("HomePage", views.home, name="home"),
    path("doctorpage", views.doctor, name="doctor"),
    path("contactpage", views.contact, name="contact"),

]

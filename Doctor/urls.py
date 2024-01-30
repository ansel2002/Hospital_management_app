from django.urls import path, include
from . import views


urlpatterns = [
    path("HomePage", views.home, name="home"),
    path("doctorpage", views.doctor, name="doctor"),
    path("contactpage", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("blog-details", views.blogdetails, name="blogdetails"),
    path("about", views.about, name="aboutus"),
    path("Login", views.Login, name="login"),
    path("Logout",views.Logout,name="logout"),
    path("Register",views.Register,name="register"),
  
    
    ]

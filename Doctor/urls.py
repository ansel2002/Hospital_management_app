from django.urls import path, include
from . import views


urlpatterns = [
    path("HomePage", views.doctorhome, name="home-doctor"),
    path("doctorpage", views.doctor, name="doctor"),
    path("contactpage", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("blog-details", views.blogdetails, name="blogdetails"),
    path("about", views.about, name="aboutus"),
    path("Login", views.userLogin, name="doc-login"),
    path("Logout",views.userLogout,name="logout"),
    path("Register",views.userRegister,name="doc-register"),
    path("Dashboard",views.doctor_dashboard,name="doc_Dashboard"),
    path("ADD_appointment",views.add_appointment,name="ADD_appointment")
    
    ]

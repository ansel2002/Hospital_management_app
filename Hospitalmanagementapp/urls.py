"""Hospitalmanagementapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include
from ManagementApp.views import index

from Hospitalmanagementapp import settings
from Admin import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("Pharmacy/", include("Pharmacy.urls")),
    path("Doctor/", include("Doctor.urls")),
     path("Doctor/", include("django.contrib.auth.urls")),
    path("Patient/",include("Patient.urls")),
    path('AboutUs', views.homeaboutus,name='home-about'),
    path('ContactUs', views.contactus,name='ContactUs'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path
from Patient import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import patient_login_view









#---------FOR PATIENT RELATED URLS-------------------------------------

urlpatterns = [
    path('patient-login', views.patient_login_view, name='patient-login'),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),    


]
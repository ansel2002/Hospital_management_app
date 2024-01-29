import uuid
import requests
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .import forms
from Admin import models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from datetime import datetime,date
from django.conf import settings
from django.db.models import Q
import os


def patient_home(request):
    return render(request, 'patient/patient_home.html')

def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'patient':patient,
    'doctorName':doctor.get_name,
    'patientMobile':patient.mobile,
    'patientAddress':patient.address,
    'symptoms':patient.symptoms,
    'doctorDepartment':doctor.department,
    'admitDate':patient.admitDate,
    'InsuranceProvider':patient.patientInsuranceProvider,
    'PolicyNumber':patient.patientPolicyNumber,
    'patientId':patient.id
    }
    return render(request,'patient/patient_dashboard.html',context=mydict)


def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'patient/patient_appointment.html',{'patient':patient})

def patient_book_appointment_view(request):
    appointmentForm=forms.PatientAppointmentForm()
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    message=None
    mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm=forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            desc=request.POST.get('description')

            doctor=models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
            
            # if doctor.department == 'Cardiologist':
            #     if 'heart' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            # if doctor.department == 'Dermatologists':
            #     if 'skin' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            # if doctor.department == 'Emergency Medicine Specialists':
            #     if 'fever' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            # if doctor.department == 'Allergists/Immunologists':
            #     if 'allergy' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            # if doctor.department == 'Anesthesiologists':
            #     if 'surgery' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            # if doctor.department == 'Colon and Rectal Surgeons':
            #     if 'cancer' in desc:
            #         pass
            #     else:
            #         print('else')
            #         message="Please Choose Doctor According To Disease"
            #         return render(request,'patient/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('patient-view-appointment')
    return render(request,'patient/patient_book_appointment.html',context=mydict)

def patient_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'patient/patient_view_doctor.html',{'patient':patient,'doctors':doctors})

def search_doctor_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    # whatever user write in search box we get in query
    query = request.GET['query']
    doctors=models.Doctor.objects.all().filter(status=True).filter(Q(department__icontains=query)| Q(user__first_name__icontains=query))
    return render(request,'patient/patient_view_doctor.html',{'patient':patient,'doctors':doctors})


def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'patient/patient_view_appointment.html',{'appointments':appointments,'patient':patient})

def patient_discharge_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    patientDict=None
    # Try to get the patient discharged details for our user
    try:
        dischargeDetails=models.PatientDischargeDetails.objects.get(patientId=patient.id)
    except models.PatientDischargeDetails.DoesNotExist:
        patientDict={
            'is_discharged':False,
            'patient':patient,
        }
    else:
        patientDict ={
        'is_discharged':True,
        'patient':patient,
        'patientId':patient.id,
        'patientName':patient.get_name,
        'assignedDoctorName':dischargeDetails.assignedDoctorName,
        'address':patient.address,
        'mobile':patient.mobile,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'releaseDate':dischargeDetails.releaseDate,
        'daySpent':dischargeDetails.daySpent,
        'medicineCost':dischargeDetails.medicineCost,
        'roomCharge':dischargeDetails.roomCharge,
        'doctorFee':dischargeDetails.doctorFee,
        'OtherCharge':dischargeDetails.OtherCharge,
        'total':dischargeDetails.total,
        'paid':dischargeDetails.total - dischargeDetails.remaining,
        'remaining': dischargeDetails.remaining,
        }
    return render(request,'patient/patient_discharge.html',context=patientDict)



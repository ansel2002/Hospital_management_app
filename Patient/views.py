import uuid
import requests
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from Hospitalmanagementapp.settings import LOG_PATH
from .import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,date
from django.conf import settings
from django.db.models import Q
import logging
import os

def patient_login_view(request):
    return render(request, 'patientlogin.html')


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def patientclick_view(request):
    try:
        if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
        return render(request,'patient/patientclick.html')
    except Exception as e:
        logging.error("error in patientclick_view,error is {}".format(e)) 
        return render(request,'patient/patientclick.html')  
    
def patient_signup_view(request):
    try:
        userForm=forms.PatientUserForm()
        patientForm=forms.PatientForm()
        mydict={'userForm':userForm,'patientForm':patientForm}
        if request.method=='POST':
            userForm=forms.PatientUserForm(request.POST)
            patientForm=forms.PatientForm(request.POST,request.FILES)
            if userForm.is_valid() and patientForm.is_valid():
                user=userForm.save()
                user.set_password(user.password)
                user.save()
                patient=patientForm.save(commit=False)
                patient.user=user
                patient.assignedDoctorId=request.POST.get('assignedDoctorId')
                patient.isDischarged=False
                patient=patient.save()
                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)
                return HttpResponseRedirect('patientlogin')
            else:
                messages.error(request,"Patient User Exist.")
                logging.error("error in patient_signup_view with data already exist.")    
    except Exception as e:
        logging.error("error in patient_signup_view, error is {}".format(e))
        messages.error(request, "There was an internel server error")
        return HttpResponseRedirect('patientlogin')

    return render(request,'hospital/patientsignup.html',context=mydict)

#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
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

def some_function():
    REST_API_PORT = 8000
    url = f'http://localhost:{REST_API_PORT}/transactions'


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'patient/patient_appointment.html',{'patient':patient})


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
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

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'patient/patient_view_appointment.html',{'appointments':appointments,'patient':patient})

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
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
    return render(request,'hospital/patient_discharge.html',context=patientDict)


@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def update_patient_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm, 'patient': patient}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient.save()
            return redirect('patient-dashboard')
    # return render(request,'Admin/admin_update_patient.html',context=mydict)
    return render(request,'Admin/patient_update_patient.html',context=mydict)


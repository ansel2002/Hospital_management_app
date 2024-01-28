from django.shortcuts import render
import uuid
import requests
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from Hospitalmanagementapp.settings import LOG_PATH
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,date
from django.conf import settings
from django.db.models import Q
import logging
import os
# Create your views here.
#log files
#os.makedirs('/var/www/HospitalManagement/hospital/logs', exist_ok=True)
os.makedirs('logs', exist_ok=True)
logFileName= os.path.join(LOG_PATH, str(datetime.now().strftime("%m_%d_%Y") + ".log"))
logging.basicConfig(filename=logFileName,  format='%(asctime)s %(message)s', level=logging.ERROR)

REST_API_PORT = os.getenv('REST_API_PORT')

# Create your views here.
def home_view(request):
    try:
        if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
        return render(request,'Admin/index.html')
    except Exception as e:
        logging.error("error in home_view, error is {}".format(e)) 
        return render(request,'Admin/index.html')   

def adminclick_view(request):
    try:
        if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
        return render(request,'Admin/adminclick.html')
    except Exception as e:
        logging.error("error in adminclick_view, error is {}".format(e)) 
        return render(request,'Admin/adminclick.html')  


def admin_signup_view(request):
    try:
        form=forms.AdminSigupForm()
        if request.method=='POST':
            form=forms.AdminSigupForm(request.POST)
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
                my_admin_group = Group.objects.get_or_create(name='ADMIN')
                my_admin_group[0].user_set.add(user)
                return HttpResponseRedirect('adminlogin')
            else:
                messages.error(request,"Admin User Exist.")
                logging.error("error in admin_signup_view with data already exist.")    
    except Exception as e:
        logging.error("error in admin_signup_view, error is {}".format(e))
        return HttpResponseRedirect('adminlogin')
    return render(request,'Admin/adminsignup.html',{'form':form})



def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def authentication_view(request):
    OTPForm = forms.OneTimePasswordForm()
    context = {'form': OTPForm}
    if request.method == 'POST':
        OTPForm = forms.OneTimePasswordForm(request.POST)
        if OTPForm.is_valid():
            entered_otp = OTPForm['code'].value()
            valid_otp = settings.OTP.now()
            if valid_otp == entered_otp:
                print('The user has entered a valid OTP. Logging in')
                return HttpResponseRedirect('afterlogin')
            else:
                print('The user has entered an incorrect OTP code.')
                messages.error(request, "Incorrect OTP Code.")
        else:
            messages.error(request, "Incorrect OTP Code.")
    return render(request, 'Admin/authentication.html', context)




#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR , STAFF, INSURANCESTAFF OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'Admin/doctor_wait_for_approval.html')
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
        else:
            return render(request,'Admin/patient_wait_for_approval.html')
        


#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    hospitalstaffs=models.HospitalStaff.objects.all().order_by('-id')
    labstaff = models.LabStaff.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    insurance=models.Insurance.objects.all().order_by('-id')

    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().filter(status=False).count()

    hospitalstaffcount=models.HospitalStaff.objects.all().filter(status=True).count()
    pendinghospitalstaffcount=models.HospitalStaff.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'hospitalstaffs':hospitalstaffs,
    'labstaff':labstaff,
    'patients':patients,
    'insurance':insurance,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'hospitalstaffcount':hospitalstaffcount,
    'pendinghospitalstaffcount':pendinghospitalstaffcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'Admin/admin_dashboard.html',context=mydict)

# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'Admin/admin_view_doctor_specialisation.html',{'doctors':doctors})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'Admin/admin_view_doctor.html',{'doctors':doctors})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-view-doctor')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    try:
        doctor=models.Doctor.objects.get(id=pk)
        
        user=models.User.objects.get(id=doctor.user_id)

        userForm=forms.DoctorUserForm(instance=user)
        doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
        mydict={'userForm':userForm,'doctorForm':doctorForm}
        if request.method=='POST':
            userForm=forms.DoctorUserForm(request.POST,instance=user)
            doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
            if userForm.is_valid() and doctorForm.is_valid():
                user=userForm.save()
                user.set_password(user.password)
                user.save()
                doctor=doctorForm.save(commit=False)
                doctor.status=True
                doctor.save()
                
                return redirect('admin-view-doctor')
    except Exception as e:
        logging.error("error in update_doctor_view, error is {}".format(e))
        return redirect('admin-view-doctor')
    return render(request,'Admin/admin_update_doctor.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    try:
        userForm=forms.DoctorUserForm()
        doctorForm=forms.DoctorForm()
        mydict={'userForm':userForm,'doctorForm':doctorForm}
        if request.method=='POST':
            userForm=forms.DoctorUserForm(request.POST)
            doctorForm=forms.DoctorForm(request.POST, request.FILES)
            if userForm.is_valid() and doctorForm.is_valid():
                user=userForm.save()
                user.set_password(user.password)
                user.save()

                doctor=doctorForm.save(commit=False)
                doctor.user=user
                doctor.status=True
                doctor.save()

                my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
                my_doctor_group[0].user_set.add(user)
                return HttpResponseRedirect('admin-view-doctor')
            else:
                logging.error("invalid form with data exist in admin doctor view")
                return HttpResponseRedirect('admin-add-doctor')
    except Exception as e:
        logging.error("error in admin add doctor view, error is {}".format(e))
        return redirect('admin-view-doctor')        
    return render(request,'hospital/admin_add_doctor.html',context=mydict)

# approving doctor
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'Admin/admin_approve_doctor.html',{'doctors':doctors})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    #those whose approval are needed
    try:
        doctor=models.Doctor.objects.get(id=pk)
        doctor.status=True
        doctor.save()
        # return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})
        return redirect(reverse('admin-approve-doctor'))
    except Exception as e:
        logging.error("error in admin_approve_doctor_view,error is {}".format(e))
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
        return redirect(reverse('admin-approve-doctor'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_doctor_view(request,pk):
    try:
        doctor=models.Doctor.objects.get(id=pk)
        user=models.User.objects.get(id=doctor.user_id)
        user.delete()
        doctor.delete()
        return redirect('admin-approve-doctor')
    except Exception as e:
        logging.error("error in reject_doctor_view,error is {}".format(e))
        return redirect('admin-approve-doctor') 
    

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'Admin/admin_patient.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'Admin/admin_patient.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'Admin/admin_view_patient.html',{'patients':patients})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient') 

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
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
                patient.status=True
                patient.assignedDoctorId=request.POST.get('assignedDoctorId')
                patient.save()

                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)

                return HttpResponseRedirect('admin-view-patient')

            else:
            
                logging.error("invalid form with data exist in admin view patient")
                return HttpResponseRedirect('admin-add-patient')
    except Exception as e: 
        logging.error("error in add admin patient view, error is {}".format(e))  
        return redirect('admin-view-patient')        
    return render(request,'Admin/admin_add_patient.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'Admin/admin_patient.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all().filter(status=True)
    return render(request,'Admin/admin_view_patient.html',{'patients':patients})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    try:
        patient=models.Patient.objects.get(id=pk)
        user=models.User.objects.get(id=patient.user_id)
        user.delete()
        patient.delete()
        return redirect('admin-view-patient')
    except Exception as e:
        logging.error("error in delete patient view from hospital, error is {}".format(e))
        return redirect('admin-view-patient')  
    
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    try:
        patient=models.Patient.objects.get(id=pk)
        user=models.User.objects.get(id=patient.user_id)

        userForm=forms.PatientUserForm(instance=user)
        patientForm=forms.PatientForm(request.FILES,instance=patient)
        mydict={'userForm':userForm,'patientForm':patientForm}
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
                return redirect('admin-view-patient')
    except Exception as e: 
        logging.error("error in update patient view, error is {}".format(e))  
        return redirect('admin-view-patient')             
    return render(request,'Admin/admin_update_patient.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
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
                patient.status=True
                patient.assignedDoctorId=request.POST.get('assignedDoctorId')
                patient.isDischarged=False
                patient.save()

                my_patient_group = Group.objects.get_or_create(name='PATIENT')
                my_patient_group[0].user_set.add(user)

                return HttpResponseRedirect('admin-view-patient')

            else:
                logging.error("invalid form with data exist in admin view patient")
                return HttpResponseRedirect('admin-add-patient')
    except Exception as e: 
        logging.error("error in add admin patient view, error is {}".format(e))  
        return redirect('admin-view-patient')        
    return render(request,'hospital/admin_add_patient.html',context=mydict)

#------------------FOR APPROVING PATIENT BY ADMIN----------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_patient_view(request):
    #those whose approval are needed
    try:
        patients=models.Patient.objects.all().filter(status=False)
        return render(request,'Admin/admin_approve_patient.html',{'patients':patients})
    except Exception as e:
        logging.error("error in admin approve patient view from hospital, error is {}".format(e))
        return render(request,'Admin/admin_approve_patient.html',{'patients':patients})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_patient_view(request,pk):
    try:
        patient=models.Patient.objects.get(id=pk)
        patient.status=True
        patient.save()
        return redirect(reverse('admin-approve-patient'))
    except Exception as e:   
        logging.error("error in approve patient view from hospital, error is {}".format(e))
        return redirect(reverse('admin-approve-patient'))
        
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_patient_view(request,pk):
    try:
        patient=models.Patient.objects.get(id=pk)
        user=models.User.objects.get(id=patient.user_id)
        user.delete()
        patient.delete()
        return redirect('admin-approve-patient')
    except Exception as e:
        logging.error("error in reject_patient_view,error is {}".format(e))
        return redirect('admin-approve-patient') 
    

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def discharge_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    days=(date.today()-patient.admitDate) #2 days, 0:00:00
    assignedDoctor=models.User.objects.all().filter(id=patient.assignedDoctorId)
    d=days.days # only how many day that is 2
    patientDict={
        'patientId':pk,
        'name':patient.get_name,
        'mobile':patient.mobile,
        'address':patient.address,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'todayDate':date.today(),
        'day':d,
        'assignedDoctorName':assignedDoctor[0].first_name,
    }
    if request.method == 'POST':
        feeDict ={
            'roomCharge':int(request.POST['roomCharge'])*int(d),
            'doctorFee':request.POST['doctorFee'],
            'medicineCost' : request.POST['medicineCost'],
            'OtherCharge' : request.POST['OtherCharge'],
            'total':(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        }
        patientDict.update(feeDict)
        #for updating to database patientDischargeDetails (pDD)
        pDD=models.PatientDischargeDetails()
        pDD.patientId=pk
        pDD.patientName=patient.get_name
        pDD.assignedDoctorName=assignedDoctor[0].first_name
        pDD.address=patient.address
        pDD.mobile=patient.mobile
        pDD.symptoms=patient.symptoms
        pDD.admitDate=patient.admitDate
        pDD.releaseDate=date.today()
        pDD.daySpent=int(d)
        pDD.medicineCost=int(request.POST['medicineCost'])
        pDD.roomCharge=int(request.POST['roomCharge'])*int(d)
        pDD.doctorFee=int(request.POST['doctorFee'])
        pDD.OtherCharge=int(request.POST['OtherCharge'])
        pDD.total=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        pDD.remaining=(int(request.POST['roomCharge'])*int(d))+int(request.POST['doctorFee'])+int(request.POST['medicineCost'])+int(request.POST['OtherCharge'])
        pDD.save()
        
        # Discharge the patient
        patient.isDischarged = True
        patient.save()
        return render(request,'Admin/patient_final_bill.html',context=patientDict)
    return render(request,'Admin/patient_generate_bill.html',context=patientDict)


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

def download_pdf_view(request,pk):
    dischargeDetails=models.PatientDischargeDetails.objects.get(patientId=pk).order_by('-id')[:1]
    dict={
        'patientName':dischargeDetails.patientName,
        'assignedDoctorName':dischargeDetails.assignedDoctorName,
        'address':dischargeDetails.address,
        'mobile':dischargeDetails.mobile,
        'symptoms':dischargeDetails.symptoms,
        'patientInsuranceProvider':dischargeDetails.patientInsuranceProvider,
        'patientPolicyNumber':dischargeDetails.patientPolicyNumber,
        'admitDate':dischargeDetails.admitDate,
        'releaseDate':dischargeDetails.releaseDate,
        'daySpent':dischargeDetails.daySpent,
        'medicineCost':dischargeDetails.medicineCost,
        'roomCharge':dischargeDetails.roomCharge,
        'doctorFee':dischargeDetails.doctorFee,
        'OtherCharge':dischargeDetails.OtherCharge,
        'total':dischargeDetails.total,
        'paid':dischargeDetails.total - dischargeDetails.remaining,
        'remaining':dischargeDetails.remaining,
    }
    return render_to_pdf('hospital/download_bill.html',dict)


#-----------------APPOINTMENT START--------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_appointment_view(request):
    return render(request,'Admin/admin_appointment.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_appointment_view(request):
    try:

        appointments=models.Appointment.objects.all().filter(status=True)
        return render(request,'Admin/admin_view_appointment.html',{'appointments':appointments})
    except Exception as e:
        logging.error("error in admin-view-appointment-view , error is {}".format(e))
        return render(request,'Admin/admin_view_appointment.html',{'appointments':appointments})
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_appointment_view(request):
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status=True
            appointment.save()
            patient = models.Patient.objects.get(user__id=appointment.patientId)
            patient.isDischarged = False
            patient.save()
        return HttpResponseRedirect('admin-view-appointment')
    return render(request,'hospital/admin_add_appointment.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_appointment_view(request):
    #those whose approval are needed
    try:
        appointments=models.Appointment.objects.all().filter(status=False)
        return render(request,'Admin/admin_approve_appointment.html',{'appointments':appointments})
    except Exception as e:
        logging.error("error in admin-approve-appointment-view , error is {}".format(e))
        return render(request,'Admin/admin_approve_appointment.html',{'appointments':appointments})
    
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_appointment_view(request,pk):
    try:
        appointment=models.Appointment.objects.get(id=pk)
        appointment.status=True
        appointment.save()
        patient = models.Patient.objects.get(user__id=appointment.patientId)
        patient.isDischarged = False
        patient.save()
        return redirect(reverse('admin-approve-appointment'))
    except Exception as e:
        logging.error("error in admin-approve-appointment,error is {}".format) 
        return redirect('admin-approve-appointment')
            
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_appointment_view(request,pk):
    try:
        appointment=models.Appointment.objects.get(id=pk)
        appointment.delete()
        return redirect('admin-approve-appointment')
    except Exception as e:
        logging.error("error in reject-appointment-view,error is {}".format) 
        return redirect('admin-approve-appointment')
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import MyLogInFrm, MyRegFrom, ChangeProfileFrm, AppointmentForm
from .models import Schedule, Contact, Doctor, Appointment
from django.urls import is_valid_path
import datetime


# from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'Patient/index.html')

def about(request):
    return render(request, 'Patient/about.html')


def service(request):
    return render(request, 'Patient/service.html')


def gallery(request):
    return render(request, 'Patient/gallery.html')


def team(request):
    return render(request, 'Patient/team.html')


def appointment(request):
    return render(request, 'Patient/appointment.html')


def blog(request):
    return render(request, 'Patient/blog.html')


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        return render(request, 'thanks.html')
    else:
        return render(request, 'Patient/contact.html')


def registration(request):
    if request.POST:
        form = MyRegFrom(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Patient registration is successful')
            except Exception as e:
                messages.error(request, 'Patient registration is unsuccessful')
    else:
        form = MyRegFrom()
    context = {'form': form}
    return render(request, 'registration.html', context)


def UserLogin(request):
    if request.POST:
        form = MyLogInFrm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile')
    else:
        form = MyLogInFrm()
    return render(request, 'login.html', {'form': form})


def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def profile(request):
    if request.user.is_authenticated:
        alldoc = Schedule.objects.raw(
            "SELECT s.*, d.* FROM myapplications_schedule s INNER JOIN myapplications_doctor d ON s.doctor_id=d.d_id")
        return render(request, 'profile.html', {'alldoc': alldoc})
    else:
        return HttpResponseRedirect('/login')


def changeProfile(request):
    if request.user.is_authenticated:
        if request.POST:
            form = ChangeProfileFrm(request.POST, instance=request.user)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Profile Update successfully')
                except Exception as e:
                    messages.error(request, e)
        else:
            form = ChangeProfileFrm(instance=request.user)
        return render(request, 'changeProfile.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def makeAppoint(request, d_id):
    if request.user.is_authenticated:
        if request.POST:
            schedule = Schedule.objects.get(doctor=d_id)
            sDays = schedule.days.split()
            appdate = datetime.datetime.strptime(request.POST.get('app_fix_date'), "%Y-%m-%d").date()
            appSDay = appdate.strftime('%A')
            # print(appSDay)
            # print(sDays)
            form = AppointmentForm(request.POST)
            if form.is_valid():
                f = 0
                for d in sDays:
                    if appSDay == d:
                        f = 1
                if f == 1:
                    instance = form.save(False)
                    instance.doctor_id = d_id
                    instance.user_id = request.user.id
                    instance.save()
                    messages.success(request, 'Your appointment has been made successfully')
                else:
                    messages.error(request, 'Doctor will not available that day')
        else:
            form = AppointmentForm()
        alldoc = Schedule.objects.raw(
            "SELECT s.*, d.* FROM myapplications_schedule s INNER JOIN myapplications_doctor d ON s.doctor_id=d.d_id WHERE s.doctor_id={}".format(
                d_id))
        return render(request, 'appoint.html', {'alldoc': alldoc, 'form': form})
    else:
        return HttpResponseRedirect('/login')


def appointmentHistory(request):
    if request.user.is_authenticated:
        myApp = Appointment.objects.raw(
            "SELECT a.*, d.d_name, s.days, s.time_slot FROM myapplications_appointment a INNER JOIN myapplications_doctor d ON  a.doctor_id=d.d_id INNER JOIN myapplications_schedule s ON a.doctor_id=s.doctor_id WHERE a.user_id={}".format(
                request.user.id))
        return render(request, 'Patient/appointmenthistory.html', {'myapp': myApp})
    else:
        return HttpResponseRedirect('/login')

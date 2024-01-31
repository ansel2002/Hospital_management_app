from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Appointment
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Create your views here.
def doctorhome(request):
    return render(request, "Doctor/home.html", context={})


def doctor(request):
    return render(request, "Doctor/doctors.html", context={})


def contact(request):
    return render(request, "Doctor/contact.html", context={})


def blog(request):
    return render(request, "Doctor/blog.html", context={})


def blogdetails(request):
    return render(request, "Doctor/blog-details.html", context={})


def about(request):
    return render(request, "Doctor/about.html", context={})


def userLogin(request):
    if request.method == "POST":
        username1 = request.POST["Username"].strip()
        password1 = request.POST["Password"].strip()
        print(username1, password1)
        user = authenticate(request,username=username1, password=password1)
        print(user)
        if user is not None:
            login(request, user)
            print(user)
            return redirect("home-doctor")
        else:
            print(user)
            messages.success(
                request, ("there was error logging in !!!!! . please try againn")
            )
            return redirect("home-doctor")

    else:
        return render(request, "Doctor/login.html", context={})


def userLogout(request):
    logout(request)
    messages.success(request, ("You were logged out !!!!"))
    return redirect("home-doctor")


def userRegister(request):
    if request.method == "POST":
        username1 = request.POST.get("Username").strip()
        passsword1 = request.POST.get("Password").strip()
        email1=request.POST.get('email').strip()
        user = User.objects.create_user(
            email=email1,username=username1, password=passsword1)
        user.save()
        
        
        messages.success(request, ("Registration is succesfull"))
        return redirect("home-doctor")
    else:
        return redirect("doc-login")


def doctor_dashboard(request):
    appointments = Appointment.objects.all()
    return render(request, "Doctor/dashboard.html", {"appointments": appointments})


def add_appointment(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        appointment_date = request.POST.get("appointment_date")
        Appointment.objects.create(
            patient_name=patient_name, appointment_date=appointment_date
        )
        return redirect("doc_Dashboard")
    return render(request, "Doctor/add_appointment.html")

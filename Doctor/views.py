from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


# Create your views here.
def home(request):
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


def Login(request):
    if request.method == "POST":
        username = request.POST["Username"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(
                request, ("there was error logging in !!!!! . please try againn")
            )
            return redirect("login")

    else:
        return render(request, "Doctor/login.html", context={})


def Logout(request):
    logout(request)
    messages.success(request, ("You were logged out !!!!"))
    return redirect("home")


def Register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["Username"]
            passsword = form.cleaned_data["Password"]
            user = authenticate(username=username, passsword=passsword)
            login(request, user)
            messages.success(request, ("Registration is succesfull"))
            return redirect("home")
    else:
         form = RegisterUserForm()
    
    return render(request,"Doctor/login.html",{
            "form": form,
            })


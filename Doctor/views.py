from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
            messages.success(request, ("there was error logging in !!!!! . please try againn"))
            return redirect("login")

    else:
        return render(request, "Doctor/login.html", context={})

def Logout(request):
    logout(request)
    messages.success(request, ("You were logged out !!!!"))
    return redirect('home')
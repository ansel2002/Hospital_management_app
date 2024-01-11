from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Doctor/home.html", context={})


def doctor(request):
    return render(request, "Doctor/doctors.html", context={})

def contact(request):
    return render(request,"Doctor/contact.html",context={})

def blog(request):
    return render(request,"Doctor/blog.html",context={})

def blogdetails(request):
    return render(request,"Doctor/blog-details.html",context={})

def about(request):
    return render(request,"Doctor/about.html",context={})

def Login(request):
    return render(request,"Doctor/login.html",context={})
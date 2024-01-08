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
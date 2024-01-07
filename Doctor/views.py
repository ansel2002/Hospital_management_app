from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "Doctor/home.html", context={})


def doctor(request):
    return render(request, "Doctor/doctors.html", context={})

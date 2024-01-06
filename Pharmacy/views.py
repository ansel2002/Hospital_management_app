from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "Pharmacy/about.html", context={})

def cart(request):
    return render(request, "Pharmacy/cart.html", context={})

def home(request):
    return render(request, "Pharmacy/home.html", context={})

from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "Pharmacy/about.html", context={})

def cart(request):
    return render(request, "Pharmacy/cart.html", context={})

def home(request):
    return render(request, "Pharmacy/home.html", context={})

def contact(request):
    return render(request, "Pharmacy/contact.html", context={})

def store(request):
    return render(request, "Pharmacy/store.html", context={})

def shop(request):
    return render(request, "Pharmacy/shop-single.html", context={})

def checkout(request):
    return render(request, "Pharmacy/checkout.html", context={})


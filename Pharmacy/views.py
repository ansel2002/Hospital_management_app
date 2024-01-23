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

<<<<<<< HEAD
=======
def thankyou(request):
    return render(request, "Pharmacy/thankyou.html", context={})

>>>>>>> ed88edbd53316a93b858096890b7d21610237d3a

def logintoapp(request):
    
    return render(request)
<<<<<<< HEAD
=======

>>>>>>> ed88edbd53316a93b858096890b7d21610237d3a
def store(request):
    return render(request, "Pharmacy/store.html", context={})

def shop(request):
    return render(request, "Pharmacy/shop-single.html", context={})

def checkout(request):
    return render(request, "Pharmacy/checkout.html", context={})

<<<<<<< HEAD
=======
def addItem(request, product_id):
    return(request,)


def addQnty(request,product_id):
    obj=addItem(product_id=id)
    obj.Qnty=Qnty+1
    return(request,)

def removeQnty(request, product_id,currentQnty):
    obj= addItem(product_id=id)
    obj.Qnty=Qnty-1


>>>>>>> ed88edbd53316a93b858096890b7d21610237d3a

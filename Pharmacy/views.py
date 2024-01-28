from django.shortcuts import render,redirect
from Pharmacy.models import Store

# Create your views here.

def about(request):
    return render(request, "Pharmacy/about.html", context={})

def cart(request):
    return render(request, "Pharmacy/cart.html", context={})

def home(request):
    return render(request, "Pharmacy/home.html", context={})

def contact(request):
    return render(request, "Pharmacy/contact.html", context={})

def thankyou(request):
    return render(request, "Pharmacy/thankyou.html", context={})


def product(request):
    return render(request, "Pharmacy/product_table.html", context={})


def logintoapp(request):
    
    return render(request)

def store(request):
    return render(request, "Pharmacy/store.html", context={})

def shop(request):
    return render(request, "Pharmacy/shop-single.html", context={})

def checkout(request):
    return render(request, "Pharmacy/checkout.html", context={})

# def updateStore(request):
#     return render(request, "Pharmacy/updateStore.html", context={})
# def addItem(request, product_id):
#     return(request,)


# def addQnty(request,product_id):
#     obj=addItem(product_id=id)
#     obj.Qnty=Qnty+1
#     return(request,)

# def removeQnty(request, product_id,currentQnty):
#     obj= addItem(product_id=id)
#     obj.Qnty=Qnty-1

def addProduct(request):
    if request.method=="POST":
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        quantity=request.POST.get('Qnty')
        image=request.FILES.get('img')
        expiry_date=request.POST.get('expiry_date')
        provider=request.POST.get('provider')
        route=request.POST.get('route')
        status = False
        if provider == "True":
            status = True
        product_details=Store(product_id=product_id,product_name=product_name,description=description,price=price,quantity=quantity,image=image,expiry_date=expiry_date,provider_status=status,medication_route=route)
        product_details.save()
        return redirect('addProduct')
    
    product_details=Store.objects.all()
    return render(request,'pharmacy\\updateStore.html', {'product_details':product_details})

# def addToStore(request):


    


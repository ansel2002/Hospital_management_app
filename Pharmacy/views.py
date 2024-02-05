from django.shortcuts import render, redirect
from Pharmacy.models import Store, medicineRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render,redirect
from Pharmacy.models import Store, medicineRequest, Cart,CartItems
from Admin.models import Patient


# Create your views here.


def about(request):
    return render(request, "Pharmacy/about.html", context={})


def cart(request):
    return render(request, "Pharmacy/cart.html", context={})


def homePage(request):
    return render(request, "Pharmacy/home.html", context={})


def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("requestfirstname")
        last_name = request.POST.get("requestlastname")
        contact_number = request.POST.get("requestnumber")
        medicine_name = request.POST.get("requestmedicine")
        prescription = request.FILES.get("prescription")
        requestDate = request.POST.get("requestdate")
        request_details = medicineRequest(
            first=first_name,
            last=last_name,
            contact=contact_number,
            medicine_name=medicine_name,
            prescription=prescription,
            Date=requestDate,
        )
        request_details.save()
        return redirect("contactUs")
    return render(request, "Pharmacy/contact.html", context={})


def thankyou(request):
    return render(request, "Pharmacy/thankyou.html", context={})


def portal(request):
    return render(request, "Pharmacy/pharmacy_portal.html", context={})


def addProduct(request):
    return render(request, "Pharmacy/product_table.html", context={})


def logintoapp(request):

    return render(request)

def store(request,):
    product_details=Store.objects.all()
    return render(request, "Pharmacy/store.html", context={'product_details':product_details})

def shop(request,id):
    product = Store.objects.get(product_id=id)
    return render(request, "Pharmacy/shop-single.html", context={'product':product})


def checkout(request):
    return render(request, "Pharmacy/checkout.html", context={})


def updateStore(request):
    return render(request, "Pharmacy/updateStore.html", context={})


def Request(request):
    return render(request, "Pharmacy/viewRequest.html", context={})


# def addItem(request, product_id):
#     return(request,)
# def addItem(request, product_id):
#     return(request,)


# def addQnty(request,product_id):
#     obj=addItem(product_id=id)
#     obj.Qnty=Qnty+1
#     return(request,)


def catelogue(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        quantity = request.POST.get("Qnty")
        image = request.FILES.get("img")
        expiry_date = request.POST.get("expiry_date")
        provider = request.POST.get("provider")
        route = request.POST.get("route")
        status = False
        if provider == "True":
            status = True
        print(product_name, "-------")
        product_details = Store(
            product_id=product_id,
            product_name=product_name,
            description=description,
            price=price,
            quantity=quantity,
            image=image,
            expiry_date=expiry_date,
            provider_status=status,
            medication_route=route,
        )
        product_details.save()
        return redirect("catelogue")

    product_details = Store.objects.all()
    return render(
        request, "pharmacy\\updateStore.html", {"product_details": product_details}
    )


def deleteProduct(request, id):
    product = Store.objects.get(product_id=id)
    product.delete()
    return redirect("catelogue")


def editProduct(request, id):
    product = Store.objects.get(product_id=id)
    return render(request, "Pharmacy\\editProduct.html", {"product": product})


def viewRequest(request):
    request_details = medicineRequest.objects.all()
    return render(
        request, "pharmacy\\viewRequest.html", {"request_details": request_details}
    )


def pharm_login(request):
    if request.method == "POST":
        email1 = request.POST["Email"].strip()
        password1 = request.POST["Password"].strip()
        print(email1, password1)
        user = authenticate(request, email=email1, password=password1)
        print(user)
        if user is not None:
            login(request, user)
            print(user)
        else:

            messages.success(
                request, ("there was error logging in !!!!! . please try againn")
            )
            return redirect("homePage")

    else:
        return render(request, "Pharmacy/pharm_login.html", context={})


def pharm_register(request):
    if request.method == "POST":
        passsword1 = request.POST.get("password")
        email1 = request.POST.get("Email")
        user = User.objects.create_user(email=email1, password=passsword1)
        user.save()

        messages.success(request, ("Registration is succesfull"))
        return redirect("homePage")
    else:
        return redirect("pharm_login")

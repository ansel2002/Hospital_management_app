from django.db import models

# Models for product
class Store(models.Model):  
    product_id = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(blank=False,max_length=200)
    description = models.TextField(blank=False,max_length=200)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='product_images/')
    expiry_date = models.DateField(blank=False)
    provider_status = models.BooleanField(blank=True)
    medication_route = models.TextField(blank=False,max_length=20)  

    def __str__(self):
        return str(self.product_name.__str__())

class Cart(models.Model): 
    cart_id = models.CharField(max_length=20,primary_key=True)
    user_id = models.CharField(blank=False,max_length=20)
    user_name = models.CharField(blank=False,max_length=50)  
    total = models.FloatField(blank=False)

    def __self__(self):
        return f"Cart for {self.user_name}"

class CartItems(models.Model): 
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE,blank=False)
    product_id = models.ForeignKey(Store, on_delete=models.CASCADE,blank=False)
    quantity = models.PositiveIntegerField(blank=False)  

    def __str__(self):
        return str({self.cart_id.__str__()}) + "-" + str({self.product_id.__str__()})

class Billing(models.Model):  
    user_id = models.CharField(max_length=20,blank=False)
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    country = models.CharField(max_length=50,blank=False)  
    address = models.CharField(max_length=100,blank=False)  
    state = models.CharField(max_length=50,blank=False)  
    pincode = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    phone = models.IntegerField(blank=False)
    order_notes = models.TextField(max_length=500,blank=False) 

    def __str__(self):
        return str({self.first_name.__str__()}) + "-" + str({self.last_name.__str__()}) + "-" + str({self.phone.__str__()})
        
class medicineRequest(models.Model):
    first = models.CharField(max_length=50,blank=False)
    last = models.CharField(max_length=50,blank=False)
    contact = models.IntegerField(blank=False)
    medicine_name = models.CharField(max_length=50,blank=False)
    prescription = models.ImageField(upload_to='prescriptions/')
    Date=models.DateField(blank=False)

    def __str__(self):
        return str(self.medicine_name.__str__())
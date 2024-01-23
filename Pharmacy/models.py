from django.db import models

# Models for product
class Store(models.Model):  
    product_id = models.CharField(max_length=20, primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField()
    expiry_date = models.DateField()
    provider_status = models.BooleanField()
    latex_free_status = models.BooleanField()  
    medication_route = models.TextField()  

class Cart(models.Model): 
    cart_id = models.CharField(max_length=20,primary_key=True)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=50)  
    total = models.FloatField()

class CartItems(models.Model): 
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()  

class Billing(models.Model):  
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)  
    address = models.CharField(max_length=100)  
    state = models.CharField(max_length=50)  
    pincode = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    order_notes = models.TextField(max_length=500) 


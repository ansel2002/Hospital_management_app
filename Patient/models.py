from django.db import models
from Doctor.models import models
from django.contrib.auth.models import User
from django.db import models
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


# Create your models here.  

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, verbose_name='Contact Number')
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=12)


# class newpatient(models.Model):
#     username=models.models.CharField(max_length=50)
#     email=models.EmailField(max_length=254)
#     password=models.IntegerField()

class Doctor(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=255, verbose_name='Doctor Name')
    d_mobile = models.CharField(max_length=15, verbose_name='Doctor Contact Number')
    d_qualification = models.CharField(max_length=255)
    d_specialist = models.CharField(max_length=255)
    d_yoe = models.CharField(max_length=2, verbose_name='Year Of Experience')
    remaining = models.IntegerField(default=0,null=True)  

class Schedule(models.Model):
    sid = models.AutoField(primary_key=True)
    days = models.CharField(max_length=255, verbose_name='Doctors Available')
    time_slot = models.CharField(max_length=255, verbose_name='Timing')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor', verbose_name='Doctor')


class Appointment(models.Model):
    app_id = models.AutoField(primary_key=True,)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctors', verbose_name='Doctor')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient', verbose_name='Patient')
    app_made_on = models.DateField(auto_now_add=True, blank=False, verbose_name='Appointment Booking Date')
    app_fix_date = models.DateField(verbose_name='Appointment Date', blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name


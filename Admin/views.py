from django.shortcuts import render
import uuid
#import requests
from django.shortcuts import render,redirect,reverse

# Create your views here.
def Dashboard(request):
    return render(request,'dashboard.html',context  ={})
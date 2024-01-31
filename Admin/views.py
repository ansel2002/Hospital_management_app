from django.shortcuts import render
import uuid
#import requests
from django.shortcuts import render,redirect,reverse

# Create your views here.
def HomePage(request):
    return render(request,'index.html',context  ={})

def Contact(request):
    return render(request,'contact.html',context ={})

def About(request):
    return render(request,'about.html',context ={})
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    name=request.GET['name']
    password=request.GET['password']
    address=request.GET['address']
    mail=request.GET['mail']
    return render(request,"output.html",{'Name':name,'Password':password,'Address':address,'Mail':mail})
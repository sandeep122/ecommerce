from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import render,redirect


def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'store.html',context)


def checkout(request):
    return render(request,'checkout.html')

def main(request):
    return render(request,'main.html')

def offer(request):
    offers=Offer.objects.all()
    context={'offers':offers}
    return render(request,'offer.html',context)

def add_to_cart(request,name,price):
    name=Product.objects.get(name)
    cart=Cart(request)
    cart.add(name,price)

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            print("login failled")
            return redirect('login')
    else:

        return render(request,'login.html')

def cartes(request):
 
    return render(request,'cartes.html')


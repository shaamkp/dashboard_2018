from django.shortcuts import render, redirect
from product.models import Product
from user.models import Login
from django.contrib.auth import authenticate



def user_login(request):  
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session["username"] = username
            return  redirect("/")

    return render(request, "registration/login.html")


def user_logout(request):
    if "username" in request.session:
        del request.session["username"]
        
    return redirect('/') 



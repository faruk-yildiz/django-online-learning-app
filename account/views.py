from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):

    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"account/login.html",{
                "error":"kullanıcı adı ya da parola yanlış"
            })
    return render(request,"account/login.html")

def signUp_request(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request,"account/signup.html",{"error":"Bu kullanıcı adı kullanılıyor"})
        else:
            user=User.objects.create(username=username,password=password)
            user.save()
            return redirect("login")
    return render(request,"account/signup.html")

def logout_request(request):
    logout(request)
    return redirect("home")
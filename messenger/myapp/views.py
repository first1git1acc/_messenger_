from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.models import User

class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"plasceholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Username"}))

class Registration(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

def main_page(request):
    return render(request,"myapp/main_page.html")

def for_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("myapp:user_page"))
    return render(request,"myapp/logining.html",{
        "login_form":Login(),
    })

def for_registration(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
                new_user = User.objects.create_user(password=password,username=username,email=email)
                new_user.save()
                return HttpResponseRedirect(reverse("myapp:for_login"))
            else:
                return render(request,"myapp/regstration.html",{
                    "registration_form":Registration(),
                    "error":"User with the same email or username already exist!"
                })

    return render(request,"myapp/registration.html",{
        "registration_form":Registration(),
    })

def user_page(request):
    return render(request,"myapp/userpage.html")

def  log_out(request):
    logout(request)
    return render(request,"myapp/main_page.html")

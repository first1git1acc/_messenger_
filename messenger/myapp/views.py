from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

class Login(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={"plasceholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Username"}))

class Registration(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

def main_page(request):
    return render(request,"myapp/main_page.html")

def for_login(request):
    return render(request,"myapp/logining.html",{
        "login_form":Login(),
    })

def for_registration(request):
    return render(request,"myapp/registration.html",{
        "registration_form":Registration(),
    })


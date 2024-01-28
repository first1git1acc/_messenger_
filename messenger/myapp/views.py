from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def main_page(request):
    return render(request,"myapp/main_page.html")

def for_login(request):
    return render(request,"myapp/logining.html")

def for_registration(request):
    return render(request,"myapp/registration.html")
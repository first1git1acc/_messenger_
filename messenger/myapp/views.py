from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import userPage, Post
from django.utils import timezone
from myapp.forms import Login, Registration, add_new_post

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
    user_obj = userPage.objects.filter(user=request.user.id)[0]
    user_obj.status = "Online"
    user_obj.time = timezone.now()
    user_obj.save()
    return render(request,"myapp/userpage.html",{
        "status":user_obj.status,
        "time":user_obj.time,
        "all_posts":Post.objects.all()
    })

def  log_out(request):
    user_obj = userPage.objects.filter(user=request.user.id)[0]
    user_obj.status = "Offline"
    user_obj.save()
    logout(request)
    return render(request,"myapp/main_page.html")

def adding_post(request):
    if request.method == "POST":
        form = add_new_post(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            slug = form.cleaned_data['slug']
            obj = Post(title = title, body = body, slug = slug, add_time = timezone.now(), user = request.user)
            obj.save()
            return HttpResponseRedirect(reverse('myapp:user_page'))
    return render(request,'myapp/add_post.html',{
        "post_form":add_new_post(),
    })

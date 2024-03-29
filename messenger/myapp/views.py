from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import userPage, Post, Comment
from django.utils import timezone
from myapp.forms import Login, Registration, add_new_post, find_form, Commentar, find_by_tags
from django.shortcuts import get_object_or_404
from taggit.models import Tag
#from django.core.mail import send_mail

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
    if request.method == "POST":
        form = find_form(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            day = form.cleaned_data['day']
            slug = form.cleaned_data['slug']
            print(year,month,day,slug)
            post = get_object_or_404(Post, 
                             add_time__year = year,
                             add_time__month = month,
                             add_time__day = day,
                             slug = slug
                             )
            return HttpResponseRedirect(reverse('myapp:find_post', args = (post.add_time.year,
                                                                           post.add_time.month,
                                                                           post.add_time.day,
                                                                           post.slug)))

    return render(request,"myapp/userpage.html",{
        "status":user_obj.status,
        "time":user_obj.time,
        "all_posts":Post.objects.filter(user=request.user.id),
        "find_form":find_form(),
        "tag_form":find_by_tags()
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

def find_post(request, year, month, day, slug):
    post = get_object_or_404(Post, 
                             add_time__year = year,
                             add_time__month = month,
                             add_time__day = day,
                             slug = slug
                             )
    comments = post.comments.filter(active=True)
    return render(request,'myapp/post_which_finded.html',{
        "post":post,
        "comments":comments
    })

def shared(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'myapp/shared.html',{
        "post":post,
        "comment_form":Commentar(),
    })

def post_comment(request, id):
    post = get_object_or_404(Post, id=id)
    comment = None
    form = Commentar(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request,'myapp/shared.html',{
        "post":post,
        "comment_form":Commentar(),
        "comment":comment
    })

def find_post_by_tag(request):
    tag = None
    posts = None
    tag_slug = request.POST['tagg']
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
    
    return render(request,'myapp/for_tag_finder.html',{
        "tag":tag,
        "posts":posts
    })

        








'''def send_email(request):
    sent = False
    if request.method == "POST":
        form = Email(request.POST,initial={'email_from': request.user.email})
        if form.is_valid():
            email_from = form.cleaned_data['email_from']
            email_to = form.cleaned_data['email_to']
            text = form.cleaned_data['text']
            send_mail('email form django', text, email_from, [email_to])
            sent = True
            return HttpResponseRedirect(reverse("myapp:user_page"))
    return render(request,'myapp/send_email.html',{
        "email_form":Email(),
        "sent":sent,
    })'''
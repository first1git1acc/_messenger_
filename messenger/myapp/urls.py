from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.main_page, name = "main_page"),
    path("login", views.for_login, name = "for_login"),
    path("registration", views.for_registration, name = "for_registration"),
    path("userpage", views.user_page, name = "user_page"),
    path("log_out", views.log_out, name = "log_out"),
    path("add_post", views.adding_post, name = "adding_post"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>", views.find_post, name = "find_post"),
]
 #path("send_email", views.send_email, name = "send_email")
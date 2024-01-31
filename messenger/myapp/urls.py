from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("",views.main_page,name="main_page"),
    path("login",views.for_login,name="for_login"),
    path("registration",views.for_registration,name="for_registration"),
    path("userpage",views.user_page,name="user_page"),
    path("log_out",views.log_out,name="log_out")
]
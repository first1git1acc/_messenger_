from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("",views.main_page,name="index"),
    path("login",views.for_login,name="for_login"),
    path("registration",views.for_registration,name="for_registration")
]
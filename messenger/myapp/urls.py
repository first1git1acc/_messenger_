from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("",views.main_page,name="index")
]
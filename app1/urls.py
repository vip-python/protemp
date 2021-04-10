from django.urls import path
from app1 import views

app_name="app1"

urlpatterns = [
    path("app1/",views.index,name="app1"),
]

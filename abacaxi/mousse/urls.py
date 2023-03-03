from django.urls import path
from . import views

urlpatterns = [
     path("hello", views.hello, name="hello"),
     path("img", views.index, name="index")
]

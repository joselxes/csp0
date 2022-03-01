
from django.urls import path
from . import views


app_name = "searchs"
urlpatterns = [
    path("", views.index, name="index"),
    path("img", views.img, name="img"),
    path("adv", views.adv, name="adv"),
]

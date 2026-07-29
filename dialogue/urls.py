from django.urls import path

from . import views


app_name = "dialogue"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("payment/", views.payment, name="payment"),
    path("success/", views.success, name="success"),
]

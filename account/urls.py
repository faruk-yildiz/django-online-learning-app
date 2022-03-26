from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("login",views.login_request,name="login"),
    path("signup",views.signUp_request,name="signup"),
    path("logout",views.logout_request,name="logout"),
]

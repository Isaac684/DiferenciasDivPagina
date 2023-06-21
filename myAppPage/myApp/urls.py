from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('loginapp.html', views.login),
    path('signupapp.html', views.signup)
]
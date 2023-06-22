from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('loginapp', views.login),
    path('signupapp', views.signup),
    path('recover', views.recover),
    path('registrar', views.registrar, name='registrar'),
    path('loginUser', views.loginUser, name='loginUser'),
]
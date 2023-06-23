from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('loginapp', views.login),
    path('signupapp', views.signup),
    path('recover', views.recover),
    path('registerUser', views.registerUser, name='registerUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('changePassword', views.changePassword, name='changePassword'),
]
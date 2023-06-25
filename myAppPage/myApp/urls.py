from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('homepage', views.homepage),
    path('loginapp', views.login),
    path('signupapp', views.signup),
    path('recover', views.recover),
    path('registerUser', views.registerUser, name='registerUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('logout', views.logout, name='logout'),
    path('guestpage', views.guest_page, name='guestPage'),
    path('userProfile', views.userProfile, name='userProfile'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('saveEditedProfile', views.saveEditedProfile, name='saveEditedProfile'),
    path('realizarEjercicio',views.realizarEjercicio, name='realizarEjercicio'),
]
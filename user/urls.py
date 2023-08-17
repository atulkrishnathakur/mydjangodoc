from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_form, name='signup'),
    path('signsave/', views.signup_save, name='signupsave'),
    path('login/', views.sign_form, name='login_form'),
    path('loginsubmit/', views.sign_in, name='loginsubmit'),
    path('signout/', views.sign_out, name='signout'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home-temp/', views.home_temp, name='hometemp'),
    path('about-temp/', views.about_temp, name='abouttemp'),
    path('showdata/', views.show_data, name='showdata'),
]
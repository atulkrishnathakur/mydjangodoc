from django.urls import path
from .views import category
from .views import product

urlpatterns = [
    path('', category.home, name='home'),
    path('about/', category.about, name='about'),
    path('home-temp/', category.home_temp, name='hometemp'),
    path('about-temp/', category.about_temp, name='abouttemp'),
    path('showdata/', category.show_data, name='showdata'),
    path('create-category/', category.create_category, name='createcategory'),
    path('save-category/', category.save_category, name='savecategory'),
]
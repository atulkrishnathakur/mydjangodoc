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
    path('category-list/', category.category_list, name='categorylist'),
    path('category-edit/<int:id>', category.category_edit, name='categoryedit'),
    path('category-update', category.category_update, name='categoryupdate'),
    path('category-delete/<int:id>', category.category_delete, name='categorydelete'),
    path('test-log/', category.testLog, name='testlog'),
    path('create-product/',product.create_product, name='create_product'),
    path('get-category-ajax/',product.get_category_ajax,name='get_category_ajax'),
    path('saveproduct/',product.saveproduct,name='saveproduct'),
    path('product-list/',product.product_list,name='productlist')
]
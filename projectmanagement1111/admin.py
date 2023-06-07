from django.contrib import admin

# Register your models here.
from .models.categories import Category

admin.site.register(Category)
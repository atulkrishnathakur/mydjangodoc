from django.contrib import admin

# Register your models here.
from .models.categories import Category

#admin.site.register(Category)

class CategoryListAdmin(admin.ModelAdmin):
  list_display = ("category_name", "category_code", "description",)
  
admin.site.register(Category, CategoryListAdmin)
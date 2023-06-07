from django.db import models
from .categories import *

class Product(models.Model):
    id = models.BigAutoField(primary_key=True,db_column='id')
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='cat_id')
    product_name = models.CharField(max_length=100,db_column='product_name',null=False,default='NA');
    class Meta:
        db_table = 'products'
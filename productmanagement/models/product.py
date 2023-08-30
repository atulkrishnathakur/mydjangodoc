from django.db import models
from .categories import *

class Product(models.Model):
    id = models.BigAutoField(primary_key=True,db_column='id')
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE,db_column='cat_id',null=True)
    product_name = models.CharField(max_length=100,db_column='product_name',null=False,default='NA');
    status = models.SmallIntegerField(null=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    image = models.ImageField(upload_to='product_img/',null=True,db_column='image')
    class Meta:
        db_table = 'products'
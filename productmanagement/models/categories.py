from django.db import models
from datetime import date
from django.utils.timezone import now

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    description = models.CharField(max_length=50,null=True)
    sh_description = models.CharField(max_length=10,null=True,db_column='short_description')
    lg_description = models.CharField(max_length=20,null=True,db_column='long_description')
    status = models.SmallIntegerField(null=True,default=1)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table = 'categories'
    def __str__(self):
        return f"{self.category_name} {self.description}"
 
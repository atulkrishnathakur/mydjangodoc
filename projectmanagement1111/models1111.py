from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    
    class Meta:
        db_table = 'categories'

from django.db import models

class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=120,null=True)
    category_code = models.CharField(max_length=50,null=True,unique=True)
    description = models.CharField(max_length=50,null=True)
    sh_description = models.CharField(max_length=10,null=True,db_column='short_description')
    lg_description = models.CharField(max_length=20,null=True,db_column='long_description')
    class Meta:
        db_table = 'categories'
    def __str__(self):
        return f"{self.category_name} {self.description}"
 
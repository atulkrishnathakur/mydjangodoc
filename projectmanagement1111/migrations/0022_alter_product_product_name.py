# Generated by Django 4.2.1 on 2023-05-25 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0021_product_product_name_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(db_column='product_name', default=True, max_length=100),
        ),
    ]

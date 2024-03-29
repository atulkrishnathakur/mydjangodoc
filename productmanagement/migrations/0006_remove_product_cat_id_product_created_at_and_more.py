# Generated by Django 4.2.1 on 2023-08-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0005_product_cat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(db_column='image', null=True, upload_to='product_img/'),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

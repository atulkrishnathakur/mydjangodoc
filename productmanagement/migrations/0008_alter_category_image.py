# Generated by Django 4.2.1 on 2023-06-21 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0007_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(db_column='image', null=True, upload_to='category_img/'),
        ),
    ]
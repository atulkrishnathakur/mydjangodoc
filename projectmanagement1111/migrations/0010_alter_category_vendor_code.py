# Generated by Django 4.2.1 on 2023-05-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0009_category_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='vendor_code',
            field=models.CharField(default=0, max_length=50),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-24 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0010_alter_category_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='vendor_code',
        ),
    ]

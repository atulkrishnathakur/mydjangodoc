# Generated by Django 4.2.1 on 2023-05-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]

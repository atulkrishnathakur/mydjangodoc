# Generated by Django 4.2.1 on 2023-08-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(db_column='phone', max_length=20, null=True),
        ),
    ]
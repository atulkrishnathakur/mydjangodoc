# Generated by Django 4.2.1 on 2023-05-25 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanagement', '0024_alter_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='lg_description',
            field=models.CharField(db_column='long_description', max_length=20, null=True),
        ),
    ]

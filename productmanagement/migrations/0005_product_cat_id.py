# Generated by Django 4.2.1 on 2023-08-30 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0004_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(db_column='cat_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='productmanagement.category'),
        ),
    ]

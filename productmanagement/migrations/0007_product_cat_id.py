# Generated by Django 4.2.1 on 2023-08-30 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0006_remove_product_cat_id_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(db_column='cat_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='productmanagement.category'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-29 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='lg_description',
            field=models.CharField(db_column='long_description', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='sh_description',
            field=models.CharField(db_column='short_description', max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='product_name', default='NA', max_length=100)),
                ('cat_id', models.ForeignKey(db_column='cat_id', on_delete=django.db.models.deletion.CASCADE, to='productmanagement.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]

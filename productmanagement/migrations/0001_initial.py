# Generated by Django 4.2.1 on 2023-05-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=120, null=True)),
                ('category_code', models.CharField(max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]

# Generated by Django 2.0 on 2018-09-16 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20180913_2137'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MealPrice',
            new_name='UserMeal',
        ),
    ]

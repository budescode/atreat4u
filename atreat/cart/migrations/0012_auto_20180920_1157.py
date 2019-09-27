# Generated by Django 2.0 on 2018-09-20 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20180917_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinemasdetail_cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cinemasdetail_cart',
            name='usercart',
        ),
        migrations.RemoveField(
            model_name='comedy_cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='comedy_cart',
            name='usercart',
        ),
        migrations.RemoveField(
            model_name='meal_cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='meal_cart',
            name='usercart',
        ),
        migrations.RemoveField(
            model_name='salondetail_cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='salondetail_cart',
            name='usercart',
        ),
        migrations.DeleteModel(
            name='CinemasDetail_Cart',
        ),
        migrations.DeleteModel(
            name='Comedy_Cart',
        ),
        migrations.DeleteModel(
            name='Meal_Cart',
        ),
        migrations.DeleteModel(
            name='SalonDetail_Cart',
        ),
    ]

# Generated by Django 2.0 on 2018-11-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0030_usermeal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomedydouble',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usercomedyround',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usercomedysingle',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usercomedyvip',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 2.0 on 2018-11-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0027_usermeal_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermeal',
            name='Total_price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
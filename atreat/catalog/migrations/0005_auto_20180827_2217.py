# Generated by Django 2.0 on 2018-08-27 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_salon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='price',
        ),
        migrations.RemoveField(
            model_name='salon',
            name='slug',
        ),
    ]

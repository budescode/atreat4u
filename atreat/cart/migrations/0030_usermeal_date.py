# Generated by Django 2.0 on 2018-11-13 09:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0029_cinemaquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermeal',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
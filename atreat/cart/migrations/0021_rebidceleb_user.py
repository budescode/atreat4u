# Generated by Django 2.0 on 2018-11-03 12:56

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_remove_rebidceleb_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rebidceleb',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=50),
        ),
    ]

# Generated by Django 2.0 on 2018-11-02 07:04

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_auto_20181031_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='RebidCeleb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=django.contrib.auth.models.User, max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
            ],
        ),
    ]
# Generated by Django 2.0 on 2018-11-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0024_auto_20181104_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealQuantityForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]

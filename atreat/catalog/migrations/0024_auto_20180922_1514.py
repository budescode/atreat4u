# Generated by Django 2.0 on 2018-09-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20180922_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_location', to='catalog.Restaurants'),
        ),
    ]

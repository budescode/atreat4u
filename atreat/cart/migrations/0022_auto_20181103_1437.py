# Generated by Django 2.0 on 2018-11-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0021_rebidceleb_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rebidceleb',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15, max_length=50),
        ),
    ]

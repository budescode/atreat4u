# Generated by Django 2.0 on 2018-08-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_comedy'),
    ]

    operations = [
        migrations.AddField(
            model_name='comedy',
            name='slug',
            field=models.SlugField(default='slug-field'),
            preserve_default=False,
        ),
    ]

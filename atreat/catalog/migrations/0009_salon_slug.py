# Generated by Django 2.0 on 2018-08-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_salondetail_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='slug',
            field=models.SlugField(default='slug-field'),
            preserve_default=False,
        ),
    ]
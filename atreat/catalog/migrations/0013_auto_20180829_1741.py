# Generated by Django 2.0 on 2018-08-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_restaurants_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemasdetail',
            old_name='name',
            new_name='cinema_name',
        ),
        migrations.AddField(
            model_name='cinemasdetail',
            name='movie',
            field=models.CharField(default='spy', max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.3 on 2019-01-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercinemas',
            name='location',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
    ]

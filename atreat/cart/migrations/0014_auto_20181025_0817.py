# Generated by Django 2.0 on 2018-10-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_usermeal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercinemas',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercomedydouble',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercomedyround',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercomedysingle',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercomedyvip',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersalon',
            name='user',
            field=models.CharField(default='user', max_length=50),
            preserve_default=False,
        ),
    ]

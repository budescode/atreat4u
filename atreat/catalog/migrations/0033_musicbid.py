# Generated by Django 2.0 on 2018-11-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_delete_celebrity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='none', max_length=100)),
                ('celeb', models.CharField(default='none', max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, max_length=50)),
            ],
        ),
    ]

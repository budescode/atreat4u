# Generated by Django 2.0 on 2018-10-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20181025_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelebrityBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
            ],
        ),
    ]

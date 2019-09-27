# Generated by Django 2.0 on 2018-11-02 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20180922_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema_location', to='catalog.Cinemas')),
            ],
        ),
    ]

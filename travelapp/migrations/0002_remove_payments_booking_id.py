# Generated by Django 3.1.7 on 2021-03-26 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='booking_id',
        ),
    ]

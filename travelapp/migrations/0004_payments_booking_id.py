# Generated by Django 3.1.7 on 2021-03-26 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_auto_20210326_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='booking_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travelapp.booking'),
        ),
    ]
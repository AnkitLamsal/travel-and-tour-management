# Generated by Django 3.1.7 on 2021-04-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0010_remove_payments_advance_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

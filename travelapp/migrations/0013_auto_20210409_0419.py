# Generated by Django 3.1.7 on 2021-04-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0012_auto_20210408_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_mode',
            field=models.CharField(choices=[('Visa', 'Visa'), ('Master', 'Master Card'), ('American', 'American Express'), ('Apple', 'Apple Card'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti'), ('Bitcoin', 'Bitcoin'), ('PayPal', 'PayPal')], max_length=30),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-26 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(max_length=200)),
                ('booking_start_date', models.DateField()),
                ('booking_hotel', models.CharField(max_length=200)),
                ('booking_transport', models.CharField(default='Bus', max_length=200)),
                ('number_people', models.IntegerField()),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Visa', 'Visa'), ('Master', 'Master Card'), ('American', 'American Express'), ('Apple', 'Apple Card')], max_length=30)),
                ('expiry_date', models.DateField()),
                ('booking_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travelapp.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('package_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('package_destination', models.CharField(max_length=100)),
                ('package_number_of_days', models.IntegerField()),
                ('package_description', models.CharField(max_length=300)),
                ('package_image', models.ImageField(upload_to='package_images')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.CharField(default='Nepal', max_length=100)),
                ('customer_dob', models.DateField(default='2020/01/23')),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='package_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.package'),
        ),
    ]
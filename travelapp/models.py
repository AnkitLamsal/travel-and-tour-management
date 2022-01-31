from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#Create your models here.
class Customers(models.Model):
    customer_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=100, default = 'Nepal')
    customer_dob = models.DateField(default = '2020/01/23')
    def __str__(self):
        return f'{self.customer_name}'


class Package(models.Model):
    package_name = models.CharField(max_length = 100, primary_key = True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    package_destination = models.CharField(max_length = 100, unique= True)
    package_number_of_days = models.IntegerField()
    package_description = models.CharField(max_length = 300, null =True)
    package_image = models.ImageField(upload_to = 'package_images')
    per_person_amt = models.IntegerField()
    def __str__(self):
        return self.package_name

class Booking(models.Model):
    # booking_id = models.IntegerField(primary_key = True)
    booking_type = models.CharField(max_length = 200)
    booking_start_date = models.DateField()
    hotel = (('Annapurna',"Hotel Del Annapurna"),('Hyatt','Hyatt regency'),('Malla ','Hotel malla'),('Everest','Hotel Everest'),('Mahakali', 'Hotel Mahakali'))
    booking_hotel = models.CharField(max_length = 200,choices = hotel)
    booking_transport  = models.CharField(max_length = 200, default = 'Bus')
    number_people = models.IntegerField()
    # payment_card_number = models.ForeignKey(Payments, on_delete = models.CASCADE)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    package_name = models.ForeignKey(Package, on_delete = models.CASCADE)    
    
    def __str__(self):
        return f'{self.booking_type}'
    def get_absolute_url(self):
        return reverse("travelapp:booking_detail", kwargs= {'pk':self.pk})  # 
    
# class Payments(models.Model):
#     # pay_id = models.AutoField(primary_key = True,)
#     modes= (('Visa','Visa'), ('Master','Master Card'), ('American','American Express'), ('Apple','Apple Card'))
#     # payment_holder_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     payment_mode = models.CharField(max_length =30, choices= modes)
#     expiry_date = models.DateField()
#     # payment_card_number = models.CharField(max_length=20, primary_key = True)
#     # booking_id = models.ForeignKey(Booking, on_delete = models.CASCADE, null = True)
#     def __str__(self):
#         return self.payment_mode
#     def get_absolute_url(self):
#         return reverse('admin:index')

class Payments(models.Model):
    modes= (('Visa','Visa'), ('Master','Master Card'), ('American','American Express'), ('Apple','Apple Card'),('Esewa', 'Esewa'), ('Khalti','Khalti'),('Bitcoin','Bitcoin'),
    ('PayPal', 'PayPal')
    )
    payment_mode = models.CharField(max_length =30, choices = modes)
    voucher_no = models.CharField(max_length = 20, default = None, null = True)
    booking_id = models.ForeignKey('Booking', on_delete = models.CASCADE, null = True)
    def __str__(self):
        return f'{self.payment_mode}'
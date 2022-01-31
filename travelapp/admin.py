from django.contrib import admin
from travelapp.models import Customers, Payments, Package,Booking
#Register your models here.
admin.site.register(Customers)
admin.site.register(Payments)
admin.site.register(Package)
admin.site.register(Booking)
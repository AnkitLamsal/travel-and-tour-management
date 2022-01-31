from django.contrib.auth.models import User
from django import forms
from travelapp.models import Customers, User, Payments, Package, Booking
from creditcards.forms import CardNumberField

class CustomerProfileForm(forms.ModelForm):
    customer_address = forms.CharField(required =False, widget = forms.TextInput())
    customer_dob = forms.DateField(required = False, widget = forms.DateInput())
    class Meta():
        model = Customers
        exclude = ('customer_name',)

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class CustomerUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email')


class PaymentForm(forms.ModelForm):
    #modes= (('Visa','Visa'), ('Master','Master Card'), ('American','American Express'), ('Apple','Apple Card'))
    # payment_mode = forms.CharField(max_length = '30',choices = modes)
    # expiry_date = forms.DateField()
    # payment_card_number = forms.CharField(label = "Enter Debit/Credit Card Number")
    class Meta():
        model = Payments
        exclude = ('booking_id',)

    
class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [] 

class BookingForm(forms.ModelForm):
    types = (('Travel','Travel Package'), ('Tour','Tour Package'),('Hiking','Hiking Package'),('Trekking','Trekking Package'))
    booking_type = forms.ChoiceField(choices = types, label = 'Choose Your Travelling Model')
    booking_start_date = forms.DateField(label = "Enter Your Starting Date")
    vehicles = (("Bus",'Bus'),('Van','Van'),("Micro Bus",'Micro'),('car','Car'))
    booking_transport = forms.ChoiceField(choices = vehicles, label = "Choose Your Vehicle Type")
    hotel = (('Annapurna',"Hotel Del Annapurna"),('Hyatt','Hyatt regency'),('Malla ','Hotel malla'),('Everest','Hotel Everest'))
    booking_hotel = forms.ChoiceField(choices= hotel, label= "Choose Your Hotel")
    number_people = forms.IntegerField(label = 'Enter Total Number Of People') 
    class Meta():
        model = Booking
        exclude = ('booked_by','')

class BookingUpdateForm(forms.ModelForm):
    types = (('Travel','Travel Package'), ('Tour','Tour Package'),('Hiking','Hiking Package'),('Trekking','Trekking Package'))
    booking_type = forms.ChoiceField(choices = types, label = 'Choose Your Travelling Model', required = False)
    booking_start_date = forms.DateField(label = "Enter Your Starting Date",required = False)
    vehicles = (("Bus",'Bus'),('Van','Van'),("Micro Bus",'Micro'),('car','Car'))
    booking_transport = forms.ChoiceField(choices = vehicles, label = "Choose Your Vehicle Type",required = False)
    hotel = (('Annapurna',"Hotel Del Annapurna"),('Hyatt','Hyatt regency'),('Malla ','Hotel malla'),('Everest','Hotel Everest'),('Mahakali', 'Hotel Mahakali'))
    booking_hotel = forms.ChoiceField(choices= hotel, label= "Choose Your Hotel",required = False)
    number_people = forms.IntegerField(label = 'Enter Total Number Of People',required = False) 
    class Meta():
        model = Booking
        exclude = ('booked_by','package_name','payment-card_number')


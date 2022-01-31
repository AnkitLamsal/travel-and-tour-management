from django.shortcuts import render, redirect
from travelapp.models import Customers, Payments, Package, Booking
from travelapp.forms import CustomerForm, CustomerProfileForm,CustomerUpdateForm, PaymentForm, UserDeleteForm, BookingForm,BookingUpdateForm
# For Login Authentication 
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.models import User
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView
from django.utils.decorators import method_decorator


# Create your views here.
def index(request): 
    return render(request, 'travelapp/index.html')
# Customer Creation
def signup(request):
    registered = False
    if request.method == 'POST':
        customer_form = CustomerForm(data= request.POST)
        customerprofile_form = CustomerProfileForm(data = request.POST)
        if customer_form.is_valid() and customerprofile_form.is_valid():
            # customer main -- name, email and password
            customer = customer_form.save()
            customer.set_password(customer.password)
            customer.save()

            # customer new datas --address and date
            customerprofile = customerprofile_form.save(commit = False)
            customerprofile.customer_name = customer
            customerprofile.save()
            registered =True
            return render(request, 'travelapp/login.html')
        else:
            print(customer_form.errors,customerprofile_form.errors)
    else:
        customer_form = CustomerForm()
        customerprofile_form = CustomerProfileForm()
    return render(request, 'travelapp/customers_form.html', {'userform': customer_form, 'customerform':customerprofile_form, 'registered':registered})  

# Login Authentication
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentication
        user = authenticate(username=username, password= password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('travelapp:index'))
            else:
                return HttpResponse("Your Account is not active.")
        else:
            print("Login Failed.")
            print("Username: {}  \n Password:{} ".format(username,password))
            return HttpResponse("Invalid Login Details")
    else:
        return render(request, 'travelapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('travelapp:index'))

@login_required
def special(request):
    return HttpResponse("You Are SucessFully Logged In!")

# class DeleteCustomerView(DeleteView):
#     success_url = reverse_lazy('travelapp:index')
#     template_name = "travelapp/customer_delete.html"
#     model = User
#     #This is the original form
#     def get_object(self, queryset=None):
#         return self.request.user




@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('travelapp:index')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'travelapp/customer_delete.html', context)

class CustomerUpdateView(UpdateView):
    success_url = reverse_lazy('travelapp:index')
    template_name = "travelapp/customer_update.html"
    model = User
    form_class= CustomerUpdateForm
    def get_object(self, queryset=None):
        return self.request.user

class PaymentCreateView(CreateView):
    template_name = "travelapp/payment_form.html"
    model = Payments
    success_url = reverse_lazy('travelapp:index')
    form_class = PaymentForm
    # @method_decorator(login_required)
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.payment_holder_name  = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(PaymentCreateView, self).form_valid(form)

class PaymentDeleteView(DeleteView):
    success_url = reverse_lazy('travelapp:index')
    template_name = "travelapp/payment_delete.html"
    model = Payments


class CustomerDetailView(DetailView):
    model = Customers
    template_name = 'inventory/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['username']  = User.objects.filter().order_by(F('username').asc())
        # other code
        return context

# class BookingCreateView(CreateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'travelapp/booking_create_form.html'
#     success_url = reverse_lazy('travelapp:booking_list') 
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.booked_by  = self.request.user
#         #article.save()  # This is redundant, see comments.
#         obj.save()
#         return super(BookingCreateView, self).form_valid(form)

def BookingCreateView1(request):
    if request.method == 'POST':
        registered = False
        Book_form = BookingForm(data = request.POST or None)
        pay_form = PaymentForm(data = request.POST or None)
        if Book_form.is_valid() and pay_form.is_valid():
            # customer main -- name, email and password
            book = Book_form.save(commit = False)
            book.booked_by = request.user
            book.save()
            pay = pay_form.save(commit = False)
            pay.booking_id = book
            pay.save()
            registered = True
            # customer = customer_form.save()
            return redirect(reverse('travelapp:booking_list'))
        else:
            print(Book_form.errors, pay_form.errors)
    else:
        Book_form = BookingForm()
        pay_form = PaymentForm()

        context = {
        # 'delete_form': delete_form, 
        'Bform' : Book_form,
        'Pform' : pay_form
        }
    return render(request, 'travelapp/book_detail.html', context)

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingUpdateForm
    success_url = reverse_lazy('travelapp:booking_list')
    template_name = 'travelapp/booking_update_form.html' 

class BookingListView(ListView):
    model = Booking
    def get_queryset(self):
        return Booking.objects.filter(booked_by=self.request.user)

class BookingDeleteView(DeleteView):
    model = Booking
    queryset = Booking.objects.all()
    success_url = reverse_lazy('travelapp:booking_list')
    template_name  = 'travelapp/booking_delete.html'

class PackageListView(ListView):
    model = Package

class BookingDetailView(DetailView):
    context_object_name = 'booking_detail'
    model = Booking
    template_name = 'travelapp/bookings_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(BookingDetailView, self).get_context_data(**kwargs)
    #     context['payment']  = Payments.objects.all()
    #     return context



class myUserDetailView(DetailView):
    model = Customers
    template_name = 'travelapp/customer_detail.html'


def booking_detail_view(request,pk):
    payment_obj = Payments.objects.get(pk=pk)
    booking_obj = Booking.objects.filter(id=payment_obj.id)
    # booking_obj = Booking.objects.get(pk=pk)
    # payment_obj = Payments.objects.filter(booking_id_id= booking_obj)
    context = {'booking':booking_obj,'payment':payment_obj,'pk':pk}
    return render(request, 'travelapp/booking_detail_.html', context=context)

def booking_list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}  
    # add the dictionary during initialization
    context["value"] = Booking.objects.all().order_by("id")
    user = Booking.created_by()
    customer = Customer.objects.get( user = user)
    context['id']=customer
    return render(request, "travelapp/list_book.html", context)

def customerdetail(request):
    context = {}
    context['customer'] = Customers.objects.filter(customer_name = request.user)
    return render(request, "travelapp/customer_detail.html", context)

def userlist(request):
    context = {}
    context['list'] =User.objects.all()
    return render(request, "travelapp/user_list.html", context)
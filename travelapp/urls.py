from travelapp import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = 'travelapp'

urlpatterns = [
    path('', views.index, name = 'index'),
    #user CRUD urls
    path('create-user/', views.signup, name = 'user_create'),
    path('login-user/', views.user_login, name= 'user_login'),
    path('update-user/' ,views.CustomerUpdateView.as_view(), name = 'user_update'),
    path('logout-user/', views.user_logout, name = 'user_logout'),
    path('detail-user/<pk>/', views.myUserDetailView.as_view(), name = "x" ),
    path('delete-user/', views.deleteuser, name='user_delete'),
    #Booking CRUD
    path('myB/', views.BookingCreateView1,name='booking_create__'),
    path('book-list/update/<pk>/', views.BookingUpdateView.as_view(), name = 'booking_update'),
    path('book-list/', views.BookingListView.as_view(), name='booking_list'),
    path('delete-book/<pk>/', views.BookingDeleteView.as_view(), name='booking_delete'),
    path('book-list/<pk>/',views.booking_detail_view, name= 'booki'),
    path('package/', views.PackageListView.as_view(), name= 'package_list'),
    path('detail-user/', views.customerdetail, name='user_detail'),
    path('user-list/', views.userlist, name='list-user')    

]
urlpatterns+=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


    #path('create-payment/', views.PaymentCreateView.as_view(), name = 'payment_create'),
    # path('create-book/', views.BookingCreateView.as_view(), name='booking_create'),
    #path(r'^update/(?p<pk>\d+)/$', views.BookingUpdateView.as_view(), name = 'booking_update'),
    # path('booking/<int:id>/', views.bookView, name = 'booking'),
    # path('list__/', views.booking_list_view, name='list_book'),
        #path('book-list/<pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
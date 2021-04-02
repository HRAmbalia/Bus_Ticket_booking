from django.urls import path
#
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#

urlpatterns = [
    # path('', views.homePage, name='index'),
    path('search/', views.search, name='search'),
    path('search/bookBus', views.bookBus, name='searchBus'),
    path('myBooking/', views.booking, name='bookings'),
    path('chgPassword/', views.chgpass, name='chgpass'),
    path('myBooking/print_pdf', views.print_pdf, name='printPDF'),
    path('myBooking/deleteTicket', views.dltTicket, name='deleteTicket'),
    path('payment', views.payFare, name='payment')
]
# urlpatterns += staticfiles_urlpatterns()

# make payment gateway
# make print PDF gateway
# validate seat number in seat booking in "bookBus.html" and in "bookBus" function.
# empty ticketDetails database
# try to remove session attributes - from, to, travel_date
# try to develop cancel ticket - DONE
# add image to website
# update logged-in home page
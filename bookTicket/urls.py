from django.urls import path
#
from . import views
#

urlpatterns = [
    # path('', views.homePage, name='index'),
    path('search/', views.search, name='search'),
    path('search/bookBus', views.bookBus, name='searchBus'),
    path('myBooking/', views.booking, name='bookings'),
    path('chgPassword/', views.chgpass, name='chgpass'),
    
]
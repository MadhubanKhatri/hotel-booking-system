from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('room_booking/<int:room_no>/', views.room_booking,name='room_booking'),
    path('booking_confirm/<int:room_num>/', views.booking_confirm, name="booking_confirm")
]
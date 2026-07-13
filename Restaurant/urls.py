from django.urls import path
from .views import MenuListCreateView, BookingListCreateView

urlpatterns = [
    path('menu/', MenuListCreateView.as_view(), name='menu-list'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list'),
]
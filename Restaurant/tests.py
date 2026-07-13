from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu, Booking


class MenuTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(
            name="Greek Salad",
            price=12.99,
            description="Fresh salad with feta cheese"
        )

    def test_get_menu_list(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        data = {
            "name": "Bruschetta",
            "price": 8.50,
            "description": "Toasted bread with tomatoes"
        }
        response = self.client.post('/restaurant/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)


class BookingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date="2026-07-20",
            booking_time="19:00:00"
        )

    def test_get_booking_list(self):
        response = self.client.get('/restaurant/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        data = {
            "name": "Jane Smith",
            "number_of_guests": 2,
            "booking_date": "2026-07-21",
            "booking_time": "20:00:00"
        }
        response = self.client.post('/restaurant/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)
        
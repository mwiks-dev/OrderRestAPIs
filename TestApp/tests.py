from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest.mock import patch
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Customer, Order

# user auth test
class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email='test@example.com')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)

# customer profile test
class CustomerProfileTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='customer', password='testpass123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_customer_profile(self):
        response = self.client.post(reverse('create-customer'), {'name': 'John Doe', 'code': 'XYZ123', 'phone_number': '+254700000000'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'John Doe')

# order creation test
class OrderCreationTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='customer', password='testpass123')
        self.customer = Customer.objects.create(user=self.user, name='John Doe', code='XYZ123', phone_number='+254700000000')
        self.client.force_authenticate(user=self.user)

    @patch('TestApp.utils.send_order_confirmation_sms')
    def test_create_order(self, mock_send_sms):
        response = self.client.post(reverse('create-order'), {'item': 'Widget', 'budget': '100.00'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        self.assertFalse(mock_send_sms.called, "The send_order_confirmation_sms function was not called")
        if mock_send_sms.called:
            phone_number_arg = mock_send_sms.call_args[0][0]
            self.assertEqual(phone_number_arg, '+2547000000000')
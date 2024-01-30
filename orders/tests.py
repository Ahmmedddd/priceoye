from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from shop.models import Product
from .models import Order, OrderDetail

class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com')
        self.product = Product.objects.create(name='Test Product', price=19.99, stock_quantity=10)


    def test_create_order_with_order_details(self):
        # Create an order
        order_data = {
            "user": self.user.id,  # Assuming your Order model has a 'user' field
            # Populate other order fields here
        }

        order_response = self.client.post('/api/orders/', order_data, format='json')
        self.assertEqual(order_response.status_code, status.HTTP_201_CREATED)
        order_id = order_response.data['id']

        # Create a product (if needed for your OrderDetail model)
        product_data = {
            # Populate product fields here
        }

        product_response = self.client.post('/api/products/', product_data, format='json')
        self.assertEqual(product_response.status_code, status.HTTP_201_CREATED)
        product_id = product_response.data['id']

        # Create order details
        order_details_data = {
            "quantity": 1,
            "subtotal": 100.0,
            "order": order_id,
            "product": product_id,
            # Populate other order details fields here
        }

        response = self.client.post('/api/orders/order-details/', order_details_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


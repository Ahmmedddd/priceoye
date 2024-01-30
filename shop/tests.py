import unittest

from rest_framework import status
from .models import Product  # Replace 'your_api_module' with the actual module where your Product class is defined

class TestProductAPI(unittest.TestCase):

    def setUp(self):
        # You may initialize any necessary resources or set up configurations here
        pass

    def tearDown(self):
        # You may clean up any resources created during the test here
        pass

    def test_create_product_valid_data(self):
        # Test case for creating a product with valid data

        # Arrange
        product_data = {
            "name": "Product Name",
            "description": "Product Description",
            "price": "10.99",
            "stock_quantity": 100,
            "brand": 1,
            "category": 2
        }

        # Act
        product = Product(**product_data)

        # Assert
        self.assertEqual(product.name, "Product Name")
        self.assertEqual(product.description, "Product Description")
        self.assertEqual(product.price, "10.99")
        self.assertEqual(product.stock_quantity, 100)
        self.assertEqual(product.brand, 1)
        self.assertEqual(product.category, 2)


    def test_create_product_invalid_data(self):
        # Test case for creating a product with invalid data

        # Arrange
        invalid_product_data = {
            # Missing required fields 'name', 'description', 'price', 'stock_quantity'
            "brand": 1,
            "category": 2
        }

        # Act and Assert
        with self.assertRaises(ValueError):
            product = Product(**invalid_product_data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

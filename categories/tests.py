from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        # Create a category for testing
        self.category = Category.objects.create(name='Test Category')

    def test_create_category(self):
        data = {'name': 'New Category'}
        response = self.client.post('/categories/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # Adjust based on your setup

    def test_read_category(self):
        response = self.client.get(f'/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Category')

    def test_update_category(self):
        data = {'name': 'Updated Category'}
        response = self.client.put(f'/categories/{self.category.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(id=self.category.id).name, 'Updated Category')

    def test_delete_category(self):
        response = self.client.delete(f'/categories/{self.category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)

    def test_list_categories(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Category')

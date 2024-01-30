from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from brands.models import Brand
from .serializers import BrandSerializer

class BrandTest(APITestCase):
    def setUp(self):
        self.brand_data = {'name': 'samsung'}
        self.brand = Brand.objects.create(**self.brand_data)
        self.serializer = BrandSerializer(instance=self.brand)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name']))

    def test_data_matches_brand_model(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.brand.name)

    def test_get_brand(self):
            url = reverse('brands-detail', args=[self.brand.id])  # Use the correct name for the brand detail URL
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['name'], 'samsung')

    def test_create_method(self):
        new_brand_data = {'name': 'New Brand'}
        serializer = BrandSerializer(data=new_brand_data)
        self.assertTrue(serializer.is_valid())
        new_brand = serializer.save()
        self.assertIsInstance(new_brand, Brand)
        self.assertEqual(new_brand.name, new_brand_data['name'])

    def test_update_brand(self):
        url = reverse('brands-detail', args=[self.brand.id])  # Use the correct name for the brand detail URL
        updated_data = {'name': 'UpdatedBrand'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.get(id=self.brand.id).name, 'UpdatedBrand')

    def test_list_brands(self):
        url = reverse('brands-list')  # Use the correct name for the brand list URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(title="Pizza", price=200, inventory=10)
        MenuItem.objects.create(title="Burger", price=150, inventory=5)

    def test_getall(self):
        client = APIClient()
        response = client.get("/restaurant/menu-items/")

        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

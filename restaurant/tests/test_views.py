from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuView
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def tearDown(self):
        Menu.objects.all().delete()


    def test_getall(self):
        it = Menu.objects.all()
        for i in it:
            x = MenuSerializer(i)
            self.assertEquals(str(x.data), "{'id': 1, 'title': 'IceCream', 'price': '80.00', 'inventory': 100}")
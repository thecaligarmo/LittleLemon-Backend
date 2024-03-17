from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase) :
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def tearDown(self):
        Menu.objects.all().delete()

    def test_instance(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(str(item), "IceCream : 80.00")
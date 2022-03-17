from django.test import TestCase

# Create your tests here.

from stock.models import ProductWatcher,Market
from django.contrib.auth.models import User

class AnimalTestCase(TestCase):
    def setUp(self):
        market = Market.objects.create(name="RsOnline",strategy="stock.strategy.rs_online.RsOnline")
        user = User.objects.create(username="test",password="thisother")
        ProductWatcher.objects.create(name="Product", url="google.es",minimum_stock=2000,market=market,user=user)


    def test_correct_setup(self):
        market = Market.objects.first()
        user = User.objects.first()
        pwatcher = ProductWatcher.objects.first()
        self.assertEqual(market.name, 'RsOnline')
        self.assertEqual(user.username, 'test')
        self.assertEqual(pwatcher.name, 'Product')
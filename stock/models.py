from django.db import models
from strategy_field.fields import StrategyField
from strategy_field.registry import Registry
from stock.strategy.abstract_market_strategy import AbstractMarketStrategy
from stock.strategy.rs_online import RsOnline
from django.contrib.auth.models import User
# Create your models here.


registry = Registry(AbstractMarketStrategy)
registry.register(RsOnline)

class Market(models.Model):
    name = models.CharField(max_length=200)
    strategy = StrategyField(registry=registry)

class ProductWatcher(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    minimum_stock = models.IntegerField()
    market = models.ForeignKey(Market,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT,default=None)




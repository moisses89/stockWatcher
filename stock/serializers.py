from django.contrib.auth.models import User
from stock.models import ProductWatcher,Market
from rest_framework import serializers


class ProductWatcherSerializer(serializers.HyperlinkedModelSerializer):
    market = serializers.SerializerMethodField()

    class Meta:
        model = ProductWatcher
        fields = ['name', 'url', 'minimum_stock','market','market_id']

    # Get name of market instead the id
    def get_market(self,obj):
        return obj.market.name



class MarketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Market
        fields = ['id','name']


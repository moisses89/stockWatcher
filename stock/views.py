from rest_framework import viewsets
from rest_framework import permissions
from stock.serializers import ProductWatcherSerializer,MarketSerializer
from stock.models import ProductWatcher,Market

class ProductWatcherList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProductWatcher.objects.all()
    serializer_class = ProductWatcherSerializer
    permission_classes = [permissions.IsAuthenticated]



class MarketList(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


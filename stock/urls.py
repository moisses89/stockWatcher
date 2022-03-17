from django.db import router
from django.urls import path, include
from rest_framework import routers
from stock.views import ProductWatcherList,MarketList

from stock import views

router = routers.DefaultRouter()
router.register(r'watchers', views.ProductWatcherList)
router.register(r'markets', views.MarketList)



urlpatterns = [
    path('', include(router.urls))
]
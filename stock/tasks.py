from celery import shared_task

from getStock.celery import app
from stock.models import ProductWatcher,Market

@shared_task
def getStock():
    products = ProductWatcher.objects.all()
    for product in products:
        stock = product.market.strategy.getStock(product.url)
        if (stock < product.minimum_stock):
            print("Alarm! Stock reached the minimum!")
            # TODO send email


app.conf.beat_schedule = {
    "getStock": {
        "task": "stock.tasks.getStock",
        "schedule": 10.0
    }
}


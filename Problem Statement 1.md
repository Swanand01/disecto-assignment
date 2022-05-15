### Problem Statement 1:
Describe a stepwise methodology using pseudocode/specific code to auto
generate a list of products/items with low stock/expiry from the inventory
database. The list must be updated at 12 A.M. daily


To solve this problem, the following changes could be made to the Product model: 
`inventory_count` and `min_qty` attributes could be added.

`inventory_count` : Amount of the product available in the inventory.

`min_qty`: The amount of Product available at which it is flagged. If the `inventory_count` of the product is less than `min_qty`, the Product will be flagged as low stock. 

The scheduling of the task to be run at 12AM daily can be done using Celery and Celery Beat.
```
from accounts.models import Product
from django.db.models import F
from celery import shared_task, states

@shared_task(bind=True, name='get_low_stock_products',)
def get_low_stock_products():
    low_stock_products = Product.objects.filter(inventory_count__lte=F("min_qty"))
    # Do something with low_stock_products
```


```
app.conf.beat_schedule = {
    "get_low_stock_products": {
        "task": "get_low_stock_products",  # <---- Name of task
        "schedule": crontab(hour='24', # <---- Run at 12 AM daily
                            minute=0,
                            )
    },
}
```
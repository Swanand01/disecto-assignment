from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Represents a Product in the inventory.

    attrs:
    name: Name of the Product
    description: Product description
    price: Price per unit
    """
    name = models.CharField(max_length=250, default='')
    description = models.TextField(default='')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    """
    Represents a Product in the Order.

    attrs:
    product: ForeignKey relation to Product
    quantity: Quantity of the product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name + " - " + str(self.quantity)


class Order(models.Model):
    """
    Represents a user's Order

    attrs:
    user: ForeignKey relation to User
    products: ManyToManyField containing all OrderProducts
    is_placed: Placed status of the Order
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order")
    products = models.ManyToManyField(OrderProduct, blank=True)
    is_placed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "'s order " + str(self.id)

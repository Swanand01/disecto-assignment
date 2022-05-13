from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField(default='')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name + " - " + str(self.quantity)


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="order", unique=True)
    products = models.ManyToManyField(OrderProduct, blank=True)
    is_placed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "'s order"

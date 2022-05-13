from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField(default='')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class CartProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart", unique=True)
    products = models.ManyToManyField(
        CartProduct, blank=True, related_name="cart_products")

    def __str__(self):
        return self.user.username + "'s cart"
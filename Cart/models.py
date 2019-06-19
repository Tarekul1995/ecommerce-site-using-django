from django.db import models
from Account.models import Customer_Account
from Product.models import Product


class Createcart(models.Model):
    user = models.ForeignKey(Customer_Account, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

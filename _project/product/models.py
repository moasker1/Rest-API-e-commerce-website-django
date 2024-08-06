from django.db import models
from django.contrib.auth.models import User


class Category(models.TextChoices):
    COMPUTERS= "C omputers"
    FOOD = "Food"
    KIDS = "Kids"
    HOME = "Home"

class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2, default=0, blank=False)
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=200 , choices=Category.choices)
    rating = models.DecimalField(max_digits=7,decimal_places=2, default=0, blank=False)
    stock = models.IntegerField(default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
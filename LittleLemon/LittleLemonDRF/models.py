from django.db import models
from django.db.models import SmallIntegerField


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = SmallIntegerField()
    category =models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
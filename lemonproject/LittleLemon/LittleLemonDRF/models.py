from django.db import models
from django.db.models import SmallIntegerField


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = SmallIntegerField()



from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    menuItem_id = models.smallIntegerField()
    rating = models.smallIntegerField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
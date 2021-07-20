from djongo import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    available_balance = models.FloatField()
    total_profit_loss = models.FloatField()

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.FloatField()
    quantity_tbf = models.FloatField(default=0) #quantity to be filled
    profit_loss = models.FloatField()
    type = models.TextField()
    status = models.TextField(default='active')
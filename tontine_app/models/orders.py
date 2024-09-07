from django.db import models
from django.contrib.auth import get_user_model
from .account import Account

User = get_user_model()
class Transaction(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField() 

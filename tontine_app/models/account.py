from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    payment = models.IntegerField()
    solde = models.IntegerField(default=0)
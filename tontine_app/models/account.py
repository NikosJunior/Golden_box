from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    payment = models.IntegerField()
    balance = models.IntegerField(default=0)


    def __str__(self):
        return self.user.first_name
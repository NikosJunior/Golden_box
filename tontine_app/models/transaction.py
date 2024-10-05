from django.db import models
from django.contrib.auth import get_user_model
from .account import Account

User = get_user_model()
class Transaction(models.Model):
    PAYEMENT_CHOICES = [
        ('cash', 'Espece'),
        ('online', 'En ligne')
    ]

    TRANSACTION_CHOICES = [
        ('deposit', 'Depot'),
        ('withdraw', 'Retrait')
    ]

    TRANSACTION_STATUS = [
        ('pending', 'en cours'),
        ('done' , 'valider'),
        ('canceled', 'annuler')
    ]

    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    transaction_date = models.DateField(blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField() 
    payment_type = models.CharField(max_length= 10, choices = PAYEMENT_CHOICES, default= 'cash')
    transaction_type = models.CharField(max_length = 10, choices = TRANSACTION_CHOICES, default= 'deposit' )
    status = models.CharField(max_length = 10, choices = TRANSACTION_STATUS, default = 'pending', blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'transaction_date'], name='unique_account_per_day')
        ]

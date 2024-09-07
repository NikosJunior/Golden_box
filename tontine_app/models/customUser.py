from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPES = (
        ('manager', 'Manager'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    GENDERS = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    user_type = models.CharField(max_length = 20, choices= USER_TYPES, default ='customer')
    sexe = models.CharField(max_length = 20, choices = GENDERS )
    contact = models.CharField(max_length = 15)
    address = models.CharField(max_length=255)


    def __str__(self):
            return self.username

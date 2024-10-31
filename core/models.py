from django.db import models
from django.contrib.auth.models import AbstractUser

    
class User(AbstractUser):
    USER_TYPES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True)  
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)  
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=70, blank=True, null=True, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="Employee")

    def __str__(self):
        return self.username

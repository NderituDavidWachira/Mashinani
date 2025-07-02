from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    USER_TYPES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    
    # Remove redundant username declaration (inherited from AbstractUser)
    # Increase field lengths and add proper validation
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Full name of the user"
    )
    
    phone = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text="Phone number in international format"
    )
    
    # Password field should inherit from AbstractUser (no need to redeclare)
    # Remove: password = models.CharField(...)
    
    # Customize the inherited username field instead
    username = models.CharField(
        max_length=150,  # Standard Django username length
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    )
    
    user_type = models.CharField(
        max_length=20,  # Reduced since your choices are <20 chars
        choices=USER_TYPES,
        default='employee'  # Match the first value in USER_TYPES
    )

    def __str__(self):
        return self.username or self.email

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
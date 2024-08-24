from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('meseros', 'Meseros'),
        ('cocina', 'Cocina'),
        ('caja', 'Caja'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='meseros')

    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
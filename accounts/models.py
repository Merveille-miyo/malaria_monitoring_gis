from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('sysadmin', 'System Administrator'),
        ('healthworker', 'Health Worker'),
        ('medofficer', 'Medical Officer'),
        ('analyst', 'Health Analyst'),
        ('publicuser', 'Public User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='publicuser')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

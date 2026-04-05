from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('ADVERTISER', 'Advertiser'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ADMIN')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.company_name or f"{self.user.username}'s Profile"

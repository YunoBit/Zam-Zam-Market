from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    nick = models.CharField(
        max_length=100
    )
    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    address = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username



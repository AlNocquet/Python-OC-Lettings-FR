"""Database model for the profiles application."""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Represent additional profile information for a Django user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the associated username."""
        return self.user.username

"""Database models for the lettings application."""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Represent the postal address associated with a letting."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
    )

    class Meta:
        """Define display metadata for the Address model."""

        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Return a readable representation of the address."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Represent a letting linked to a single address."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the letting title."""
        return self.title

"""Unit tests for lettings models."""

from django.test import TestCase

from lettings.models import Address, Letting


class LettingsModelTests(TestCase):
    """Test the behavior of the lettings application models."""

    @classmethod
    def setUpTestData(cls):
        """Create reusable model data for unit tests."""
        cls.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='CA',
            zip_code=12345,
            country_iso_code='USA',
        )
        cls.letting = Letting.objects.create(
            title='Test Letting',
            address=cls.address,
        )

    def test_address_string_representation(self):
        """Check that an address has the expected readable representation."""
        self.assertEqual(str(self.address), '123 Test Street')

    def test_letting_string_representation(self):
        """Check that a letting is represented by its title."""
        self.assertEqual(str(self.letting), 'Test Letting')

    def test_address_plural_name(self):
        """Check the corrected plural name used by Django admin."""
        self.assertEqual(Address._meta.verbose_name_plural, 'Addresses')

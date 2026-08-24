"""Unit tests for profiles models."""

from django.contrib.auth.models import User
from django.test import TestCase

from profiles.models import Profile


class ProfileModelTests(TestCase):
    """Test the behavior of the Profile model."""

    @classmethod
    def setUpTestData(cls):
        """Create reusable user and profile data for unit tests."""
        cls.user = User.objects.create_user(
            username='ModelTestUser',
            password='test-password',
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city='Paris',
        )

    def test_profile_string_representation(self):
        """Check that a profile is represented by its username."""
        self.assertEqual(str(self.profile), 'ModelTestUser')

    def test_profile_user_reverse_relation(self):
        """Check the standard reverse relation from User to Profile."""
        self.assertEqual(self.user.profile, self.profile)

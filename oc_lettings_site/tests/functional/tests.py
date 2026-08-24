"""Functional tests for the main user browsing journeys."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting
from profiles.models import Profile


class BrowsingJourneyTests(TestCase):
    """Test representative user journeys across the site."""

    @classmethod
    def setUpTestData(cls):
        """Create reusable data for functional browsing tests."""
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
        cls.user = User.objects.create_user(
            username='TestUser',
            password='test-password',
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city='Paris',
        )

    def test_user_can_browse_from_home_to_letting_detail(self):
        """Check the complete browsing journey to a letting detail page."""
        home_response = self.client.get(reverse('index'))
        list_response = self.client.get(reverse('lettings:index'))
        detail_response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )

        self.assertEqual(home_response.status_code, 200)
        self.assertEqual(list_response.status_code, 200)
        self.assertContains(list_response, self.letting.title)
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, self.letting.title)

    def test_user_can_browse_from_home_to_profile_detail(self):
        """Check the complete browsing journey to a profile detail page."""
        home_response = self.client.get(reverse('index'))
        list_response = self.client.get(reverse('profiles:index'))
        detail_response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )

        self.assertEqual(home_response.status_code, 200)
        self.assertEqual(list_response.status_code, 200)
        self.assertContains(list_response, self.user.username)
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, self.user.username)

"""Tests for profiles URLs and views."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from profiles import views
from profiles.models import Profile


class ProfilesURLTests(TestCase):
    """Test URL routing for the profiles application."""

    def test_index_url_resolves_to_index_view(self):
        """Check that the profiles index URL resolves to the index view."""
        url = reverse('profiles:index')

        self.assertEqual(url, '/profiles/')
        self.assertEqual(resolve(url).func, views.index)

    def test_detail_url_resolves_to_profile_view(self):
        """Check that a profile detail URL resolves to the profile view."""
        url = reverse('profiles:profile', args=['TestUser'])

        self.assertEqual(url, '/profiles/TestUser/')
        self.assertEqual(resolve(url).func, views.profile)


class ProfilesViewTests(TestCase):
    """Test responses and templates for profiles views."""

    @classmethod
    def setUpTestData(cls):
        """Create reusable user and profile data for the view tests."""
        cls.user = User.objects.create_user(
            username='TestUser',
            password='test-password',
        )
        cls.profile = Profile.objects.create(
            user=cls.user,
            favorite_city='Paris',
        )

    def test_index_view_returns_200_and_uses_expected_template(self):
        """Check the profiles index response, template, and content."""
        response = self.client.get(reverse('profiles:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, self.user.username)

    def test_detail_view_returns_200_and_uses_expected_template(self):
        """Check the profile detail response, template, and context."""
        response = self.client.get(
            reverse('profiles:profile', args=[self.user.username])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

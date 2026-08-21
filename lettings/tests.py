"""Tests for lettings URLs and views."""

from django.test import TestCase
from django.urls import resolve, reverse

from . import views
from .models import Address, Letting


class LettingsURLTests(TestCase):
    """Test URL routing for the lettings application."""

    def test_index_url_resolves_to_index_view(self):
        """Check that the lettings index URL resolves to the index view."""
        url = reverse('lettings:index')

        self.assertEqual(url, '/lettings/')
        self.assertEqual(resolve(url).func, views.index)

    def test_detail_url_resolves_to_letting_view(self):
        """Check that a letting detail URL resolves to the letting view."""
        url = reverse('lettings:letting', args=[1])

        self.assertEqual(url, '/lettings/1/')
        self.assertEqual(resolve(url).func, views.letting)


class LettingsViewTests(TestCase):
    """Test responses and templates for lettings views."""

    @classmethod
    def setUpTestData(cls):
        """Create reusable letting data for the view tests."""
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

    def test_index_view_returns_200_and_uses_expected_template(self):
        """Check the lettings index response, template, and content."""
        response = self.client.get(reverse('lettings:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, self.letting.title)

    def test_detail_view_returns_200_and_uses_expected_template(self):
        """Check the letting detail response, template, and context."""
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.address)

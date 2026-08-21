from django.test import TestCase
from django.urls import resolve, reverse

from . import views
from .models import Address, Letting


class LettingsURLTests(TestCase):

    def test_index_url_resolves_to_index_view(self):
        url = reverse('lettings:index')

        self.assertEqual(url, '/lettings/')
        self.assertEqual(resolve(url).func, views.index)

    def test_detail_url_resolves_to_letting_view(self):
        url = reverse('lettings:letting', args=[1])

        self.assertEqual(url, '/lettings/1/')
        self.assertEqual(resolve(url).func, views.letting)


class LettingsViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
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
        response = self.client.get(reverse('lettings:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, self.letting.title)

    def test_detail_view_returns_200_and_uses_expected_template(self):
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.address)

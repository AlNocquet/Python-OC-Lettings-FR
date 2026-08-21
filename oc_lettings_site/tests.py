"""Tests for the main site error handling."""

from django.test import RequestFactory, SimpleTestCase, override_settings

from . import urls, views


class ErrorPageTests(SimpleTestCase):
    """Test the custom 404 and 500 error pages."""

    def test_custom_error_handlers_are_configured(self):
        """Check that the project URL configuration uses custom handlers."""
        self.assertEqual(
            urls.handler404,
            'oc_lettings_site.views.error_404',
        )
        self.assertEqual(
            urls.handler500,
            'oc_lettings_site.views.error_500',
        )

    @override_settings(DEBUG=False)
    def test_404_page_returns_custom_response(self):
        """Check that an unknown URL returns the custom 404 page."""
        response = self.client.get('/page-that-does-not-exist/')

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, '404', status_code=404)
        self.assertContains(
            response,
            'The page you are looking for could not be found.',
            status_code=404,
        )

    def test_500_handler_returns_custom_response(self):
        """Check that the 500 handler renders the custom error page."""
        request = RequestFactory().get('/forced-error/')
        response = views.error_500(request)

        self.assertEqual(response.status_code, 500)
        self.assertContains(response, '500', status_code=500)
        self.assertContains(
            response,
            'An unexpected error occurred. Please try again later.',
            status_code=500,
        )

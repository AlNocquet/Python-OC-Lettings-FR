"""Views for the main OC Lettings site."""

import logging

from django.shortcuts import render


logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros, vitae dapibus nisi lorem
# dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis
# quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non
# finibus neque cursus id.
def index(request):
    """Display the site home page."""
    logger.info("Home page requested.")
    return render(request, 'index.html')


def error_404(request, exception):
    """Render the custom page-not-found response."""
    logger.warning("Custom 404 page rendered.")
    return render(request, '404.html', status=404)


def error_500(request):
    """Render the custom internal-server-error response."""
    logger.error("Custom 500 page rendered.")
    return render(request, '500.html', status=500)

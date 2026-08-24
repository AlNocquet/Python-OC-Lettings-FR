"""Views for the profiles application."""

import logging

from django.shortcuts import render

from .models import Profile


logger = logging.getLogger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """Display the list of all profiles."""
    logger.info("Profiles list requested.")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque
# quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam
# dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males
def profile(request, username):
    """Display the profile associated with the given username."""
    logger.info("Profile detail requested.")
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

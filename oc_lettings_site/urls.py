"""Root URL configuration for the OC Lettings site."""

from django.contrib import admin
from django.urls import include, path

from . import views


handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

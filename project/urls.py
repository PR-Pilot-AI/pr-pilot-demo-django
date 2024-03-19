"""
URL Configuration for the Django project.
"""

from django.contrib import admin
from django.urls import path, include
from healthz.views import healthz_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz/', healthz_view, name='healthz'),
    path('accounts/', include('allauth.urls')),
]
from django.urls import path

from .views import about_me, contact_me, sample_api

urlpatterns = [
    path('', about_me, name='main'),
    path('contact_me/', contact_me, name='contact-me'),
    path('sample_api/', sample_api, name='sample-api'),
]
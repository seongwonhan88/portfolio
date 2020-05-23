from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'personal',
    'common_handler',
    'widget_tweaks', # https://pypi.org/project/django-widget-tweaks/
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PORTFOLIO_LOCAL_DB_NAME', 'portfolio'),
        'USER': os.environ.get('PORTFOLIO_LOCAL_DB_USER', 'portfolio'),
        'PASSWORD': os.environ.get('PORTFOLIO_LOCAL_DB_PASSWORD', 'portfolio'),
        'HOST': os.environ.get('PORTFOLIO_LOCAL_DB_HOST', 'postgres'),
        'PORT': 5432
    }
}

STATIC_URL = '/static/'

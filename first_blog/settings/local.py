from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
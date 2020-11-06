from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = ['djangoblogfernando.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
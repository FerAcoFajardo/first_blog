from .base import *
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = ['djangoblogfernando.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'depgcmfi2u36md',
        'USER': 'wuxxrcastvjfnu',
        'PASSWORD': '0cb82be425974c8e0d02871928f0916ac714aca785f9874d616d104b2cdfe043',
        'HOST': 'ec2-54-158-190-214.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')
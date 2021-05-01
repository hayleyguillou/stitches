"""
Development settings
"""

from .base import *

DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stitches',
        'USER': 'stitcher',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
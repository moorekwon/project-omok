from ._base import *

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.prod.application'

INSTALLED_APPS += []

ALLOWED_HOSTS += [
    '*'
]

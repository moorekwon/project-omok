from ._base import *

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'

ALLOWED_HOSTS += [
    '*'
]

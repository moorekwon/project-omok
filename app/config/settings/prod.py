from ._base import *

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.prod.application'

INSTALLED_APPS += []

ALLOWED_HOSTS += [
    '*'
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}
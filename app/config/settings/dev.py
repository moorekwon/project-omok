from ._base import *

DEBUG = True
WSGI_APPLICATION = 'config.wsgi.dev.application'

INSTALLED_APPS += [
    'django_extensions',
]

ALLOWED_HOSTS += [
    '*'
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('*.hyegg.xyz', 6379)],
        },
    },
}
from ._base import *

DEBUG = False
WSGI_APPLICATION = 'config.wsgi.prod.application'

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
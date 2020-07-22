import os

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if SETTINGS_MODULE == 'config.settings':
    from .dev import *
elif not SETTINGS_MODULE:
    from .prod import *

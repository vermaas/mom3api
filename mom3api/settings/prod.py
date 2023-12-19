from mom3api.settings.base import *

# Set to False to allow writes
SITE_READ_ONLY = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lofar_mom3',
        'USER': 'xxxxxx',
        'PASSWORD': 'xxxxxx',
        'HOST': 'dbsrv2.astron.nl',   # Or an IP Address that your DB is hosted on
        'PORT': '3307',
    }
}
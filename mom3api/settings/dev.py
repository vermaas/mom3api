from mom3api.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lofar_mom3',
        'USER': 'root',
        'PASSWORD': 'my_sql_2023_!@#',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
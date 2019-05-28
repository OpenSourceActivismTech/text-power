from __future__ import absolute_import, unicode_literals

# -----------------------------------------------------------------------------------
# Sample RapidPro settings file, this should allow you to deploy RapidPro locally on
# a PostgreSQL database.
#
# The following are requirements:
#     - a postgreSQL database named 'temba', with a user name 'temba' and
#       password 'temba' (with postgis extensions installed)
#     - a redis instance listening on localhost
# -----------------------------------------------------------------------------------

import warnings
import copy

SECRET_KEY = 'asdf this is a bad secret key'

from .settings_textpower import *  # noqa

IS_PROD = False
DEBUG = True
DEBUG_TOOLBAR = True

HOSTNAME = 'spacedogxyz.ngrok.io'
ALLOWED_HOSTS = ['*']

# allow signups on dev
BRANDING['textpower']['allow_signups'] = True

# -----------------------------------------------------------------------------------
# Database Configuration(we expect a Postgres instance on localhost)
# -----------------------------------------------------------------------------------
_default_database_config = {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'temba',
    'USER': 'temba',
    'PASSWORD': 'temba',
    'HOST': 'localhost',
    'PORT': '',
    'ATOMIC_REQUESTS': True,
    'CONN_MAX_AGE': 60,
    'OPTIONS': {}
}
_direct_database_config = _default_database_config.copy()
_default_database_config['DISABLE_SERVER_SIDE_CURSORS'] = True

DATABASES = {
    'default': _default_database_config,
    'direct': _direct_database_config
}

# -----------------------------------------------------------------------------------
# Redis & Cache Configuration (we expect a Redis instance on localhost)
# -----------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/%s" % (REDIS_HOST, REDIS_PORT, REDIS_DB),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "collectfast": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "collectfast_cache",
    }
}

INTERNAL_IPS = ['*',]

# -----------------------------------------------------------------------------------
# Load development apps
# -----------------------------------------------------------------------------------
INSTALLED_APPS = INSTALLED_APPS + ('storages', )
if DEBUG_TOOLBAR:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar', )

# -----------------------------------------------------------------------------------
# In development, add in extra logging for exceptions and the debug toolbar
# -----------------------------------------------------------------------------------
MIDDLEWARE = ('temba.middleware.ExceptionMiddleware',) + MIDDLEWARE
if DEBUG_TOOLBAR:
    MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE

# -----------------------------------------------------------------------------------
# In development, perform background tasks in the web thread (synchronously)
# -----------------------------------------------------------------------------------
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'memory'

# -----------------------------------------------------------------------------------
# This setting throws an exception if a naive datetime is used anywhere. (they should
# always contain a timezone)
# -----------------------------------------------------------------------------------
warnings.filterwarnings('error', r"DateTimeField .* received a naive datetime",
                        RuntimeWarning, r'django\.db\.models\.fields')

# -----------------------------------------------------------------------------------
# Reset static file compression and storage on development
# -----------------------------------------------------------------------------------
STATIC_URL = '/sitestatic/'
STORAGE_URL = 'localhost:8000/sitestatic'
COMPRESS_URL = STATIC_URL+'/'

COLLECTFAST_ENABLED = False
COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

DEFAULT_FILE_STORAGE = 'textpower.storage_backends.LocalStaticStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE 
COMPRESS_STORAGE = DEFAULT_FILE_STORAGE
COMPRESS_OFFLINE_CONTEXT = []

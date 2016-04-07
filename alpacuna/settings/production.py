from .base import *

DEBUG = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    }
}

ADMIN_MEDIA_PREFIX = '/static/grappelli/'
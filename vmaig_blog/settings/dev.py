# coding: utf-8

from .base import *

COMPRESS_ENABLED = False

WSGI_APPLICATION = 'vmaig_blog.wsgi_dev.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'boboblog',
        'USER': 'root',
        'PASSWORD': 'qqdb123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# cache配置
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
    #'memcache': {
    #    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #    'LOCATION': '127.0.0.1:11211',
    #    'options': {
    #        'MAX_ENTRIES': 1024,
    #    }
    #},
    #"redis": {
    #    "BACKEND": "django_redis.cache.RedisCache",
    #    "LOCATION": "redis://127.0.0.1:6379/1",
    #    "OPTIONS": {
    #        "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #    }
    #}
}

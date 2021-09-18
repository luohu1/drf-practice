from .base import *  # NOQA
from .base import INSTALLED_APPS

DEBUG = True
ALLOWED_HOSTS = ['*', ]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS += [
    # third party apps
    'rest_framework',
    'drf_spectacular',
    # local apps
    'account',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'DRF Practices API',
    'DESCRIPTION': 'drf-practices description',
    'VERSION': 'v1',
    'CONTACT': {
        'name': 'Luo Hui',
        'url': 'https://github.com/luohu1/drf-practices',
        'email': 'mylhmail@163.com'
    },
    'LICENSE': {'name': 'MIT License'},
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'drf_practices',
        'PORT': 3306,
        'CONN_MAX_AGE': 60
    }
}

from .base import *  # NOQA
from .base import INSTALLED_APPS

DEBUG = True
ALLOWED_HOSTS = ['*', ]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
AUTH_USER_MODEL = 'account.User'

INSTALLED_APPS += [
    'account'
]

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

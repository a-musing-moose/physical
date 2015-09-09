# -*- coding: utf-8 -*-
import os


BASE_DIR = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = '%w#%6_isg#t82^ts55l)rrydkj84z$3s-d5)&abqtv*mn&xupd'

DEBUG = os.getenv("DJANGO_DEBUG", "Off").strip().lower() in (
    "true", "yes", "1", "on"
)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'rest_framework',
    'physical'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")

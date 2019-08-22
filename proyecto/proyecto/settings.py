"""
Django settings for proyecto project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ct4!b^rh@%5fx2*)r55)+m69k408l2%=g6b^zxrx33t$a!)^(4'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False#
DEBUG = True

ALLOWED_HOSTS = ['*']
LOGIN_REDIRECT_URL='/'
LOGIN_URL = "/login/"
#LOGIN_URL="/accounts/login/?next=/aplicacion/"
#LOGIN_URL = "/login"
#LOGIN_URL =None

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'push_notifications',
    'webpush',
    'aplicacion',
    'channels',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto.wsgi.application'
ASGI_APPLICATION = "proyecto.routing.application"



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [("redis-server-name", 6379)],
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


PUSH_NOTIFICATIONS_SETTINGS = {
'GCM_API_KEY': '< your api key >',
'APNS_CERTIFICATE': '/path/to/your/certificate.pem',
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'myproject',
		'USER': 'myprojectuser',
		'PASSWORD': 'password',
		'HOST': 'localhost',
		'PORT': '',
	}
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": "BP3iooycd2ZGd3cUVi5mxCWwAwbP16ARsbZSvX0hGj5DwyNbyR6pmchNJqfiTnqUufzX2OjIepVExXQrNx3gltc",
   "VAPID_PRIVATE_KEY": "GaUb3h2dccLKEaIwMYn_MQ4EGCMnLcVykW5E36QBuuw",
   "VAPID_ADMIN_EMAIL": "admin@example.com"
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# ingles
#LANGUAGE_CODE = 'en-us'

# español
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS=(
        os.path.join(BASE_DIR, "locale"),
)

ugettext = lambda s: s
# LANGUAGES = (
#     ('es',ugettext('Español')),
#     ('en',ugettext('Inglés')),
#     ('en-us',ugettext('Inglés')),
# )

LANGUAGES = (
    ('es',_('Español')),
    ('en',_('Inglés')),
    ('en-us',_('Inglés USA')),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
        STATIC_DIR,
]

STATIC_ROOT= os.path.join(BASE_DIR, 'staticfiles')

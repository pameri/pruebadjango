"""
Django settings for prueba project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '558-fnnoy$$!#3&o=lr@orog9s*8(7v*_of5(g#27ta64!8204'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prueba.apps.main',
    'prueba.apps.social',
    'sorl.thumbnail',
    #'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'prueba.urls'

WSGI_APPLICATION = 'prueba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'sqlserver_ado', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'C:\\Aptana\\recetario\\recetario.db',                      # Or path to database file if using sqlite3.
        #'NAME': 'PORTAL',                      # Or path to database file if using sqlite3.
        'NAME': 'PRUEBA',
        'USER': 'sa',                      # Not used with sqlite3.
        'PASSWORD': 'sistemas',                  # Not used with sqlite3.
        'HOST': '.\SQL2008',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
                    #'provider': 'SQLOLEDB',
                    'provider': 'SQLNCLI10',                    
                    #'use_mars' : True,
                    'extra_params': 'DataTypeCompatibility=80;MARS Connection=True;',                    
                    }
    },
    
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'prueba/media')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
                 os.path.join(BASE_DIR,'prueba/static'),
                 )

TEMPLATE_DIRS = (
                 os.path.join(BASE_DIR,'prueba/templates'),
                 )
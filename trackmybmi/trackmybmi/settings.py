"""
Django settings for trackmybmi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('TRACKMYBMI_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('TRACKMYBMI_DEBUG', 'off') == 'on'
TEMPLATE_DEBUG = os.environ.get('TRACKMYBMI_TEMPLATE_DEBUG') == 'on' or DEBUG

ALLOWED_HOSTS = os.environ.get('TRACKMYBMI_ALLOWED_HOSTS', 'localhost'
                                                                ).split(',')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'custom_user',
    'users',
    'measurements',
)

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'trackmybmi.urls'

WSGI_APPLICATION = 'trackmybmi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['TRACKMYBMI_DB_NAME'],
        'USER': os.environ['TRACKMYBMI_DB_USER'],
        'PASSWORD': os.environ['TRACKMYBMI_DB_PASSWORD'],
        'HOST': os.environ.get('TRACKMYBMI_DB_HOST') or '127.0.0.1',
        'PORT': os.environ.get('TRACKMYBMI_DB_PORT') or '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

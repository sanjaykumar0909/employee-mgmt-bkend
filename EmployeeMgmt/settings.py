"""
Django settings for EmployeeMgmt project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
get_debug= os.environ.get('DJANGO_DEBUG', 'false').lower()
DEBUG = get_debug== "true"

get_allowed_hosts= os.environ.get('ALLOWED_HOSTS', default=False)
if (get_allowed_hosts):
    ALLOWED_HOSTS= get_allowed_hosts.split(' ')
else:
    ALLOWED_HOSTS=[]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'mainapp',
    'django_extensions',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EmployeeMgmt.urls'
CORS_ALLOW_ALL_ORIGINS= True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'EmployeeMgmt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DB_CONFIG= {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'EmployeeMgmt',
        'USER': "postgres",
        'PASSWORD': "1234",
        'HOST': "localhost",
        'PORT': '5432'
    }
DATABASES= {

}
# internal render DB link (to be used on production in render web service)
DB_CONFIG if os.environ.get('LOCALHOST') else dj_database_url.parse(os.environ.get('DATABASE_URL'))

# external render DB link (connect to render DB from locally)
# DATABASES['default']= dj_database_url.parse("postgres://emp_mgmt_db_user:4qW5wvoKcZHV2Bv1QxgbcwOgoGsxoSxx@dpg-cpk7pl7sc6pc73eofi2g-a.singapore-postgres.render.com/emp_mgmt_db")


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

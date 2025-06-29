"""
Django settings for config project.

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
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-+0k*&_&$!3%t#i%j8a&=-8b1j#k^+@v&_d*6&t&u*z8v7d*z&z')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = [
    'fletcraft.co.za',
    'www.fletcraft.co.za', 
    'fletcraft-software.onrender.com',
    'localhost',
    '127.0.0.1',
    '*'  # Allow all hosts for now, can restrict later
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL and DATABASE_URL.strip():
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://fletcraft.co.za",
    "https://www.fletcraft.co.za",
    "https://fletcraft-software.onrender.com",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

# Allow all origins in development and production for now
CORS_ALLOW_ALL_ORIGINS = True

# Allow credentials for CORS
CORS_ALLOW_CREDENTIALS = True

# Additional CORS headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CSRF settings for Django admin
CSRF_TRUSTED_ORIGINS = [
    "https://fletcraft.co.za",
    "https://www.fletcraft.co.za", 
    "https://fletcraft-software.onrender.com",
]

# Temporarily disable CSRF for easier admin access
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_SAMESITE = 'Lax'

# Allow admin access from any origin temporarily
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# PayFast Configuration - LIVE CREDENTIALS
# These should be set as environment variables in production
PAYFAST_MERCHANT_ID = os.environ.get('PAYFAST_MERCHANT_ID', '13245841')
PAYFAST_MERCHANT_KEY = os.environ.get('PAYFAST_MERCHANT_KEY', 'kzyobsh5zlvrw')  
PAYFAST_PASSPHRASE = os.environ.get('PAYFAST_PASSPHRASE', 'Redeclip5e-8298')
PAYFAST_URL = os.environ.get('PAYFAST_URL', 'https://www.payfast.co.za/eng/process')
FRONTEND_URL = os.environ.get('FRONTEND_URL', 'https://fletcraft.co.za')

# PayFast Configuration
# Use environment variables for production security
PAYFAST_MERCHANT_ID = os.environ.get('PAYFAST_MERCHANT_ID', '13245841')  # Live merchant ID
PAYFAST_MERCHANT_KEY = os.environ.get('PAYFAST_MERCHANT_KEY', 'kzyobsh5zlvrw')  # Live merchant key
PAYFAST_PASSPHRASE = os.environ.get('PAYFAST_PASSPHRASE', 'Redeclip5e-8298')  # Live passphrase
PAYFAST_URL = os.environ.get('PAYFAST_URL', 'https://www.payfast.co.za/eng/process')  # Live PayFast URL
FRONTEND_URL = os.environ.get('FRONTEND_URL', 'https://fletcraft.co.za')  # Frontend URL for redirects

# PayFast ITN (Instant Transaction Notification) settings
PAYFAST_ITN_HOST_CHECK = os.environ.get('PAYFAST_ITN_HOST_CHECK', 'True').lower() == 'true'  # Verify ITN comes from PayFast
PAYFAST_ITN_VERIFY_SSL = os.environ.get('PAYFAST_ITN_VERIFY_SSL', 'True').lower() == 'true'  # Verify SSL certificates
